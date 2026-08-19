# Scientific Plotting Guide for Claude

> Distilled from [annalena-k/tutorial_making_beautiful_plots](https://github.com/annalena-k/tutorial_making_beautiful_plots) — a full tutorial covering the plotting workflow from data preparation to LaTeX integration, with a ready-to-use colorblind-friendly color palette package.

This file configures Claude's behavior when helping with scientific figure making. Follow these rules in every plotting task unless the user explicitly overrides one.

---

## Core principle

Every figure makes exactly one point. Before writing any code, identify what that point is. If you cannot state it in one sentence, ask the user before proceeding.

Remove every element that does not directly support that point. No grid lines unless axes are insufficient. No top or right spines. No redundant legend entries. No abbreviations that need caption explanations.

---

## Colors and accessibility

**Never use the default matplotlib color cycle.** Never use the `jet` colormap.

Always use a colorblind-safe palette. In order of preference:

| Use case | Palette |
|---|---|
| Default (up to 8 categories) | `okabe_and_ito()` |
| Vivid/high-contrast (up to 7) | `paul_tol_bright()` |
| Soft tones, filled areas (up to 10) | `paul_tol_muted()` |
| Paired comparisons | `nceas_two_color_pairs()` |
| Divergent data | `nceas_blue_to_red()` or `nceas_purple_to_green()` |
| 5 high-contrast colors | `ibm_design_library()` |

If the `cb_colors` package is available in the project, use it:

```python
from cb_colors import palettes
c = palettes.okabe_and_ito()
# Keys: "black", "orange", "sky_blue", "bluish_green", "yellow",
#       "blue", "vermillion", "reddish_purple"
```

If `cb_colors` is not available, paste these dicts directly into your notebook:

```python
OKABE_AND_ITO = {
    "black":          "#000000",
    "orange":         "#E69F00",
    "sky_blue":       "#56B4E9",
    "bluish_green":   "#009E73",
    "yellow":         "#F0E442",
    "blue":           "#0072B2",
    "vermillion":     "#D55E00",
    "reddish_purple": "#CC79A7",
}  # Okabe & Ito (2008) https://jfly.uni-koeln.de/color/

PAUL_TOL_BRIGHT = {
    "blue":   "#4477AA",
    "cyan":   "#66CCEE",
    "green":  "#228833",
    "yellow": "#CCBB44",
    "red":    "#EE6677",
    "purple": "#AA3377",
    "grey":   "#BBBBBB",
}  # Tol (2021) https://personal.sron.nl/~pault/

PAUL_TOL_MUTED = {
    "indigo":    "#332288",
    "cyan":      "#88CCEE",
    "teal":      "#44AA99",
    "green":     "#117733",
    "olive":     "#999933",
    "sand":      "#DDCC77",
    "rose":      "#CC6677",
    "wine":      "#882255",
    "purple":    "#AA4499",
    "pale_grey": "#DDDDDD",
}  # Tol (2021) https://personal.sron.nl/~pault/

IBM_DESIGN_LIBRARY = {
    "blue":    "#648FFF",
    "purple":  "#785EF0",
    "magenta": "#DC267F",
    "orange":  "#FE6100",
    "gold":    "#FFB000",
}  # IBM Design Language https://www.ibm.com/design/language/color/

ACCESSIBLE_COLORS = {
    "blue":        "#3F90DA",
    "orange":      "#FFA90E",
    "purple":      "#832DB6",
    "red":         "#BD1F01",
    "gray":        "#94A4A2",
    "dark_orange": "#E76300",
    "light_blue":  "#92DADD",
    "dark_gray":   "#717581",
    "tan":         "#B9AC70",
    "brown":       "#A96B59",
}  # Petroff (2021) https://arxiv.org/abs/2107.02270

NCEAS_TWO_COLOR_PAIRS = {
    "yellow_blue":   ["#FDB338", "#025196"],
    "tan_turquoise": ["#E3BE6B", "#3DB1A6"],
    "orange_purple": ["#EB6123", "#512888"],
    "green_purple":  ["#295E11", "#58094F"],
    "blue_red":      ["#2F67B1", "#BF2C23"],
    "blue_pink":     ["#10559A", "#DB4C77"],
    "yellow_pink":   ["#F4B301", "#DB1048"],
    "brown_blue":    ["#6A4A3C", "#0F65A1"],
}  # Phillips / NCEAS (2022), pixel-verified

NCEAS_BLUE_TO_RED = [
    "#1065AB", "#3A93C3", "#8EC4DE", "#D1E5F0", "#F9F0F9",
    "#FEDBC7", "#F6A482", "#D75F4C", "#B31529",
]  # Phillips / NCEAS (2022)

NCEAS_PURPLE_TO_GREEN = [
    "#742881", "#986EAC", "#C3A4CF", "#E5D4E8", "#F9F0F9",
    "#D9F1D5", "#ADD4A0", "#5CAE63", "#1B7939",
]  # Phillips / NCEAS (2022)
```

**Always use line style as a second visual channel** (solid, dashed, dotted) alongside color. This makes figures readable in greyscale and by colorblind readers.

---

## Figure size

Set the figure width to match the exact column width of the target journal. Include it in LaTeX without rescaling (`\includegraphics[width=\columnwidth]{...}`). This is the only way to guarantee font sizes match.

| Journal / Conference | Single column | Full text width |
|---|---|---|
| NeurIPS | 5.5 in | 5.5 in |
| ICML | 3.25 in | 6.75 in |
| PRL / PRB | 3.375 in | 6.75 in |
| MNRAS | 3.32 in | 6.97 in |
| A&A | 3.54 in | 7.28 in |

```python
COLWIDTH = 3.375   # PRL single column, in inches
ASPECT   = 3 / 4  # height / width
fig, ax = plt.subplots(figsize=(COLWIDTH, COLWIDTH * ASPECT))
```

---

## Style file

Load a `matplotlibrc` file at the top of every notebook, before any other matplotlib import:

```python
import matplotlib
matplotlib.rc_file("../../matplotlibrc_ml")   # adjust path as needed
import matplotlib.pyplot as plt
```

If no `matplotlibrc_ml` exists in the project, create one at the project root with exactly this content (tuned for ML conference papers; adjust `font.size` for other venues):

```
# matplotlibrc_ml — ML conference style (NeurIPS/ICML/ICLR)
# font.size 7.5 matches NeurIPS body text; set to 9.0 for PRL/PRB

text.usetex          : False
mathtext.default     : regular

font.family          : serif
font.serif           : Computer Modern, DejaVu Serif
font.sans-serif      : DejaVu Sans
font.cursive         : DejaVu Sans
font.size            : 7.5
figure.titlesize     : 7.5
legend.fontsize      : 7.5
axes.titlesize       : 7.5
axes.labelsize       : 7.5
xtick.labelsize      : 7.5
ytick.labelsize      : 7.5

image.interpolation   : nearest
image.resample        : False
image.composite_image : True

axes.spines.left     : True
axes.spines.bottom   : True
axes.spines.top      : False
axes.spines.right    : False
axes.grid            : False

axes.linewidth       : 1.0
xtick.major.width    : 1.0
xtick.minor.width    : 1.0
ytick.major.width    : 1.0
ytick.minor.width    : 1.0

xtick.major.size     : 2.5
xtick.minor.size     : 1.5
ytick.major.size     : 2.5
ytick.minor.size     : 1.5
xtick.major.pad      : 2.5
ytick.major.pad      : 2.5

lines.linewidth      : 1.0
lines.markersize     : 3

savefig.dpi          : 500
savefig.format       : pdf
savefig.bbox         : tight
savefig.pad_inches   : 0.1

svg.image_inline     : True
svg.fonttype         : none

legend.frameon       : False
```

---

## Fonts

Match the figure font to the paper font. Set `font.family: serif` and `font.serif: Computer Modern` for most ML venues. For physics journals with LaTeX rendering, set `text.usetex: True` and use CMU Serif.

Do not mix font families between figure and surrounding text. A figure that uses a different font than the paper body text reads as a foreign object.

---

## Saving figures

Save as **PDF** for any figure going into a LaTeX paper (vector, small file, git-friendly):

```python
fig.savefig("../pdf/fig_01.pdf", transparent=True)
```

Save as **PNG at 300 DPI** for slides and web:

```python
fig.savefig("../pdf/fig_01_slides.png", dpi=300, transparent=True)
```

Commit the PDFs to git alongside the code and data.

---

## Multiple versions

Every notebook should have a `VERSION` switch near the top:

```python
VERSION = "paper"   # "paper" | "slides" | "dark"

if VERSION == "paper":
    FIGWIDTH = 3.375; FONT_SIZE = 9.0; SUFFIX = ""; TRANSPARENT = True
elif VERSION == "slides":
    FIGWIDTH = 5.0;   FONT_SIZE = 14.0; SUFFIX = "_slides"; TRANSPARENT = False
elif VERSION == "dark":
    FIGWIDTH = 5.0;   FONT_SIZE = 14.0; SUFFIX = "_dark"; TRANSPARENT = True

import matplotlib
matplotlib.rcParams.update({"font.size": FONT_SIZE})
```

---

## Folder structure

Each figure (or closely related group) gets its own folder:

```
{number}_{descriptive_name}/
├── data/       # small summary files — only what goes into the figure
├── notebooks/  # one notebook per figure
└── pdf/        # output PDFs — committed to git
```

Number folders to match paper figure numbers (`01_`, `02_`). Move unused figures to `z_backlog_plots/` rather than deleting them.

**Do not plot from raw model outputs or large simulation files.** Extract exactly what you need into a small JSON, YAML, CSV, or HDF5 summary file first. Plotting should take seconds, not minutes.

---

## Data files

- JSON or YAML for scalars, short lists, and tables
- CSV for tabular data
- HDF5 for arrays, samples, and time series
- Each summary file contains only what is actually plotted, nothing more
- Include enough metadata to understand the file six months later without re-running the pipeline

---

## LaTeX integration

Assemble multi-panel figures in LaTeX using `subfig` + `stackengine`, not in Python. Save each panel as a separate PDF and combine them with `\subfloat` + `\stackinset`. This keeps panels independently updatable.

```latex
\usepackage{subfig}
\usepackage{stackengine}
```

Panel labels (**a**, **b**) are placed via `\stackinset` so they use the paper's font and are part of the compiled PDF.

---

## What to avoid

- Default matplotlib colors (`C0`, `C1`, ...)
- The `jet` colormap
- Red vs. green as the primary distinction between two groups
- Grid lines unless the axes alone are insufficient for reading values
- Top and right spines
- Legends inside the data area when they overlap content
- Font sizes that don't match the surrounding paper text
- Plotting directly from large raw data files
- Legends that repeat what the axis labels already say
- More than one key message per figure
