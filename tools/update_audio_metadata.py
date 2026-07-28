#!/usr/bin/env python3
"""
新荘音頭デジタルアーカイブ
音源メタデータ確認スクリプト

metadata/shinso-ondo.yaml を正本として読み込み、
audio/ 以下の各音源ファイルを performances の情報と照合し、
書き込み予定の音源メタデータを表示する。

この版では音源ファイルを変更しない。
"""

from __future__ import annotations

import argparse
from pathlib import Path

from shinso_metadata import (
    build_audio_metadata,
    build_performance_indexes,
    find_audio_files,
    load_yaml_metadata,
    match_audio_file_to_performance,
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
            "新荘音頭のYAML正本と音源ファイルを照合し、"
            "音源タグの書き込み予定を表示します。"
            "この版では実ファイルを変更しません。"
        )
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
    return argument_parser.parse_args()


def main() -> None:
    command_line_arguments = parse_command_line_arguments()
    metadata = load_yaml_metadata(METADATA_FILE_PATH)
    audio_file_paths = find_audio_files(AUDIO_DIRECTORY_PATH)
    performance_by_id, performance_by_file_path = build_performance_indexes(
        metadata
    )

    matched_file_count = 0
    unmatched_file_count = 0

    print()
    print("==========================================")
    print(" 新荘音頭 音源メタデータ・プレビュー")
    print("==========================================")
    print()
    print(f"メタデータ正本 : {METADATA_FILE_PATH}")
    print(f"検出した音源数 : {len(audio_file_paths)}")
    print(
        "ジャケット画像 : "
        + ("あり" if COVER_ART_FILE_PATH.exists() else "なし")
    )
    print()
    print("注意: この版では音源ファイルを一切変更しません。")

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
        if command_line_arguments.show_unmatched_only:
            continue

        audio_metadata = build_audio_metadata(metadata, performance)
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

    if matched_file_count:
        print(
            "次段階では、このプレビュー内容を"
            "MP3・WAV向けタグへ変換します。"
        )

    if command_line_arguments.show_metadata:
        display_complete_metadata(metadata)


if __name__ == "__main__":
    main()
