#!/usr/bin/env python3
import json
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SCRIPT_DIR)
SKILLS_JSON = os.path.join(ROOT_DIR, 'skills.json')

with open(SKILLS_JSON, 'r', encoding='utf-8') as f:
    skills = json.load(f)

categories = {}
for s in skills:
    categories.setdefault(s['category'], []).append(s)

category_meta = {
    'engineering-workflow': {
        'title_en': '🛠️ Engineering, Architecture & Agent Workflows',
        'title_ar': '🛠️ الهندسة البرمجية وتخطيط وسير عمل الوكلاء',
        'desc_en': 'Core process skills (Superpowers v7.0.2), test-driven development, systematic debugging, subagent-driven development, code review, merge resolution, Flutter/Dart tooling, and architecture specs.',
        'desc_ar': 'مهارات تخطيط وتطوير البرمجيات الأساسية (Superpowers v7.0.2)، التطوير الموجه بالاختبارات (TDD)، استكشاف الأخطاء المنهجي، إدارة الوكلاء الفرعيين، مراجعة الكود، وحلول فلاتر ودارت المعمارية.'
    },
    'frontend-ui': {
        'title_en': '🎨 Frontend, UI Design & Design Systems',
        'title_ar': '🎨 تصميم الواجهات الأمامية وأنظمة التصميم',
        'desc_en': 'Anti-slop design taste, shadcn/ui, brutalist and minimalist systems, Google Stitch, Apple HIG, Figma-to-code pipelines, D3 visualizations, and Three.js 3D shaders.',
        'desc_ar': 'أنظمة التصميم الراقية وتطوير واجهات المستخدم دون قوالب مكررة، مكتبات shadcn/ui، التصاميم التجريدية والمينيمالية، Google Stitch، إرشادات آبل Apple HIG، والتحويل من فيجما إلى كود.'
    },
    'ai-media-generation': {
        'title_en': '✨ AI Media, Image, Audio & Video Generation',
        'title_ar': '✨ توليد الوسائط بالذكاء الاصطناعي (صور، صوت، فيديو)',
        'desc_en': 'Comprehensive integrations for Fal.ai, Venice.ai, Sora, Google Imagen, Midjourney/DALL-E style image generators, device mockups, and AI music production.',
        'desc_ar': 'تكاملات كاملة لنماذج Fal.ai و Venice.ai و OpenAI Sora و Google Imagen، وتوليد الصور التوضيحية وتعديلها ونماذج الأجهزة 3D والموسيقى الذكية.'
    },
    'presentation-docs': {
        'title_en': '📄 Presentations, Decks & Document Automation',
        'title_ar': '📄 العروض التقديمية والوثائق والتقارير التنفيذية',
        'desc_en': 'Apple Keynote-quality slides, PowerPoint automation (PptxGenJS), OpenXML DOCX, PDF generators, executive memos, and Swiss international editorial layouts.',
        'desc_ar': 'تصميم وتوليد عروض بوربوينت وكي نوت بأعلى جودة واحترافية، مستندات Word DOCX و PDF و Excel XLSX، وتقارير البيانات والمذكرات التنفيذية.'
    },
    'motion-animation': {
        'title_en': '🎬 Motion, GSAP & Video Animation',
        'title_ar': '🎬 التحريك والأنيميشن التفاعلي وموشن الفيديو',
        'desc_en': 'Full GSAP suite (ScrollTrigger, Flip, Timeline, Performance), Remotion React video compositions, Hyperframes cinematic templates, and micro-interaction polish.',
        'desc_ar': 'مكتبة حركات GSAP المتكاملة لجميع أطر العمل، إنتاج الفيديو البرمجي عبر Remotion و Hyperframes، وتأثيرات الموشن الدقيقة والانتقالات السينمائية.'
    },
    'marketing-copywriting': {
        'title_en': '📣 Marketing, Brand & Copywriting',
        'title_ar': '📣 التسويق وكتابة المحتوى وهوية العلامة التجارية',
        'desc_en': 'Conversion-focused copywriting, creative direction frameworks, advertising psychology, brand voice guides, and social media viral cards.',
        'desc_ar': 'كتابة الإعلانات التسويقية الاحترافية، أطر العمل الإبداعية، علم النفس التسويقي، بناء هوية العلامة التجارية، وبطاقات السوشيال ميديا.'
    },
    'agent-tools-guides': {
        'title_en': '🧭 Agent Tools, Browsing & Assistant Personas',
        'title_ar': '🧭 أدوات الوكلاء وأتمتة المتصفح والمساعدين المتخصصين',
        'desc_en': 'Browser automation with agent-browser, screenshot captures, Antigravity guides, custom MCP server builders, and interactive advisory personas.',
        'desc_ar': 'أتمتة المتصفح وسطح المكتب، التقاط الشاشات، دلائل Antigravity، أدوات بناء خوادم MCP، والمساعدين الموجهين للاستشارات والتقييم.'
    }
}

# 1. English README
lines_en = [
    '# 🤖 AI Agent Skills Collection',
    '',
    '[![Total Skills](https://img.shields.io/badge/Total%20Skills-264-blue.svg)](skills.json)',
    '[![Categories](https://img.shields.io/badge/Categories-7-green.svg)](#-categories-summary)',
    '[![Superpowers](https://img.shields.io/badge/Superpowers-v7.0.2%20Latest-purple.svg)](skills/engineering-workflow/brainstorming)',
    '[![Compatibility](https://img.shields.io/badge/Harness-Antigravity%20%7C%20Claude%20Code%20%7C%20Codex%20%7C%20Cursor%20%7C%20OpenCode-orange.svg)](#-installation--setup)',
    '[![License](https://img.shields.io/badge/License-MIT-brightgreen.svg)](LICENSE)',
    '[![العربية](https://img.shields.io/badge/Language-%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9-red.svg)](README_AR.md)',
    '',
    '> A curated, production-ready collection of **264 agent skills** following the open `SKILL.md` specification. Designed for autonomous AI coding agents including **Google Antigravity**, **Claude Code**, **OpenAI Codex**, **Cursor**, and **OpenCode**.',
    '',
    '---',
    '',
    '## 📚 Quick Navigation',
    '',
    '- [✨ Overview](#-overview)',
    '- [📦 Categories Summary](#-categories-summary)',
    '- [🚀 Installation & Setup](#-installation--setup)',
    '- [🔍 Complete Skills Catalog](#-complete-skills-catalog)',
    '  - [🛠️ Engineering & Workflows](#️-engineering-architecture--agent-workflows-75-skills)',
    '  - [🎨 Frontend & UI Design](#-frontend-ui-design--design-systems-56-skills)',
    '  - [✨ AI Media & Generation](#-ai-media-image-audio--video-generation-38-skills)',
    '  - [📄 Presentations & Documents](#-presentations-decks--document-automation-30-skills)',
    '  - [🎬 Motion & Animation](#-motion-gsap--video-animation-28-skills)',
    '  - [🧭 Agent Tools & Guides](#-agent-tools-browsing--assistant-personas-21-skills)',
    '  - [📣 Marketing & Copywriting](#-marketing-brand--copywriting-16-skills)',
    '- [🔄 Updating Skills](#-updating-skills)',
    '- [📄 License](#-license)',
    '',
    '---',
    '',
    '## ✨ Overview',
    '',
    'This repository consolidates the most capable agent skills into a single structured, versioned, and easily deployable hub. Skills follow the standard 3-tier progressive disclosure model:',
    '1. **Metadata Frontmatter (`YAML`)**: Enables instant, lightweight discovery without bloating prompt context.',
    '2. **Core Instructions (`SKILL.md`)**: Loaded on demand when the agent recognizes relevance.',
    '3. **Bundled Assets / Scripts**: Reference guides, deterministic Python/bash scripts, and templates stored alongside the skill.',
    '',
    '---',
    '',
    '## 📦 Categories Summary',
    '',
    '| Category | Count | Primary Focus |',
    '| :--- | :---: | :--- |'
]

for cat_key, meta in category_meta.items():
    cnt = len(categories.get(cat_key, []))
    lines_en.append(f"| **{meta['title_en']}** | **{cnt}** | {meta['desc_en']} |")

lines_en.extend([
    '',
    '---',
    '',
    '## 🚀 Installation & Setup',
    '',
    '### Method 1: Automated Script (`install.sh`)',
    'Clone the repository and run the installer:',
    '```bash',
    'git clone https://github.com/abdelrahmanDev006/ai-agent-skills.git',
    'cd ai-agent-skills',
    'chmod +x install.sh',
    './install.sh',
    '```',
    '',
    '#### Selective / Targeted Installation Examples:',
    '```bash',
    '# 1. Install all skills into Antigravity global config:',
    './install.sh --target ~/.gemini/config/skills',
    '',
    '# 2. Install only Frontend & UI skills into current workspace:',
    './install.sh --category frontend-ui --target ./.agents/skills',
    '',
    '# 3. Install a single skill via symlink for zero disk duplication:',
    './install.sh --skill brainstorming --target ~/.gemini/config/skills --link',
    '```',
    '',
    '### Method 2: Manual Installation',
    'Copy the desired category or skill folder directly into your harness directory:',
    '- **Google Antigravity:** `~/.gemini/config/skills/` (Global) or `<workspace>/.agents/skills/`',
    '- **Claude Code:** `~/.claude/skills/` (Global) or `<workspace>/.claude/skills/`',
    '- **Codex / OpenAI:** `~/.codex/skills/`',
    '- **Cursor / Windsurf:** `<workspace>/.agents/skills/`',
    '',
    '---',
    '',
    '## 🔍 Complete Skills Catalog',
    ''
])

for cat_key, meta in category_meta.items():
    items = sorted(categories.get(cat_key, []), key=lambda x: x['name'])
    lines_en.extend([
        f"### {meta['title_en']} ({len(items)} skills)",
        '',
        f"> {meta['desc_en']}",
        '',
        '| Skill Name | Description | Link |',
        '| :--- | :--- | :---: |'
    ])
    for it in items:
        clean_desc = it['description'].replace('|', '-').replace('\n', ' ').strip()
        if len(clean_desc) > 130:
            clean_desc = clean_desc[:127] + '...'
        lines_en.append(f"| **`{it['name']}`** | {clean_desc} | [View]({it['relative_path']}/SKILL.md) |")
    lines_en.append('')

lines_en.extend([
    '---',
    '',
    '## 🔄 Updating Skills',
    '',
    'To sync the latest updates from upstream repositories (including new Superpowers releases and community additions):',
    '```bash',
    'git pull origin main',
    './install.sh --target ~/.gemini/config/skills',
    '```',
    '',
    '## 📄 License',
    '',
    'Distributed under the [MIT License](LICENSE).',
    ''
])

with open(os.path.join(ROOT_DIR, 'README.md'), 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines_en))

# 2. Arabic README_AR.md
lines_ar = [
    '# 🤖 مستودع مهارات وكلاء الذكاء الاصطناعي (AI Agent Skills)',
    '',
    '[![إجمالي المهارات](https://img.shields.io/badge/%D8%A5%D8%AC%D9%85%D8%A7%D9%84%D9%8A%20%D8%A7%D9%84%D9%85%D9%87%D8%A7%D8%B1%D8%A7%D8%AA-264-blue.svg)](skills.json)',
    '[![التصنيفات](https://img.shields.io/badge/%D8%A7%D9%84%D8%AA%D8%B5%D9%86%D9%8A%D9%81%D8%A7%D8%AA-7-green.svg)](#-ملخص-التصنيفات)',
    '[![سوبر باورز](https://img.shields.io/badge/Superpowers-v7.0.2%20%D8%A7%D9%84%D8%A3%D8%AD%D8%AF%D8%AB-purple.svg)](skills/engineering-workflow/brainstorming)',
    '[![التوافق](https://img.shields.io/badge/%D8%A7%D9%84%D8%AA%D9%88%D8%A7%D9%81%D9%82-Antigravity%20%7C%20Claude%20Code%20%7C%20Codex%20%7C%20Cursor%20%7C%20OpenCode-orange.svg)](#-طريقة-التثبيت-والاستخدام)',
    '[![الرخصة](https://img.shields.io/badge/%D8%A7%D9%84%D8%B1%D8%AE%D8%B5%D8%A9-MIT-brightgreen.svg)](LICENSE)',
    '[![English](https://img.shields.io/badge/Language-English-blue.svg)](README.md)',
    '',
    '> مكتبة متكاملة ومنظمة تضم **264 مهارة متخصصة** لوكلاء البرمجة والذكاء الاصطناعي، مبنية وفق المعيار القياسي `SKILL.md`، ومتوافقة تماماً مع **Google Antigravity** و **Claude Code** و **OpenAI Codex** و **Cursor** و **OpenCode**.',
    '',
    '---',
    '',
    '## 📚 الفهرس السريع',
    '',
    '- [✨ نبذة عن المستودع](#-نبذة-عن-المستودع)',
    '- [📦 ملخص التصنيفات](#-ملخص-التصنيفات)',
    '- [🚀 طريقة التثبيت والاستخدام](#-طريقة-التثبيت-والاستخدام)',
    '- [🔍 دليل المهارات الكامل](#-دليل-المهارات-الكامل)',
    '  - [🛠️ الهندسة البرمجية وسير عمل الوكلاء (75 مهارة)](#️-الهندسة-البرمجية-وتخطيط-وسير-عمل-الوكلاء-75-مهارة)',
    '  - [🎨 الواجهات وتصميم الأنظمة (56 مهارة)](#-تصميم-الواجهات-الأمامية-وأنظمة-التصميم-56-مهارة)',
    '  - [✨ توليد الوسائط بالذكاء الاصطناعي (38 مهارة)](#-توليد-الوسائط-بالذكاء-الاصطناعي-صور-صوت-فيديو-38-مهارة)',
    '  - [📄 العروض والوثائق والتقارير (30 مهارة)](#-العروض-التقديمية-والوثائق-والتقارير-التنفيذية-30-مهارة)',
    '  - [🎬 التحريك والموشن فيديو (28 مهارة)](#-التحريك-والأنيميشن-التفاعلي-وموشن-الفيديو-28-مهارة)',
    '  - [🧭 أدوات الوكلاء والمتصفح (21 مهارة)](#-أدوات-الوكلاء-وأتمتة-المتصفح-والمساعدين-المتخصصين-21-مهارة)',
    '  - [📣 التسويق وصناعة المحتوى (16 مهارة)](#-التسويق-وكتابة-المحتوى-وهوية-العلامة-التجارية-16-مهارة)',
    '- [🔄 تحديث المهارات](#-تحديث-المهارات)',
    '- [📄 الترخيص](#-الترخيص)',
    '',
    '---',
    '',
    '## ✨ نبذة عن المستودع',
    '',
    'تم تجميع هذه المهارات وتحديثها لتضم أحدث إصدارات **Superpowers v7.0.2** بالإضافة إلى مكتبات التصميم، التحريك، والذكاء الاصطناعي الأكثر تطوراً. تعتمد كل مهارة على المعمارية ثلاثية الطبقات:',
    '1. **البيانات الوصفية (`YAML Frontmatter`)**: تتيح للوكيل اكتشاف المهارة واستدعائها في اللحظة المناسبة دون استهلاك سياق الذاكرة.',
    '2. **التعليمات التفصيلية (`SKILL.md`)**: يتم تحميلها ديناميكياً فقط عندما يحتاجها الوكيل لمهمة محددة.',
    '3. **المراجع والسكربتات المرفقة (`Scripts & Assets`)**: أدوات برمجية وسكربتات Python/Bash وقوالب جاهزة للتنفيذ المباشر.',
    '',
    '---',
    '',
    '## 📦 ملخص التصنيفات',
    '',
    '| التصنيف | العدد | الوصف والنطاق الأساسي |',
    '| :--- | :---: | :--- |'
]

for cat_key, meta in category_meta.items():
    cnt = len(categories.get(cat_key, []))
    lines_ar.append(f"| **{meta['title_ar']}** | **{cnt}** | {meta['desc_ar']} |")

lines_ar.extend([
    '',
    '---',
    '',
    '## 🚀 طريقة التثبيت والاستخدام',
    '',
    '### الطريقة 1: السكربت التلقائي (`install.sh`)',
    'قم باستنساخ المستودع وتشغيل السكربت التفاعلي المباشر:',
    '```bash',
    'git clone https://github.com/abdelrahmanDev006/ai-agent-skills.git',
    'cd ai-agent-skills',
    'chmod +x install.sh',
    './install.sh',
    '```',
    '',
    '#### أمثلة للتثبيت المخصص والموجه:',
    '```bash',
    '# 1. تثبيت كافة المهارات داخل إعدادات Antigravity العامة:',
    './install.sh --target ~/.gemini/config/skills',
    '',
    '# 2. تثبيت مهارات الواجهات الأمامية فقط داخل مشروع العمل الحالي:',
    './install.sh --category frontend-ui --target ./.agents/skills',
    '',
    '# 3. تثبيت مهارة واحدة عبر رابط رمزي (Symlink) لتوفير المساحة وتحديثها تلقائياً:',
    './install.sh --skill brainstorming --target ~/.gemini/config/skills --link',
    '```',
    '',
    '### الطريقة 2: التثبيت اليدوي',
    'يمكنك نسخ أي مجلد مهارة مباشرة إلى مجلد المهارات الخاص بالأداة التي تستخدمها:',
    '- **Google Antigravity:** `~/.gemini/config/skills/` (شامل) أو `<workspace>/.agents/skills/` (خاص بالمشروع)',
    '- **Claude Code:** `~/.claude/skills/` أو `<workspace>/.claude/skills/`',
    '- **Codex / OpenAI:** `~/.codex/skills/`',
    '- **Cursor / Windsurf:** `<workspace>/.agents/skills/`',
    '',
    '---',
    '',
    '## 🔍 دليل المهارات الكامل',
    ''
])

for cat_key, meta in category_meta.items():
    items = sorted(categories.get(cat_key, []), key=lambda x: x['name'])
    lines_ar.extend([
        f"### {meta['title_ar']} ({len(items)} مهارة)",
        '',
        f"> {meta['desc_ar']}",
        '',
        '| اسم المهارة | الوصف والغرض | الرابط |',
        '| :--- | :--- | :---: |'
    ])
    for it in items:
        clean_desc = it['description'].replace('|', '-').replace('\n', ' ').strip()
        if len(clean_desc) > 130:
            clean_desc = clean_desc[:127] + '...'
        lines_ar.append(f"| **`{it['name']}`** | {clean_desc} | [عرض]({it['relative_path']}/SKILL.md) |")
    lines_ar.append('')

lines_ar.extend([
    '---',
    '',
    '## 🔄 تحديث المهارات',
    '',
    'لسحب أحدث التحديثات والإصدارات الجديدة للمهارات من المستودع:',
    '```bash',
    'git pull origin main',
    './install.sh --target ~/.gemini/config/skills',
    '```',
    '',
    '## 📄 الترخيص',
    '',
    'هذا المستودع منشور تحت رخصة [MIT License](LICENSE).',
    ''
])

with open(os.path.join(ROOT_DIR, 'README_AR.md'), 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines_ar))

print("README.md and README_AR.md generated cleanly.")
