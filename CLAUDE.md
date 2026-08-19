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

If `cb_colors` is not available, use these hex values for Okabe & Ito:
`#000000`, `#E69F00`, `#56B4E9`, `#009E73`, `#F0E442`, `#0072B2`, `#D55E00`, `#CC79A7`

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

Key settings to always configure in the style file or via `rcParams.update`:
- `axes.spines.top: False` and `axes.spines.right: False`
- `axes.grid: False`
- `legend.frameon: False`
- `font.size` matching journal body text (7.5 pt for NeurIPS, 9 pt for PRL)
- `savefig.format: pdf` and `savefig.bbox: tight`

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
