"""書き込んだ音源タグを再読込して検証する。"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from mutagen.mp3 import MP3
from mutagen.wave import WAVE

from .model import AudioMetadata


@dataclass(frozen=True, slots=True)
class VerificationResult:
    """音源一件分のタグ検証結果。"""

    audio_file_path: Path
    errors: tuple[str, ...]

    @property
    def is_valid(self) -> bool:
        return not self.errors


def _expected_title(audio_metadata: AudioMetadata) -> str:
    if audio_metadata.version_title:
        return (
            f"{audio_metadata.title}"
            f"（{audio_metadata.version_title}）"
        )
    return audio_metadata.title


def _frame_text(tags: object, frame_id: str) -> str | None:
    frame = tags.get(frame_id)  # type: ignore[attr-defined]
    if frame is None:
        return None
    text = getattr(frame, "text", None)
    if isinstance(text, list) and text:
        return str(text[0])
    return None


def _compare(
    errors: list[str],
    label: str,
    actual: str | None,
    expected: str | None,
) -> None:
    if actual != expected:
        errors.append(
            f"{label}: expected={expected!r}, actual={actual!r}"
        )


def verify_audio_tags(
    audio_file_path: Path,
    audio_metadata: AudioMetadata,
) -> VerificationResult:
    """必須タグを再読込して期待値と比較する。"""

    extension = audio_file_path.suffix.lower()
    if extension == ".mp3":
        audio = MP3(audio_file_path)
    elif extension == ".wav":
        audio = WAVE(audio_file_path)
    else:
        return VerificationResult(
            audio_file_path,
            (f"検証未対応の形式です: {extension}",),
        )

    if audio.tags is None:
        return VerificationResult(
            audio_file_path,
            ("ID3タグがありません。",),
        )

    errors: list[str] = []
    _compare(
        errors,
        "Title",
        _frame_text(audio.tags, "TIT2"),
        _expected_title(audio_metadata),
    )
    _compare(
        errors,
        "Album",
        _frame_text(audio.tags, "TALB"),
        audio_metadata.title,
    )
    _compare(
        errors,
        "Artist",
        _frame_text(audio.tags, "TPE1"),
        " / ".join(audio_metadata.artists) or None,
    )
    _compare(
        errors,
        "Performance ID",
        _frame_text(
            audio.tags,
            "TXXX:PERFORMANCE_ID",
        ),
        audio_metadata.performance_id,
    )
    _compare(
        errors,
        "License",
        _frame_text(audio.tags, "TXXX:LICENSE"),
        audio_metadata.license_name,
    )

    return VerificationResult(
        audio_file_path=audio_file_path,
        errors=tuple(errors),
    )
