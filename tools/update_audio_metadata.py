#!/usr/bin/env python3
"""
新荘音頭デジタルアーカイブ
音源メタデータ確認・更新スクリプト

通常実行ではプレビューのみを表示する。
--write を指定した場合だけ、バックアップ後にMP3・WAVへタグを書き込み、
書き込み後の内容を再読込して検証する。
"""

from __future__ import annotations

import argparse
from pathlib import Path

from shinso_metadata import (
    SUPPORTED_WRITABLE_EXTENSIONS,
    AudioMetadata,
    backup_audio_file,
    build_audio_metadata,
    build_performance_indexes,
    create_backup_directory,
    find_audio_files,
    load_yaml_metadata,
    match_audio_file_to_performance,
    verify_audio_tags,
    write_audio_tags,
)
from shinso_metadata.display import (
    display_audio_metadata_preview,
    display_complete_metadata,
    display_unmatched_audio_file,
)


PROJECT_ROOT_DIRECTORY = Path(__file__).resolve().parent.parent
METADATA_FILE_PATH = PROJECT_ROOT_DIRECTORY / "metadata" / "shinso-ondo.yaml"
AUDIO_DIRECTORY_PATH = PROJECT_ROOT_DIRECTORY / "audio"
COVER_ART_FILE_PATH = (
    PROJECT_ROOT_DIRECTORY / "images" / "artwork" / "cover.png"
)


def parse_command_line_arguments() -> argparse.Namespace:
    argument_parser = argparse.ArgumentParser(
        description=(
            "新荘音頭のYAML正本と音源ファイルを照合します。"
            "通常はプレビューのみ、--write 指定時だけタグを書き込みます。"
        )
    )
    argument_parser.add_argument(
        "--write",
        action="store_true",
        help=(
            "バックアップを作成してからMP3・WAVへタグを書き込み、"
            "自動検証します。"
        ),
    )
    argument_parser.add_argument(
        "--verify",
        action="store_true",
        help="既存のMP3・WAVタグをYAML正本と照合します。",
    )
    argument_parser.add_argument(
        "--show-metadata",
        action="store_true",
        help="読み込んだYAMLの内容全体を表示します。",
    )
    argument_parser.add_argument(
        "--show-unmatched-only",
        action="store_true",
        help="YAMLと対応しない音源だけを表示します。",
    )
    command_line_arguments = argument_parser.parse_args()

    if command_line_arguments.write and command_line_arguments.verify:
        argument_parser.error(
            "--write と --verify は同時に指定できません。"
        )

    return command_line_arguments


def display_header(mode: str, audio_file_count: int) -> None:
    print()
    print("==========================================")
    print(f" 新荘音頭 音源メタデータ・{mode}")
    print("==========================================")
    print()
    print(f"メタデータ正本 : {METADATA_FILE_PATH}")
    print(f"検出した音源数 : {audio_file_count}")
    print(
        "ジャケット画像 : "
        + ("あり" if COVER_ART_FILE_PATH.exists() else "なし")
    )
    print()


def display_verification_result(
    audio_file_path: Path,
    audio_metadata: AudioMetadata,
) -> bool:
    verification_result = verify_audio_tags(
        audio_file_path,
        audio_metadata,
    )
    relative_file_path = audio_file_path.relative_to(
        PROJECT_ROOT_DIRECTORY
    )

    if verification_result.is_valid:
        print(f"○ 検証成功 : {relative_file_path}")
        return True

    print(f"× 検証失敗 : {relative_file_path}")
    for error in verification_result.errors:
        print(f"  - {error}")
    return False


def main() -> None:
    command_line_arguments = parse_command_line_arguments()
    metadata = load_yaml_metadata(METADATA_FILE_PATH)
    audio_file_paths = find_audio_files(AUDIO_DIRECTORY_PATH)
    performance_by_id, performance_by_file_path = build_performance_indexes(
        metadata
    )

    if command_line_arguments.write:
        mode = "書き込み"
    elif command_line_arguments.verify:
        mode = "検証"
    else:
        mode = "プレビュー"

    display_header(mode, len(audio_file_paths))

    if not command_line_arguments.write:
        print("注意: この実行では音源ファイルを変更しません。")
    else:
        print(
            "注意: 対応するMP3・WAVをバックアップ後に更新します。"
        )

    matched_items: list[tuple[Path, AudioMetadata, str]] = []
    matched_file_count = 0
    unmatched_file_count = 0

    for audio_file_path in audio_file_paths:
        performance, match_method = match_audio_file_to_performance(
            audio_file_path=audio_file_path,
            project_root_directory=PROJECT_ROOT_DIRECTORY,
            performance_by_id=performance_by_id,
            performance_by_file_path=performance_by_file_path,
        )

        if performance is None:
            unmatched_file_count += 1
            display_unmatched_audio_file(
                audio_file_path,
                PROJECT_ROOT_DIRECTORY,
            )
            continue

        matched_file_count += 1
        audio_metadata = build_audio_metadata(metadata, performance)
        matched_items.append(
            (audio_file_path, audio_metadata, match_method)
        )

        if (
            not command_line_arguments.show_unmatched_only
            and not command_line_arguments.verify
        ):
            display_audio_metadata_preview(
                audio_file_path=audio_file_path,
                project_root_directory=PROJECT_ROOT_DIRECTORY,
                audio_metadata=audio_metadata,
                match_method=match_method,
            )

    print()
    print("==========================================")
    print(" 照合結果")
    print("==========================================")
    print(f"○ 対応済み : {matched_file_count}")
    print(f"△ 対応なし : {unmatched_file_count}")
    print()

    if command_line_arguments.verify:
        success_count = 0
        failure_count = 0
        print("タグ検証を開始します。")
        print()
        for audio_file_path, audio_metadata, _ in matched_items:
            if audio_file_path.suffix.lower() not in SUPPORTED_WRITABLE_EXTENSIONS:
                print(
                    "△ 検証対象外 : "
                    f"{audio_file_path.relative_to(PROJECT_ROOT_DIRECTORY)}"
                )
                continue
            if display_verification_result(
                audio_file_path,
                audio_metadata,
            ):
                success_count += 1
            else:
                failure_count += 1

        print()
        print(f"○ 検証成功 : {success_count}")
        print(f"× 検証失敗 : {failure_count}")

    elif command_line_arguments.write:
        writable_items = [
            item
            for item in matched_items
            if item[0].suffix.lower() in SUPPORTED_WRITABLE_EXTENSIONS
        ]

        if not writable_items:
            print("書き込み対象となるMP3・WAVがありません。")
        else:
            backup_directory = create_backup_directory(
                PROJECT_ROOT_DIRECTORY
            )
            print(f"バックアップ先 : {backup_directory}")
            print()

            success_count = 0
            failure_count = 0

            for audio_file_path, audio_metadata, _ in writable_items:
                relative_file_path = audio_file_path.relative_to(
                    PROJECT_ROOT_DIRECTORY
                )
                try:
                    backup_file_path = backup_audio_file(
                        audio_file_path,
                        PROJECT_ROOT_DIRECTORY,
                        backup_directory,
                    )
                    print(
                        f"○ バックアップ : {relative_file_path}"
                        f" -> {backup_file_path.relative_to(PROJECT_ROOT_DIRECTORY)}"
                    )
                    write_audio_tags(
                        audio_file_path,
                        audio_metadata,
                        (
                            COVER_ART_FILE_PATH
                            if COVER_ART_FILE_PATH.exists()
                            else None
                        ),
                    )
                    if display_verification_result(
                        audio_file_path,
                        audio_metadata,
                    ):
                        success_count += 1
                    else:
                        failure_count += 1
                except Exception as error:
                    failure_count += 1
                    print(f"× 書き込み失敗 : {relative_file_path}")
                    print(f"  - {error}")

            print()
            print(f"○ 書き込み・検証成功 : {success_count}")
            print(f"× 失敗               : {failure_count}")
            print(f"バックアップ先       : {backup_directory}")

    elif matched_file_count:
        print(
            "書き込む場合は --write、既存タグを確認する場合は "
            "--verify を指定してください。"
        )

    if command_line_arguments.show_metadata:
        display_complete_metadata(metadata)


if __name__ == "__main__":
    main()
