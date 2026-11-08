#!/usr/bin/env bash
# Installs the hack-* skills for Claude Code (user-level, available in every project).
# Uses symlinks so edits made by hack-retro land in this git clone and can be committed.
set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CLAUDE_DIR="${CLAUDE_CONFIG_DIR:-$HOME/.claude}"
SKILLS_DIR="$CLAUDE_DIR/skills"

mkdir -p "$SKILLS_DIR"

link() {  # link <target> <link_path>
  local target="$1" path="$2"
  if [ -L "$path" ]; then
    ln -sfn "$target" "$path"
  elif [ -e "$path" ]; then
    echo "skip: $path exists and is not a symlink (remove it to install)" >&2
    return
  else
    ln -s "$target" "$path"
  fi
  echo "linked $path -> $target"
}

link "$REPO" "$CLAUDE_DIR/hack-hackathon"
for skill in "$REPO"/skills/*/; do
  link "${skill%/}" "$SKILLS_DIR/$(basename "$skill")"
done

echo
echo "Done. Start Claude Code in your hackathon project and run /hack"
