#!/usr/bin/env python3
"""
新荘音頭デジタルアーカイブ
音源メタデータ更新スクリプト

metadata/shinso-ondo.yaml を正本として読み込み、
audio/ 以下の各音源ファイルを performances の情報と照合し、
書き込み予定の音源メタデータを表示する。

この版では音源ファイルを変更しない。
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
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
# Audio Metadata Model
# ==========================================

@dataclass(frozen=True)
class AudioMetadata:
    """
    YAML正本から音源タグ向けに組み立てた中間メタデータ。
    """

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


# ==========================================
# Command-line Arguments
# ==========================================

def parse_command_line_arguments() -> argparse.Namespace:
    """
    コマンドライン引数を読み込む。
    """

    argument_parser = argparse.ArgumentParser(
        description=(
            "新荘音頭のYAML正本と音源ファイルを照合し、"
            "音源タグの書き込み予定を表示します。"
            "この版では実ファイルを変更しません。"
        )
    )

    argument_parser.add_argument(
        "--show-metadata",
        action="store_true",
        help="読み込んだYAMLの内容全体を表示します。",
    )

    argument_parser.add_argument(
        "--show-unmatched-only",
        action="store_true",
        help="YAMLと対応しない音源だけを表示します。",
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
# General Helpers
# ==========================================

def as_list(value: Any) -> list[Any]:
    """
    値を安全にリストとして扱う。
    """

    if value is None:
        return []

    if isinstance(value, list):
        return value

    return [value]


def unique_strings(values: list[str]) -> tuple[str, ...]:
    """
    文字列の順序を維持したまま重複を除く。
    """

    result: list[str] = []

    for value in values:
        normalized_value = value.strip()

        if (
            normalized_value
            and normalized_value not in result
        ):
            result.append(normalized_value)

    return tuple(result)


def get_agent_name(agent: Any) -> str | None:
    """
    人物・組織情報から表示名を取り出す。
    """

    if isinstance(agent, str):
        stripped_agent = agent.strip()
        return stripped_agent or None

    if not isinstance(agent, dict):
        return None

    name = agent.get("name")

    if isinstance(name, str) and name.strip():
        return name.strip()

    return None


def get_nested_value(
    mapping: dict[str, Any],
    *keys: str,
) -> Any:
    """
    辞書を安全にたどる。
    """

    current_value: Any = mapping

    for key in keys:
        if not isinstance(current_value, dict):
            return None

        current_value = current_value.get(key)

    return current_value


# ==========================================
# Work Metadata Extraction
# ==========================================

def extract_main_title(metadata: dict[str, Any]) -> str:
    """
    作品の本タイトルを取得する。
    """

    work = metadata.get("work", {})

    if not isinstance(work, dict):
        return "新荘音頭"

    title = work.get("title")

    if isinstance(title, str) and title.strip():
        return title.strip()

    if isinstance(title, dict):
        main_title = title.get("main")

        if (
            isinstance(main_title, str)
            and main_title.strip()
        ):
            return main_title.strip()

    return "新荘音頭"


def extract_credit_names(
    metadata: dict[str, Any],
    role: str,
) -> tuple[str, ...]:
    """
    work.credits から指定された役割の名前を取得する。

    辞書形式と、role付きリスト形式の両方を扱う。
    """

    work = metadata.get("work", {})

    if not isinstance(work, dict):
        return ()

    credits = work.get("credits")

    names: list[str] = []

    if isinstance(credits, dict):
        role_entries = as_list(credits.get(role))

        for role_entry in role_entries:
            name = get_agent_name(role_entry)

            if name:
                names.append(name)

    elif isinstance(credits, list):
        for credit in credits:
            if not isinstance(credit, dict):
                continue

            if credit.get("role") != role:
                continue

            name = get_agent_name(credit)

            if name:
                names.append(name)

    return unique_strings(names)


# ==========================================
# Rights Metadata Extraction
# ==========================================

def extract_rights_information(
    metadata: dict[str, Any],
) -> tuple[
    str | None,
    str | None,
    str | None,
]:
    """
    権利表示、ライセンス名、ライセンスURLを取得する。
    """

    rights = metadata.get("rights", {})

    if not isinstance(rights, dict):
        return None, None, None

    rightsholder_names: list[str] = []

    for rightsholder in as_list(
        rights.get("rightsholder")
    ):
        name = get_agent_name(rightsholder)

        if name:
            rightsholder_names.append(name)

    copyright_notice: str | None = None

    if rightsholder_names:
        copyright_notice = (
            "© "
            + " / ".join(
                unique_strings(rightsholder_names)
            )
        )

    license_value = rights.get("license")

    license_name: str | None = None
    license_url: str | None = None

    if isinstance(license_value, str):
        license_name = license_value.strip() or None

    elif isinstance(license_value, dict):
        for key in (
            "abbreviation",
            "name",
            "label",
        ):
            candidate = license_value.get(key)

            if (
                isinstance(candidate, str)
                and candidate.strip()
            ):
                license_name = candidate.strip()
                break

        for key in (
            "url",
            "URL",
            "uri",
        ):
            candidate = license_value.get(key)

            if (
                isinstance(candidate, str)
                and candidate.strip()
            ):
                license_url = candidate.strip()
                break

    return (
        copyright_notice,
        license_name,
        license_url,
    )


def extract_repository_url(
    metadata: dict[str, Any],
) -> str | None:
    """
    repository セクションからURLを取得する。
    """

    repository = metadata.get("repository")

    if isinstance(repository, str):
        return repository.strip() or None

    if not isinstance(repository, dict):
        return None

    for key in (
        "url",
        "repository_url",
        "web_url",
        "html_url",
    ):
        candidate = repository.get(key)

        if (
            isinstance(candidate, str)
            and candidate.strip()
        ):
            return candidate.strip()

    return None


# ==========================================
# Performance Metadata Extraction
# ==========================================

def extract_performer_names(
    performance: dict[str, Any],
    role: str,
) -> tuple[str, ...]:
    """
    performance.performers から指定役割の名前を取得する。
    """

    names: list[str] = []

    for performer in as_list(
        performance.get("performers")
    ):
        if not isinstance(performer, dict):
            continue

        if performer.get("role") != role:
            continue

        name = get_agent_name(performer)

        if name:
            names.append(name)

    return unique_strings(names)


def extract_conductor_name(
    performance: dict[str, Any],
) -> str | None:
    """
    指揮者名を取得する。
    """

    conductor_names = extract_performer_names(
        performance,
        "conductor",
    )

    if conductor_names:
        return conductor_names[0]

    return None


def build_audio_metadata(
    metadata: dict[str, Any],
    performance: dict[str, Any],
) -> AudioMetadata:
    """
    YAML正本から音源タグ向け中間メタデータを生成する。
    """

    performance_id = performance.get("id")

    if (
        not isinstance(performance_id, str)
        or not performance_id.strip()
    ):
        raise ValueError(
            "performances の各項目には id が必要です。"
        )

    version_title = performance.get(
        "version_title"
    )

    if not isinstance(version_title, str):
        version_title = ""

    manifestation = performance.get(
        "manifestation",
        {},
    )

    if not isinstance(manifestation, dict):
        manifestation = {}

    copyright_notice, license_name, license_url = (
        extract_rights_information(metadata)
    )

    return AudioMetadata(
        performance_id=performance_id.strip(),
        title=extract_main_title(metadata),
        version_title=version_title.strip(),
        artists=extract_performer_names(
            performance,
            "vocals",
        ),
        musicians=extract_performer_names(
            performance,
            "musician",
        ),
        conductor=extract_conductor_name(
            performance
        ),
        composer=extract_credit_names(
            metadata,
            "composer",
        ),
        arranger=extract_credit_names(
            metadata,
            "arranger",
        ),
        lyricist=extract_credit_names(
            metadata,
            "lyricist",
        ),
        producer=extract_credit_names(
            metadata,
            "producer",
        ),
        recording_date=string_or_none(
            manifestation.get("recording_date")
        ),
        publication_date=string_or_none(
            manifestation.get("publication_date")
        ),
        copyright_notice=copyright_notice,
        license_name=license_name,
        license_url=license_url,
        repository_url=extract_repository_url(
            metadata
        ),
    )


def string_or_none(value: Any) -> str | None:
    """
    値を文字列へ変換する。
    """

    if value is None:
        return None

    converted_value = str(value).strip()

    return converted_value or None


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
# Performance Index
# ==========================================

def build_performance_indexes(
    metadata: dict[str, Any],
) -> tuple[
    dict[str, dict[str, Any]],
    dict[str, dict[str, Any]],
]:
    """
    performance.id と item.files[].file_name の索引を作る。
    """

    performances = metadata.get("performances")

    if not isinstance(performances, list):
        raise ValueError(
            "YAMLに performances のリストがありません。"
        )

    by_id: dict[str, dict[str, Any]] = {}
    by_file_path: dict[str, dict[str, Any]] = {}

    for performance in performances:
        if not isinstance(performance, dict):
            continue

        performance_id = performance.get("id")

        if (
            not isinstance(performance_id, str)
            or not performance_id.strip()
        ):
            raise ValueError(
                "performances に id のない項目があります。"
            )

        normalized_performance_id = (
            performance_id.strip()
        )

        if normalized_performance_id in by_id:
            raise ValueError(
                "performance.id が重複しています: "
                f"{normalized_performance_id}"
            )

        by_id[normalized_performance_id] = (
            performance
        )

        item = performance.get("item", {})

        if not isinstance(item, dict):
            continue

        files = item.get("files", [])

        for file_metadata in as_list(files):
            if not isinstance(
                file_metadata,
                dict,
            ):
                continue

            file_name = file_metadata.get(
                "file_name"
            )

            if (
                not isinstance(file_name, str)
                or not file_name.strip()
            ):
                continue

            normalized_file_path = (
                Path(file_name)
                .as_posix()
                .lstrip("./")
            )

            if normalized_file_path in by_file_path:
                raise ValueError(
                    "item.files[].file_name が"
                    "重複しています: "
                    f"{normalized_file_path}"
                )

            by_file_path[normalized_file_path] = (
                performance
            )

    return by_id, by_file_path


def match_audio_file_to_performance(
    audio_file_path: Path,
    performance_by_id: dict[
        str,
        dict[str, Any],
    ],
    performance_by_file_path: dict[
        str,
        dict[str, Any],
    ],
) -> tuple[dict[str, Any] | None, str]:
    """
    音源ファイルを演奏情報へ対応させる。

    1. item.files[].file_name の完全一致
    2. ファイル名stemとperformance.idの一致
    """

    relative_file_path = (
        audio_file_path
        .relative_to(PROJECT_ROOT_DIRECTORY)
        .as_posix()
    )

    performance = performance_by_file_path.get(
        relative_file_path
    )

    if performance is not None:
        return performance, "item.files[].file_name"

    performance = performance_by_id.get(
        audio_file_path.stem
    )

    if performance is not None:
        return performance, "ファイル名stem"

    return None, "対応なし"


# ==========================================
# Display Helpers
# ==========================================

def display_value(
    label: str,
    value: str | tuple[str, ...] | None,
) -> None:
    """
    一つのメタデータ項目を表示する。
    """

    if isinstance(value, tuple):
        display_text = " / ".join(value)
    else:
        display_text = value or "（未設定）"

    print(f"  {label:<14}: {display_text}")


def display_audio_metadata_preview(
    audio_file_path: Path,
    audio_metadata: AudioMetadata,
    match_method: str,
) -> None:
    """
    音源一件分の書き込み予定を表示する。
    """

    relative_file_path = (
        audio_file_path
        .relative_to(PROJECT_ROOT_DIRECTORY)
    )

    print()
    print("○ 対応する演奏情報が見つかりました")
    print(f"  ファイル       : {relative_file_path}")
    print(f"  形式           : {audio_file_path.suffix.lower()}")
    print(f"  照合方法       : {match_method}")
    print(f"  performance ID : {audio_metadata.performance_id}")

    display_value(
        "タイトル",
        audio_metadata.title,
    )
    display_value(
        "版表示",
        audio_metadata.version_title,
    )
    display_value(
        "歌唱",
        audio_metadata.artists,
    )
    display_value(
        "演奏",
        audio_metadata.musicians,
    )
    display_value(
        "指揮",
        audio_metadata.conductor,
    )
    display_value(
        "作曲",
        audio_metadata.composer,
    )
    display_value(
        "編曲",
        audio_metadata.arranger,
    )
    display_value(
        "作詞",
        audio_metadata.lyricist,
    )
    display_value(
        "制作",
        audio_metadata.producer,
    )
    display_value(
        "録音年",
        audio_metadata.recording_date,
    )
    display_value(
        "公開日",
        audio_metadata.publication_date,
    )
    display_value(
        "権利表示",
        audio_metadata.copyright_notice,
    )
    display_value(
        "ライセンス",
        audio_metadata.license_name,
    )
    display_value(
        "ライセンスURL",
        audio_metadata.license_url,
    )
    display_value(
        "リポジトリ",
        audio_metadata.repository_url,
    )


def display_unmatched_audio_file(
    audio_file_path: Path,
) -> None:
    """
    対応しない音源を表示する。
    """

    relative_file_path = (
        audio_file_path
        .relative_to(PROJECT_ROOT_DIRECTORY)
    )

    print()
    print("△ 対応する演奏情報がありません")
    print(f"  ファイル : {relative_file_path}")
    print(f"  stem     : {audio_file_path.stem}")


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

    (
        performance_by_id,
        performance_by_file_path,
    ) = build_performance_indexes(metadata)

    matched_file_count = 0
    unmatched_file_count = 0

    print()
    print("==========================================")
    print(" 新荘音頭 音源メタデータ・プレビュー")
    print("==========================================")
    print()
    print(f"メタデータ正本 : {METADATA_FILE_PATH}")
    print(f"検出した音源数 : {len(audio_file_paths)}")
    print(
        "ジャケット画像 : "
        + (
            "あり"
            if COVER_ART_FILE_PATH.exists()
            else "なし"
        )
    )
    print()
    print(
        "注意: この版では音源ファイルを"
        "一切変更しません。"
    )

    for audio_file_path in audio_file_paths:
        (
            performance,
            match_method,
        ) = match_audio_file_to_performance(
            audio_file_path=audio_file_path,
            performance_by_id=performance_by_id,
            performance_by_file_path=(
                performance_by_file_path
            ),
        )

        if performance is None:
            unmatched_file_count += 1

            display_unmatched_audio_file(
                audio_file_path
            )

            continue

        matched_file_count += 1

        if (
            command_line_arguments
            .show_unmatched_only
        ):
            continue

        audio_metadata = build_audio_metadata(
            metadata=metadata,
            performance=performance,
        )

        display_audio_metadata_preview(
            audio_file_path=audio_file_path,
            audio_metadata=audio_metadata,
            match_method=match_method,
        )

    print()
    print("==========================================")
    print(" 照合結果")
    print("==========================================")
    print(f"○ 対応済み : {matched_file_count}")
    print(f"△ 対応なし : {unmatched_file_count}")
    print()

    if matched_file_count:
        print(
            "次段階では、このプレビュー内容を"
            "MP3・WAV向けタグへ変換します。"
        )

    if command_line_arguments.show_metadata:
        display_complete_metadata(metadata)


if __name__ == "__main__":
    main()
