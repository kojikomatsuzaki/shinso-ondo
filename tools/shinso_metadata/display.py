"""音源メタデータ照合結果の表示。"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

from .model import AudioMetadata


def display_value(
    label: str,
    value: str | tuple[str, ...] | None,
) -> None:
    if isinstance(value, tuple):
        display_text = " / ".join(value)
    else:
        display_text = value or "（未設定）"
    print(f"  {label:<14}: {display_text}")


def display_audio_metadata_preview(
    audio_file_path: Path,
    project_root_directory: Path,
    audio_metadata: AudioMetadata,
    match_method: str,
) -> None:
    relative_file_path = audio_file_path.relative_to(project_root_directory)

    print()
    print("○ 対応する演奏情報が見つかりました")
    print(f"  ファイル       : {relative_file_path}")
    print(f"  形式           : {audio_file_path.suffix.lower()}")
    print(f"  照合方法       : {match_method}")
    print(f"  performance ID : {audio_metadata.performance_id}")

    display_value("タイトル", audio_metadata.title)
    display_value("版表示", audio_metadata.version_title)
    display_value("歌唱", audio_metadata.artists)
    display_value("演奏", audio_metadata.musicians)
    display_value("指揮", audio_metadata.conductor)
    display_value("作曲", audio_metadata.composer)
    display_value("編曲", audio_metadata.arranger)
    display_value("作詞", audio_metadata.lyricist)
    display_value("制作", audio_metadata.producer)
    display_value("録音年", audio_metadata.recording_date)
    display_value("公開日", audio_metadata.publication_date)
    display_value("権利表示", audio_metadata.copyright_notice)
    display_value("ライセンス", audio_metadata.license_name)
    display_value("ライセンスURL", audio_metadata.license_url)
    display_value("リポジトリ", audio_metadata.repository_url)


def display_unmatched_audio_file(
    audio_file_path: Path,
    project_root_directory: Path,
) -> None:
    relative_file_path = audio_file_path.relative_to(project_root_directory)

    print()
    print("△ 対応する演奏情報がありません")
    print(f"  ファイル : {relative_file_path}")
    print(f"  stem     : {audio_file_path.stem}")


def display_complete_metadata(metadata: dict[str, Any]) -> None:
    print()
    print("==========================================")
    print(" YAML読み込み内容")
    print("==========================================")
    print()
    print(yaml.safe_dump(metadata, allow_unicode=True, sort_keys=False))
