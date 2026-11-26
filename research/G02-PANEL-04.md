# G02-PANEL-04 — From printed panel to executable presentation

2026-11-19. Bounded follow-up to [G02-PANEL-03](G02-PANEL-03.md). R1 documentary observations, R0 candidate transfer architecture. No old software executed, serialized format decoded, game footage inspected, or complete historical layered shōjo specimen newly acquired. Keep the latter acquisition gap explicit.

## A. CELSYS: production-to-player pipeline, 2003–2015

CELSYS December 2003 announcement, pp.1–3, with p.2 workflow diagram visually inspected: paper acquisition/scan and correction (ComicScan) -> line/tone separation, balloon regions and ComicStudio-format conversion (ComicStudioEnterprise) -> panel regions, content behavior, preview and save (FrameEditor) -> device playback (ComicSurfing). The announcement describes vector-based data for different device resolutions, dimensions and operating systems; this does not establish that every layer is vector or that all exports are resolution independent. FrameEditor enumerates panel/page presentation order, transition effects, hotspot and vibration events, default display size; list includes planned future support explicitly. The diagram confirms division of tool responsibilities, not the executable data schema.

July 2004 announcement describes zoom, panel navigation and balloon enlargement and Ver.2.0 pipeline: SCANNER; EQUALIZER (line, tone, balloon and grayscale separation); EFFECTOR (panel metadata, output/preview); EFFECTOR-J (raster sequential/紙芝居 mode, image quality, scroll and effects); ANALYZER (batch processing). Text inspected; p.3 screenshot failed. 2007 ITmedia report identifies localized Effector Neo (split and effects), Effector HandsFrame (dimensions and scroll order), Checker (proofing), among eight enterprise tools. CELSYS's 2015 BS Reader announcement confirms panel display and vibration/effects supported as a later product capability. These distinct releases cannot be collapsed into a single 2003 shipped feature list.

JEPA industry retrospective by CELSYS's 川上陽介 records a 2002 unreleased PDA viewer feeding mobile work, 2003 KDDI solution, 2004 other carrier support, 2006 BookSurfing, 600 sites and over 2.1 million content files as of October 2008 (company-reported figures, not audited market share or readers). The firm explicitly describes building a content production line and tool support with publishing partners. Documented institutional path from anime tooling (RETAS!PRO) and manga tooling to digital distribution; not proof of direct code inheritance or retro game lineage.

2017 magazine-k retrospective describes raster 紙芝居 production and pan/tilt, directional movement, sound/vibration. Author argues apparently redundant panels in print can become tedious when isolated, and omission/reordering raises editorial integrity issues. This is practitioner interpretation, not controlled user research. Do not equate all feature-phone manga, later reading apps and webtoons.

## B. Manga Word Processor (マンガワープロ)

IPA archived 3-page project report, developer 儀間武晃 (University of Electro-Communications). A working Windows/.NET 2.0 and Microsoft.Ink prototype is reported. Motivation: page-spanning panel arrangements are hard to revise after drawing. Panel-level content and drawing, text, source framing, relative size and page-turn (メクリ) constraint feed automatic rectangular layout according to page shape/binding direction, with interactive editing. Fig.1 caption identifies drawing and framing editing; figure screenshot failed, so no independent visual UI description. Intended facilitation of conversion to different book dimensions/page counts, not established publisher adoption. Publication year not verified from report. No executable/source obtained; algorithm and supported complexity untested. Strong technical precedent for separable content, crop, ordering and page allocation; not proof that expressive nonrectangular layering can be automatically recovered.

## C. Format adaptation as editorial work

TOPPAN クロレ's account documents both print-to-vertical and vertical-to-print services. Staff report different spacing, panel emphasis, background and balloon positions; design decisions sometimes delegated to prepress operators. These are real process reports, not measured timing or universal aesthetics. The DNP/Jump TOON interview records problems with detail density and legibility on phone displays; editors describe replacing spread-edge hooks with repeated anticipation/payoff and ask to retain stage-specific files for origination, name, line art, color and typesetting. This is a live production/asset-custody comparator, not a universal vertical workflow. Kato Kohei's Jump TOON NEXT interview contrasts spread-level simultaneous information with sequential scrolling and the need to sustain interest panel by panel. Individual design rationale, not eye tracking. No sample artwork or native editor files inspected.

## D. Commercial game adjacency: Gravity Daze 2

Famitsu 2017-01-18 team statements: designer 森田 explicitly owned comic-demo panel layout and animation, describes moving bande dessinée, and invites controller tilt to enjoy depth; lead 堀 separately names movie/comic-demo responsibility. Direct creator testimony to actual game presentation roles and input-dependent perceptual presentation, not implementation details (no parallax algorithm, render pass, complete clip or source code inspected). This case derives from bande dessinée, not proof of Japanese manga influence or CELSYS reuse. Retain Koei Tecmo JP2020069317A as a separate proposed manga-specific transfer (APERTURE-03).

## E. Candidate synthesis: presentation is an authored transformation

A master composition C contains source image supports, panel masks, anchors, layers, reading precedence and editorial intent. A presentation variant V specifies a target aperture, source-to-destination maps, co-visibility groups, reveal schedule, state transitions, input and optional effect events. Distinguish:
- static spread: several panels simultaneously visible (attention order need not equal visibility);
- panel player: discrete order and per-panel crop/motion/effects; selected content may lose compositional neighbors;
- vertical canvas: viewport T(s) translated by reader-controlled scroll s; reveal depends on geometry/scroll, not a fixed time;
- interactive game: viewport and panel visibility depend on time and state/input, potentially distinct from simulation and narrative time.

For target k, require source support coverage under all declared transforms, protected cue legibility, intended order and explicitly preserved/changed co-visibility groups. Record changed framing/layer persistence/text/effects and require author/editor review of editorially significant changes. A crop algorithm does not certify semantic equivalence. A region/event map is a candidate architecture only, not a reconstructed CELSYS file format or mandatory feature list. No new prototype or global aspect ratio. Next: recover an inspectable public source-to-runtime panel sequence or authoring format (e.g. an open format with sample files and player) and separately retain the pending historical layered specimen. Do not disturb G02 aperture, S06, G06 or Suzuki/AM2 cursors.

## Sources (accessed 2026-11-19)

- PN04-S01 R1: CELSYS [2003-12-01 ComicSurfing announcement](https://celsys.com/files/user/pdf/company/press/2003/031202_comicsurfing.pdf), pp.1–3 text, p.2 screenshot workflow visually inspected.
- PN04-S02 R1: CELSYS [2004-07-22 ComicStudioEnterprise 2.0 announcement](https://celsys.com/files/user/pdf/company/press/2004/Celsys_News_2004_07_22_Web.pdf), p.3 text, screenshot cache miss.
- PN04-S03 R1: ITmedia [2007-08-10 localized enterprise authoring tools](https://www.itmedia.co.jp/news/article/0708/10/1070810060/).
- PN04-S04 R1: CELSYS [2015-06-19 BS Reader for Browser](https://prtimes.jp/main/html/rd/p/000000195.000005223.html).
- PN04-S05 R1 company retrospective: JEPA [BookSurfing history, 川上陽介](https://www.jepa.or.jp/jepa/chronicle/26-2/).
- PN04-S06 R1 bounded retrospective interpretation: [Digital manga grammar, 2017-06-23](https://magazine-k.jp/2017/06/23/neo-manga-industry-03/).
- PN04-S07 R1 reported prototype: IPA [マンガワープロ](https://www.ipa.go.jp/archive/files/000006921.pdf), pp.1–3 text; screenshot p.2 cache miss.
- PN04-S08 R1 firsthand production text: [TOPPAN クロレ コミックコンテンツ](https://digital.toppan-colorer.co.jp/column/3850).
- PN04-S09 R1 editor interview: [DNP × Jump TOON](https://www.dnp.co.jp/biz/column/detail/20176071_4969.html).
- PN04-S10 R1 artist interview: [Jump TOON NEXT 加藤航平](https://jumptoon-next.com/portal/articles/53FV0D684KNzpMZ7lpvWsY).
- PN04-S11 R1 firsthand game staff statements: [Famitsu 2017-01-18 Gravity Daze 2](https://www.famitsu.com/news/201701/18125036.html), 森田/堀 entries.

No source PDF, artwork or copyrighted asset redistributed. No software binaries or runtime test.

## Source/runtime follow-up

[G02-PANEL-05](G02-PANEL-05.md) traces ACBF schema/sample XML, pinned Krita export code and a guided reader's polygon-to-bounds conversion, plus EPUB navigation. Static inspection and metadata arithmetic, no runtime or original CELSYS format recovery.
