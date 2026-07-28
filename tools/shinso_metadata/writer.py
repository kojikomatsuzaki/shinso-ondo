"""AudioMetadataをMP3・WAVのID3タグへ書き込む。"""

from __future__ import annotations

from pathlib import Path

from mutagen.id3 import (
    APIC,
    COMM,
    ID3,
    TALB,
    TCOM,
    TCOP,
    TDRC,
    TDRL,
    TEXT,
    TIT2,
    TIPL,
    TPE1,
    TPE2,
    TPE3,
    TXXX,
    WXXX,
)
from mutagen.mp3 import MP3
from mutagen.wave import WAVE

from .model import AudioMetadata

SUPPORTED_WRITABLE_EXTENSIONS = {".mp3", ".wav"}


def _join(values: tuple[str, ...]) -> str:
    return " / ".join(values)


def _display_title(audio_metadata: AudioMetadata) -> str:
    if audio_metadata.version_title:
        return (
            f"{audio_metadata.title}"
            f"（{audio_metadata.version_title}）"
        )
    return audio_metadata.title


def _set_text_frame(tags: ID3, frame: object) -> None:
    tags.delall(frame.HashKey)  # type: ignore[attr-defined]
    tags.add(frame)  # type: ignore[arg-type]


def _set_txxx(tags: ID3, description: str, value: str | None) -> None:
    tags.delall(f"TXXX:{description}")
    if value:
        tags.add(TXXX(encoding=3, desc=description, text=[value]))


def _set_wxxx(tags: ID3, description: str, value: str | None) -> None:
    tags.delall(f"WXXX:{description}")
    if value:
        tags.add(WXXX(encoding=3, desc=description, url=value))


def _set_common_id3_tags(
    tags: ID3,
    audio_metadata: AudioMetadata,
    cover_art_file_path: Path | None,
) -> None:
    """MP3とWAVに共通するID3フレームを設定する。"""

    _set_text_frame(
        tags,
        TIT2(encoding=3, text=[_display_title(audio_metadata)]),
    )
    _set_text_frame(
        tags,
        TALB(encoding=3, text=[audio_metadata.title]),
    )

    if audio_metadata.artists:
        _set_text_frame(
            tags,
            TPE1(encoding=3, text=[_join(audio_metadata.artists)]),
        )
    else:
        tags.delall("TPE1")

    if audio_metadata.musicians:
        _set_text_frame(
            tags,
            TPE2(encoding=3, text=[_join(audio_metadata.musicians)]),
        )
    else:
        tags.delall("TPE2")

    if audio_metadata.conductor:
        _set_text_frame(
            tags,
            TPE3(encoding=3, text=[audio_metadata.conductor]),
        )
    else:
        tags.delall("TPE3")

    if audio_metadata.composer:
        _set_text_frame(
            tags,
            TCOM(encoding=3, text=[_join(audio_metadata.composer)]),
        )
    else:
        tags.delall("TCOM")

    if audio_metadata.lyricist:
        _set_text_frame(
            tags,
            TEXT(encoding=3, text=[_join(audio_metadata.lyricist)]),
        )
    else:
        tags.delall("TEXT")

    involved_people: list[list[str]] = []
    involved_people.extend(
        ["arranger", name] for name in audio_metadata.arranger
    )
    involved_people.extend(
        ["producer", name] for name in audio_metadata.producer
    )
    tags.delall("TIPL")
    if involved_people:
        tags.add(TIPL(encoding=3, people=involved_people))

    if audio_metadata.recording_date:
        _set_text_frame(
            tags,
            TDRC(encoding=3, text=[audio_metadata.recording_date]),
        )
    else:
        tags.delall("TDRC")

    if audio_metadata.publication_date:
        _set_text_frame(
            tags,
            TDRL(encoding=3, text=[audio_metadata.publication_date]),
        )
    else:
        tags.delall("TDRL")

    if audio_metadata.copyright_notice:
        _set_text_frame(
            tags,
            TCOP(encoding=3, text=[audio_metadata.copyright_notice]),
        )
    else:
        tags.delall("TCOP")

    _set_txxx(tags, "SUBTITLE", audio_metadata.version_title)
    _set_txxx(tags, "PERFORMANCE_ID", audio_metadata.performance_id)
    _set_txxx(tags, "LICENSE", audio_metadata.license_name)
    _set_wxxx(tags, "LICENSE", audio_metadata.license_url)
    _set_wxxx(tags, "REPOSITORY", audio_metadata.repository_url)

    tags.delall("COMM:archive-note:jpn")
    tags.add(
        COMM(
            encoding=3,
            lang="jpn",
            desc="archive-note",
            text=[
                "metadata/shinso-ondo.yaml を正本として生成"
            ],
        )
    )

    tags.delall("APIC")
    if cover_art_file_path and cover_art_file_path.exists():
        mime_type = (
            "image/png"
            if cover_art_file_path.suffix.lower() == ".png"
            else "image/jpeg"
        )
        tags.add(
            APIC(
                encoding=3,
                mime=mime_type,
                type=3,
                desc="Cover",
                data=cover_art_file_path.read_bytes(),
            )
        )


def write_audio_tags(
    audio_file_path: Path,
    audio_metadata: AudioMetadata,
    cover_art_file_path: Path | None = None,
) -> None:
    """音源形式に応じてID3タグを書き込む。"""

    extension = audio_file_path.suffix.lower()
    if extension not in SUPPORTED_WRITABLE_EXTENSIONS:
        raise ValueError(
            f"タグ書き込み未対応の形式です: {extension}"
        )

    if extension == ".mp3":
        audio = MP3(audio_file_path, ID3=ID3)
        if audio.tags is None:
            audio.add_tags()
        assert audio.tags is not None
        _set_common_id3_tags(
            audio.tags,
            audio_metadata,
            cover_art_file_path,
        )
        audio.save(v2_version=3)
        return

    audio = WAVE(audio_file_path)
    if audio.tags is None:
        audio.add_tags()
    assert audio.tags is not None
    _set_common_id3_tags(
        audio.tags,
        audio_metadata,
        cover_art_file_path,
    )
    audio.save()
