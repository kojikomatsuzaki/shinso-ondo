"""新荘音頭の正本メタデータを各用途へ変換するための共通部品。"""

from .loader import load_yaml_metadata
from .mapper import build_audio_metadata
from .matcher import (
    build_performance_indexes,
    find_audio_files,
    match_audio_file_to_performance,
)
from .model import AudioMetadata

__all__ = [
    "AudioMetadata",
    "build_audio_metadata",
    "build_performance_indexes",
    "find_audio_files",
    "load_yaml_metadata",
    "match_audio_file_to_performance",
]
