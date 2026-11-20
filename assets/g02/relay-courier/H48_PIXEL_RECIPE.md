# Relay Courier h48 — registered pixel-edit recipe (nonexecuting ledger)

**2026-11-19**. Companion to [G02-SPECIMEN-02](../../../research/G02-SPECIMEN-02.md). This is sufficient to audit artistic decisions and coordinate conventions, but the complete tested executable and images reside in the named downloadable ZIP (SHA-256 `fb7401b4f60a7fc635212a9519b54ad3d30248e0f155de62e588670818e6d163`). Do not represent this file as an independent renderer or an already compiled Unity scene.

- Input: all four `relay_courier_{neutral,stride,attack,recoil}_h48.png` and the neutral lens revision, generated from five original 256×320 layered SVGs by `build.py`.
- Native output: RGBA 192×192, top-left coordinate, authored pivot (96,174). Zero change to pixel support; new colors only where source alpha≥128.
- Reduction B: each source RGBA alpha≥128 pixel gets opaque palette color with minimum **unweighted squared Euclidean RGB difference**; other source pixels transparent.
- Palette keys: `ink #182237`, `shadow #305069`, `dark #26394F`, `suit #317987`, `highlight #69B5AE`, `face #F0D4AC`, `face_shadow #CCAD8E`, `amber #E9A74D`, `lens #A8E7EA`, `rose #BD6279`, `cream #F5ECD9`.
- Color-guard C: render only original named `face-mark` and `relay-lens` layers at **source scale 48/258.5** and registered translation, threshold their alpha≥128. If an automatically assigned `rose` pixel is not within `face-mark`, and not within `relay-lens` for a lens-color revision, replace it with the nearest color from the remaining ten keys, evaluated against the **original pixel's RGB**. This avoids mistaking antialiased ear/clothing pixels for the intentional cheek stripe. Then apply literal 1px edits below. Note an artistic pink stripe may deliberately extend beyond its original isolated mask: those exceptions are explicit native-pixel edits.
- Literal paint operation syntax: `group, x, y, color-key` (32 candidate ops per pose; existing matching values do not increase changed-pixel count). The crest/face rows receive a pose-specific `(dx,dy)`: neutral (0,0), stride (0,-1), attack (0,0), recoil (2,1). Relay and body positions are unshifted. Skip requested pixels outside original alpha≥128; keep a log. In the lens revision, replace `lens` paint key by `rose` for **relay group only**.

**Crest and face (apply the offsets):**
```csv
group,x,y,color
crest,93,130,ink
crest,94,129,highlight
crest,95,130,highlight
crest,96,130,highlight
crest,97,129,highlight
crest,98,130,ink
face,93,135,face
face,94,136,ink
face,95,136,face_shadow
face,97,135,face
face,98,136,ink
face,97,138,face
face,98,138,rose
face,99,138,rose
face,99,139,rose
face,97,139,face_shadow
```

**Left relay (no offsets):**
```csv
group,x,y,color
relay,88,143,amber
relay,89,143,amber
relay,89,144,lens
relay,90,144,lens
relay,89,145,lens
relay,90,145,lens
relay,88,146,amber
relay,91,146,amber
```

**Suit/belt (no offsets):**
```csv
group,x,y,color
suit,94,148,highlight
suit,94,149,highlight
suit,95,150,suit
suit,98,154,shadow
suit,96,156,suit
suit,99,157,shadow
belt,95,160,dark
belt,98,160,ink
```

**Measurement:** alpha≥128 bounds unchanged for all four poses; 38/44/45/40 total RGBA pixel changes between automatic B and authored C for neutral/stride/attack/recoil respectively. These totals are not sums of guard+paint counts because the same native pixel can be changed twice. Five native source artifacts retain their original ground registration. A separate original lens change propagates to seven C pixels in neutral. Test environment Python, Pillow 12.3.0, CairoSVG 2.8.2. No source-local evaluator, independent observer result, animation, game import or art commission claimed.

Full packaging/measurement details: [G02-SPECIMEN-02](../../../research/G02-SPECIMEN-02.md). The original neutral SVG is already [in this directory](relay_courier_neutral.svg). The other four SVGs, executable generator and exported PNGs remain conversation-attachment custody pending full repo import.
