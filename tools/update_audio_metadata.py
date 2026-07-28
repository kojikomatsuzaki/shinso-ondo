#!/usr/bin/env python3
"""
新荘音頭デジタルアーカイブ
音源メタデータ更新スクリプト

metadata/shinso-ondo.yaml を正本として読み込み、
audio/ 以下の音源ファイルとジャケット画像の状態を確認する。

この初版では、音源ファイルのタグは変更しない。
"""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

import yaml


# ==========================================
# Project Paths
# ==========================================

PROJECT_ROOT_DIRECTORY = Path(__file__).resolve().parent.parent

METADATA_FILE_PATH = (
    PROJECT_ROOT_DIRECTORY
    / "metadata"
    / "shinso-ondo.yaml"
)

AUDIO_DIRECTORY_PATH = (
    PROJECT_ROOT_DIRECTORY
    / "audio"
)

COVER_ART_FILE_PATH = (
    PROJECT_ROOT_DIRECTORY
    / "images"
    / "artwork"
    / "cover.png"
)


# ==========================================
# Supported Audio Formats
# ==========================================

SUPPORTED_AUDIO_FILE_EXTENSIONS = {
    ".mp3",
    ".wav",
    ".flac",
    ".aif",
    ".aiff",
    ".m4a",
}


# ==========================================
# Command-line Arguments
# ==========================================

def parse_command_line_arguments() -> argparse.Namespace:
    """
    コマンドライン引数を読み込む。
    """

    argument_parser = argparse.ArgumentParser(
        description=(
            "新荘音頭のYAML正本と音源ファイルを確認します。"
            "この初版では音源タグを書き換えません。"
        )
    )

    argument_parser.add_argument(
        "--show-metadata",
        action="store_true",
        help="読み込んだYAMLの内容全体を表示します。",
    )

    return argument_parser.parse_args()


# ==========================================
# Metadata Loading
# ==========================================

def load_yaml_metadata(
    metadata_file_path: Path,
) -> dict[str, Any]:
    """
    YAML正本を読み込む。
    """

    if not metadata_file_path.exists():
        raise FileNotFoundError(
            "メタデータ正本が見つかりません。\n"
            f"確認した場所: {metadata_file_path}"
        )

    with metadata_file_path.open(
        "r",
        encoding="utf-8",
    ) as metadata_file:
        loaded_metadata = yaml.safe_load(metadata_file)

    if loaded_metadata is None:
        raise ValueError(
            "メタデータ正本が空です。"
        )

    if not isinstance(loaded_metadata, dict):
        raise ValueError(
            "YAMLの最上位要素は辞書形式である必要があります。"
        )

    return loaded_metadata


# ==========================================
# Audio File Discovery
# ==========================================

def find_audio_files(
    audio_directory_path: Path,
) -> list[Path]:
    """
    audioディレクトリ以下から音源ファイルを探す。
    """

    if not audio_directory_path.exists():
        return []

    audio_file_paths = [
        file_path
        for file_path in audio_directory_path.rglob("*")
        if (
            file_path.is_file()
            and file_path.suffix.lower()
            in SUPPORTED_AUDIO_FILE_EXTENSIONS
        )
    ]

    return sorted(audio_file_paths)


# ==========================================
# Display Helpers
# ==========================================

def display_project_summary(
    metadata: dict[str, Any],
    audio_file_paths: list[Path],
) -> None:
    """
    読み込み結果を表示する。
    """

    print()
    print("==========================================")
    print(" 新荘音頭 音源メタデータ確認")
    print("==========================================")
    print()

    print(f"プロジェクトルート: {PROJECT_ROOT_DIRECTORY}")
    print(f"メタデータ正本:     {METADATA_FILE_PATH}")
    print(f"音源ディレクトリ:   {AUDIO_DIRECTORY_PATH}")
    print(f"ジャケット画像:     {COVER_ART_FILE_PATH}")

    print()
    print("------------------------------------------")
    print(" YAML最上位キー")
    print("------------------------------------------")

    for metadata_key in metadata.keys():
        print(f"- {metadata_key}")

    print()
    print("------------------------------------------")
    print(" ジャケット画像")
    print("------------------------------------------")

    if COVER_ART_FILE_PATH.exists():
        print("○ cover.png が見つかりました。")
    else:
        print("△ cover.png はまだありません。")

    print()
    print("------------------------------------------")
    print(" 検出した音源")
    print("------------------------------------------")

    if not audio_file_paths:
        print("△ 対象となる音源ファイルは見つかりませんでした。")
    else:
        for audio_file_path in audio_file_paths:
            relative_audio_file_path = (
                audio_file_path.relative_to(
                    PROJECT_ROOT_DIRECTORY
                )
            )

            print(f"- {relative_audio_file_path}")

    print()
    print(f"音源ファイル数: {len(audio_file_paths)}")
    print()
    print("この段階では、音源タグは変更していません。")
    print()


def display_complete_metadata(
    metadata: dict[str, Any],
) -> None:
    """
    YAMLの内容全体を表示する。
    """

    print()
    print("==========================================")
    print(" YAML読み込み内容")
    print("==========================================")
    print()

    print(
        yaml.safe_dump(
            metadata,
            allow_unicode=True,
            sort_keys=False,
        )
    )


# ==========================================
# Main
# ==========================================

def main() -> None:
    """
    スクリプト全体を実行する。
    """

    command_line_arguments = (
        parse_command_line_arguments()
    )

    metadata = load_yaml_metadata(
        METADATA_FILE_PATH
    )

    audio_file_paths = find_audio_files(
        AUDIO_DIRECTORY_PATH
    )

    display_project_summary(
        metadata=metadata,
        audio_file_paths=audio_file_paths,
    )

    if command_line_arguments.show_metadata:
        display_complete_metadata(metadata)


if __name__ == "__main__":
    main()
