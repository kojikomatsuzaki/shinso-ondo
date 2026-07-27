#!/usr/bin/env bash
set -euo pipefail

# 新荘音頭デジタルアーカイブ
# index-en.html を削除し、現在の変更をコミットして push するスクリプト
#
# 使い方:
#   1. このファイルをリポジトリ直下へ置く
#   2. chmod +x push-update.sh
#   3. ./push-update.sh
#
# 任意のコミットメッセージ:
#   ./push-update.sh "Update multilingual top page and documentation"

COMMIT_MESSAGE="${1:-Update top page structure and remove index-en.html}"

# Git リポジトリ内か確認
if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
    echo "エラー: Gitリポジトリ内で実行してください。"
    exit 1
fi

REPO_ROOT="$(git rev-parse --show-toplevel)"
cd "$REPO_ROOT"

echo "リポジトリ: $REPO_ROOT"

# 念のため対象リポジトリか確認
REPO_NAME="$(basename "$REPO_ROOT")"
if [[ "$REPO_NAME" != "shinso-ondo" ]]; then
    echo "注意: 現在のリポジトリ名は '$REPO_NAME' です。"
    read -r -p "このリポジトリで続行しますか？ [y/N]: " answer
    case "$answer" in
        y|Y|yes|YES) ;;
        *) echo "中止しました。"; exit 1 ;;
    esac
fi

# 廃止した英語版トップページを削除
if [[ -e "index-en.html" ]]; then
    rm -f "index-en.html"
    echo "削除: index-en.html"
else
    echo "index-en.html は既に存在しません。"
fi

echo
echo "現在の変更:"
git status --short

if git diff --quiet && git diff --cached --quiet && [[ -z "$(git ls-files --others --exclude-standard)" ]]; then
    echo
    echo "コミット対象の変更はありません。"
    exit 0
fi

echo
read -r -p "上記の変更をすべてコミットして push しますか？ [y/N]: " answer
case "$answer" in
    y|Y|yes|YES) ;;
    *) echo "中止しました。"; exit 1 ;;
esac

# 削除・変更・新規作成をすべてステージ
git add -A

echo
echo "ステージ済みの変更:"
git diff --cached --stat

# コミット
git commit -m "$COMMIT_MESSAGE"

# 現在のブランチを確認
BRANCH="$(git branch --show-current)"
if [[ -z "$BRANCH" ]]; then
    echo "エラー: detached HEAD のため push できません。"
    exit 1
fi

# upstream の有無に応じて push
if git rev-parse --abbrev-ref --symbolic-full-name '@{u}' >/dev/null 2>&1; then
    git push
else
    git push -u origin "$BRANCH"
fi

echo
echo "完了しました。"
echo "ブランチ: $BRANCH"
echo "コミット: $(git rev-parse --short HEAD)"
