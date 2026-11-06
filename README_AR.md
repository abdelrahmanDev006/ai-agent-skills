# 🤖 مستودع مهارات وكلاء الذكاء الاصطناعي (AI Agent Skills)

[![إجمالي المهارات](https://img.shields.io/badge/%D8%A5%D8%AC%D9%85%D8%A7%D9%84%D9%8A%20%D8%A7%D9%84%D9%85%D9%87%D8%A7%D8%B1%D8%A7%D8%AA-264-blue.svg)](skills.json)
[![التصنيفات](https://img.shields.io/badge/%D8%A7%D9%84%D8%AA%D8%B5%D9%86%D9%8A%D9%81%D8%A7%D8%AA-7-green.svg)](#-ملخص-التصنيفات)
[![سوبر باورز](https://img.shields.io/badge/Superpowers-v7.0.2%20%D8%A7%D9%84%D8%A3%D8%AD%D8%AF%D8%AB-purple.svg)](skills/engineering-workflow/brainstorming)
[![التوافق](https://img.shields.io/badge/%D8%A7%D9%84%D8%AA%D9%88%D8%A7%D9%81%D9%82-Antigravity%20%7C%20Claude%20Code%20%7C%20Codex%20%7C%20Cursor%20%7C%20OpenCode-orange.svg)](#-طريقة-التثبيت-والاستخدام)
[![الرخصة](https://img.shields.io/badge/%D8%A7%D9%84%D8%B1%D8%AE%D8%B5%D8%A9-MIT-brightgreen.svg)](LICENSE)
[![English](https://img.shields.io/badge/Language-English-blue.svg)](README.md)

> مكتبة متكاملة ومنظمة تضم **264 مهارة متخصصة** لوكلاء البرمجة والذكاء الاصطناعي، مبنية وفق المعيار القياسي `SKILL.md`، ومتوافقة تماماً مع **Google Antigravity** و **Claude Code** و **OpenAI Codex** و **Cursor** و **OpenCode**.

---

## 📚 الفهرس السريع

- [✨ نبذة عن المستودع](#-نبذة-عن-المستودع)
- [📦 ملخص التصنيفات](#-ملخص-التصنيفات)
- [🚀 طريقة التثبيت والاستخدام](#-طريقة-التثبيت-والاستخدام)
- [🔍 دليل المهارات الكامل](#-دليل-المهارات-الكامل)
  - [🛠️ الهندسة البرمجية وسير عمل الوكلاء (75 مهارة)](#️-الهندسة-البرمجية-وتخطيط-وسير-عمل-الوكلاء-75-مهارة)
  - [🎨 الواجهات وتصميم الأنظمة (56 مهارة)](#-تصميم-الواجهات-الأمامية-وأنظمة-التصميم-56-مهارة)
  - [✨ توليد الوسائط بالذكاء الاصطناعي (38 مهارة)](#-توليد-الوسائط-بالذكاء-الاصطناعي-صور-صوت-فيديو-38-مهارة)
  - [📄 العروض والوثائق والتقارير (30 مهارة)](#-العروض-التقديمية-والوثائق-والتقارير-التنفيذية-30-مهارة)
  - [🎬 التحريك والموشن فيديو (28 مهارة)](#-التحريك-والأنيميشن-التفاعلي-وموشن-الفيديو-28-مهارة)
  - [🧭 أدوات الوكلاء والمتصفح (21 مهارة)](#-أدوات-الوكلاء-وأتمتة-المتصفح-والمساعدين-المتخصصين-21-مهارة)
  - [📣 التسويق وصناعة المحتوى (16 مهارة)](#-التسويق-وكتابة-المحتوى-وهوية-العلامة-التجارية-16-مهارة)
- [🔄 تحديث المهارات](#-تحديث-المهارات)
- [📄 الترخيص](#-الترخيص)

---

## ✨ نبذة عن المستودع

تم تجميع هذه المهارات وتحديثها لتضم أحدث إصدارات **Superpowers v7.0.2** بالإضافة إلى مكتبات التصميم، التحريك، والذكاء الاصطناعي الأكثر تطوراً. تعتمد كل مهارة على المعمارية ثلاثية الطبقات:
1. **البيانات الوصفية (`YAML Frontmatter`)**: تتيح للوكيل اكتشاف المهارة واستدعائها في اللحظة المناسبة دون استهلاك سياق الذاكرة.
2. **التعليمات التفصيلية (`SKILL.md`)**: يتم تحميلها ديناميكياً فقط عندما يحتاجها الوكيل لمهمة محددة.
3. **المراجع والسكربتات المرفقة (`Scripts & Assets`)**: أدوات برمجية وسكربتات Python/Bash وقوالب جاهزة للتنفيذ المباشر.

---

## 📦 ملخص التصنيفات

| التصنيف | العدد | الوصف والنطاق الأساسي |
| :--- | :---: | :--- |
| **🛠️ الهندسة البرمجية وتخطيط وسير عمل الوكلاء** | **75** | مهارات تخطيط وتطوير البرمجيات الأساسية (Superpowers v7.0.2)، التطوير الموجه بالاختبارات (TDD)، استكشاف الأخطاء المنهجي، إدارة الوكلاء الفرعيين، مراجعة الكود، وحلول فلاتر ودارت المعمارية. |
| **🎨 تصميم الواجهات الأمامية وأنظمة التصميم** | **56** | أنظمة التصميم الراقية وتطوير واجهات المستخدم دون قوالب مكررة، مكتبات shadcn/ui، التصاميم التجريدية والمينيمالية، Google Stitch، إرشادات آبل Apple HIG، والتحويل من فيجما إلى كود. |
| **✨ توليد الوسائط بالذكاء الاصطناعي (صور، صوت، فيديو)** | **38** | تكاملات كاملة لنماذج Fal.ai و Venice.ai و OpenAI Sora و Google Imagen، وتوليد الصور التوضيحية وتعديلها ونماذج الأجهزة 3D والموسيقى الذكية. |
| **📄 العروض التقديمية والوثائق والتقارير التنفيذية** | **30** | تصميم وتوليد عروض بوربوينت وكي نوت بأعلى جودة واحترافية، مستندات Word DOCX و PDF و Excel XLSX، وتقارير البيانات والمذكرات التنفيذية. |
| **🎬 التحريك والأنيميشن التفاعلي وموشن الفيديو** | **28** | مكتبة حركات GSAP المتكاملة لجميع أطر العمل، إنتاج الفيديو البرمجي عبر Remotion و Hyperframes، وتأثيرات الموشن الدقيقة والانتقالات السينمائية. |
| **📣 التسويق وكتابة المحتوى وهوية العلامة التجارية** | **16** | كتابة الإعلانات التسويقية الاحترافية، أطر العمل الإبداعية، علم النفس التسويقي، بناء هوية العلامة التجارية، وبطاقات السوشيال ميديا. |
| **🧭 أدوات الوكلاء وأتمتة المتصفح والمساعدين المتخصصين** | **21** | أتمتة المتصفح وسطح المكتب، التقاط الشاشات، دلائل Antigravity، أدوات بناء خوادم MCP، والمساعدين الموجهين للاستشارات والتقييم. |

---

## 🚀 طريقة التثبيت والاستخدام

### الطريقة 1: السكربت التلقائي (`install.sh`)
قم باستنساخ المستودع وتشغيل السكربت التفاعلي المباشر:
```bash
git clone https://github.com/abdelrahmanDev006/ai-agent-skills.git
cd ai-agent-skills
chmod +x install.sh
./install.sh
```

#### أمثلة للتثبيت المخصص والموجه:
```bash
# 1. تثبيت كافة المهارات داخل إعدادات Antigravity العامة:
./install.sh --target ~/.gemini/config/skills

# 2. تثبيت مهارات الواجهات الأمامية فقط داخل مشروع العمل الحالي:
./install.sh --category frontend-ui --target ./.agents/skills

# 3. تثبيت مهارة واحدة عبر رابط رمزي (Symlink) لتوفير المساحة وتحديثها تلقائياً:
./install.sh --skill brainstorming --target ~/.gemini/config/skills --link
```

### الطريقة 2: التثبيت اليدوي
يمكنك نسخ أي مجلد مهارة مباشرة إلى مجلد المهارات الخاص بالأداة التي تستخدمها:
- **Google Antigravity:** `~/.gemini/config/skills/` (شامل) أو `<workspace>/.agents/skills/` (خاص بالمشروع)
- **Claude Code:** `~/.claude/skills/` أو `<workspace>/.claude/skills/`
- **Codex / OpenAI:** `~/.codex/skills/`
- **Cursor / Windsurf:** `<workspace>/.agents/skills/`

---

## 🔍 دليل المهارات الكامل

### 🛠️ الهندسة البرمجية وتخطيط وسير عمل الوكلاء (75 مهارة)

> مهارات تخطيط وتطوير البرمجيات الأساسية (Superpowers v7.0.2)، التطوير الموجه بالاختبارات (TDD)، استكشاف الأخطاء المنهجي، إدارة الوكلاء الفرعيين، مراجعة الكود، وحلول فلاتر ودارت المعمارية.

| اسم المهارة | الوصف والغرض | الرابط |
| :--- | :--- | :---: |
| **`analyze-github-flake`** | Expertise in analyzing flake github issues in the flutter/flutter repository. Use when a user wants to analyze the flakiness of... | [عرض](skills/engineering-workflow/analyze-github-flake/SKILL.md) |
| **`brainstorming`** | You MUST use this before any creative work - creating features, building components, adding functionality, modifying behavior, ... | [عرض](skills/engineering-workflow/brainstorming/SKILL.md) |
| **`caveman`** | > | [عرض](skills/engineering-workflow/caveman/SKILL.md) |
| **`claude-handoff`** | Hand the current conversation off to a fresh background agent that picks up the work immediately. | [عرض](skills/engineering-workflow/claude-handoff/SKILL.md) |
| **`code-review`** | Review the changes since a fixed point (commit, branch, tag, or merge-base) along two axes: Standards (does the code follow thi... | [عرض](skills/engineering-workflow/code-review/SKILL.md) |
| **`dart-log-failure-parser`** | Parse failures from Dart and Flutter test logs. | [عرض](skills/engineering-workflow/dart-log-failure-parser/SKILL.md) |
| **`diagnosing-bugs`** | Diagnosis loop for hard bugs and performance regressions. Use when the user says "diagnose"/"debug this", or reports something ... | [عرض](skills/engineering-workflow/diagnosing-bugs/SKILL.md) |
| **`diagnosing-superpowers`** | Use when a superpowers session went wrong and your human partner wants to know why — repeated work, ignored plans, stumbles, po... | [عرض](skills/engineering-workflow/diagnosing-superpowers/SKILL.md) |
| **`dispatching-parallel-agents`** | Use when facing 2+ independent tasks that can be worked on without shared state or sequential dependencies | [عرض](skills/engineering-workflow/dispatching-parallel-agents/SKILL.md) |
| **`domain-modeling`** | Build and sharpen a project's domain model. Use when discussing codebase terminology, writing or editing a CONTEXT.md, or recor... | [عرض](skills/engineering-workflow/domain-modeling/SKILL.md) |
| **`executing-plans`** | Use when executing an implementation plan in the current session as the implementer yourself — your human partner chose inline ... | [عرض](skills/engineering-workflow/executing-plans/SKILL.md) |
| **`export-download-debugging`** | - | [عرض](skills/engineering-workflow/export-download-debugging/SKILL.md) |
| **`find-release`** | A skill to find the lowest Dart and Flutter release containing a given commit. Use this skill whenever users ask about when a c... | [عرض](skills/engineering-workflow/find-release/SKILL.md) |
| **`finishing-a-development-branch`** | Use when implementation is complete, all tests pass, and you need to decide how to integrate the work | [عرض](skills/engineering-workflow/finishing-a-development-branch/SKILL.md) |
| **`flutter-animating-apps`** | - | [عرض](skills/engineering-workflow/flutter-animating-apps/SKILL.md) |
| **`flutter-cherry-pick`** | How to land a formal cherry-pick of a merged PR for the flutter/flutter repo stable or beta channel. Only use for flutter/flutt... | [عرض](skills/engineering-workflow/flutter-cherry-pick/SKILL.md) |
| **`flutter-pr-checks-finder`** | Find failing checks on a Flutter PR and locate the corresponding LUCI log URLs. | [عرض](skills/engineering-workflow/flutter-pr-checks-finder/SKILL.md) |
| **`git-guardrails-claude-code`** | Set up Claude Code hooks to block dangerous git commands (push, reset --hard, clean, branch -D, etc.) before they execute. Use ... | [عرض](skills/engineering-workflow/git-guardrails-claude-code/SKILL.md) |
| **`grill-me`** | A relentless interview to sharpen a plan or design. | [عرض](skills/engineering-workflow/grill-me/SKILL.md) |
| **`grill-with-docs`** | A relentless interview to sharpen a plan or design, which also creates docs (ADR's and glossary) as we go. | [عرض](skills/engineering-workflow/grill-with-docs/SKILL.md) |
| **`grilling`** | Grill the user relentlessly about a plan, decision, or idea. Use when the user wants to stress-test their thinking, or uses any... | [عرض](skills/engineering-workflow/grilling/SKILL.md) |
| **`handoff`** | Compact the current conversation into a handoff document for another agent to pick up. | [عرض](skills/engineering-workflow/handoff/SKILL.md) |
| **`i-have-adhd`** | Shape output for a reader with ADHD: lead with the next action, number multi-step work, restate state across turns, suppress ta... | [عرض](skills/engineering-workflow/i-have-adhd/SKILL.md) |
| **`implement`** | Implement a piece of work based on a spec or set of tickets. | [عرض](skills/engineering-workflow/implement/SKILL.md) |
| **`implement-spec`** | Implement a specification in code. | [عرض](skills/engineering-workflow/implement-spec/SKILL.md) |
| **`improve-codebase-architecture`** | Scan a codebase for deepening opportunities, present them as a visual HTML report, then grill through whichever one you pick. | [عرض](skills/engineering-workflow/improve-codebase-architecture/SKILL.md) |
| **`loop-me`** | Grill me about specs for the workflows I want to build, within this workspace. | [عرض](skills/engineering-workflow/loop-me/SKILL.md) |
| **`mcp-builder`** | Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with external services throug... | [عرض](skills/engineering-workflow/mcp-builder/SKILL.md) |
| **`migrate-to-shoehorn`** | Migrate test files from `as` type assertions to @total-typescript/shoehorn. Use when user mentions shoehorn, wants to replace `... | [عرض](skills/engineering-workflow/migrate-to-shoehorn/SKILL.md) |
| **`migrate-workflows`** | Automatically migrate legacy workflows to modern skills across global and workspace configurations. Scans for existing workflow... | [عرض](skills/engineering-workflow/migrate-workflows/SKILL.md) |
| **`output-skill`** | - | [عرض](skills/engineering-workflow/output-skill/SKILL.md) |
| **`permissioned-github`** | Guidelines for interacting with GitHub and request permissions from the user when commands fail due to restrictions in the agen... | [عرض](skills/engineering-workflow/permissioned-github/SKILL.md) |
| **`plugin`** | How to manage and create plugins — namespaced bundles of skills, agents, rules, MCP servers and hooks that install, enable and ... | [عرض](skills/engineering-workflow/plugin/SKILL.md) |
| **`ponytail`** | > | [عرض](skills/engineering-workflow/ponytail/SKILL.md) |
| **`ponytail-audit`** | > | [عرض](skills/engineering-workflow/ponytail-audit/SKILL.md) |
| **`ponytail-debt`** | > | [عرض](skills/engineering-workflow/ponytail-debt/SKILL.md) |
| **`ponytail-gain`** | > | [عرض](skills/engineering-workflow/ponytail-gain/SKILL.md) |
| **`ponytail-help`** | > | [عرض](skills/engineering-workflow/ponytail-help/SKILL.md) |
| **`ponytail-review`** | > | [عرض](skills/engineering-workflow/ponytail-review/SKILL.md) |
| **`pr-feedback-quality-gate`** | - | [عرض](skills/engineering-workflow/pr-feedback-quality-gate/SKILL.md) |
| **`prototype`** | Build a throwaway prototype to answer a design question. Use when the user wants to sanity-check whether a state model or logic... | [عرض](skills/engineering-workflow/prototype/SKILL.md) |
| **`rebuilding-flutter-tool`** | Rebuilds the Flutter tool and CLI. Use when a user asks to compile, update, regenerate, or rebuild the Flutter tool or CLI. | [عرض](skills/engineering-workflow/rebuilding-flutter-tool/SKILL.md) |
| **`receiving-code-review`** | Use when receiving code review feedback, before implementing suggestions, especially if feedback seems unclear or technically q... | [عرض](skills/engineering-workflow/receiving-code-review/SKILL.md) |
| **`requesting-code-review`** | Use when completing tasks, implementing major features, or before merging to verify work meets requirements | [عرض](skills/engineering-workflow/requesting-code-review/SKILL.md) |
| **`research`** | Investigate a question against high-trust primary sources and capture the findings as a Markdown file in the repo. Use when the... | [عرض](skills/engineering-workflow/research/SKILL.md) |
| **`resolving-merge-conflicts`** | Use when you need to resolve an in-progress git merge/rebase conflict. | [عرض](skills/engineering-workflow/resolving-merge-conflicts/SKILL.md) |
| **`retro`** | Conduct a retrospective on a coding session. | [عرض](skills/engineering-workflow/retro/SKILL.md) |
| **`reverse-engineer-anything`** | Reverse engineer native, managed, Electron/JavaScript, packaged, firmware, and browser targets with REA. Use shipped-artifact o... | [عرض](skills/engineering-workflow/reverse-engineer-anything/SKILL.md) |
| **`run-workflow`** | >- | [عرض](skills/engineering-workflow/run-workflow/SKILL.md) |
| **`scaffold-exercises`** | Create exercise directory structures with sections, problems, solutions, and explainers that pass linting. Use when user wants ... | [عرض](skills/engineering-workflow/scaffold-exercises/SKILL.md) |
| **`setup-matt-pocock-skills`** | Configure this repo for the engineering skills: set up its issue tracker, triage label vocabulary, and domain doc layout. Run o... | [عرض](skills/engineering-workflow/setup-matt-pocock-skills/SKILL.md) |
| **`setup-pre-commit`** | Set up Husky pre-commit hooks with lint-staged (Prettier), type checking, and tests in the current repo. Use when user wants to... | [عرض](skills/engineering-workflow/setup-pre-commit/SKILL.md) |
| **`setup-ts-deep-modules`** | Wire dependency-cruiser into a TypeScript repo so each package is a deep module, with implementation hidden in subfolders and r... | [عرض](skills/engineering-workflow/setup-ts-deep-modules/SKILL.md) |
| **`shepherd-prs`** | > | [عرض](skills/engineering-workflow/shepherd-prs/SKILL.md) |
| **`subagent-driven-development`** | Use when executing implementation plans with independent tasks in the current session | [عرض](skills/engineering-workflow/subagent-driven-development/SKILL.md) |
| **`systematic-debugging`** | Use when encountering any bug, test failure, or unexpected behavior, before proposing fixes | [عرض](skills/engineering-workflow/systematic-debugging/SKILL.md) |
| **`tdd`** | Test-driven development. Use when the user wants to build features or fix bugs test-first, mentions "red-green-refactor", or wa... | [عرض](skills/engineering-workflow/tdd/SKILL.md) |
| **`teach`** | Teach the user a new skill or concept, within this workspace. | [عرض](skills/engineering-workflow/teach/SKILL.md) |
| **`test-driven-development`** | Use when implementing any feature or bugfix, before writing implementation code | [عرض](skills/engineering-workflow/test-driven-development/SKILL.md) |
| **`to-questionnaire`** | Turn a decision you can't fully answer into a questionnaire for someone else to fill in. | [عرض](skills/engineering-workflow/to-questionnaire/SKILL.md) |
| **`to-spec`** | Turn the current conversation into a spec and publish it to the project issue tracker: no interview, just synthesis of what you... | [عرض](skills/engineering-workflow/to-spec/SKILL.md) |
| **`to-tickets`** | Break a plan, spec, or the current conversation into a set of tracer-bullet tickets, each declaring its blocking edges, publish... | [عرض](skills/engineering-workflow/to-tickets/SKILL.md) |
| **`triage`** | Move issues and external PRs through a state machine of triage roles, categorise, verify, grill if needed, and write agent-read... | [عرض](skills/engineering-workflow/triage/SKILL.md) |
| **`updating-android-sdk`** | Upgrades Flutter's Android SDK dependency to a new Android API version (or preview/canary release) in packages.txt, verifies CI... | [عرض](skills/engineering-workflow/updating-android-sdk/SKILL.md) |
| **`upgrade-browser`** | Upgrade browser versions (Chrome or Firefox) in the Flutter Web Engine and/or Framework tests. Use when asked to roll or upgrad... | [عرض](skills/engineering-workflow/upgrade-browser/SKILL.md) |
| **`using-git-worktrees`** | Use when starting feature work that needs isolation from current workspace or before executing implementation plans - ensures a... | [عرض](skills/engineering-workflow/using-git-worktrees/SKILL.md) |
| **`using-superpowers`** | Use when starting any conversation - establishes how to find and use skills, requiring skill invocation before ANY response inc... | [عرض](skills/engineering-workflow/using-superpowers/SKILL.md) |
| **`verification-before-completion`** | Use when about to claim work is complete, fixed, or passing, before committing or creating PRs - requires running verification ... | [عرض](skills/engineering-workflow/verification-before-completion/SKILL.md) |
| **`vibe-to-agentic-framework`** | The conceptual framework behind the presentation — what "Vibe Coding to Agentic Engineering" means, why the journey is structur... | [عرض](skills/engineering-workflow/vibe-to-agentic-framework/SKILL.md) |
| **`wait-what`** | Stop. That last message did not land: re-pitch it. | [عرض](skills/engineering-workflow/wait-what/SKILL.md) |
| **`wayfinder`** | Plan a huge chunk of work (more than one agent session can hold) as a shared map of decision tickets on your issue tracker, and... | [عرض](skills/engineering-workflow/wayfinder/SKILL.md) |
| **`webapp-testing`** | Toolkit for interacting with and testing local web applications using Playwright. Supports verifying frontend functionality, de... | [عرض](skills/engineering-workflow/webapp-testing/SKILL.md) |
| **`wizard`** | Generate an interactive bash wizard that walks a human through steps only they can perform. Use when provisioning infrastructur... | [عرض](skills/engineering-workflow/wizard/SKILL.md) |
| **`writing-plans`** | Use when you have a spec or requirements for a multi-step task, before touching code | [عرض](skills/engineering-workflow/writing-plans/SKILL.md) |
| **`writing-skills`** | Use when creating new skills, editing existing skills, or verifying skills work before deployment | [عرض](skills/engineering-workflow/writing-skills/SKILL.md) |

### 🎨 تصميم الواجهات الأمامية وأنظمة التصميم (56 مهارة)

> أنظمة التصميم الراقية وتطوير واجهات المستخدم دون قوالب مكررة، مكتبات shadcn/ui، التصاميم التجريدية والمينيمالية، Google Stitch، إرشادات آبل Apple HIG، والتحويل من فيجما إلى كود.

| اسم المهارة | الوصف والغرض | الرابط |
| :--- | :--- | :---: |
| **`algorithmic-art`** | Creating algorithmic art using p5.js with seeded randomness and interactive parameter exploration. Use this when users request ... | [عرض](skills/frontend-ui/algorithmic-art/SKILL.md) |
| **`apple-hig`** | - | [عرض](skills/frontend-ui/apple-hig/SKILL.md) |
| **`artifacts-builder`** | - | [عرض](skills/frontend-ui/artifacts-builder/SKILL.md) |
| **`banner-design`** | Design banners for social media, ads, website heroes, creative assets, and print. Multiple art direction options with optional ... | [عرض](skills/frontend-ui/banner-design/SKILL.md) |
| **`brutalist-skill`** | - | [عرض](skills/frontend-ui/brutalist-skill/SKILL.md) |
| **`canvas-design`** | Create beautiful visual art in .png and .pdf documents using design philosophy. You should use this skill when the user asks to... | [عرض](skills/frontend-ui/canvas-design/SKILL.md) |
| **`codebase-design`** | Shared vocabulary for designing deep modules. Use when the user wants to design or improve a module's interface, find deepening... | [عرض](skills/frontend-ui/codebase-design/SKILL.md) |
| **`color-expert`** | - | [عرض](skills/frontend-ui/color-expert/SKILL.md) |
| **`d3-visualization`** | - | [عرض](skills/frontend-ui/d3-visualization/SKILL.md) |
| **`design`** | Comprehensive design skill: brand identity, design tokens, UI styling, logo generation (55 styles, Gemini, Atlas Cloud, or MuAP... | [عرض](skills/frontend-ui/design/SKILL.md) |
| **`design-brief`** | - | [عرض](skills/frontend-ui/design-brief/SKILL.md) |
| **`design-consultation`** | - | [عرض](skills/frontend-ui/design-consultation/SKILL.md) |
| **`design-md`** | - | [عرض](skills/frontend-ui/design-md/SKILL.md) |
| **`design-review`** | - | [عرض](skills/frontend-ui/design-review/SKILL.md) |
| **`design-system`** | Token architecture, component specifications, and slide generation. Three-layer tokens (primitive→semantic→component), CSS vari... | [عرض](skills/frontend-ui/design-system/SKILL.md) |
| **`emil-design-eng`** | - | [عرض](skills/frontend-ui/emil-design-eng/SKILL.md) |
| **`faq-page`** | - | [عرض](skills/frontend-ui/faq-page/SKILL.md) |
| **`figma-code-connect-components`** | - | [عرض](skills/frontend-ui/figma-code-connect-components/SKILL.md) |
| **`figma-create-design-system-rules`** | - | [عرض](skills/frontend-ui/figma-create-design-system-rules/SKILL.md) |
| **`figma-create-new-file`** | - | [عرض](skills/frontend-ui/figma-create-new-file/SKILL.md) |
| **`figma-generate-design`** | - | [عرض](skills/frontend-ui/figma-generate-design/SKILL.md) |
| **`figma-generate-library`** | - | [عرض](skills/frontend-ui/figma-generate-library/SKILL.md) |
| **`figma-implement-design`** | - | [عرض](skills/frontend-ui/figma-implement-design/SKILL.md) |
| **`figma-use`** | - | [عرض](skills/frontend-ui/figma-use/SKILL.md) |
| **`frontend-design`** | Guidance for distinctive, intentional visual design when building new UI or reshaping an existing one. Helps with aesthetic dir... | [عرض](skills/frontend-ui/frontend-design/SKILL.md) |
| **`frontend-dev`** | - | [عرض](skills/frontend-ui/frontend-dev/SKILL.md) |
| **`frontend-skill`** | - | [عرض](skills/frontend-ui/frontend-skill/SKILL.md) |
| **`generative_ui`** | How to render rich interactive HTML widgets inline in the chat or as standalone artifacts. Use this skill when you want to show... | [عرض](skills/frontend-ui/generative_ui/SKILL.md) |
| **`gpt-tasteskill`** | - | [عرض](skills/frontend-ui/gpt-tasteskill/SKILL.md) |
| **`hand-drawn-diagrams`** | - | [عرض](skills/frontend-ui/hand-drawn-diagrams/SKILL.md) |
| **`impeccable-design-polish`** | - | [عرض](skills/frontend-ui/impeccable-design-polish/SKILL.md) |
| **`login-flow`** | Mobile login and authentication flow screens | [عرض](skills/frontend-ui/login-flow/SKILL.md) |
| **`minimalist-skill`** | - | [عرض](skills/frontend-ui/minimalist-skill/SKILL.md) |
| **`paywall-upgrade-cro`** | - | [عرض](skills/frontend-ui/paywall-upgrade-cro/SKILL.md) |
| **`plan-design-review`** | - | [عرض](skills/frontend-ui/plan-design-review/SKILL.md) |
| **`platform-design`** | - | [عرض](skills/frontend-ui/platform-design/SKILL.md) |
| **`redesign-skill`** | - | [عرض](skills/frontend-ui/redesign-skill/SKILL.md) |
| **`reference-design-contract`** | - | [عرض](skills/frontend-ui/reference-design-contract/SKILL.md) |
| **`shadcn-ui`** | - | [عرض](skills/frontend-ui/shadcn-ui/SKILL.md) |
| **`shader-dev`** | - | [عرض](skills/frontend-ui/shader-dev/SKILL.md) |
| **`soft-skill`** | - | [عرض](skills/frontend-ui/soft-skill/SKILL.md) |
| **`stitch-loop`** | - | [عرض](skills/frontend-ui/stitch-loop/SKILL.md) |
| **`stitch-skill`** | - | [عرض](skills/frontend-ui/stitch-skill/SKILL.md) |
| **`swiftui-design`** | - | [عرض](skills/frontend-ui/swiftui-design/SKILL.md) |
| **`taste-skill`** | - | [عرض](skills/frontend-ui/taste-skill/SKILL.md) |
| **`taste-skill-v1`** | - | [عرض](skills/frontend-ui/taste-skill-v1/SKILL.md) |
| **`theme-factory`** | Toolkit for styling artifacts with a theme. These artifacts can be slides, docs, reportings, HTML landing pages, etc. There are... | [عرض](skills/frontend-ui/theme-factory/SKILL.md) |
| **`threejs`** | - | [عرض](skills/frontend-ui/threejs/SKILL.md) |
| **`ui-plugin-navigation`** | Discover UI plugin panels relevant to the current task and surface a one-click pill in chat to open (toggle) them in the side p... | [عرض](skills/frontend-ui/ui-plugin-navigation/SKILL.md) |
| **`ui-skills`** | - | [عرض](skills/frontend-ui/ui-skills/SKILL.md) |
| **`ui-styling`** | Create beautiful, accessible user interfaces with shadcn/ui components (built on Radix UI + Tailwind), Tailwind CSS utility-fir... | [عرض](skills/frontend-ui/ui-styling/SKILL.md) |
| **`ui-ux-pro-max`** | UI/UX design intelligence for web, mobile, and desktop. This skill should be used when designing, building, reviewing, or fixin... | [عرض](skills/frontend-ui/ui-ux-pro-max/SKILL.md) |
| **`web-artifacts-builder`** | Suite of tools for creating elaborate, multi-component claude.ai HTML artifacts using modern frontend web technologies (React, ... | [عرض](skills/frontend-ui/web-artifacts-builder/SKILL.md) |
| **`web-clone`** | > | [عرض](skills/frontend-ui/web-clone/SKILL.md) |
| **`web-design-guidelines`** | - | [عرض](skills/frontend-ui/web-design-guidelines/SKILL.md) |
| **`wpds`** | - | [عرض](skills/frontend-ui/wpds/SKILL.md) |

### ✨ توليد الوسائط بالذكاء الاصطناعي (صور، صوت، فيديو) (38 مهارة)

> تكاملات كاملة لنماذج Fal.ai و Venice.ai و OpenAI Sora و Google Imagen، وتوليد الصور التوضيحية وتعديلها ونماذج الأجهزة 3D والموسيقى الذكية.

| اسم المهارة | الوصف والغرض | الرابط |
| :--- | :--- | :---: |
| **`ai-music-album`** | - | [عرض](skills/ai-media-generation/ai-music-album/SKILL.md) |
| **`card-twitter`** | Twitter quote or data card designed to pair with a post. | [عرض](skills/ai-media-generation/card-twitter/SKILL.md) |
| **`card-xiaohongshu`** | Xiaohongshu-style knowledge cards, arranged as a swipeable multi-card carousel. | [عرض](skills/ai-media-generation/card-xiaohongshu/SKILL.md) |
| **`ecommerce-image-workflow`** | - | [عرض](skills/ai-media-generation/ecommerce-image-workflow/SKILL.md) |
| **`fal-3d`** | - | [عرض](skills/ai-media-generation/fal-3d/SKILL.md) |
| **`fal-generate`** | - | [عرض](skills/ai-media-generation/fal-generate/SKILL.md) |
| **`fal-image-edit`** | - | [عرض](skills/ai-media-generation/fal-image-edit/SKILL.md) |
| **`fal-kling-o3`** | - | [عرض](skills/ai-media-generation/fal-kling-o3/SKILL.md) |
| **`fal-lip-sync`** | - | [عرض](skills/ai-media-generation/fal-lip-sync/SKILL.md) |
| **`fal-realtime`** | - | [عرض](skills/ai-media-generation/fal-realtime/SKILL.md) |
| **`fal-restore`** | - | [عرض](skills/ai-media-generation/fal-restore/SKILL.md) |
| **`fal-train`** | - | [عرض](skills/ai-media-generation/fal-train/SKILL.md) |
| **`fal-tryon`** | - | [عرض](skills/ai-media-generation/fal-tryon/SKILL.md) |
| **`fal-upscale`** | - | [عرض](skills/ai-media-generation/fal-upscale/SKILL.md) |
| **`fal-video-edit`** | - | [عرض](skills/ai-media-generation/fal-video-edit/SKILL.md) |
| **`fal-vision`** | - | [عرض](skills/ai-media-generation/fal-vision/SKILL.md) |
| **`gif-sticker-maker`** | - | [عرض](skills/ai-media-generation/gif-sticker-maker/SKILL.md) |
| **`image-enhancer`** | - | [عرض](skills/ai-media-generation/image-enhancer/SKILL.md) |
| **`image-to-code-skill`** | - | [عرض](skills/ai-media-generation/image-to-code-skill/SKILL.md) |
| **`imagegen`** | - | [عرض](skills/ai-media-generation/imagegen/SKILL.md) |
| **`imagegen-frontend-mobile`** | - | [عرض](skills/ai-media-generation/imagegen-frontend-mobile/SKILL.md) |
| **`imagegen-frontend-web`** | - | [عرض](skills/ai-media-generation/imagegen-frontend-web/SKILL.md) |
| **`imagen`** | - | [عرض](skills/ai-media-generation/imagen/SKILL.md) |
| **`mockup-device-3d`** | Static iPhone and MacBook 3D-style showcase with real HTML embedded on screens, glass-lens refraction, and 360-degree turntable... | [عرض](skills/ai-media-generation/mockup-device-3d/SKILL.md) |
| **`pixelbin-media`** | - | [عرض](skills/ai-media-generation/pixelbin-media/SKILL.md) |
| **`poster-hero`** | Vertical poster or Moments-style share image with strong visual impact. | [عرض](skills/ai-media-generation/poster-hero/SKILL.md) |
| **`replicate`** | - | [عرض](skills/ai-media-generation/replicate/SKILL.md) |
| **`slack-gif-creator`** | Knowledge and utilities for creating animated GIFs optimized for Slack. Provides constraints, validation tools, and animation c... | [عرض](skills/ai-media-generation/slack-gif-creator/SKILL.md) |
| **`social-reddit-card`** | Realistic Reddit post card with vote rail and comment count, suited to video overlays or story sharing. | [عرض](skills/ai-media-generation/social-reddit-card/SKILL.md) |
| **`social-spotify-card`** | Spotify Now Playing-style card with album art, progress bar, and playback controls, suited to video overlays or personal homepa... | [عرض](skills/ai-media-generation/social-spotify-card/SKILL.md) |
| **`social-x-post-card`** | Realistic X post card with engagement metrics (likes, reposts, views), suited to video overlays or shareable image cards. | [عرض](skills/ai-media-generation/social-x-post-card/SKILL.md) |
| **`sora`** | - | [عرض](skills/ai-media-generation/sora/SKILL.md) |
| **`speech`** | - | [عرض](skills/ai-media-generation/speech/SKILL.md) |
| **`venice-audio-music`** | - | [عرض](skills/ai-media-generation/venice-audio-music/SKILL.md) |
| **`venice-audio-speech`** | - | [عرض](skills/ai-media-generation/venice-audio-speech/SKILL.md) |
| **`venice-image-edit`** | - | [عرض](skills/ai-media-generation/venice-image-edit/SKILL.md) |
| **`venice-image-generate`** | - | [عرض](skills/ai-media-generation/venice-image-generate/SKILL.md) |
| **`venice-video`** | - | [عرض](skills/ai-media-generation/venice-video/SKILL.md) |

### 📄 العروض التقديمية والوثائق والتقارير التنفيذية (30 مهارة)

> تصميم وتوليد عروض بوربوينت وكي نوت بأعلى جودة واحترافية، مستندات Word DOCX و PDF و Excel XLSX، وتقارير البيانات والمذكرات التنفيذية.

| اسم المهارة | الوصف والغرض | الرابط |
| :--- | :--- | :---: |
| **`article-magazine`** | Huashu / huashu-md-html-inspired magazine article layout for turning Markdown or notes into a polished long-form HTML essay. | [عرض](skills/presentation-docs/article-magazine/SKILL.md) |
| **`data-report`** | Turns CSV, Excel, or JSON data into a polished visual report page. | [عرض](skills/presentation-docs/data-report/SKILL.md) |
| **`deck-guizang-editorial`** | Editorial magazine meets e-ink: 10 layouts and 5 palettes (Ink, Indigo Porcelain, Forest Ink, Kraft Paper, Dune). | [عرض](skills/presentation-docs/deck-guizang-editorial/SKILL.md) |
| **`deck-open-slide-canvas`** | Locked 1920x1080 canvas deck with React component-level free composition, not bound to a fixed template. | [عرض](skills/presentation-docs/deck-open-slide-canvas/SKILL.md) |
| **`deck-swiss-international`** | 16-column grid, one saturated accent, and 22 locked layouts (Klein Blue, Lemon, Mint, Safety Orange). | [عرض](skills/presentation-docs/deck-swiss-international/SKILL.md) |
| **`digits-fintech-swiss-template`** | - | [عرض](skills/presentation-docs/digits-fintech-swiss-template/SKILL.md) |
| **`doc`** | - | [عرض](skills/presentation-docs/doc/SKILL.md) |
| **`doc-coauthoring`** | Guide users through a structured workflow for co-authoring documentation. Use when user wants to write documentation, proposals... | [عرض](skills/presentation-docs/doc-coauthoring/SKILL.md) |
| **`doc-kami-parchment`** | Warm parchment canvas (#f5f4ed), monochrome ink-blue accent (#1B365D), one serif family, and editorial-grade typography. | [عرض](skills/presentation-docs/doc-kami-parchment/SKILL.md) |
| **`docx`** | Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx files) or Word templates (.do... | [عرض](skills/presentation-docs/docx/SKILL.md) |
| **`editorial-burgundy-principles-template`** | - | [عرض](skills/presentation-docs/editorial-burgundy-principles-template/SKILL.md) |
| **`field-notes-editorial-template`** | - | [عرض](skills/presentation-docs/field-notes-editorial-template/SKILL.md) |
| **`frontend-slides`** | - | [عرض](skills/presentation-docs/frontend-slides/SKILL.md) |
| **`html-ppt-retro-quarterly-review`** | - | [عرض](skills/presentation-docs/html-ppt-retro-quarterly-review/SKILL.md) |
| **`minimax-docx`** | - | [عرض](skills/presentation-docs/minimax-docx/SKILL.md) |
| **`minimax-pdf`** | - | [عرض](skills/presentation-docs/minimax-pdf/SKILL.md) |
| **`nanobanana-ppt`** | - | [عرض](skills/presentation-docs/nanobanana-ppt/SKILL.md) |
| **`pdf`** | Use this skill whenever the user wants to do anything with PDF files. This includes reading or extracting text/tables from PDFs... | [عرض](skills/presentation-docs/pdf/SKILL.md) |
| **`ppt-keynote`** | Apple Keynote-quality slides, one card per screen, with keyboard left/right navigation. | [عرض](skills/presentation-docs/ppt-keynote/SKILL.md) |
| **`ppt-master`** | > | [عرض](skills/presentation-docs/ppt-master/SKILL.md) |
| **`pptx`** | Use this skill any time a .pptx or .potx file is involved in any way — as input, output, or both. This includes: creating slide... | [عرض](skills/presentation-docs/pptx/SKILL.md) |
| **`pptx-generator`** | - | [عرض](skills/presentation-docs/pptx-generator/SKILL.md) |
| **`pptx-html-fidelity-audit`** | Audit a python-pptx export against its source HTML deck, identify layout/content drift (footer overflow, cropped content, missi... | [عرض](skills/presentation-docs/pptx-html-fidelity-audit/SKILL.md) |
| **`presentation-structure`** | Knowledge about the presentation slide format, weight system, navigation, and section structure | [عرض](skills/presentation-docs/presentation-structure/SKILL.md) |
| **`presentation-styling`** | Knowledge about CSS classes, component patterns, and syntax highlighting in the presentation | [عرض](skills/presentation-docs/presentation-styling/SKILL.md) |
| **`release-notes-one-pager`** | - | [عرض](skills/presentation-docs/release-notes-one-pager/SKILL.md) |
| **`research-decision-room`** | - | [عرض](skills/presentation-docs/research-decision-room/SKILL.md) |
| **`resume-modern`** | Modern minimal resume, single A4 page, ready for print or PDF export. | [عرض](skills/presentation-docs/resume-modern/SKILL.md) |
| **`slides`** | Create strategic HTML presentations with Chart.js, design tokens, responsive layouts, copywriting formulas, and contextual slid... | [عرض](skills/presentation-docs/slides/SKILL.md) |
| **`xlsx`** | Use this skill any time a spreadsheet file is the primary input or output. This means any task where the user wants to: open, r... | [عرض](skills/presentation-docs/xlsx/SKILL.md) |

### 🎬 التحريك والأنيميشن التفاعلي وموشن الفيديو (28 مهارة)

> مكتبة حركات GSAP المتكاملة لجميع أطر العمل، إنتاج الفيديو البرمجي عبر Remotion و Hyperframes، وتأثيرات الموشن الدقيقة والانتقالات السينمائية.

| اسم المهارة | الوصف والغرض | الرابط |
| :--- | :--- | :---: |
| **`8-bit-orbit-video-template`** | - | [عرض](skills/motion-animation/8-bit-orbit-video-template/SKILL.md) |
| **`after-hours-editorial-template`** | - | [عرض](skills/motion-animation/after-hours-editorial-template/SKILL.md) |
| **`chat-motion-overlay`** | Generate configurable chat motion overlays from a transcript or screenshot, including plain bubble scenes, app-style chat conta... | [عرض](skills/motion-animation/chat-motion-overlay/SKILL.md) |
| **`emilkowalski-motion`** | - | [عرض](skills/motion-animation/emilkowalski-motion/SKILL.md) |
| **`frame-data-chart-nyt`** | NYT-newsroom typography, staggered reveal animation, and editorial-grade charts (line, bar, or range band). | [عرض](skills/motion-animation/frame-data-chart-nyt/SKILL.md) |
| **`frame-flowchart-sticky`** | SVG curve connectors, sticky-note nodes, and cursor interaction with a whiteboard-brainstorm feel. | [عرض](skills/motion-animation/frame-flowchart-sticky/SKILL.md) |
| **`frame-glitch-title`** | Digital glitch, chromatic offset, and data-corruption title frame for video transitions or cyberpunk heroes. | [عرض](skills/motion-animation/frame-glitch-title/SKILL.md) |
| **`frame-light-leak-cinema`** | Film light leaks, grain, 16:9 letterbox, and large serif type for cinematic openings or chapter cards. | [عرض](skills/motion-animation/frame-light-leak-cinema/SKILL.md) |
| **`frame-liquid-bg-hero`** | WebGL-style fluid displacement background with a quote overlay, suited to video intros, landing heroes, or posters. | [عرض](skills/motion-animation/frame-liquid-bg-hero/SKILL.md) |
| **`frame-logo-outro`** | Segmented logo assembly, glow bloom, and tagline reveal for video outros or brand closing frames. | [عرض](skills/motion-animation/frame-logo-outro/SKILL.md) |
| **`frame-macos-notification`** | Realistic macOS notification banner with app icon, title, and body, suited to video overlays or product teasers. | [عرض](skills/motion-animation/frame-macos-notification/SKILL.md) |
| **`gsap-core`** | - | [عرض](skills/motion-animation/gsap-core/SKILL.md) |
| **`gsap-frameworks`** | - | [عرض](skills/motion-animation/gsap-frameworks/SKILL.md) |
| **`gsap-performance`** | - | [عرض](skills/motion-animation/gsap-performance/SKILL.md) |
| **`gsap-plugins`** | - | [عرض](skills/motion-animation/gsap-plugins/SKILL.md) |
| **`gsap-react`** | - | [عرض](skills/motion-animation/gsap-react/SKILL.md) |
| **`gsap-scrolltrigger`** | - | [عرض](skills/motion-animation/gsap-scrolltrigger/SKILL.md) |
| **`gsap-timeline`** | - | [عرض](skills/motion-animation/gsap-timeline/SKILL.md) |
| **`gsap-utils`** | - | [عرض](skills/motion-animation/gsap-utils/SKILL.md) |
| **`remotion`** | - | [عرض](skills/motion-animation/remotion/SKILL.md) |
| **`review-animations`** | - | [عرض](skills/motion-animation/review-animations/SKILL.md) |
| **`swiss-creative-mode-template`** | - | [عرض](skills/motion-animation/swiss-creative-mode-template/SKILL.md) |
| **`swiss-user-research-video-template`** | - | [عرض](skills/motion-animation/swiss-user-research-video-template/SKILL.md) |
| **`vfx-text-cursor`** | Cursor light trail, chromatic rays, and directional flares for word-by-word quote reveals in video intros. | [عرض](skills/motion-animation/vfx-text-cursor/SKILL.md) |
| **`video-downloader`** | - | [عرض](skills/motion-animation/video-downloader/SKILL.md) |
| **`video-hyperframes`** | Hyperframes / Remotion-compatible continuous frame animation with autoplay support. | [عرض](skills/motion-animation/video-hyperframes/SKILL.md) |
| **`weread-year-in-review-video-template`** | - | [عرض](skills/motion-animation/weread-year-in-review-video-template/SKILL.md) |
| **`youtube-clipper`** | - | [عرض](skills/motion-animation/youtube-clipper/SKILL.md) |

### 📣 التسويق وكتابة المحتوى وهوية العلامة التجارية (16 مهارة)

> كتابة الإعلانات التسويقية الاحترافية، أطر العمل الإبداعية، علم النفس التسويقي، بناء هوية العلامة التجارية، وبطاقات السوشيال ميديا.

| اسم المهارة | الوصف والغرض | الرابط |
| :--- | :--- | :---: |
| **`ad-creative`** | - | [عرض](skills/marketing-copywriting/ad-creative/SKILL.md) |
| **`brand`** | Brand voice, visual identity, messaging frameworks, asset management, brand consistency. Activate for branded content, tone of ... | [عرض](skills/marketing-copywriting/brand/SKILL.md) |
| **`brand-extract`** | - | [عرض](skills/marketing-copywriting/brand-extract/SKILL.md) |
| **`brand-guidelines`** | Applies Anthropic's official brand colors and typography to any sort of artifact that may benefit from having Anthropic's look-... | [عرض](skills/marketing-copywriting/brand-guidelines/SKILL.md) |
| **`brandkit`** | - | [عرض](skills/marketing-copywriting/brandkit/SKILL.md) |
| **`competitive-ads-extractor`** | - | [عرض](skills/marketing-copywriting/competitive-ads-extractor/SKILL.md) |
| **`copywriting`** | - | [عرض](skills/marketing-copywriting/copywriting/SKILL.md) |
| **`creative-director`** | - | [عرض](skills/marketing-copywriting/creative-director/SKILL.md) |
| **`internal-comms`** | A set of resources to help me write all kinds of internal communications, using the formats that my company likes to use. Claud... | [عرض](skills/marketing-copywriting/internal-comms/SKILL.md) |
| **`marketing-psychology`** | - | [عرض](skills/marketing-copywriting/marketing-psychology/SKILL.md) |
| **`screenshots-marketing`** | - | [عرض](skills/marketing-copywriting/screenshots-marketing/SKILL.md) |
| **`writing-beats`** | Writing, exploit; assemble raw material into a journey of beats, grounding each term before a beat leans on it. | [عرض](skills/marketing-copywriting/writing-beats/SKILL.md) |
| **`writing-for-agents`** | Writing documents for agents. Use when creating or editing skills, or modifying AGENTS.md or CLAUDE.md. | [عرض](skills/marketing-copywriting/writing-for-agents/SKILL.md) |
| **`writing-fragments`** | Writing, explore: mine raw fragments, no structure yet. | [عرض](skills/marketing-copywriting/writing-fragments/SKILL.md) |
| **`writing-guidelines`** | - | [عرض](skills/marketing-copywriting/writing-guidelines/SKILL.md) |
| **`writing-shape`** | Writing, exploit: shape raw material into an article, paragraph by paragraph. | [عرض](skills/marketing-copywriting/writing-shape/SKILL.md) |

### 🧭 أدوات الوكلاء وأتمتة المتصفح والمساعدين المتخصصين (21 مهارة)

> أتمتة المتصفح وسطح المكتب، التقاط الشاشات، دلائل Antigravity، أدوات بناء خوادم MCP، والمساعدين الموجهين للاستشارات والتقييم.

| اسم المهارة | الوصف والغرض | الرابط |
| :--- | :--- | :---: |
| **`academy-guide`** | > | [عرض](skills/agent-tools-guides/academy-guide/SKILL.md) |
| **`agent-browser`** | - | [عرض](skills/agent-tools-guides/agent-browser/SKILL.md) |
| **`agent-desktop`** | > | [عرض](skills/agent-tools-guides/agent-desktop/SKILL.md) |
| **`agy-customizations`** | >- | [عرض](skills/agent-tools-guides/agy-customizations/SKILL.md) |
| **`antigravity_guide`** | Provides a comprehensive guide, quick reference, and sitemap for Google Antigravity (AGY), including the Antigravity CLI (agy),... | [عرض](skills/agent-tools-guides/antigravity_guide/SKILL.md) |
| **`ask-matt`** | Ask which skill or flow fits your situation. A router over the skills in this repo. | [عرض](skills/agent-tools-guides/ask-matt/SKILL.md) |
| **`automation`** | Interactive guide to design and create a scheduled background automation. Use this skill when the user wants to create an autom... | [عرض](skills/agent-tools-guides/automation/SKILL.md) |
| **`claude-api`** | -- | [عرض](skills/agent-tools-guides/claude-api/SKILL.md) |
| **`claude-code-best-practice`** | Comprehensive collection of agentic coding best practices, tips, multi-agent teams architectures, subagent workflows, MCP integ... | [عرض](skills/agent-tools-guides/claude-code-best-practice/SKILL.md) |
| **`discernment-nudge`** | > | [عرض](skills/agent-tools-guides/discernment-nudge/SKILL.md) |
| **`domain-name-brainstormer`** | - | [عرض](skills/agent-tools-guides/domain-name-brainstormer/SKILL.md) |
| **`enhance-prompt`** | - | [عرض](skills/agent-tools-guides/enhance-prompt/SKILL.md) |
| **`full-page-screenshot`** | - | [عرض](skills/agent-tools-guides/full-page-screenshot/SKILL.md) |
| **`hatch-pet`** | Create, repair, validate, preview, and package Codex-compatible animated pet spritesheets from character art, screenshots, gene... | [عرض](skills/agent-tools-guides/hatch-pet/SKILL.md) |
| **`library-curator`** | - | [عرض](skills/agent-tools-guides/library-curator/SKILL.md) |
| **`od-next-media-inputs`** | - | [عرض](skills/agent-tools-guides/od-next-media-inputs/SKILL.md) |
| **`screenshot`** | - | [عرض](skills/agent-tools-guides/screenshot/SKILL.md) |
| **`skill-creator`** | Create new skills, modify and improve existing skills, and measure skill performance. Use when users want to create a skill fro... | [عرض](skills/agent-tools-guides/skill-creator/SKILL.md) |
| **`time-skill`** | Display the current time in Pakistan Standard Time (PKT, UTC+5). Use when the user asks for the current time, Pakistan time, or... | [عرض](skills/agent-tools-guides/time-skill/SKILL.md) |
| **`weather-fetcher`** | Instructions for fetching current weather temperature data for Dubai, UAE from Open-Meteo API | [عرض](skills/agent-tools-guides/weather-fetcher/SKILL.md) |
| **`weather-svg-creator`** | Creates an SVG weather card showing the current temperature for Dubai. Writes the SVG to orchestration-workflow/weather.svg and... | [عرض](skills/agent-tools-guides/weather-svg-creator/SKILL.md) |

---

## 🔄 تحديث المهارات

لسحب أحدث التحديثات والإصدارات الجديدة للمهارات من المستودع:
```bash
git pull origin main
./install.sh --target ~/.gemini/config/skills
```

## 📄 الترخيص

هذا المستودع منشور تحت رخصة [MIT License](LICENSE).
