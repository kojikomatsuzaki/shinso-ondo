"""新荘音頭の正本メタデータを各用途へ変換するための共通部品。"""

from .backup import backup_audio_file, create_backup_directory
from .loader import load_yaml_metadata
from .mapper import build_audio_metadata
from .matcher import (
    build_performance_indexes,
    find_audio_files,
    match_audio_file_to_performance,
)
from .model import AudioMetadata
from .verify import VerificationResult, verify_audio_tags
from .writer import SUPPORTED_WRITABLE_EXTENSIONS, write_audio_tags

__all__ = [
    "AudioMetadata",
    "SUPPORTED_WRITABLE_EXTENSIONS",
    "VerificationResult",
    "backup_audio_file",
    "build_audio_metadata",
    "build_performance_indexes",
    "create_backup_directory",
    "find_audio_files",
    "load_yaml_metadata",
    "match_audio_file_to_performance",
    "verify_audio_tags",
    "write_audio_tags",
]
