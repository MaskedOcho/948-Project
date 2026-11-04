# 948 FM 1947 — Remodel Model

Interactive 3D remodel model of a 1963 brick ranch (1,354 sq ft) in Hillsboro, TX.

## Live shared model
**https://claude.ai/artifact/8MYaLFjXaDRcwwWMhuVYNT** — the working copy everyone edits together.
Only people the owner shares it with (Share menu → Contributor or Editor) can open or change it.
Edits there sync live for everyone; this repo is the backup of the code and exports.

- **index.html** — the complete app in one file (three.js r128 inlined, works offline and on GitHub Pages)
- **src-artifact.html** — the same app loading three.js from CDNs (source of truth)
- **build.py** — rebuilds `index.html` from the source (`npm i three@0.128.0` first)
- **docs/** — original DXF / OBJ / layout JSON exports and preview renders

## Features
Editable floor plan · first-person walkthrough · street, aerial, bird's-eye and 360° tours ·
time of day · design studio with a material ID per surface (presets, colors, texture URL or upload) ·
saved designs · optional furniture · GLB export (offline file).

![Walkthrough views](docs/walkthrough-views.png)
