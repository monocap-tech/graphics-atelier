# GA-R01-S01-01 — Character instruction packets: meaning, decision authority, and delivery custody

**Opened:** 2026-11-18. **Maturity:** R1 for documented case-level claims; R0 for complete end-to-end cross-representation handoff. **Evidence:** EK-A primary practitioner/studio accounts; EK-B published independent commissioning guides; government model specification is an adjacent-domain governance reference, not evidence of actual game-studio practice. **Domains:** G02 / VG06 / VG08, with G03/G09 interfaces. **Decision:** continue S01; do not universalize.

## Target

Find and compare publicly inspectable character-design briefs, direction procedures, and actual handoff terms, preferably including a commercial and an independent game-production example. Determine what a document *can* specify, what the illustrator must interpret, how revisions become approved, and which details remain insufficient for downstream sprite/3D/animated representation.

No copyrighted artwork, spreadsheet attachments, contract forms, private source files or third-party illustrations are copied to this repo.

## Source ledger (inspected 2026-11-18)

| ID | Type / provenance | Inspected | Reliable bounded observation | Not demonstrated |
|---|---|---|---|---|
| S01A | [Akatsuki creative director Yōichi Shibata in CGWORLD, 2018-11-12](https://cgworld.jp/interview/201811-akatsuki.html), JP company-sponsored interview, EK-A | Relevant prose under ＜設計1＞ / ＜設計2＞ and Hachinai example | Akatsuki creates デザイン指示書 for internal/external illustrators. Separates design (appearance) from setting (backstory/character specification), relates game→character→individual still theme, character/story/acting-direction; staff coordinate with planners. The character's Bearmax attachment is a specifically narrative-bearing motif, not an arbitrary large graphic element. | Full original internal brief, editable masters, all approval log, contract or measurable impact on sprite conversion |
| S01B | [GIKUTAS / Search Field, Sachi and Gikuta design process, 2021-07-14](https://gikutas.jp/magazine/interview/210) + [continuation 2021-07-22](https://gikutas.jp/magazine/interview/211), JP publisher/commission-side process with artist Ariyoshi, EK-A | Narrative text for steps ①–⑧, public intermediate-design illustrations referenced on site | Initial 指示書 specifies look/personality/pose. Three initial human design candidates, client selection and feedback, face alternatives, 大ラフ, 色ラフ, 詳細ラフ, final line and color. Explicit changes: glasses thinner for eye visibility; selected search-symbol necklace and hair accent; Gikuta's plush impression emphasized while USB tail maintains AI reference; pose is arranged to show USB tail. Finished version checked face/glasses shadows. | Native editable files, complete production-ready rights/delivery terms, reuse of same asset as pixel sprite or model |
| S01C | [Ryōhei Tsuneishi, ㉒発注編e, 2020-07-29](https://note.com/ryodist/n/nccab784d973d) and [⑳発注編c](https://note.com/ryodist/n/n7d4fb919b005), JP independent visual-novel production log, EK-B | Complete publicly printed text of proposed character instruction for Ko-iro Rindō, organized under 基本情報, 外側情報, 内側情報, 参考イメージ | An inspectable independent *textual brief*: goal, age range, build, face, permitted hairstyle variation, personality, actions/speech and reference *attributes*. Creator argues information must be selected and grouped for readability, not endlessly added. A linked XLSX attachment exists but was **not opened**. | Whether a contracted artist accepted/revised it or a finished design and runtime handoff faithfully implemented it; XLSX content |
| S01D | [だらねこ, 絵が描けない人のためのイラスト依頼術, 2025-12-31](https://note.com/daraneko_games/n/n9774a1df9c19), JP independent developer's retrospective guide from actual commissions, EK-B | Published sample structure and method, not linked underlying Google Sheet | Distinguishes overview, working terms, dispute terms, detailed creative specification; explicitly names revisions, file format (PSD/PNG/JPEG), usage/portfolio rights, payment and source references. Reports one 600×800-pixel commission insufficient for later publicity reuse; a lesson about downstream use changing technical requirements. A Google spreadsheet template and an earlier commissioned-character detail sheet are linked. | Linked Sheets content, complete verified contractual arrangements; the author's view on contracts is **not** legal guidance and does not supersede written rights review |
| S01E | [AQUASTAR staff art director Ōta, NeON character case, 2021-06-17 (updated 2022-05-18)](https://aqua-star.co.jp/blog/illustrator-skill_006/), JP production team's firsthand retrospective, EK-A | Original expected-character table discussed, images and full described multi-variant approval process | An initial description with vague 'mood' and 'desirable' terms conflicted in part with stylized reference images vs stated tall anatomy; staff held a clarification meeting before drawing, then approved jacket vs coat, color, hairstyles and finished detail in separated passes. A short depiction was used to consider character personality and later animation. | Full signed source specifications, independently measurable costs of the ambiguity, pixel-art deliverables |
| S01F | [Agency for Cultural Affairs, animation work-commissioning example specification form, section (4) I-1-②](https://www.bunka.go.jp/seisaku/bunka_gyosei/kibankyoka/kenshukai/pdf/93994001_03.pdf), JP public advisory **template**, EK-B adjacent-domain document | Web-rendered PDF p.22 (zero-based screenshot index 21) and related explanatory text, section beginning around printed p.22 | Separately lists commissioning chain, delivered products, supplied starting materials, administrator, instruction/inspection personnel, acceptance criteria, formats, stages, changes and contractual conjunction. Recommended specs can include paper format or digital resolution/size/file type. It describes an agreed specification rather than assuming a unilateral fixed brief. | This is **not** an actual executed contract, nor a universal Japanese game development specification, nor automatic rights authorization. Its instructions concern animation work. |
| S01G | [Nora, individual game commissioning retrospect, 2026-09-03](https://note.com/stray_dog0012/n/nb1ccebf6214d), JP self-report, EK-B | Commissioning section about six-to-seven figures and expression variants | Reports small first commission as an approval trial, neutral pose to accommodate 5 expression states, and a conflicting text/image reference ('apron' vs 'jacket') discovered midway, requiring an audit. | Independent verification of the transaction, actual reference packet, general prevalence of these errors |

Dates above are page publication dates when known, not claims about when all work occurred. Published exemplars are heterogeneous (mobile-game stills, company mascots, visual novel stills, animation commissioning); **none** is a complete verified original illustration→dot-art production packet. Do not collapse them into one historical standard. Source photos and illustrations may contain third-party references; publication on a page does not grant repository redistribution rights.

## Comparative packet completeness matrix

Legend: **E** explicit inspectable account/text; **P** partial/indirectly documented; **—** not demonstrated in accessible material. This audits source coverage, not the quality of the actual private production.

| Field / requirement | Akatsuki | GIKUTAS | Tsuneishi independent | Daraneko independent | Agency template |
|---|---|---|---|---|---|
| Creative theme / intent | E | E | E | E | — |
| Physical traits / design reference | P | E | E | E | — |
| Personality / character world | E | E | E | E | — |
| Explicit design alternatives & approvals | P | E | — | P | P (role/process, not designs) |
| Story-bearing or identity-bearing small features | E | E | P | P | — |
| Usage context and alternate outputs | E (stills) | E (social character) | P (VN) | E (game/promotion) | P (animation work) |
| Technical export size/formats | — | — | — | E | E (specified as required field) |
| Revision/inspection authority | P | E | — | E | E |
| Contractual rights and payment arrangements | — | — | — | E (author's practice) | P (linked contract, separate terms) |
| Target-native sprite/palette/pose/anchor requirements | — | — | — | — | — |
| Documented downstream sprite/modelling revision propagation | — | — | — | — | — |

Where publication describes a source packet without displaying its actual full content, an **E** denotes specifically *attested* requirements or decision behavior, not direct possession of every field.

## Findings and tensions

1. **Meaning vs depiction:** Akatsuki explicitly separates 設定 from デザイン. An identity-bearing object can derive its importance from story or brand, not from occupied pixels. GIKUTAS makes the relation concrete: mechanical identity is carried by the USB tail and made visible through a chosen pose. This does not prove that every icon/sprite of the character must depict it.
2. **Directive vs interpreted choice:** A 指示書 does not inherently eliminate artist judgment. GIKUTAS's three-to-one exploration and AQUASTAR's explicit ambiguity negotiation show proposed/revised decisions becoming canonical only after feedback.
3. **Readability vs completeness:** Tsuneishi advocates selecting and grouping decisive information; Daraneko advises retaining detailed information while moving it down the document. These approaches are not necessarily contradictory: a short operative summary and a distinct detailed appendix can coexist. Their optimal lengths have not been tested.
4. **Source fidelity vs future use:** Daraneko's 600×800 example shows that matching the initial runtime image size may be insufficient for other published uses. This is a first-person caution, **not** evidence that any particular 3000px standard is correct.
5. **Text vs images:** AQUASTAR's expressed high stature vs reference proportions and Nora's apron-vs-jacket discrepancy show that the packet must say how to resolve conflicts. Automatically privileging text or a single image is a **proposed policy question**, not an attested universal studio rule.
6. **Creative approval vs delivery custody:** Agency animation forms assign instruction, checking, and managing roles plus format/delivery requirements. They should not be imported wholesale as game contracts, and public PDFs do not confer third-party artwork rights.
7. **Missing bridge to sprite adaptation:** None of the surveyed cases provides an inspected full source-layer/approved-assets→native-pixel sprites→multiple pose/representation variants→export/version agreement. S01 is not closed by a successful illustration brief alone.

## Synthesis: four distinct specification layers (our model, not historic terminology)

- **Interpretive:** audience/scene/character intention; character/world/story constraints; expressive priorities; meaning of details.
- **Visual authority:** physical design, orientation, asymmetry, color relations, permitted changes; reference priority; approval state of each variant.
- **Production interface:** roles/acceptance, intermediate files, size/density, layering/registration, poses, palette and runtime usage; change requests, checkpoints, downstream consequences.
- **Custody and governance:** origin/rights/license or negotiated use, compensation, deliverables, editable masters, distribution/portfolio scope, revision and dispute process.

One file need not contain all layers, and not every work needs a large contract. But **failing to distinguish them makes source art seem more authoritative and reusable than the evidence warrants**.

### Adaptation stress-test, not yet executed

An original fictional character has a high-visibility scar (identity), one lower-visibility asymmetrical wrist charm (story-bearing), and another freely changeable accessory (decoration). Downstream outputs requested: small gameplay raster, character portrait, model sheet. Create short two-level brief (priority summary + linked detailed construction/rights information), deliberately contrast one missing reference angle, then ask two independent renderers/roles to mark:
- what was conserved, simplified, replaced, hidden for context, or escalated for approval;
- conflicts between stated intentions and image examples;
- which delivered file can legally/technically be edited and resold or repurposed (requires actual agreement, not speculative permission);
- whether a later approved charm-color change propagates correctly to every affected variant.

The **first** executable test should be smaller than a full sprite library: one original source drawing, one alternative crop/sprite and one revision, with precommitted authority and format fields. Record disagreements and hours, not just resemblance.

## Open obligations and next questions

- Recover a **complete, lawfully inspectable** actual brief including version/approval history and final editable delivery; the GIKUTAS and Tsuneishi publication excerpts are strong but not full delivered packets.
- Understand how a character's immutable/optional features are authored and approved in a **documented** pixel-sprite or 3D game pipeline. Avoid presupposing a master single-source hierarchy.
- Determine who has authority to approve omission/exaggeration when the target representation cannot display a story-bearing object.
- Test source-text vs image-priority rules on a new *original* specimen and report failure cases. Another person's work cannot be used to assert rights by analogy.

**Decision:** Keep GA-R01-S01 open after this R1 source qualification. A possible S01-02 is *design approval and representation change authority*: actual variant/version handoffs, artist-led deviations and documented revisions. Preserve independent research time; no artificial schedule, no unified doctrine, and no Suzuki/AM2 duplication.
