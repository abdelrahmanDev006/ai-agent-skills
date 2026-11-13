# 🤖 AI Agent Skills Collection

[![Total Skills](https://img.shields.io/badge/Total%20Skills-264-blue.svg)](skills.json)
[![Categories](https://img.shields.io/badge/Categories-7-green.svg)](#-categories-summary)
[![Superpowers](https://img.shields.io/badge/Superpowers-v7.0.2%20Latest-purple.svg)](skills/engineering-workflow/brainstorming)
[![Compatibility](https://img.shields.io/badge/Harness-Antigravity%20%7C%20Claude%20Code%20%7C%20Codex%20%7C%20Cursor%20%7C%20OpenCode-orange.svg)](#-installation--setup)
[![License](https://img.shields.io/badge/License-MIT-brightgreen.svg)](LICENSE)
[![العربية](https://img.shields.io/badge/Language-%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9-red.svg)](README_AR.md)

> A curated, production-ready collection of **264 agent skills** following the open `SKILL.md` specification. Designed for autonomous AI coding agents including **Google Antigravity**, **Claude Code**, **OpenAI Codex**, **Cursor**, and **OpenCode**.

---

## 📚 Quick Navigation

- [✨ Overview](#-overview)
- [📦 Categories Summary](#-categories-summary)
- [🚀 Installation & Setup](#-installation--setup)
- [🔍 Complete Skills Catalog](#-complete-skills-catalog)
  - [🛠️ Engineering & Workflows](#️-engineering-architecture--agent-workflows-75-skills)
  - [🎨 Frontend & UI Design](#-frontend-ui-design--design-systems-56-skills)
  - [✨ AI Media & Generation](#-ai-media-image-audio--video-generation-38-skills)
  - [📄 Presentations & Documents](#-presentations-decks--document-automation-30-skills)
  - [🎬 Motion & Animation](#-motion-gsap--video-animation-28-skills)
  - [🧭 Agent Tools & Guides](#-agent-tools-browsing--assistant-personas-21-skills)
  - [📣 Marketing & Copywriting](#-marketing-brand--copywriting-16-skills)
- [🔄 Updating Skills](#-updating-skills)
- [📄 License](#-license)

---

## ✨ Overview

This repository consolidates the most capable agent skills into a single structured, versioned, and easily deployable hub. Skills follow the standard 3-tier progressive disclosure model:
1. **Metadata Frontmatter (`YAML`)**: Enables instant, lightweight discovery without bloating prompt context.
2. **Core Instructions (`SKILL.md`)**: Loaded on demand when the agent recognizes relevance.
3. **Bundled Assets / Scripts**: Reference guides, deterministic Python/bash scripts, and templates stored alongside the skill.

---

## 📦 Categories Summary

| Category | Count | Primary Focus |
| :--- | :---: | :--- |
| **🛠️ Engineering, Architecture & Agent Workflows** | **75** | Core process skills (Superpowers v7.0.2), test-driven development, systematic debugging, subagent-driven development, code review, merge resolution, Flutter/Dart tooling, and architecture specs. |
| **🎨 Frontend, UI Design & Design Systems** | **56** | Anti-slop design taste, shadcn/ui, brutalist and minimalist systems, Google Stitch, Apple HIG, Figma-to-code pipelines, D3 visualizations, and Three.js 3D shaders. |
| **✨ AI Media, Image, Audio & Video Generation** | **38** | Comprehensive integrations for Fal.ai, Venice.ai, Sora, Google Imagen, Midjourney/DALL-E style image generators, device mockups, and AI music production. |
| **📄 Presentations, Decks & Document Automation** | **30** | Apple Keynote-quality slides, PowerPoint automation (PptxGenJS), OpenXML DOCX, PDF generators, executive memos, and Swiss international editorial layouts. |
| **🎬 Motion, GSAP & Video Animation** | **28** | Full GSAP suite (ScrollTrigger, Flip, Timeline, Performance), Remotion React video compositions, Hyperframes cinematic templates, and micro-interaction polish. |
| **📣 Marketing, Brand & Copywriting** | **16** | Conversion-focused copywriting, creative direction frameworks, advertising psychology, brand voice guides, and social media viral cards. |
| **🧭 Agent Tools, Browsing & Assistant Personas** | **21** | Browser automation with agent-browser, screenshot captures, Antigravity guides, custom MCP server builders, and interactive advisory personas. |

---

## 🚀 Installation & Setup

### Method 1: Automated Script (`install.sh`)
Clone the repository and run the installer:
```bash
git clone https://github.com/abdelrahmanDev006/ai-agent-skills.git
cd ai-agent-skills
chmod +x install.sh
./install.sh
```

#### Selective / Targeted Installation Examples:
```bash
# 1. Install all skills into Antigravity global config:
./install.sh --target ~/.gemini/config/skills

# 2. Install only Frontend & UI skills into current workspace:
./install.sh --category frontend-ui --target ./.agents/skills

# 3. Install a single skill via symlink for zero disk duplication:
./install.sh --skill brainstorming --target ~/.gemini/config/skills --link
```

### Method 2: Manual Installation
Copy the desired category or skill folder directly into your harness directory:
- **Google Antigravity:** `~/.gemini/config/skills/` (Global) or `<workspace>/.agents/skills/`
- **Claude Code:** `~/.claude/skills/` (Global) or `<workspace>/.claude/skills/`
- **Codex / OpenAI:** `~/.codex/skills/`
- **Cursor / Windsurf:** `<workspace>/.agents/skills/`

---

## 🔍 Complete Skills Catalog

### 🛠️ Engineering, Architecture & Agent Workflows (75 skills)

> Core process skills (Superpowers v7.0.2), test-driven development, systematic debugging, subagent-driven development, code review, merge resolution, Flutter/Dart tooling, and architecture specs.

| Skill Name | Description | Link |
| :--- | :--- | :---: |
| **`analyze-github-flake`** | Expertise in analyzing flake github issues in the flutter/flutter repository. Use when a user wants to analyze the flakiness of... | [View](skills/engineering-workflow/analyze-github-flake/SKILL.md) |
| **`brainstorming`** | You MUST use this before any creative work - creating features, building components, adding functionality, modifying behavior, ... | [View](skills/engineering-workflow/brainstorming/SKILL.md) |
| **`caveman`** | > | [View](skills/engineering-workflow/caveman/SKILL.md) |
| **`claude-handoff`** | Hand the current conversation off to a fresh background agent that picks up the work immediately. | [View](skills/engineering-workflow/claude-handoff/SKILL.md) |
| **`code-review`** | Review the changes since a fixed point (commit, branch, tag, or merge-base) along two axes: Standards (does the code follow thi... | [View](skills/engineering-workflow/code-review/SKILL.md) |
| **`dart-log-failure-parser`** | Parse failures from Dart and Flutter test logs. | [View](skills/engineering-workflow/dart-log-failure-parser/SKILL.md) |
| **`diagnosing-bugs`** | Diagnosis loop for hard bugs and performance regressions. Use when the user says "diagnose"/"debug this", or reports something ... | [View](skills/engineering-workflow/diagnosing-bugs/SKILL.md) |
| **`diagnosing-superpowers`** | Use when a superpowers session went wrong and your human partner wants to know why — repeated work, ignored plans, stumbles, po... | [View](skills/engineering-workflow/diagnosing-superpowers/SKILL.md) |
| **`dispatching-parallel-agents`** | Use when facing 2+ independent tasks that can be worked on without shared state or sequential dependencies | [View](skills/engineering-workflow/dispatching-parallel-agents/SKILL.md) |
| **`domain-modeling`** | Build and sharpen a project's domain model. Use when discussing codebase terminology, writing or editing a CONTEXT.md, or recor... | [View](skills/engineering-workflow/domain-modeling/SKILL.md) |
| **`executing-plans`** | Use when executing an implementation plan in the current session as the implementer yourself — your human partner chose inline ... | [View](skills/engineering-workflow/executing-plans/SKILL.md) |
| **`export-download-debugging`** | - | [View](skills/engineering-workflow/export-download-debugging/SKILL.md) |
| **`find-release`** | A skill to find the lowest Dart and Flutter release containing a given commit. Use this skill whenever users ask about when a c... | [View](skills/engineering-workflow/find-release/SKILL.md) |
| **`finishing-a-development-branch`** | Use when implementation is complete, all tests pass, and you need to decide how to integrate the work | [View](skills/engineering-workflow/finishing-a-development-branch/SKILL.md) |
| **`flutter-animating-apps`** | - | [View](skills/engineering-workflow/flutter-animating-apps/SKILL.md) |
| **`flutter-cherry-pick`** | How to land a formal cherry-pick of a merged PR for the flutter/flutter repo stable or beta channel. Only use for flutter/flutt... | [View](skills/engineering-workflow/flutter-cherry-pick/SKILL.md) |
| **`flutter-pr-checks-finder`** | Find failing checks on a Flutter PR and locate the corresponding LUCI log URLs. | [View](skills/engineering-workflow/flutter-pr-checks-finder/SKILL.md) |
| **`git-guardrails-claude-code`** | Set up Claude Code hooks to block dangerous git commands (push, reset --hard, clean, branch -D, etc.) before they execute. Use ... | [View](skills/engineering-workflow/git-guardrails-claude-code/SKILL.md) |
| **`grill-me`** | A relentless interview to sharpen a plan or design. | [View](skills/engineering-workflow/grill-me/SKILL.md) |
| **`grill-with-docs`** | A relentless interview to sharpen a plan or design, which also creates docs (ADR's and glossary) as we go. | [View](skills/engineering-workflow/grill-with-docs/SKILL.md) |
| **`grilling`** | Grill the user relentlessly about a plan, decision, or idea. Use when the user wants to stress-test their thinking, or uses any... | [View](skills/engineering-workflow/grilling/SKILL.md) |
| **`handoff`** | Compact the current conversation into a handoff document for another agent to pick up. | [View](skills/engineering-workflow/handoff/SKILL.md) |
| **`i-have-adhd`** | Shape output for a reader with ADHD: lead with the next action, number multi-step work, restate state across turns, suppress ta... | [View](skills/engineering-workflow/i-have-adhd/SKILL.md) |
| **`implement`** | Implement a piece of work based on a spec or set of tickets. | [View](skills/engineering-workflow/implement/SKILL.md) |
| **`implement-spec`** | Implement a specification in code. | [View](skills/engineering-workflow/implement-spec/SKILL.md) |
| **`improve-codebase-architecture`** | Scan a codebase for deepening opportunities, present them as a visual HTML report, then grill through whichever one you pick. | [View](skills/engineering-workflow/improve-codebase-architecture/SKILL.md) |
| **`loop-me`** | Grill me about specs for the workflows I want to build, within this workspace. | [View](skills/engineering-workflow/loop-me/SKILL.md) |
| **`mcp-builder`** | Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with external services throug... | [View](skills/engineering-workflow/mcp-builder/SKILL.md) |
| **`migrate-to-shoehorn`** | Migrate test files from `as` type assertions to @total-typescript/shoehorn. Use when user mentions shoehorn, wants to replace `... | [View](skills/engineering-workflow/migrate-to-shoehorn/SKILL.md) |
| **`migrate-workflows`** | Automatically migrate legacy workflows to modern skills across global and workspace configurations. Scans for existing workflow... | [View](skills/engineering-workflow/migrate-workflows/SKILL.md) |
| **`output-skill`** | - | [View](skills/engineering-workflow/output-skill/SKILL.md) |
| **`permissioned-github`** | Guidelines for interacting with GitHub and request permissions from the user when commands fail due to restrictions in the agen... | [View](skills/engineering-workflow/permissioned-github/SKILL.md) |
| **`plugin`** | How to manage and create plugins — namespaced bundles of skills, agents, rules, MCP servers and hooks that install, enable and ... | [View](skills/engineering-workflow/plugin/SKILL.md) |
| **`ponytail`** | > | [View](skills/engineering-workflow/ponytail/SKILL.md) |
| **`ponytail-audit`** | > | [View](skills/engineering-workflow/ponytail-audit/SKILL.md) |
| **`ponytail-debt`** | > | [View](skills/engineering-workflow/ponytail-debt/SKILL.md) |
| **`ponytail-gain`** | > | [View](skills/engineering-workflow/ponytail-gain/SKILL.md) |
| **`ponytail-help`** | > | [View](skills/engineering-workflow/ponytail-help/SKILL.md) |
| **`ponytail-review`** | > | [View](skills/engineering-workflow/ponytail-review/SKILL.md) |
| **`pr-feedback-quality-gate`** | - | [View](skills/engineering-workflow/pr-feedback-quality-gate/SKILL.md) |
| **`prototype`** | Build a throwaway prototype to answer a design question. Use when the user wants to sanity-check whether a state model or logic... | [View](skills/engineering-workflow/prototype/SKILL.md) |
| **`rebuilding-flutter-tool`** | Rebuilds the Flutter tool and CLI. Use when a user asks to compile, update, regenerate, or rebuild the Flutter tool or CLI. | [View](skills/engineering-workflow/rebuilding-flutter-tool/SKILL.md) |
| **`receiving-code-review`** | Use when receiving code review feedback, before implementing suggestions, especially if feedback seems unclear or technically q... | [View](skills/engineering-workflow/receiving-code-review/SKILL.md) |
| **`requesting-code-review`** | Use when completing tasks, implementing major features, or before merging to verify work meets requirements | [View](skills/engineering-workflow/requesting-code-review/SKILL.md) |
| **`research`** | Investigate a question against high-trust primary sources and capture the findings as a Markdown file in the repo. Use when the... | [View](skills/engineering-workflow/research/SKILL.md) |
| **`resolving-merge-conflicts`** | Use when you need to resolve an in-progress git merge/rebase conflict. | [View](skills/engineering-workflow/resolving-merge-conflicts/SKILL.md) |
| **`retro`** | Conduct a retrospective on a coding session. | [View](skills/engineering-workflow/retro/SKILL.md) |
| **`reverse-engineer-anything`** | Reverse engineer native, managed, Electron/JavaScript, packaged, firmware, and browser targets with REA. Use shipped-artifact o... | [View](skills/engineering-workflow/reverse-engineer-anything/SKILL.md) |
| **`run-workflow`** | >- | [View](skills/engineering-workflow/run-workflow/SKILL.md) |
| **`scaffold-exercises`** | Create exercise directory structures with sections, problems, solutions, and explainers that pass linting. Use when user wants ... | [View](skills/engineering-workflow/scaffold-exercises/SKILL.md) |
| **`setup-matt-pocock-skills`** | Configure this repo for the engineering skills: set up its issue tracker, triage label vocabulary, and domain doc layout. Run o... | [View](skills/engineering-workflow/setup-matt-pocock-skills/SKILL.md) |
| **`setup-pre-commit`** | Set up Husky pre-commit hooks with lint-staged (Prettier), type checking, and tests in the current repo. Use when user wants to... | [View](skills/engineering-workflow/setup-pre-commit/SKILL.md) |
| **`setup-ts-deep-modules`** | Wire dependency-cruiser into a TypeScript repo so each package is a deep module, with implementation hidden in subfolders and r... | [View](skills/engineering-workflow/setup-ts-deep-modules/SKILL.md) |
| **`shepherd-prs`** | > | [View](skills/engineering-workflow/shepherd-prs/SKILL.md) |
| **`subagent-driven-development`** | Use when executing implementation plans with independent tasks in the current session | [View](skills/engineering-workflow/subagent-driven-development/SKILL.md) |
| **`systematic-debugging`** | Use when encountering any bug, test failure, or unexpected behavior, before proposing fixes | [View](skills/engineering-workflow/systematic-debugging/SKILL.md) |
| **`tdd`** | Test-driven development. Use when the user wants to build features or fix bugs test-first, mentions "red-green-refactor", or wa... | [View](skills/engineering-workflow/tdd/SKILL.md) |
| **`teach`** | Teach the user a new skill or concept, within this workspace. | [View](skills/engineering-workflow/teach/SKILL.md) |
| **`test-driven-development`** | Use when implementing any feature or bugfix, before writing implementation code | [View](skills/engineering-workflow/test-driven-development/SKILL.md) |
| **`to-questionnaire`** | Turn a decision you can't fully answer into a questionnaire for someone else to fill in. | [View](skills/engineering-workflow/to-questionnaire/SKILL.md) |
| **`to-spec`** | Turn the current conversation into a spec and publish it to the project issue tracker: no interview, just synthesis of what you... | [View](skills/engineering-workflow/to-spec/SKILL.md) |
| **`to-tickets`** | Break a plan, spec, or the current conversation into a set of tracer-bullet tickets, each declaring its blocking edges, publish... | [View](skills/engineering-workflow/to-tickets/SKILL.md) |
| **`triage`** | Move issues and external PRs through a state machine of triage roles, categorise, verify, grill if needed, and write agent-read... | [View](skills/engineering-workflow/triage/SKILL.md) |
| **`updating-android-sdk`** | Upgrades Flutter's Android SDK dependency to a new Android API version (or preview/canary release) in packages.txt, verifies CI... | [View](skills/engineering-workflow/updating-android-sdk/SKILL.md) |
| **`upgrade-browser`** | Upgrade browser versions (Chrome or Firefox) in the Flutter Web Engine and/or Framework tests. Use when asked to roll or upgrad... | [View](skills/engineering-workflow/upgrade-browser/SKILL.md) |
| **`using-git-worktrees`** | Use when starting feature work that needs isolation from current workspace or before executing implementation plans - ensures a... | [View](skills/engineering-workflow/using-git-worktrees/SKILL.md) |
| **`using-superpowers`** | Use when starting any conversation - establishes how to find and use skills, requiring skill invocation before ANY response inc... | [View](skills/engineering-workflow/using-superpowers/SKILL.md) |
| **`verification-before-completion`** | Use when about to claim work is complete, fixed, or passing, before committing or creating PRs - requires running verification ... | [View](skills/engineering-workflow/verification-before-completion/SKILL.md) |
| **`vibe-to-agentic-framework`** | The conceptual framework behind the presentation — what "Vibe Coding to Agentic Engineering" means, why the journey is structur... | [View](skills/engineering-workflow/vibe-to-agentic-framework/SKILL.md) |
| **`wait-what`** | Stop. That last message did not land: re-pitch it. | [View](skills/engineering-workflow/wait-what/SKILL.md) |
| **`wayfinder`** | Plan a huge chunk of work (more than one agent session can hold) as a shared map of decision tickets on your issue tracker, and... | [View](skills/engineering-workflow/wayfinder/SKILL.md) |
| **`webapp-testing`** | Toolkit for interacting with and testing local web applications using Playwright. Supports verifying frontend functionality, de... | [View](skills/engineering-workflow/webapp-testing/SKILL.md) |
| **`wizard`** | Generate an interactive bash wizard that walks a human through steps only they can perform. Use when provisioning infrastructur... | [View](skills/engineering-workflow/wizard/SKILL.md) |
| **`writing-plans`** | Use when you have a spec or requirements for a multi-step task, before touching code | [View](skills/engineering-workflow/writing-plans/SKILL.md) |
| **`writing-skills`** | Use when creating new skills, editing existing skills, or verifying skills work before deployment | [View](skills/engineering-workflow/writing-skills/SKILL.md) |

### 🎨 Frontend, UI Design & Design Systems (56 skills)

> Anti-slop design taste, shadcn/ui, brutalist and minimalist systems, Google Stitch, Apple HIG, Figma-to-code pipelines, D3 visualizations, and Three.js 3D shaders.

| Skill Name | Description | Link |
| :--- | :--- | :---: |
| **`algorithmic-art`** | Creating algorithmic art using p5.js with seeded randomness and interactive parameter exploration. Use this when users request ... | [View](skills/frontend-ui/algorithmic-art/SKILL.md) |
| **`apple-hig`** | - | [View](skills/frontend-ui/apple-hig/SKILL.md) |
| **`artifacts-builder`** | - | [View](skills/frontend-ui/artifacts-builder/SKILL.md) |
| **`banner-design`** | Design banners for social media, ads, website heroes, creative assets, and print. Multiple art direction options with optional ... | [View](skills/frontend-ui/banner-design/SKILL.md) |
| **`brutalist-skill`** | - | [View](skills/frontend-ui/brutalist-skill/SKILL.md) |
| **`canvas-design`** | Create beautiful visual art in .png and .pdf documents using design philosophy. You should use this skill when the user asks to... | [View](skills/frontend-ui/canvas-design/SKILL.md) |
| **`codebase-design`** | Shared vocabulary for designing deep modules. Use when the user wants to design or improve a module's interface, find deepening... | [View](skills/frontend-ui/codebase-design/SKILL.md) |
| **`color-expert`** | - | [View](skills/frontend-ui/color-expert/SKILL.md) |
| **`d3-visualization`** | - | [View](skills/frontend-ui/d3-visualization/SKILL.md) |
| **`design`** | Comprehensive design skill: brand identity, design tokens, UI styling, logo generation (55 styles, Gemini, Atlas Cloud, or MuAP... | [View](skills/frontend-ui/design/SKILL.md) |
| **`design-brief`** | - | [View](skills/frontend-ui/design-brief/SKILL.md) |
| **`design-consultation`** | - | [View](skills/frontend-ui/design-consultation/SKILL.md) |
| **`design-md`** | - | [View](skills/frontend-ui/design-md/SKILL.md) |
| **`design-review`** | - | [View](skills/frontend-ui/design-review/SKILL.md) |
| **`design-system`** | Token architecture, component specifications, and slide generation. Three-layer tokens (primitive→semantic→component), CSS vari... | [View](skills/frontend-ui/design-system/SKILL.md) |
| **`emil-design-eng`** | - | [View](skills/frontend-ui/emil-design-eng/SKILL.md) |
| **`faq-page`** | - | [View](skills/frontend-ui/faq-page/SKILL.md) |
| **`figma-code-connect-components`** | - | [View](skills/frontend-ui/figma-code-connect-components/SKILL.md) |
| **`figma-create-design-system-rules`** | - | [View](skills/frontend-ui/figma-create-design-system-rules/SKILL.md) |
| **`figma-create-new-file`** | - | [View](skills/frontend-ui/figma-create-new-file/SKILL.md) |
| **`figma-generate-design`** | - | [View](skills/frontend-ui/figma-generate-design/SKILL.md) |
| **`figma-generate-library`** | - | [View](skills/frontend-ui/figma-generate-library/SKILL.md) |
| **`figma-implement-design`** | - | [View](skills/frontend-ui/figma-implement-design/SKILL.md) |
| **`figma-use`** | - | [View](skills/frontend-ui/figma-use/SKILL.md) |
| **`frontend-design`** | Guidance for distinctive, intentional visual design when building new UI or reshaping an existing one. Helps with aesthetic dir... | [View](skills/frontend-ui/frontend-design/SKILL.md) |
| **`frontend-dev`** | - | [View](skills/frontend-ui/frontend-dev/SKILL.md) |
| **`frontend-skill`** | - | [View](skills/frontend-ui/frontend-skill/SKILL.md) |
| **`generative_ui`** | How to render rich interactive HTML widgets inline in the chat or as standalone artifacts. Use this skill when you want to show... | [View](skills/frontend-ui/generative_ui/SKILL.md) |
| **`gpt-tasteskill`** | - | [View](skills/frontend-ui/gpt-tasteskill/SKILL.md) |
| **`hand-drawn-diagrams`** | - | [View](skills/frontend-ui/hand-drawn-diagrams/SKILL.md) |
| **`impeccable-design-polish`** | - | [View](skills/frontend-ui/impeccable-design-polish/SKILL.md) |
| **`login-flow`** | Mobile login and authentication flow screens | [View](skills/frontend-ui/login-flow/SKILL.md) |
| **`minimalist-skill`** | - | [View](skills/frontend-ui/minimalist-skill/SKILL.md) |
| **`paywall-upgrade-cro`** | - | [View](skills/frontend-ui/paywall-upgrade-cro/SKILL.md) |
| **`plan-design-review`** | - | [View](skills/frontend-ui/plan-design-review/SKILL.md) |
| **`platform-design`** | - | [View](skills/frontend-ui/platform-design/SKILL.md) |
| **`redesign-skill`** | - | [View](skills/frontend-ui/redesign-skill/SKILL.md) |
| **`reference-design-contract`** | - | [View](skills/frontend-ui/reference-design-contract/SKILL.md) |
| **`shadcn-ui`** | - | [View](skills/frontend-ui/shadcn-ui/SKILL.md) |
| **`shader-dev`** | - | [View](skills/frontend-ui/shader-dev/SKILL.md) |
| **`soft-skill`** | - | [View](skills/frontend-ui/soft-skill/SKILL.md) |
| **`stitch-loop`** | - | [View](skills/frontend-ui/stitch-loop/SKILL.md) |
| **`stitch-skill`** | - | [View](skills/frontend-ui/stitch-skill/SKILL.md) |
| **`swiftui-design`** | - | [View](skills/frontend-ui/swiftui-design/SKILL.md) |
| **`taste-skill`** | - | [View](skills/frontend-ui/taste-skill/SKILL.md) |
| **`taste-skill-v1`** | - | [View](skills/frontend-ui/taste-skill-v1/SKILL.md) |
| **`theme-factory`** | Toolkit for styling artifacts with a theme. These artifacts can be slides, docs, reportings, HTML landing pages, etc. There are... | [View](skills/frontend-ui/theme-factory/SKILL.md) |
| **`threejs`** | - | [View](skills/frontend-ui/threejs/SKILL.md) |
| **`ui-plugin-navigation`** | Discover UI plugin panels relevant to the current task and surface a one-click pill in chat to open (toggle) them in the side p... | [View](skills/frontend-ui/ui-plugin-navigation/SKILL.md) |
| **`ui-skills`** | - | [View](skills/frontend-ui/ui-skills/SKILL.md) |
| **`ui-styling`** | Create beautiful, accessible user interfaces with shadcn/ui components (built on Radix UI + Tailwind), Tailwind CSS utility-fir... | [View](skills/frontend-ui/ui-styling/SKILL.md) |
| **`ui-ux-pro-max`** | UI/UX design intelligence for web, mobile, and desktop. This skill should be used when designing, building, reviewing, or fixin... | [View](skills/frontend-ui/ui-ux-pro-max/SKILL.md) |
| **`web-artifacts-builder`** | Suite of tools for creating elaborate, multi-component claude.ai HTML artifacts using modern frontend web technologies (React, ... | [View](skills/frontend-ui/web-artifacts-builder/SKILL.md) |
| **`web-clone`** | > | [View](skills/frontend-ui/web-clone/SKILL.md) |
| **`web-design-guidelines`** | - | [View](skills/frontend-ui/web-design-guidelines/SKILL.md) |
| **`wpds`** | - | [View](skills/frontend-ui/wpds/SKILL.md) |

### ✨ AI Media, Image, Audio & Video Generation (38 skills)

> Comprehensive integrations for Fal.ai, Venice.ai, Sora, Google Imagen, Midjourney/DALL-E style image generators, device mockups, and AI music production.

| Skill Name | Description | Link |
| :--- | :--- | :---: |
| **`ai-music-album`** | - | [View](skills/ai-media-generation/ai-music-album/SKILL.md) |
| **`card-twitter`** | Twitter quote or data card designed to pair with a post. | [View](skills/ai-media-generation/card-twitter/SKILL.md) |
| **`card-xiaohongshu`** | Xiaohongshu-style knowledge cards, arranged as a swipeable multi-card carousel. | [View](skills/ai-media-generation/card-xiaohongshu/SKILL.md) |
| **`ecommerce-image-workflow`** | - | [View](skills/ai-media-generation/ecommerce-image-workflow/SKILL.md) |
| **`fal-3d`** | - | [View](skills/ai-media-generation/fal-3d/SKILL.md) |
| **`fal-generate`** | - | [View](skills/ai-media-generation/fal-generate/SKILL.md) |
| **`fal-image-edit`** | - | [View](skills/ai-media-generation/fal-image-edit/SKILL.md) |
| **`fal-kling-o3`** | - | [View](skills/ai-media-generation/fal-kling-o3/SKILL.md) |
| **`fal-lip-sync`** | - | [View](skills/ai-media-generation/fal-lip-sync/SKILL.md) |
| **`fal-realtime`** | - | [View](skills/ai-media-generation/fal-realtime/SKILL.md) |
| **`fal-restore`** | - | [View](skills/ai-media-generation/fal-restore/SKILL.md) |
| **`fal-train`** | - | [View](skills/ai-media-generation/fal-train/SKILL.md) |
| **`fal-tryon`** | - | [View](skills/ai-media-generation/fal-tryon/SKILL.md) |
| **`fal-upscale`** | - | [View](skills/ai-media-generation/fal-upscale/SKILL.md) |
| **`fal-video-edit`** | - | [View](skills/ai-media-generation/fal-video-edit/SKILL.md) |
| **`fal-vision`** | - | [View](skills/ai-media-generation/fal-vision/SKILL.md) |
| **`gif-sticker-maker`** | - | [View](skills/ai-media-generation/gif-sticker-maker/SKILL.md) |
| **`image-enhancer`** | - | [View](skills/ai-media-generation/image-enhancer/SKILL.md) |
| **`image-to-code-skill`** | - | [View](skills/ai-media-generation/image-to-code-skill/SKILL.md) |
| **`imagegen`** | - | [View](skills/ai-media-generation/imagegen/SKILL.md) |
| **`imagegen-frontend-mobile`** | - | [View](skills/ai-media-generation/imagegen-frontend-mobile/SKILL.md) |
| **`imagegen-frontend-web`** | - | [View](skills/ai-media-generation/imagegen-frontend-web/SKILL.md) |
| **`imagen`** | - | [View](skills/ai-media-generation/imagen/SKILL.md) |
| **`mockup-device-3d`** | Static iPhone and MacBook 3D-style showcase with real HTML embedded on screens, glass-lens refraction, and 360-degree turntable... | [View](skills/ai-media-generation/mockup-device-3d/SKILL.md) |
| **`pixelbin-media`** | - | [View](skills/ai-media-generation/pixelbin-media/SKILL.md) |
| **`poster-hero`** | Vertical poster or Moments-style share image with strong visual impact. | [View](skills/ai-media-generation/poster-hero/SKILL.md) |
| **`replicate`** | - | [View](skills/ai-media-generation/replicate/SKILL.md) |
| **`slack-gif-creator`** | Knowledge and utilities for creating animated GIFs optimized for Slack. Provides constraints, validation tools, and animation c... | [View](skills/ai-media-generation/slack-gif-creator/SKILL.md) |
| **`social-reddit-card`** | Realistic Reddit post card with vote rail and comment count, suited to video overlays or story sharing. | [View](skills/ai-media-generation/social-reddit-card/SKILL.md) |
| **`social-spotify-card`** | Spotify Now Playing-style card with album art, progress bar, and playback controls, suited to video overlays or personal homepa... | [View](skills/ai-media-generation/social-spotify-card/SKILL.md) |
| **`social-x-post-card`** | Realistic X post card with engagement metrics (likes, reposts, views), suited to video overlays or shareable image cards. | [View](skills/ai-media-generation/social-x-post-card/SKILL.md) |
| **`sora`** | - | [View](skills/ai-media-generation/sora/SKILL.md) |
| **`speech`** | - | [View](skills/ai-media-generation/speech/SKILL.md) |
| **`venice-audio-music`** | - | [View](skills/ai-media-generation/venice-audio-music/SKILL.md) |
| **`venice-audio-speech`** | - | [View](skills/ai-media-generation/venice-audio-speech/SKILL.md) |
| **`venice-image-edit`** | - | [View](skills/ai-media-generation/venice-image-edit/SKILL.md) |
| **`venice-image-generate`** | - | [View](skills/ai-media-generation/venice-image-generate/SKILL.md) |
| **`venice-video`** | - | [View](skills/ai-media-generation/venice-video/SKILL.md) |

### 📄 Presentations, Decks & Document Automation (30 skills)

> Apple Keynote-quality slides, PowerPoint automation (PptxGenJS), OpenXML DOCX, PDF generators, executive memos, and Swiss international editorial layouts.

| Skill Name | Description | Link |
| :--- | :--- | :---: |
| **`article-magazine`** | Huashu / huashu-md-html-inspired magazine article layout for turning Markdown or notes into a polished long-form HTML essay. | [View](skills/presentation-docs/article-magazine/SKILL.md) |
| **`data-report`** | Turns CSV, Excel, or JSON data into a polished visual report page. | [View](skills/presentation-docs/data-report/SKILL.md) |
| **`deck-guizang-editorial`** | Editorial magazine meets e-ink: 10 layouts and 5 palettes (Ink, Indigo Porcelain, Forest Ink, Kraft Paper, Dune). | [View](skills/presentation-docs/deck-guizang-editorial/SKILL.md) |
| **`deck-open-slide-canvas`** | Locked 1920x1080 canvas deck with React component-level free composition, not bound to a fixed template. | [View](skills/presentation-docs/deck-open-slide-canvas/SKILL.md) |
| **`deck-swiss-international`** | 16-column grid, one saturated accent, and 22 locked layouts (Klein Blue, Lemon, Mint, Safety Orange). | [View](skills/presentation-docs/deck-swiss-international/SKILL.md) |
| **`digits-fintech-swiss-template`** | - | [View](skills/presentation-docs/digits-fintech-swiss-template/SKILL.md) |
| **`doc`** | - | [View](skills/presentation-docs/doc/SKILL.md) |
| **`doc-coauthoring`** | Guide users through a structured workflow for co-authoring documentation. Use when user wants to write documentation, proposals... | [View](skills/presentation-docs/doc-coauthoring/SKILL.md) |
| **`doc-kami-parchment`** | Warm parchment canvas (#f5f4ed), monochrome ink-blue accent (#1B365D), one serif family, and editorial-grade typography. | [View](skills/presentation-docs/doc-kami-parchment/SKILL.md) |
| **`docx`** | Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx files) or Word templates (.do... | [View](skills/presentation-docs/docx/SKILL.md) |
| **`editorial-burgundy-principles-template`** | - | [View](skills/presentation-docs/editorial-burgundy-principles-template/SKILL.md) |
| **`field-notes-editorial-template`** | - | [View](skills/presentation-docs/field-notes-editorial-template/SKILL.md) |
| **`frontend-slides`** | - | [View](skills/presentation-docs/frontend-slides/SKILL.md) |
| **`html-ppt-retro-quarterly-review`** | - | [View](skills/presentation-docs/html-ppt-retro-quarterly-review/SKILL.md) |
| **`minimax-docx`** | - | [View](skills/presentation-docs/minimax-docx/SKILL.md) |
| **`minimax-pdf`** | - | [View](skills/presentation-docs/minimax-pdf/SKILL.md) |
| **`nanobanana-ppt`** | - | [View](skills/presentation-docs/nanobanana-ppt/SKILL.md) |
| **`pdf`** | Use this skill whenever the user wants to do anything with PDF files. This includes reading or extracting text/tables from PDFs... | [View](skills/presentation-docs/pdf/SKILL.md) |
| **`ppt-keynote`** | Apple Keynote-quality slides, one card per screen, with keyboard left/right navigation. | [View](skills/presentation-docs/ppt-keynote/SKILL.md) |
| **`ppt-master`** | > | [View](skills/presentation-docs/ppt-master/SKILL.md) |
| **`pptx`** | Use this skill any time a .pptx or .potx file is involved in any way — as input, output, or both. This includes: creating slide... | [View](skills/presentation-docs/pptx/SKILL.md) |
| **`pptx-generator`** | - | [View](skills/presentation-docs/pptx-generator/SKILL.md) |
| **`pptx-html-fidelity-audit`** | Audit a python-pptx export against its source HTML deck, identify layout/content drift (footer overflow, cropped content, missi... | [View](skills/presentation-docs/pptx-html-fidelity-audit/SKILL.md) |
| **`presentation-structure`** | Knowledge about the presentation slide format, weight system, navigation, and section structure | [View](skills/presentation-docs/presentation-structure/SKILL.md) |
| **`presentation-styling`** | Knowledge about CSS classes, component patterns, and syntax highlighting in the presentation | [View](skills/presentation-docs/presentation-styling/SKILL.md) |
| **`release-notes-one-pager`** | - | [View](skills/presentation-docs/release-notes-one-pager/SKILL.md) |
| **`research-decision-room`** | - | [View](skills/presentation-docs/research-decision-room/SKILL.md) |
| **`resume-modern`** | Modern minimal resume, single A4 page, ready for print or PDF export. | [View](skills/presentation-docs/resume-modern/SKILL.md) |
| **`slides`** | Create strategic HTML presentations with Chart.js, design tokens, responsive layouts, copywriting formulas, and contextual slid... | [View](skills/presentation-docs/slides/SKILL.md) |
| **`xlsx`** | Use this skill any time a spreadsheet file is the primary input or output. This means any task where the user wants to: open, r... | [View](skills/presentation-docs/xlsx/SKILL.md) |

### 🎬 Motion, GSAP & Video Animation (28 skills)

> Full GSAP suite (ScrollTrigger, Flip, Timeline, Performance), Remotion React video compositions, Hyperframes cinematic templates, and micro-interaction polish.

| Skill Name | Description | Link |
| :--- | :--- | :---: |
| **`8-bit-orbit-video-template`** | - | [View](skills/motion-animation/8-bit-orbit-video-template/SKILL.md) |
| **`after-hours-editorial-template`** | - | [View](skills/motion-animation/after-hours-editorial-template/SKILL.md) |
| **`chat-motion-overlay`** | Generate configurable chat motion overlays from a transcript or screenshot, including plain bubble scenes, app-style chat conta... | [View](skills/motion-animation/chat-motion-overlay/SKILL.md) |
| **`emilkowalski-motion`** | - | [View](skills/motion-animation/emilkowalski-motion/SKILL.md) |
| **`frame-data-chart-nyt`** | NYT-newsroom typography, staggered reveal animation, and editorial-grade charts (line, bar, or range band). | [View](skills/motion-animation/frame-data-chart-nyt/SKILL.md) |
| **`frame-flowchart-sticky`** | SVG curve connectors, sticky-note nodes, and cursor interaction with a whiteboard-brainstorm feel. | [View](skills/motion-animation/frame-flowchart-sticky/SKILL.md) |
| **`frame-glitch-title`** | Digital glitch, chromatic offset, and data-corruption title frame for video transitions or cyberpunk heroes. | [View](skills/motion-animation/frame-glitch-title/SKILL.md) |
| **`frame-light-leak-cinema`** | Film light leaks, grain, 16:9 letterbox, and large serif type for cinematic openings or chapter cards. | [View](skills/motion-animation/frame-light-leak-cinema/SKILL.md) |
| **`frame-liquid-bg-hero`** | WebGL-style fluid displacement background with a quote overlay, suited to video intros, landing heroes, or posters. | [View](skills/motion-animation/frame-liquid-bg-hero/SKILL.md) |
| **`frame-logo-outro`** | Segmented logo assembly, glow bloom, and tagline reveal for video outros or brand closing frames. | [View](skills/motion-animation/frame-logo-outro/SKILL.md) |
| **`frame-macos-notification`** | Realistic macOS notification banner with app icon, title, and body, suited to video overlays or product teasers. | [View](skills/motion-animation/frame-macos-notification/SKILL.md) |
| **`gsap-core`** | - | [View](skills/motion-animation/gsap-core/SKILL.md) |
| **`gsap-frameworks`** | - | [View](skills/motion-animation/gsap-frameworks/SKILL.md) |
| **`gsap-performance`** | - | [View](skills/motion-animation/gsap-performance/SKILL.md) |
| **`gsap-plugins`** | - | [View](skills/motion-animation/gsap-plugins/SKILL.md) |
| **`gsap-react`** | - | [View](skills/motion-animation/gsap-react/SKILL.md) |
| **`gsap-scrolltrigger`** | - | [View](skills/motion-animation/gsap-scrolltrigger/SKILL.md) |
| **`gsap-timeline`** | - | [View](skills/motion-animation/gsap-timeline/SKILL.md) |
| **`gsap-utils`** | - | [View](skills/motion-animation/gsap-utils/SKILL.md) |
| **`prompt-motion`** | Code-based AI motion graphics and video templates inspired by prompt-motion.com (SaaS launch, kinetic typography, bento, 120 BPM beat grid, spring physics). | [View](skills/motion-animation/prompt-motion/SKILL.md) |
| **`remotion`** | - | [View](skills/motion-animation/remotion/SKILL.md) |
| **`review-animations`** | - | [View](skills/motion-animation/review-animations/SKILL.md) |
| **`swiss-creative-mode-template`** | - | [View](skills/motion-animation/swiss-creative-mode-template/SKILL.md) |
| **`swiss-user-research-video-template`** | - | [View](skills/motion-animation/swiss-user-research-video-template/SKILL.md) |
| **`vfx-text-cursor`** | Cursor light trail, chromatic rays, and directional flares for word-by-word quote reveals in video intros. | [View](skills/motion-animation/vfx-text-cursor/SKILL.md) |
| **`video-downloader`** | - | [View](skills/motion-animation/video-downloader/SKILL.md) |
| **`video-hyperframes`** | Hyperframes / Remotion-compatible continuous frame animation with autoplay support. | [View](skills/motion-animation/video-hyperframes/SKILL.md) |
| **`weread-year-in-review-video-template`** | - | [View](skills/motion-animation/weread-year-in-review-video-template/SKILL.md) |
| **`youtube-clipper`** | - | [View](skills/motion-animation/youtube-clipper/SKILL.md) |

### 📣 Marketing, Brand & Copywriting (16 skills)

> Conversion-focused copywriting, creative direction frameworks, advertising psychology, brand voice guides, and social media viral cards.

| Skill Name | Description | Link |
| :--- | :--- | :---: |
| **`ad-creative`** | - | [View](skills/marketing-copywriting/ad-creative/SKILL.md) |
| **`brand`** | Brand voice, visual identity, messaging frameworks, asset management, brand consistency. Activate for branded content, tone of ... | [View](skills/marketing-copywriting/brand/SKILL.md) |
| **`brand-extract`** | - | [View](skills/marketing-copywriting/brand-extract/SKILL.md) |
| **`brand-guidelines`** | Applies Anthropic's official brand colors and typography to any sort of artifact that may benefit from having Anthropic's look-... | [View](skills/marketing-copywriting/brand-guidelines/SKILL.md) |
| **`brandkit`** | - | [View](skills/marketing-copywriting/brandkit/SKILL.md) |
| **`competitive-ads-extractor`** | - | [View](skills/marketing-copywriting/competitive-ads-extractor/SKILL.md) |
| **`copywriting`** | - | [View](skills/marketing-copywriting/copywriting/SKILL.md) |
| **`creative-director`** | - | [View](skills/marketing-copywriting/creative-director/SKILL.md) |
| **`internal-comms`** | A set of resources to help me write all kinds of internal communications, using the formats that my company likes to use. Claud... | [View](skills/marketing-copywriting/internal-comms/SKILL.md) |
| **`marketing-psychology`** | - | [View](skills/marketing-copywriting/marketing-psychology/SKILL.md) |
| **`screenshots-marketing`** | - | [View](skills/marketing-copywriting/screenshots-marketing/SKILL.md) |
| **`writing-beats`** | Writing, exploit; assemble raw material into a journey of beats, grounding each term before a beat leans on it. | [View](skills/marketing-copywriting/writing-beats/SKILL.md) |
| **`writing-for-agents`** | Writing documents for agents. Use when creating or editing skills, or modifying AGENTS.md or CLAUDE.md. | [View](skills/marketing-copywriting/writing-for-agents/SKILL.md) |
| **`writing-fragments`** | Writing, explore: mine raw fragments, no structure yet. | [View](skills/marketing-copywriting/writing-fragments/SKILL.md) |
| **`writing-guidelines`** | - | [View](skills/marketing-copywriting/writing-guidelines/SKILL.md) |
| **`writing-shape`** | Writing, exploit: shape raw material into an article, paragraph by paragraph. | [View](skills/marketing-copywriting/writing-shape/SKILL.md) |

### 🧭 Agent Tools, Browsing & Assistant Personas (21 skills)

> Browser automation with agent-browser, screenshot captures, Antigravity guides, custom MCP server builders, and interactive advisory personas.

| Skill Name | Description | Link |
| :--- | :--- | :---: |
| **`academy-guide`** | > | [View](skills/agent-tools-guides/academy-guide/SKILL.md) |
| **`agent-browser`** | - | [View](skills/agent-tools-guides/agent-browser/SKILL.md) |
| **`agent-desktop`** | > | [View](skills/agent-tools-guides/agent-desktop/SKILL.md) |
| **`agy-customizations`** | >- | [View](skills/agent-tools-guides/agy-customizations/SKILL.md) |
| **`antigravity_guide`** | Provides a comprehensive guide, quick reference, and sitemap for Google Antigravity (AGY), including the Antigravity CLI (agy),... | [View](skills/agent-tools-guides/antigravity_guide/SKILL.md) |
| **`ask-matt`** | Ask which skill or flow fits your situation. A router over the skills in this repo. | [View](skills/agent-tools-guides/ask-matt/SKILL.md) |
| **`automation`** | Interactive guide to design and create a scheduled background automation. Use this skill when the user wants to create an autom... | [View](skills/agent-tools-guides/automation/SKILL.md) |
| **`claude-api`** | -- | [View](skills/agent-tools-guides/claude-api/SKILL.md) |
| **`claude-code-best-practice`** | Comprehensive collection of agentic coding best practices, tips, multi-agent teams architectures, subagent workflows, MCP integ... | [View](skills/agent-tools-guides/claude-code-best-practice/SKILL.md) |
| **`discernment-nudge`** | > | [View](skills/agent-tools-guides/discernment-nudge/SKILL.md) |
| **`domain-name-brainstormer`** | - | [View](skills/agent-tools-guides/domain-name-brainstormer/SKILL.md) |
| **`enhance-prompt`** | - | [View](skills/agent-tools-guides/enhance-prompt/SKILL.md) |
| **`full-page-screenshot`** | - | [View](skills/agent-tools-guides/full-page-screenshot/SKILL.md) |
| **`hatch-pet`** | Create, repair, validate, preview, and package Codex-compatible animated pet spritesheets from character art, screenshots, gene... | [View](skills/agent-tools-guides/hatch-pet/SKILL.md) |
| **`library-curator`** | - | [View](skills/agent-tools-guides/library-curator/SKILL.md) |
| **`od-next-media-inputs`** | - | [View](skills/agent-tools-guides/od-next-media-inputs/SKILL.md) |
| **`screenshot`** | - | [View](skills/agent-tools-guides/screenshot/SKILL.md) |
| **`skill-creator`** | Create new skills, modify and improve existing skills, and measure skill performance. Use when users want to create a skill fro... | [View](skills/agent-tools-guides/skill-creator/SKILL.md) |
| **`time-skill`** | Display the current time in Pakistan Standard Time (PKT, UTC+5). Use when the user asks for the current time, Pakistan time, or... | [View](skills/agent-tools-guides/time-skill/SKILL.md) |
| **`weather-fetcher`** | Instructions for fetching current weather temperature data for Dubai, UAE from Open-Meteo API | [View](skills/agent-tools-guides/weather-fetcher/SKILL.md) |
| **`weather-svg-creator`** | Creates an SVG weather card showing the current temperature for Dubai. Writes the SVG to orchestration-workflow/weather.svg and... | [View](skills/agent-tools-guides/weather-svg-creator/SKILL.md) |

---

## 🔄 Updating Skills

To sync the latest updates from upstream repositories (including new Superpowers releases and community additions):
```bash
git pull origin main
./install.sh --target ~/.gemini/config/skills
```

## 📄 License

Distributed under the [MIT License](LICENSE).
