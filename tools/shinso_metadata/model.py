"""正本YAMLから生成する用途別メタデータモデル。"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class AudioMetadata:
    """音源タグとプレビューで共通利用する中間メタデータ。"""

    performance_id: str
    title: str
    version_title: str
    artists: tuple[str, ...]
    musicians: tuple[str, ...]
    conductor: str | None
    composer: tuple[str, ...]
    arranger: tuple[str, ...]
    lyricist: tuple[str, ...]
    producer: tuple[str, ...]
    recording_date: str | None
    publication_date: str | None
    copyright_notice: str | None
    license_name: str | None
    license_url: str | None
    repository_url: str | None
