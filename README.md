# CodeMapRT — Prioritized Regression Testing by Code Change Mapping

[![CI](https://img.shields.io/github/actions/workflow/status/yuliadrogunova/CodeMapRT/ci.yml?branch=main)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](#)

CodeMapRT is an open‑source, vendor‑neutral framework that selects and prioritizes regression tests based on recent code changes, component criticality, and historical instability. It outputs a ranked execution plan and an HTML report.

## Features
- Change‑aware test selection (changed files → components → tests)
- Risk‑based prioritization (criticality, historical flakiness, change complexity)
- Safety‑net subset to avoid missing critical regressions
- CLI + HTML report; easy CI/CD integration

## Quickstart
```bash
pip install -r requirements.txt
python -m codemaprt.cli --changed-files .codemaprt/changed_files.txt --report reports/index.html
pytest -q
```

## Demo Output
> Auto‑generated HTML report summarized below. Full report is in `reports/index.html` (created on first run or in CI).

![Full Prioritized Table](assets/CodeMapRT_Table_Full_1-33.png)

CI also builds a demo GIF from the HTML report and attaches it as an artifact (`codemaprt-gifs`).

## Repository Structure
- `codemaprt/` – framework package (mapping, prioritization, reporting, CLI)
- `.codemaprt/` – demo configuration (components/tests mapping, changed files)
- `demo_app/` – small app with modules for mapping
- `tests/` – unit, API, E2E examples
- `reports/` – HTML report output
- `assets/` – architecture diagram, PNG table, (CI) demo GIF
- `docs/` – whitepaper (DOCX + PDF)
- `.github/workflows/ci.yml` – runs selection + report and builds demo GIF

## License
MIT

## CI Artifacts
- `reports/index.html` — auto-generated prioritized regression report.
- `assets/CodeMapRT_Table_Full_1-33.png` — snapshot of the full prioritized table.
- `assets/demo.gif` — scrolling demo of the report (rebuilt in CI).
- Whitepaper available in `docs/` (DOCX + PDF).


## CI Artifacts & Demo
- Repository: [https://github.com/yuliadrogunova/codemaprt](https://github.com/yuliadrogunova/codemaprt)
- On each push to `main`, GitHub Actions publishes:
  - **codemaprt-report** — HTML report (`reports/index.html`)
  - **codemaprt-gifs** — scrolling demo GIF and full PNG table
- GitHub Pages hosts a live demo (landing + full report). See the URL in the `deploy-pages` job after the first run.
