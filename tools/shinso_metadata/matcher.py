"""音源ファイルの探索と演奏情報との照合。"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from .mapper import as_list

SUPPORTED_AUDIO_FILE_EXTENSIONS = {
    ".mp3",
    ".wav",
    ".flac",
    ".aif",
    ".aiff",
    ".m4a",
}


def find_audio_files(audio_directory_path: Path) -> list[Path]:
    """audioディレクトリ以下から対応形式の音源を探す。"""

    if not audio_directory_path.exists():
        return []

    return sorted(
        file_path
        for file_path in audio_directory_path.rglob("*")
        if file_path.is_file()
        and file_path.suffix.lower() in SUPPORTED_AUDIO_FILE_EXTENSIONS
    )


def build_performance_indexes(
    metadata: dict[str, Any],
) -> tuple[dict[str, dict[str, Any]], dict[str, dict[str, Any]]]:
    """performance.id と item.files[].file_name の索引を作る。"""

    performances = metadata.get("performances")
    if not isinstance(performances, list):
        raise ValueError("YAMLに performances のリストがありません。")

    by_id: dict[str, dict[str, Any]] = {}
    by_file_path: dict[str, dict[str, Any]] = {}

    for performance in performances:
        if not isinstance(performance, dict):
            continue

        performance_id = performance.get("id")
        if not isinstance(performance_id, str) or not performance_id.strip():
            raise ValueError("performances に id のない項目があります。")

        normalized_id = performance_id.strip()
        if normalized_id in by_id:
            raise ValueError(f"performance.id が重複しています: {normalized_id}")
        by_id[normalized_id] = performance

        item = performance.get("item", {})
        if not isinstance(item, dict):
            continue

        for file_metadata in as_list(item.get("files", [])):
            if not isinstance(file_metadata, dict):
                continue
            file_name = file_metadata.get("file_name")
            if not isinstance(file_name, str) or not file_name.strip():
                continue

            normalized_path = Path(file_name).as_posix().lstrip("./")
            if normalized_path in by_file_path:
                raise ValueError(
                    "item.files[].file_name が重複しています: "
                    f"{normalized_path}"
                )
            by_file_path[normalized_path] = performance

    return by_id, by_file_path


def match_audio_file_to_performance(
    audio_file_path: Path,
    project_root_directory: Path,
    performance_by_id: dict[str, dict[str, Any]],
    performance_by_file_path: dict[str, dict[str, Any]],
) -> tuple[dict[str, Any] | None, str]:
    """完全な相対パスを優先し、次にファイル名stemで照合する。"""

    relative_file_path = audio_file_path.relative_to(
        project_root_directory
    ).as_posix()

    performance = performance_by_file_path.get(relative_file_path)
    if performance is not None:
        return performance, "item.files[].file_name"

    performance = performance_by_id.get(audio_file_path.stem)
    if performance is not None:
        return performance, "ファイル名stem"

    return None, "対応なし"
