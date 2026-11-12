# Product Requirements

## Document status

This document is the current product source of truth for the first version. It records the user's direct decisions from the preparation interview. The existing page is an early prototype and does not override these requirements.

Last updated: 2026-11-12.

## Product purpose

The product is a single interactive web page for the 30th anniversary of «Евросервис». Employees and other visitors with the URL will view a group collage and discover each person's first and last name by interacting with the portrait.

The current prototype was published through GitHub Pages on 2026-11-12 at <https://aveann9.github.io/eu.service30years/>. This prototype publication does not mean that the page satisfies the final acceptance criteria below.

## Confirmed first-version scope

### Page and content

- One standalone Russian-language page with no additional sections or routes.
- One primary group collage containing exactly 30 people on a yacht, with the director at the helm, his wife beside him, Moscow City in the background, and a fully visible Euroservice flag behind the group.
- `collage-yacht-v7.png` is the sole visible primary collage. The preceding collage remains stored as an inactive asset and is not rendered.
- Exactly 30 interactive person zones, each mapped to one visible person.
- Each label contains only the person's first and last name.
- The user will provide final names by identifying each person on the image.
- The user will continue revising faces in the collage before hotspot mapping is finalized.
- The eyebrow text remains `Евросервис · командный портрет` without a decorative line before it.
- The main heading is exactly two lines: `Люди,` and `которые держат курс`, with no terminal period.
- The descriptive text is `Коллаж сотрудников московского отдела продаж ко дню рождения компании Евросервис`.

### Desktop behavior

- A person's label appears when the pointer hovers over that person's zone.
- The label is positioned directly above the person's head.
- The label disappears when the pointer leaves the relevant interaction area.
- Desktop click must not be required and must not pin the label open.
- Label text must have strong contrast against its background and remain easy to read.

### Mobile behavior

- Tapping a person opens that person's label.
- At most one person's label is open at a time.
- Tapping the same person again closes the label.
- Tapping another person closes the current label and opens the new one.
- Each open label includes a small close button.
- Tapping the close button closes the label.
- When touch zones overlap, the zone nearest to the tap point is selected.
- A note above the portrait recommends rotating the phone to landscape orientation for better visibility and more accurate tapping.
- The current note copy is `Поверните устройство горизонтально — так изображение будет лучше видно, а выбирать людей будет удобнее.`
- The orientation note is shown on mobile and tablet contexts and is not shown on the desktop layout.
- The page must remain usable in portrait orientation; the recommendation must not force or lock device orientation.

### Content maintenance

- The user expects to update first and last names independently.
- All person records must be kept in one clearly marked place in the source code.
- A CMS or administration interface is not required for the first version.
- Individual images in `Фото/` are retained as source materials for portrait revisions and are not loaded by the page.

### Access, language, and discoverability

- The final page will be publicly accessible without accounts or roles.
- Search indexing is not wanted. The published HTML must request `noindex`; hosting configuration must not prevent crawlers from seeing that directive.
- Only Russian user-facing content is required.
- No authentication, password protection, payments, search, filtering, analytics, forms, or external integrations are required.

### Cost and timing

- There is no fixed deadline or allocated budget.
- The preferred implementation and hosting should be free where practical.
- A future custom-domain cost is acceptable, but domain and hosting selection are deferred.

## Out of scope for the first version

- Multiple pages or navigation sections.
- Employee profile pages or expanded cards.
- Opening individual photographs on click.
- User accounts, roles, or protected content.
- Server-side data storage, a database, or a CMS.
- Search, filters, payments, forms, analytics, and third-party integrations.
- Multiple interface languages.
- Treating a prototype publication as final acceptance of the content, design, or interactions.

## Current implementation status

The existing code and assets are preserved as a prototype:

- `index.html` and `dist/index.html` contain a static Russian page with an inline SVG portrait overlay.
- `dist/assets/collage-yacht-v7.png` is the sole visible interactive portrait. It retains the localized middle-right sofa row with Светлана, Артем, Валерия, Людмила, and Наталья, applies localized identity corrections to Катя, Алина, and the director, and is covered by 30 newly mapped provisional hotspot zones.
- Inactive recovery assets remain only in the private local workspace and are not part of the public repository.
- The prototype contains exactly 30 provisional hotspot records with first-name labels. Final name-to-face confirmation is still pending.
- Desktop hover and keyboard focus expose labels; coarse-pointer clicks/taps toggle the active label.
- The prototype does not provide a label close button.
- Source and distribution HTML now request `noindex, nofollow`.
- A GitHub Pages workflow is included in the clean public repository and completed its first successful deployment on 2026-11-12.
- The current visual styling remains provisional. The eyebrow, heading, descriptive text, and orientation-note copy listed above are confirmed.
- No fresh browser acceptance pass has been completed against all requirements in this document.

These are known implementation gaps, not unresolved product decisions.

## Preliminary ideas and hypotheses

- The current page can remain a working visual basis for discussion.
- The current light page, typography, colors, spacing, and composition may change after visual review.
- Files in `Фото/` may become useful later, but no first-version feature depends on them.
- GitHub Pages is the selected hosting provider. The current public URL is <https://aveann9.github.io/eu.service30years/>.

None of these hypotheses is an approved design or feature requirement.

## Resolved conflicts

- The prototype has 31 zones, while the final product requires 30. The final portrait review will identify the 30 valid people; the extra provisional zone will be removed.
- The prototype allows click-to-pin on desktop, while the confirmed desktop behavior is hover-only. The implementation must be corrected later.
- A hosting manifest exists in `.openai/hosting.json`, but it does not configure or authorize GitHub Pages. The file does not mean that a production version is approved or deployed.

## Open questions and deferred decisions

- Final collage image and final face edits.
- Identity and first/last name of each of the 30 people.
- Exact final hotspot geometry and label anchors after the collage is stable.
- Whether individual files in `Фото/` will ever become part of the page.
- Approved visual design and any remaining interface copy not explicitly confirmed above.
- Optional custom domain and any future release-specific verification.
- Final image format and compression after visual edits are complete.

These unknowns do not block documentation, the static technical foundation, or the user-authorized prototype publication. They do block final hotspot acceptance and final visual approval.

## First-version acceptance criteria

The first version is ready for publication only when:

1. The approved collage contains the intended 30 people.
2. Exactly 30 hotspot records map accurately to those people.
3. Every record has the confirmed first and last name.
4. Desktop hover behavior works without click.
5. Mobile tap, replacement, repeated-tap close, and close-button behavior work as specified.
6. Labels appear above heads, remain readable, and handle long names without clipping.
7. Overlapping mobile targets select the nearest intended person.
8. The landscape recommendation is visible on phones without forcing orientation.
9. Keyboard focus exposes equivalent name information with a visible focus state.
10. The page is checked in current desktop and mobile browsers.
11. The final image is optimized for mobile delivery without unacceptable visual loss.
12. The page includes a `noindex` directive.
13. Documentation matches the final implementation and publication workflow.

## Design status

The design concept is not approved. Do not treat the current palette, type, spacing, layout, label shape, or effects as permanent rules. Functional structure may proceed independently. Visual decisions must be based on approved mockups, specifically annotated references, or an agreed working visual prototype.

Do not create `DESIGN.md` until stable visual decisions exist and a separate design document would materially help implementation.
