# Euroservice Anniversary Portrait

## Purpose

This project is a standalone interactive group portrait for the 30th anniversary of «Евросервис». The final Russian-language page will show exactly 30 people and reveal each person's first and last name through desktop hover or mobile tap.

## Current stage

The project is in documentation and content-preparation stage.

- A local static prototype already exists and is preserved.
- The current collage is still being revised.
- `collage-yacht-v7.png` is now the sole visible primary interactive collage.
- The preceding `collage-yacht-v4.png` portrait is retained as an inactive asset and is no longer rendered by the page.
- The primary collage has 30 provisional hover/focus zones; final name-to-face confirmation is still pending.
- The current 30 provisional hotspots must be confirmed against the final people and names.
- The visual concept is provisional.
- The user authorized the safe public push and GitHub Pages publication of the current prototype on 2026-11-12.

## Documentation

- [AGENTS.md](AGENTS.md): mandatory instructions for agents and developers.
- [REQUIREMENTS.md](REQUIREMENTS.md): current product requirements, scope, gaps, and open decisions.
- [ARCHITECTURE.md](ARCHITECTURE.md): recommended static architecture, file responsibilities, standards, and future release constraints.

Read the documents in that order before changing the project.

## Project structure

- `.github/workflows/deploy-pages.yml`: GitHub Pages deployment workflow.
- `.gitignore`: exclusions for secrets, local settings, dependencies, and temporary output.
- `index.html`: editable page source.
- `dist/index.html`: static web-root copy.
- `dist/assets/collage-yacht-v7.png`: sole public portrait asset.
- `tests/`: lightweight checks for the portrait data and Pages configuration.

Private source portraits, inactive collage versions, print masters, and local hosting metadata are intentionally kept outside this public repository.

## Git status

The public repository uses a clean `main` history containing only approved repository files.

The authorized and designated GitHub repository is [AveAnn9/eu.service30years](https://github.com/AveAnn9/eu.service30years). Access through the connected `AveAnn9` account was verified on 2026-11-11 with read and write permissions. Unless the user names another repository, future GitHub instructions for this project refer to this repository. Repository access does not replace the explicit confirmation required for commits, pushes, publication, or other remote changes under [AGENTS.md](AGENTS.md).

The GitHub repository was made public on 2026-11-12 at the user's explicit request. The Pages workflow is included; activation and the first successful deployment are verified separately in GitHub.

The `dist/` directory remains version-controlled because it is currently the project's static web root rather than generated build output. Lock files and safe example environment files are not ignored.

## Local preview

No installation or build step is required. Python 3 is available in the current development environment.

From the project root, serve the `dist` directory:

```bash
python3 -m http.server 4174 --bind 127.0.0.1 --directory dist
```

Then open:

```text
http://localhost:4174/
```

The static server workflow was previously used successfully for browser preview. A new complete browser acceptance pass is still required after the final portrait, 30 hotspots, names, and confirmed interactions are implemented.

## Build, tests, and publication

- Build command: none.
- Installed dependencies: none.
- Automated tests: Python standard-library `unittest` checks the active image, one visible portrait, 30 unique records, in-bounds hotspot geometry, matching source/distribution HTML, the `noindex` directive, and the minimal Pages workflow.
- Formatter, linter, and type checker: none.
- Publication: the release-safe repository and workflow are prepared; GitHub Pages activation and the first successful deployment still require verification in GitHub.

Do not invent or report unavailable commands. Required future checks are defined in `ARCHITECTURE.md` and the acceptance criteria in `REQUIREMENTS.md`.

Run the current automated checks with:

```bash
python3 -m unittest discover -s tests -v
```

## Next practical step

Finish the portrait revisions, identify the exact 30 people, and provide each first and last name with a clear image reference. After that, replace the provisional hotspot data and implement the confirmed desktop and mobile interaction behavior before visual approval and publication planning.
