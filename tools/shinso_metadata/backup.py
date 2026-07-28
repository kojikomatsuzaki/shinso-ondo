"""音源タグを書き込む前のバックアップ処理。"""

from __future__ import annotations

from datetime import datetime
from pathlib import Path
import shutil


def create_backup_directory(project_root_directory: Path) -> Path:
    """実行時刻ごとのバックアップディレクトリを作成する。"""

    timestamp = datetime.now().astimezone().strftime("%Y%m%d-%H%M%S")
    backup_directory = (
        project_root_directory
        / "backups"
        / "audio-tags"
        / timestamp
    )
    backup_directory.mkdir(parents=True, exist_ok=False)
    return backup_directory


def backup_audio_file(
    audio_file_path: Path,
    project_root_directory: Path,
    backup_directory: Path,
) -> Path:
    """音源をプロジェクト内の相対パスを保って複製する。"""

    relative_file_path = audio_file_path.relative_to(
        project_root_directory
    )
    backup_file_path = backup_directory / relative_file_path
    backup_file_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(audio_file_path, backup_file_path)
    return backup_file_path
