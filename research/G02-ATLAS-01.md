# G02-A02 — Comparative dimensional atlas, initial records

2026-11-18. Partial. Evidence types are kept separate: reported settings, derived nominal quantities, directly counted text masks, qualitative reference inspections, and unverified screenshot targets. No screenshot-derived exact character dimensions or universal sprite regime are claimed.

## A. Reported production settings

| Record | Native source | Intermediate | Logical representation | Caveat |
|---|---|---|---|---|
| DIM001 Guilty Gear (SRC032; prior A01) | reported 64x121 character | unspecified | reported 320x240 display | nominal ratio 121/240=50.42%, not measured body occupancy |
| DIM002 Guilty Gear X (SRC032; prior A01) | reported 136x288 character | unspecified | reported 640x480 display | nominal ratio 60%, not measured body occupancy |
| DIM003 Maskedo (SRC035/SRC044) | 128 px approx. 2m upright, 16 px per 25cm grid, eight heads | none specified | MUGEN compatibility visually compared with KOF | approximate 64 px/m; 16 palette entries including transparency; not SNK standard |
| DIM004 Atelier Eclair (SRC046, Jan 18/29 2019) | 50x50 cell | 100x100 export | initial 150x150, revised 140x140 nominal cell at 1920x1080 project | derived 13.89%→12.96% cell height/project height; visible bounds unknown, not capture occupancy |
| DIM005 Atelier Eclair (SRC046, Jan 20/30) | 960x600 raster background | 1920x1200 export | no node scaling; 200x200 nonpixel explosion frames | moving background and effects may differ in sampling and representation; no appearance or frame timing measurement |
| DIM006 Yazioh (SRC049) | 16x16 one visible color + blank | 256x192 atlas | target viewport not stated | native dimension known; no screen occupancy inferred |

## B. Direct matrix counts (DIM006)

The source prints native rows for individual ship patterns; three triangular-series masks A1/B1/C1 were transcribed for ephemeral analysis, with each row verified length 16 and 16 rows total. Counted F characters as occupied, periods as blank; computed inclusive-minimum/exclusive-maximum bounds, using top-left (0,0). No source image or matrices copied into repo. Reproduce by following the source and repeating these counts. This is a direct measurement of public text masks, not of commercial assets or screen pixels.

| Pattern | Native cell | Visible bounding box (x0,y0,x1,y1) | Occupied pixels | Coverage |
|---|---|---|---:|---:|
| A1 | 16x16 | (0,0,16,16) | 106 | 41.40625% |
| B1 | 16x16 | (0,0,16,16) | 100 | 39.0625% |
| C1 | 16x16 | (0,0,16,16) | 108 | 42.1875% |

Same cell, same bounds, different silhouettes and filled areas. These three are intentionally small and related examples, not a representative estimate of STG design. Occupied-area coverage is not subjective readability or collision area.

## C. Fit derivations (SRC047/SRC048)

Use k=floor(min(W/w,H/h)), where W,H denote output dimensions, w,h logical viewport; valid only when k>=1. Centering needs residual margins allocated explicitly. Displayed area = k*w by k*h; ratio k*k*w*h/(W*H). Compare landscape monitor outputs without rotation; these are derived, not hardware mandates.

| Viewport | 1280x720 | 1920x1080 |
|---|---|---|
| 240x320 | 2x, 480x640 | 3x, 720x960 |
| 240x360 | 2x, 480x720 | 3x, 720x1080 |
| 320x240 | 3x, 960x720 | 4x, 1280x960 |
| 640x360 | 2x, 1280x720 | 3x, 1920x1080 |
| 640x480 | 1x, 640x480 | 2x, 1280x960 |

Aspect is only one of several design variables. UI can occupy unused screen space without reducing the logical game viewport; if reserved within it, reassess actor occupancy. The 240x360 playfield is numerically economical for full-height integer scaling at these two outputs, not proof of preferred gameplay or visual quality.

## D. Commercial capture acquisition record

- REF001 [Gunvolt 3 official system page](https://gunvolt.com/en/GV3/system/) and [Fetters Gauge panel](https://gunvolt.com/en/GV3/system/img/system01/system01Box01.jpg): image opened, embedded screenshot shows Gunvolt standing inside an energy ring and HUD; marketing composite with border and unknown resize/version. Qualitative small actor/large effect relationship only; reject as native asset or exact pixel measurement. Kirin neutral capture still required.
- REF002 [KOF XIII Global Match official system](https://www.snk-corp.co.jp/us/games/kof13gm/system/): battle00.jpg and battle01.jpg requests failed; page also labels images work in progress. No measurement.
- REF003 [Ikaruga GameCube capture index](https://gamesdb.launchbox-app.com/games/details/5977-ikaruga): gameplay media listed 640x480; image request cache miss. No verified world viewport, pose or ship bounds.
- A01 Guilty Gear X and Melty Blood/Under Night comparative capture candidates still pending. A source page, thumbnail, promotional composite or game's nominal resolution is not evidence of a particular actor's native drawing dimensions.

Next: use identifiable uncropped gameplay captures (own or public permitted access), record exact release/platform/pose and visual boundaries. Keep original commercial capture files out of public repository absent rights. Measurement can proceed on lawful local user-provided captures if public links continue to fail. In parallel test an original source-to-export-to-display lab with consistent silhouettes and multiple integer scale ratios; do not block tooling experiments on capture availability. No new standard adopted.
