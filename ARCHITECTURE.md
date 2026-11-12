# Architecture

## Recommended technical solution

Use a static, dependency-free web page built with:

- semantic HTML;
- responsive CSS;
- vanilla JavaScript;
- inline SVG for the portrait image, hotspot geometry, label anchors, and interaction targets.

Do not add a framework, server, database, CMS, package manager, or build system for the confirmed first version.

## Why this is sufficient

The product has one page, one fixed portrait, 30 small data records, and limited pointer interaction. Browser-native technologies already support responsive images, interactive SVG, pointer input, focus handling, and simple state management. A framework would add installation, build, upgrade, and hosting complexity without solving a confirmed requirement.

This approach supports:

- exact SVG coordinates tied to the portrait's view box;
- desktop hover behavior;
- mobile tap behavior and nearest-zone selection;
- responsive scaling without recalculating the artwork layout;
- one clearly marked person-data collection;
- low-cost static hosting later;
- future visual changes without committing to a component library.

## Practical consequences

### Benefits

- No dependency installation or recurring software subscription.
- No backend or database to secure and maintain.
- The page can be hosted by most static hosting services.
- The complete behavior remains inspectable in a small amount of code.

### Limitations

- The user will edit names in source code rather than through an admin screen.
- Every final face or composition change may require hotspot and label-anchor review.
- Manual source and distribution copies can drift until the release workflow is consolidated.
- A public static URL cannot provide real access secrecy; `noindex` reduces search visibility but is not access control.

No alternative stack is recommended at this stage because there is no confirmed tradeoff that justifies additional complexity. Reconsider a framework or content system only if the project gains multiple pages, frequent nontechnical content editing, remote data, authentication, or materially more complex interaction.

## Standards verification

The recommendation was checked against current official documentation on 2026-11-10:

- [WHATWG HTML Living Standard](https://html.spec.whatwg.org/multipage/embedded-content.html) for embedded content and HTML/SVG use.
- [W3C SVG 2: Scripting and Interactivity](https://www.w3.org/TR/SVG2/interact.html) for interactive SVG events, hit testing, pointer events, and focus.
- [W3C Pointer Events Level 3](https://www.w3.org/TR/pointerevents3/) for hardware-independent mouse, pen, and touchscreen input. It is a W3C Recommendation dated 2026-06-30.
- [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/) for keyboard access, visible focus, orientation, contrast, and target-size considerations.
- [Google Search Central: noindex](https://developers.google.com/search/docs/crawling-indexing/block-indexing) for preventing supported search engines from indexing the page. The directive must be visible to a crawler and must not be hidden behind a blocking `robots.txt` rule.

GitHub Pages was selected as the hosting provider on 2026-11-12. The workflow completed its first successful deployment, and the prototype is available at <https://aveann9.github.io/eu.service30years/>.

## Current file organization

```text
.
├── .github/
│   └── workflows/
│       └── deploy-pages.yml
├── .gitignore
├── AGENTS.md
├── ARCHITECTURE.md
├── README.md
├── REQUIREMENTS.md
├── index.html
├── dist/
│   ├── index.html
│   └── assets/
│       └── collage-yacht-v7.png
└── tests/
│   ├── test_hotspots.py
│   └── test_pages_deployment.py
```

Current convention:

- `.gitignore` excludes secrets, local settings, dependencies, generated outputs, caches, logs, and temporary files while preserving lock files and safe example configuration.
- Root `index.html` is the editable source copy.
- `dist/` is the local web root and future static release snapshot.
- `dist/assets/collage-yacht-v7.png` is the sole portrait rendered inside the interactive SVG and is covered by 30 newly mapped provisional hotspot zones.
- Source portraits, inactive collage versions, print masters, and local hosting metadata remain in the private local workspace and are excluded from the public repository.
- `.github/workflows/deploy-pages.yml` packages only `dist/index.html` and `dist/assets/collage-yacht-v7.png`; inactive collages, source photographs, print files, and repository secrets are not included in the Pages artifact.

Until a build or release process is justified, changes to root `index.html` must be copied deliberately to `dist/index.html`, and both files must be compared before handoff. This manual duplication is the main maintenance risk in the current structure. A future publication task may consolidate the web root if that can be done without making the project harder for the user to maintain.

## Planned page responsibilities

### Markup and presentation

- Page title, short instruction text, mobile landscape recommendation, portrait container, and supporting accessibility text.
- Provisional visual styles remain editable and must not be treated as an approved design system.

### Person data

Keep all 30 records in one clearly labeled `people` collection. Each record should contain, at minimum:

- first name;
- last name;
- hotspot geometry in SVG view-box coordinates;
- a label anchor above the head.

Use descriptive field names when the data is revised. Final names must not be mixed with placeholder values.

### Interaction state

- Desktop: hover and keyboard focus expose a name; pointer click does not pin it.
- Touch: one active person ID or no active person.
- A tap selects the nearest eligible hotspot to the transformed SVG tap coordinate.
- Tapping the active person, its close button, or outside the relevant interaction closes it.
- Tapping another person replaces the active person.

Input behavior should be selected through input capabilities and pointer events rather than user-agent string detection.

### Accessibility

- Every person target must have a readable accessible name containing the final first and last name.
- Keyboard focus must provide information equivalent to pointer hover even though desktop mouse clicks are not used.
- Focus must be visible.
- Label text and close controls must meet readable contrast and practical target-size requirements.
- The page must not lock device orientation.

## Image workflow

- Preserve accepted versions instead of destructively replacing the only portrait file.
- Give each meaningful revision a versioned file name.
- Update the active SVG image reference only after reviewing the revision.
- Keep secondary static portraits outside the interactive SVG unless the user explicitly requests hotspot behavior for them.
- Recheck all 30 hotspots and label anchors after any image edit that can move a face, head, or body.
- Optimize the final delivery image only after face generation is complete. The current active PNG is approximately 2.5 MiB, so mobile-size and image-format review is required before final release.

## Content update workflow

For the first version, the user updates names in the single person-data collection. No CMS is planned. Before publication, a developer or agent must validate spelling, the 30-record count, hotspot mapping, and label layout.

Changing the portrait requires a new versioned asset and hotspot review. Changing only a name should not require changing geometry.
The active yacht image and its hotspot geometry are coupled; any future image revision requires rechecking all 30 zones and label anchors.

## Hosting and operations

The site needs only static-file hosting. GitHub Pages is the selected provider and should use the repository's standard free `github.io` URL unless the user later chooses a custom domain. A minimal GitHub Actions workflow is included in the public repository. It checks out the repository, prepares a two-file public artifact from `dist`, and deploys that artifact through the standard `github-pages` environment. It uses the workflow's scoped `GITHUB_TOKEN` permissions and does not require user-managed secrets.

The public `main` branch uses a clean history containing only approved repository files. The complete working history and private assets remain separate locally. Future public updates must preserve this separation. The workflow deploys the site to <https://aveann9.github.io/eu.service30years/>. Verifying caching and documenting rollback remain future release actions.

Before treating a deployment as the final first-version release:

- retain the user's explicit authorization for the safe public push and Pages publication;
- confirm the final portrait and names are approved for public use;
- add and verify `noindex`;
- confirm that the history being pushed does not contain source portraits or other private working assets;
- complete the acceptance checks in `REQUIREMENTS.md`;
- document the actual provider, commands, costs, and rollback procedure.

## Quality strategy

The project uses Python standard-library `unittest` for lightweight static checks. Run `python3 -m unittest discover -s tests -v`. The current checks validate the sole active portrait reference, matching source/distribution HTML, exactly 30 unique person records, hotspot bounds within the `1586 × 992` view box, the `noindex` directive, the required Pages permissions and official actions, and the restricted two-file publication artifact.

### Planned automated test priorities

The following scenarios are planned candidates for automated checks as their implementation is developed:

- the final person collection contains exactly 30 valid records;
- every final record contains a non-empty first name, last name, hotspot geometry, and label anchor;
- desktop pointer interaction exposes the correct label without click-to-pin behavior;
- touch state permits at most one open label, closes on a repeated tap, switches on another-person tap, and closes through the close control;
- overlapping touch zones select the eligible person nearest to the transformed tap coordinate;
- keyboard focus exposes the same name information and remains visibly focusable;
- a regression test accompanies a reproducible significant bug when automation provides lasting value.

The record-count and geometry-bound checks are implemented. Interaction behavior and exact face-to-name mapping still require browser and user verification.

### Planned browser and release verification

Automated checks will not replace browser QA. Before release, the planned manual or browser-driven verification includes:

- exact mapping of all 30 hotspots to the approved portrait;
- desktop hover, keyboard focus, mobile taps, close control, replacement, and repeated taps;
- portrait and landscape phone layouts plus representative tablet and desktop sizes;
- the orientation recommendation appearing only in mobile and tablet contexts;
- long Russian first and last names, label positioning above heads, contrast, and clipping;
- image loading, responsive scaling, and practical mobile asset size;
- `noindex` presence, console errors, and broken asset paths;
- critical interaction scenarios exercised end to end.

If the project later gains persistent data, integrations, or access control, add isolated tests for validation, storage, retrieval, failures, and permissions at that time. Test data must remain separate from real user data and no secret may enter the repository.

Run related checks throughout implementation, the complete configured suite before release, and dependent checks after shared code or configuration changes. A successful build is not a substitute for behavior testing, and test files are not evidence of a passing run.
