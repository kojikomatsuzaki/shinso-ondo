"""正本YAMLの読み込み。"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml


def load_yaml_metadata(metadata_file_path: Path) -> dict[str, Any]:
    """YAML正本を辞書として読み込む。"""

    if not metadata_file_path.exists():
        raise FileNotFoundError(
            "メタデータ正本が見つかりません。\n"
            f"確認した場所: {metadata_file_path}"
        )

    with metadata_file_path.open("r", encoding="utf-8") as metadata_file:
        loaded_metadata = yaml.safe_load(metadata_file)

    if loaded_metadata is None:
        raise ValueError("メタデータ正本が空です。")

    if not isinstance(loaded_metadata, dict):
        raise ValueError("YAMLの最上位要素は辞書形式である必要があります。")

    return loaded_metadata
