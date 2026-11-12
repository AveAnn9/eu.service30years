# Agent Instructions

## Communication and documentation language

- Communicate with the user in Russian, including questions, explanations, progress updates, and handoff notes.
- Write and maintain all project Markdown documents in English, including headings, rules, decisions, explanations, and open questions.
- Use English file names for project documentation.
- Preserve brand names, quotations, source material, and user-facing interface copy in their meaningful original language. The documentation language does not determine the website language.
- Translate the user's decisions accurately. Do not introduce additional product requirements while translating them into documentation.

## Source-of-truth order

When information conflicts, use this priority:

1. The user's latest explicit decision.
2. `REQUIREMENTS.md` for the current product scope and behavior.
3. `ARCHITECTURE.md` for technical decisions and constraints.
4. The current implementation.

The implementation must not silently redefine a confirmed requirement. If code and documentation disagree, either correct the code or explicitly agree on a requirement change with the user.

## Required context before work

Read these files before every project task:

1. `AGENTS.md`
2. `README.md`
3. `REQUIREMENTS.md`
4. `ARCHITECTURE.md`

Also inspect the files directly affected by the task. For portrait or hotspot work, inspect the active collage asset, the `people` data, and the SVG interaction code. For publication work, inspect `.openai/hosting.json` and obtain the user's explicit publication task before making any deployment change.

There is no approved `DESIGN.md`. Do not create one until visual decisions are approved through agreed mockups, specifically annotated references, or a working visual prototype.

## Documentation map

- `README.md`: project purpose, current stage, file map, and verified local workflow.
- `REQUIREMENTS.md`: confirmed product requirements, scope, current gaps, hypotheses, conflicts, and open questions.
- `ARCHITECTURE.md`: recommended stack, code organization, interaction model, data ownership, constraints, and deferred technical decisions.
- `AGENTS.md`: working rules for agents and developers.

Avoid duplicating the same decision across documents. Put each topic in its primary document and link to it where useful.

## Development principles

### Reuse before creation

Inspect existing components, functions, data, and styles before adding new ones. Reuse shared behavior consistently. Do not copy the same hotspot, label, or interaction logic into separate page-specific implementations.

### Separation of responsibilities

Keep presentation, interaction state, portrait data, and release/deployment concerns conceptually separate. Do not mix hosting credentials or publication logic into the page. At the current scale, a single HTML file is acceptable, but sections within it must remain clearly labeled and independently understandable.

### Proportionate structure

Do not split files or introduce abstractions based on arbitrary line counts. Do not create a universal component with many options to combine genuinely different behavior. Structure must remain proportional to this single-page project.

### Visual consistency

The current visual treatment is provisional. Do not document colors, typefaces, spacing, or composition as approved design rules. After visual approval, centralize shared visual values and reuse shared components. Do not create a separate visual system for one interaction without a documented reason.

### Dependencies

Check browser-native HTML, CSS, JavaScript, and SVG capabilities before adding a library. Record the reason for any significant dependency in `ARCHITECTURE.md`. Do not install a dependency without a concrete requirement that the current stack cannot reasonably satisfy.

### Refactoring

Preserve confirmed behavior and approved appearance during internal refactoring. Report behavior changes separately. Do not perform broad unrelated restructuring while completing a focused task.

### Interface quality

Account for responsive layouts, touch input, keyboard access, visible focus, readable contrast, long names, overlapping hotspots, and clear open/closed label states. Test both desktop hover behavior and mobile tap behavior. Loading, error, and empty states are required only when the implemented feature can produce those states.

### Performance

Avoid unnecessary libraries and heavy assets. Optimize the final portrait for practical mobile delivery without visibly damaging faces or text. Define and report concrete file sizes and browser checks instead of promising abstract maximum performance.

### Data and access

Keep placeholder names clearly distinguishable from final employee data. Do not publish personal names or portraits until the user provides the final content and explicitly requests publication. Do not store secrets in source files. Any future server-side access control must be enforced on the server, not only in the interface.

### Testing and verification

#### Add tests with implementation

Add necessary automated tests together with the functionality they protect, within the same task. Do not postpone critical-scenario coverage to a separate undefined stage.

No automated test tool is configured yet. Configure the smallest suitable testing setup when the first implemented code requires automated checks, using tools compatible with the selected stack. Do not select or configure a test tool in advance without such code.

#### Choose coverage by risk

Do not require exhaustive scenario coverage or an arbitrary code-coverage percentage. Prioritize:

- critical user journeys;
- substantial business or interaction logic;
- validation, storage, and retrieval of data when those capabilities exist;
- meaningful errors and failure modes;
- authorization and access rules if the product later introduces them.

Do not create tests for quantity, trivial static markup, or the internal structure of an implementation when the observable behavior is what matters.

#### Review tests when code changes

Before changing code, identify the affected behavior and the existing tests or checks that protect it.

- If confirmed behavior changes, update the related tests and add coverage for the new conditions in the same task.
- If behavior must remain unchanged, including during refactoring, existing behavior tests must continue to pass. Do not automatically rewrite them to follow the new implementation.
- If existing tests do not cover a substantial change, add the necessary checks.
- Do not change expected results, weaken assertions, disable tests, or remove checks merely to obtain a passing result. First determine whether the failure is caused by implementation, an agreed requirement change, or an incorrect test.

#### Protect bug fixes from regression

For a bug fix, add a regression test when the failure can be reproduced reliably and the automated check provides lasting value. When practical, first confirm that the test fails for the defect, then verify that it passes after the fix.

If automation is not appropriate, perform the best available manual or targeted check and report it explicitly.

#### Run checks throughout the task

- After implementing a feature or fix, run the related tests and checks for the affected area.
- When shared components, dependencies, configuration, or module interactions change, expand checks to dependent areas.
- Before completing a task, run all applicable checks.
- Before a release, run the full configured automated suite and exercise critical user journeys end to end.
- A successful build does not replace behavior testing.
- Automated tests do not replace browser-based visual, responsive, keyboard, mouse, and touch verification.

For this interface, browser checks must cover desktop hover without click, mobile tap state, the close control, replacement and repeated-tap behavior, keyboard focus, readable accessible names for all 30 people, hotspot accuracy, long Russian names, label contrast, and portrait and landscape layouts.

#### Isolate test data and environments

Use dedicated test data and a separate test environment when the project gains persistent data or external services. Tests must not modify real user data. Never commit credentials, access tokens, or other secrets.

#### Resolve failures rather than reporting them prematurely

If tests or other checks reveal a defect caused by the current task, determine the cause, fix it, and rerun the relevant checks without requesting separate permission for the ordinary in-scope correction. Recheck related scenarios that may have been affected and continue until applicable checks pass or a concrete blocker requires user input or unavailable resources.

If the test itself is wrong, correct it according to confirmed requirements. Ask the user when the expected behavior is genuinely ambiguous. For a pre-existing unrelated defect, assess and report its impact without starting broad unrelated work. If it blocks the current task, state that explicitly.

When a defect cannot be resolved, report what fails, the identified cause, actions already attempted, and what is required to continue.

#### Maintain testing documentation and report honestly

Update relevant documentation in the same task when test scenarios, verification rules, tools, environments, or commands change. Add test commands to `README.md` only after they are implemented and successfully verified.

In every task report, state:

- tests added or changed;
- checks run and their results;
- checks not run and the reason.

The presence of test files is not evidence that tests passed. If a required check fails or cannot run, identify verification as incomplete. No formatter, type checker, linter, automated test runner, or build pipeline is currently installed; do not claim those checks until they exist and have run successfully.

## Mandatory documentation maintenance

Documentation maintenance is part of the same task as the related change and does not require a separate user request.

### Before a change

- Identify which documents describe the affected behavior or structure.
- Check current requirements, constraints, and open questions.
- Note any mismatch between documentation and implementation.

### During a change

- Update the primary document when requirements, behavior, architecture, data, integrations, access, design status, commands, or constraints change.
- Correct or remove replaced information rather than appending a contradictory note.
- Update links and paths when files move or are renamed.
- Mark planned work as implemented only after the implementation and required checks are complete.

### Before completion

- Re-read all documents affected by the task.
- Confirm that instructions and current behavior do not contradict each other.
- Report documentation updates together with implementation results.
- State what was checked, what remains unchecked, and any relevant limitations.

Documentation must be updated when the first-version scope, user scenarios, pages, significant features, project structure, technology, dependencies, data model, data sources, integrations, access rules, approved design decisions, environment setup, commands, publication process, or important constraints change.

Do not document every internal helper or minor edit. Update documentation when omission could cause a future agent or developer to misunderstand, violate, run, or maintain the project incorrectly.

## Git and commit workflow

- The authorized GitHub repository for this project is `https://github.com/AveAnn9/eu.service30years.git` (`AveAnn9/eu.service30years`). The user explicitly authorized agents to access and work with this repository for project-related GitHub tasks.
- Unless the user explicitly identifies another repository, all future GitHub instructions for this project refer to `AveAnn9/eu.service30years`.
- GitHub access was verified on 2026-11-11 through the connected `AveAnn9` account with read, write, maintain, and administrator permissions. The repository was made public at the user's explicit request on 2026-11-12 and uses a clean public `main` history that excludes private working assets.
- Keep source portraits, inactive collage versions, print masters, and local hosting metadata out of the public history. Only add an asset when the user explicitly approves it for the public repository.
- This repository authorization does not by itself authorize a commit, push, publication, deployment, or other remote mutation. Perform those actions only when the user's current task explicitly requests them and follow the confirmation rules below.
- Do not push, publish, or transmit repository contents to an external service without explicit user authorization.
- Do not change global Git configuration. If repository-local identity or other configuration is required, use only values provided or approved by the user.
- Do not rewrite history, discard user changes, or run destructive Git operations without a direct user request.

Never create a commit automatically. Every commit requires the user's explicit confirmation for the exact proposed scope.

After each substantial, logically complete change:

1. Run the checks applicable to the change.
2. Update all related Markdown documentation.
3. Inspect the working tree, diff, and proposed commit contents.
4. Briefly report what changed and how it was verified.
5. Ask the user in Russian whether to create the proposed commit.
6. Commit only after an explicit affirmative response.

A substantial change includes completed functionality, a significant bug fix, a refactor, an architecture or configuration change, dependency changes, or a meaningful documentation update. Do not ask for a commit after each file edit or intermediate step; group related edits into one coherent change.

If the user declines, does not answer, or moves to another task, do not commit. Keep the changes in the working tree. Silence is not approval.

If changes from multiple tasks have accumulated, disclose the full proposed composition. Do not silently include postponed or unrelated work. Propose separate commits when that produces clearer history. Include code and its directly related documentation in the same commit.

Approval applies only to the described contents. If the proposed contents change materially after approval, request confirmation again.

After creating an approved commit, report:

- the short commit identifier;
- the commit message;
- whether uncommitted changes remain.

## Reporting

Every handoff must state:

- what changed;
- how it was verified;
- what was not verified;
- remaining gaps, risks, or open decisions;
- any documentation updated as part of the task.

Do not describe work as complete when required checks were not performed unless the reason and impact are clearly reported.
