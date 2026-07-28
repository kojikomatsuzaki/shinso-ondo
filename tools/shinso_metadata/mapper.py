"""正本YAMLから用途別モデルへの変換。"""

from __future__ import annotations

from typing import Any

from .model import AudioMetadata


def as_list(value: Any) -> list[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def unique_strings(values: list[str]) -> tuple[str, ...]:
    result: list[str] = []
    for value in values:
        normalized = value.strip()
        if normalized and normalized not in result:
            result.append(normalized)
    return tuple(result)


def get_agent_name(agent: Any) -> str | None:
    if isinstance(agent, str):
        return agent.strip() or None
    if not isinstance(agent, dict):
        return None
    name = agent.get("name")
    if isinstance(name, str) and name.strip():
        return name.strip()
    return None


def string_or_none(value: Any) -> str | None:
    if value is None:
        return None
    converted = str(value).strip()
    return converted or None


def extract_main_title(metadata: dict[str, Any]) -> str:
    work = metadata.get("work", {})
    if not isinstance(work, dict):
        return "新荘音頭"

    title = work.get("title")
    if isinstance(title, str) and title.strip():
        return title.strip()
    if isinstance(title, dict):
        main_title = title.get("main")
        if isinstance(main_title, str) and main_title.strip():
            return main_title.strip()
    return "新荘音頭"


def extract_credit_names(
    metadata: dict[str, Any],
    role: str,
) -> tuple[str, ...]:
    work = metadata.get("work", {})
    if not isinstance(work, dict):
        return ()

    credits = work.get("credits")
    names: list[str] = []

    if isinstance(credits, dict):
        for entry in as_list(credits.get(role)):
            name = get_agent_name(entry)
            if name:
                names.append(name)
    elif isinstance(credits, list):
        for credit in credits:
            if not isinstance(credit, dict) or credit.get("role") != role:
                continue
            name = get_agent_name(credit)
            if name:
                names.append(name)

    return unique_strings(names)


def extract_rights_information(
    metadata: dict[str, Any],
) -> tuple[str | None, str | None, str | None]:
    rights = metadata.get("rights", {})
    if not isinstance(rights, dict):
        return None, None, None

    holders = [
        name
        for holder in as_list(rights.get("rightsholder"))
        if (name := get_agent_name(holder))
    ]
    copyright_notice = (
        "© " + " / ".join(unique_strings(holders)) if holders else None
    )

    license_value = rights.get("license")
    license_name: str | None = None
    license_url: str | None = None

    if isinstance(license_value, str):
        license_name = license_value.strip() or None
    elif isinstance(license_value, dict):
        for key in ("abbreviation", "name", "label"):
            candidate = license_value.get(key)
            if isinstance(candidate, str) and candidate.strip():
                license_name = candidate.strip()
                break
        for key in ("url", "URL", "uri"):
            candidate = license_value.get(key)
            if isinstance(candidate, str) and candidate.strip():
                license_url = candidate.strip()
                break

    return copyright_notice, license_name, license_url


def extract_repository_url(metadata: dict[str, Any]) -> str | None:
    repository = metadata.get("repository")
    if isinstance(repository, str):
        return repository.strip() or None
    if not isinstance(repository, dict):
        return None

    for key in ("url", "repository_url", "web_url", "html_url"):
        candidate = repository.get(key)
        if isinstance(candidate, str) and candidate.strip():
            return candidate.strip()
    return None


def extract_performer_names(
    performance: dict[str, Any],
    role: str,
) -> tuple[str, ...]:
    names: list[str] = []
    for performer in as_list(performance.get("performers")):
        if not isinstance(performer, dict) or performer.get("role") != role:
            continue
        name = get_agent_name(performer)
        if name:
            names.append(name)
    return unique_strings(names)


def build_audio_metadata(
    metadata: dict[str, Any],
    performance: dict[str, Any],
) -> AudioMetadata:
    performance_id = performance.get("id")
    if not isinstance(performance_id, str) or not performance_id.strip():
        raise ValueError("performances の各項目には id が必要です。")

    version_title = performance.get("version_title")
    if not isinstance(version_title, str):
        version_title = ""

    manifestation = performance.get("manifestation", {})
    if not isinstance(manifestation, dict):
        manifestation = {}

    conductor_names = extract_performer_names(performance, "conductor")
    copyright_notice, license_name, license_url = extract_rights_information(
        metadata
    )

    return AudioMetadata(
        performance_id=performance_id.strip(),
        title=extract_main_title(metadata),
        version_title=version_title.strip(),
        artists=extract_performer_names(performance, "vocals"),
        musicians=extract_performer_names(performance, "musician"),
        conductor=conductor_names[0] if conductor_names else None,
        composer=extract_credit_names(metadata, "composer"),
        arranger=extract_credit_names(metadata, "arranger"),
        lyricist=extract_credit_names(metadata, "lyricist"),
        producer=extract_credit_names(metadata, "producer"),
        recording_date=string_or_none(manifestation.get("recording_date")),
        publication_date=string_or_none(manifestation.get("publication_date")),
        copyright_notice=copyright_notice,
        license_name=license_name,
        license_url=license_url,
        repository_url=extract_repository_url(metadata),
    )
