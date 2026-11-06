#!/usr/bin/env bash
# ==============================================================================
# AI Agent Skills Installer
# Seamless installer for Antigravity, Claude Code, Cursor, Codex & OpenCode
# ==============================================================================

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILLS_DIR="$SCRIPT_DIR/skills"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

echo -e "${CYAN}====================================================${NC}"
echo -e "${CYAN}        🤖 AI Agent Skills Installer               ${NC}"
echo -e "${CYAN}        260+ Curated Skills for AI Agents          ${NC}"
echo -e "${CYAN}====================================================${NC}"

usage() {
    echo -e "Usage: $0 [options]"
    echo ""
    echo "Options:"
    echo "  --target <dir>       Target skills directory (e.g., ~/.gemini/config/skills)"
    echo "  --category <cat>     Install only a specific category"
    echo "                       (engineering-workflow, frontend-ui, motion-animation,"
    echo "                        presentation-docs, ai-media-generation,"
    echo "                        marketing-copywriting, agent-tools-guides)"
    echo "  --skill <name>       Install a single skill by name"
    echo "  --link               Create symbolic links instead of copying"
    echo "  --help               Display this help message"
    echo ""
    echo "Default Targets:"
    echo "  1) Antigravity Global:    ~/.gemini/config/skills"
    echo "  2) Claude Code Global:    ~/.claude/skills"
    echo "  3) Codex Global:          ~/.codex/skills"
    echo "  4) Current Workspace:     ./.agents/skills"
    exit 1
}

# Parse options
TARGET_DIR=""
SELECTED_CATEGORY=""
SELECTED_SKILL=""
USE_SYMLINK=false

while [[ "$#" -gt 0 ]]; do
    case $1 in
        --target) TARGET_DIR="$2"; shift ;;
        --category) SELECTED_CATEGORY="$2"; shift ;;
        --skill) SELECTED_SKILL="$2"; shift ;;
        --link) USE_SYMLINK=true ;;
        --help) usage ;;
        *) echo -e "${RED}Unknown option: $1${NC}"; usage ;;
    esac
    shift
done

# If no target specified, detect or prompt
if [ -z "$TARGET_DIR" ]; then
    echo -e "\n${YELLOW}Choose target installation directory:${NC}"
    echo "1) Antigravity (~/.gemini/config/skills)"
    echo "2) Claude Code (~/.claude/skills)"
    echo "3) Codex (~/.codex/skills)"
    echo "4) Current Project Directory (./.agents/skills)"
    echo "5) Custom path"
    
    read -p "Enter choice [1-5] (default: 1): " choice
    case $choice in
        2) TARGET_DIR="$HOME/.claude/skills" ;;
        3) TARGET_DIR="$HOME/.codex/skills" ;;
        4) TARGET_DIR="$(pwd)/.agents/skills" ;;
        5) read -p "Enter custom target directory path: " TARGET_DIR ;;
        *) TARGET_DIR="$HOME/.gemini/config/skills" ;;
    esac
fi

# Expand tilde in target directory
TARGET_DIR="${TARGET_DIR/#\~/$HOME}"
mkdir -p "$TARGET_DIR"

echo -e "\n${BLUE}Target directory:${NC} $TARGET_DIR"
[ "$USE_SYMLINK" = true ] && echo -e "${BLUE}Mode:${NC} Symbolic Link" || echo -e "${BLUE}Mode:${NC} Copy"

install_skill() {
    local src="$1"
    local skill_name="$(basename "$src")"
    local dest="$TARGET_DIR/$skill_name"

    if [ "$USE_SYMLINK" = true ]; then
        ln -sfn "$src" "$dest"
    else
        rm -rf "$dest"
        cp -r "$src" "$dest"
    fi
}

installed_count=0

if [ -n "$SELECTED_SKILL" ]; then
    found_path=$(find "$SKILLS_DIR" -mindepth 2 -maxdepth 2 -type d -name "$SELECTED_SKILL" | head -n 1)
    if [ -z "$found_path" ]; then
        echo -e "${RED}Error: Skill '$SELECTED_SKILL' not found.${NC}"
        exit 1
    fi
    install_skill "$found_path"
    echo -e "${GREEN}✓ Successfully installed '$SELECTED_SKILL' into $TARGET_DIR${NC}"
    exit 0
fi

for cat_dir in "$SKILLS_DIR"/*; do
    if [ ! -d "$cat_dir" ]; then continue; fi
    cat_name="$(basename "$cat_dir")"

    if [ -n "$SELECTED_CATEGORY" ] && [ "$SELECTED_CATEGORY" != "$cat_name" ]; then
        continue
    fi

    echo -e "\n${YELLOW}Installing category: ${cat_name}${NC}"
    for skill_path in "$cat_dir"/*; do
        if [ ! -d "$skill_path" ]; then continue; fi
        install_skill "$skill_path"
        ((installed_count++))
    done
done

echo -e "\n${GREEN}====================================================${NC}"
echo -e "${GREEN}🎉 Successfully installed $installed_count skills into:${NC}"
echo -e "${GREEN}   $TARGET_DIR${NC}"
echo -e "${GREEN}====================================================${NC}"
