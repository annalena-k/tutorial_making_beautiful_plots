[← Back to overview](../README.md) · [4. Multiple versions →](04_multiple_versions.md)

---

## 3. The plotting process and its details

### 3.1 The matplotlibrc file

Matplotlib's default style is fine for quick exploratory plots but not for publication figures. A `matplotlibrc` file lets you configure all visual parameters (fonts, sizes, spines, tick marks, line widths, save settings) once, and have them apply to every plot automatically.

This repository includes two style files:
- **`matplotlibrc_ml`** — for ML conference papers (NeurIPS, ICML, ICLR). Uses Computer Modern fonts without a LaTeX installation. Font size 7.5 pt (matches NeurIPS body text).
- **`matplotlibrc_physics`** — for physics journals (PRL, PRB, MNRAS, A&A). Uses full LaTeX rendering with CMU Serif fonts. Font size 9.0 pt (matches PRL body text).

**How to use it**: At the top of every plotting notebook, before any other matplotlib import, include:

```python
import matplotlib
matplotlib.rc_file("../../matplotlibrc_ml")  # adjust path as needed

import matplotlib.pyplot as plt
import numpy as np
```

**What it configures:**

| Setting | Value (NeurIPS) | Why |
|---|---|---|
| `font.size` | 7.5 pt | Matches paper body text |
| `font.family` | serif | Matches paper font family |
| `font.serif` | Computer Modern | Matches LaTeX default |
| `axes.spines.top/right` | False | Removes decorative spines |
| `axes.grid` | False | Removes clutter |
| `lines.linewidth` | 1.0 | Thin lines look better in print |
| `xtick.major.size` | 2.5 | Smaller ticks for publication |
| `savefig.format` | pdf | Vector output for LaTeX |
| `savefig.bbox` | tight | Removes extra whitespace |
| `legend.frameon` | False | No box around legend |

The overarching goal: your figure should blend seamlessly into the paper text. Same font, same font size, same visual weight. When a reader does not consciously notice the transition from text to figure, that is a success.

### 3.2 Installing the right fonts
**Font vs. rendering:** Font and rendering control how the actual characters in your figure are set on the page. This is a whole field of study in itself (that I will not go into), but they are highly relevant for visual consistency.

**Why fonts matter:** If your figure uses a different font than the paper's body text, it looks like a foreign object pasted into the document which every reviewer notices. Matching the font creates visual coherence that the reader may not consciously be aware of, but they will feel the consistency. Depending on the TeX template provided by the journal/conference you want to submit to, you will need a different font. Common machine learning conferences use `Computer Modern` (see `matplotlibrc_ml`) while physics journals depend on `serif` fonts (see `matplotlibrc_physics`).

**Why TeX rendering might make a difference:** The `matplotlibrc_ml` explicitely sets `text.usetex: False` because it is usually not necessary. However, several greek characters look visually different if they are written in a specific font, or if they rendered with a LaTeX backend. As a result, a greek letter in your text might look differently than the same greek letter in your axis label. To avoid such differences, you can enable TeX within the matplotlibrc file by setting `text.usetex: True` which uses your system's LaTeX installation to render all text, including axis labels, tick labels, and legends. Since this usually matters more for physics papers, `matplotlibrc_physics` uses `text.usetex: True`.

Requirements:
1. A working LaTeX installation — [MacTeX](https://www.tug.org/mactex/) (macOS) or [TeX Live](https://www.tug.org/texlive/) (Linux/Windows)
2. The **CMU Serif** (Computer Modern Unicode) font installed on your system

Installing CMU Serif on macOS:
```bash
brew install --cask font-cm-unicode
```

Or download from: https://cm-unicode.sourceforge.io/

After installing a new font, refresh matplotlib's font cache (run once):
```python
import matplotlib.font_manager
matplotlib.font_manager._load_fontmanager(try_read_cache=False)
```

**Why you might need to change the font for slides and posters:**
Some fonts are designed such that they are optimally readable when printed on paper (`serif`), others are easiest to read on screens (`Computer Modern`). As a result, plots prepared with the journal font can look weird or even ridiculous on slides or posters. For example, bullet points on a slide with `serif` font are very hard to read and the text can look weird. If you want your figures to be consistent with your slides, you might need to make a figure version with your slide font.

```python
matplotlib.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["Helvetica", "Arial"],
})
```

### 3.3 Getting the right figure size

**Why it matters:** If you don't explicitly set the figure size to match the journal column width, the font sizes in your figure will not match the paper. Either the text in the figure will be too large (looks amateurish and wastes space) or too small (unreadable, forces squinting). The only way to guarantee a match is to set the figure width to exactly the column width of your target journal.

**The rule:** Save the figure at the exact width it will be displayed in the paper. Then include it with `\includegraphics[width=\columnwidth]{...}` in LaTeX without rescaling.

**How to find the column width of your target journal:**

1. Look in the journal's LaTeX template or style guide.
2. Add `\printinunitsof{in}\prntlen{\textwidth}` to your `.tex` file (requires the `printlen` package) to print the actual text width at compile time.
3. Look in the journal's `.cls` file for `\setlength{\textwidth}{...}`.
4. Ask Google or your favourite LLM.

**Common values (in inches):**

| Journal / Conference | Single column | Full text width |
|---|---|---|
| NeurIPS (2024)       | 5.5 in        | 5.5 in (single column layout) |
| ICML                 | 3.25 in       | 6.75 in |
| PRL / PRB            | 3.375 in      | 6.75 in |
| MNRAS                | 3.32 in       | 6.97 in |
| A&A                  | 3.54 in       | 7.28 in |

To convert from points to inches: `inches = pt / 72`.

**In code:**
```python
COLWIDTH = 3.375   # PRL single-column width in inches
ASPECT   = 3 / 4  # height / width — modify to reflect your figure design

fig, ax = plt.subplots(figsize=(COLWIDTH, COLWIDTH * ASPECT))
```

For a two-panel figure where each panel is its own PDF:
```python
# Each panel is saved separately at half the text width
TEXTWIDTH = 6.75
fig, ax = plt.subplots(figsize=(TEXTWIDTH / 2 - 0.05, (TEXTWIDTH / 2) * ASPECT))
# The 0.05 in leaves a small gap between panels when assembled in LaTeX
```

**Note on `savefig.bbox: tight`:** This setting (on by default in the matplotlibrc files here) trims excess whitespace around the figure and can subtly change the saved size. For most figures this is fine. If you need pixel-perfect sizing, use `savefig.pad_inches: 0` and consider turning off `bbox: tight` for that specific save call.

### 3.4 Choosing colorblind-friendly colors

**Why it matters:** Approximately 8% of men and 0.5% of women have some form of color vision deficiency ([Okabe & Ito, 2008](https://jfly.uni-koeln.de/color/); [Simunovic, 2010](https://doi.org/10.1038/eye.2009.251)). The most common type (red-green, or deuteranopia) makes red and green appear nearly identical. If your plot distinguishes two lines with red vs. green (the most common color choice in scientific figures), a significant fraction of your readers cannot read it. This is not a minor accessibility concern: If ten people look at your paper, it is highly likely that at least one of them has a color deficiency!
Something similar happens when someone prints your paper in black and white to save printer ink: The lines in the plot might not be distinguishable.

Beyond accessibility, well-chosen colors look better to everyone. Carefully selected palettes have pleasing contrast, visual balance, and purpose. 

**How to choose colors:** Ideally, your color choices are consistent across (sub)plots. For example, if you compare three versions of approaches/methods/models, each one should have a distinct color that you stick with for the whole paper. Of course, this requires careful selection: Ideally, you know all plots that you want to include in the paper. Then you sit down, collect all color combinations you need, and try to find suitable colors for each plot such that everything makes sense together. This process might take quite some time and effort

**What to avoid:** The default matplotlib color cycle is not designed with color blindness in mind. The `jet` colormap is a notorious example of a colormap that should essentially never be used (poor perceptual uniformity, terrible for color-blind readers). Red vs. green is the most common mistake in scientific plots.

**The `cb_colors` package** (included in this repository) provides several research-validated colorblind-safe palettes:

```python
from cb_colors import palettes

# Most widely recommended — 8 colors, tested under all common deficiency types
c = palettes.okabe_and_ito()
# Keys: "black", "orange", "sky_blue", "bluish_green", "yellow",
#        "blue", "vermillion", "reddish_purple"

# Good for multiple categories, clean and vibrant
c = palettes.paul_tol_bright()
# Keys: "blue", "cyan", "green", "yellow", "red", "purple", "grey"

# Softer tones, good for filled areas and overlapping distributions
c = palettes.paul_tol_muted()
# Keys: "indigo", "cyan", "teal", "green", "olive", "sand",
#        "rose", "wine", "purple", "pale_grey"

# 10-color accessible scheme for when 8 colors aren't enough
c = palettes.accessible_colors()

# 8 two-color pairs for paired comparisons (Alexandra Phillips / NCEAS, 2022)
pairs = palettes.nceas_two_color_pairs()
color_a, color_b = pairs["blue_red"]

# Divergent colormaps (9 stops, blue→white→red or purple→white→green)
btr = palettes.nceas_blue_to_red()    # list of 9 hex strings
ptg = palettes.nceas_purple_to_green()
```

All discrete palettes return dicts mapping descriptive names to hex strings:
```python
c = palettes.okabe_and_ito()
print(c["blue"])   # → "#0072b2"
```

**Usage example:**
```python
c = palettes.okabe_and_ito()

ax.plot(x, y_a, color=c["sky_blue"],   label="Method A")
ax.plot(x, y_b, color=c["vermillion"], label="Method B")
```

**Color palette overview** — all palettes included in `cb_colors`:

![Color palette overview](../cb_colors_overview/png/color_overview.png)

**Don't rely on color alone.** Also vary the line style (solid, dashed, dotted) or marker type. This makes the figure readable when printed in grayscale (still common in physics journals) and adds a second visual channel to distinguish groups. See the `02_histogram` and `03_scatter_with_errorbars` notebooks for examples.

**Testing for colorblindness:** Paste your figure into the [Coblis simulator](https://www.color-blindness.com/coblis-color-blindness-simulator/) or use the Python package `daltonize`. If you can still distinguish all elements under deuteranopia simulation, you're in good shape.
Before submitting your paper, print it once in black and white colors to check whether the colors are perceived as you expected.

### 3.5 Saving the figure

```python
fig.savefig("../pdf/fig_01.pdf", transparent=True)
```

**PDF as the preferred format:** Always save as PDF for figures that go into a LaTeX paper. PDF is a vector format: it scales to any resolution without pixelation, and the file size stays small (a few hundred KB for most scientific figures). This makes it easy to commit to git and trivial to include in LaTeX.

**Transparent background** (`transparent=True`): Saves the figure with no background fill. This is important for:
- Dark-themed slides: the figure doesn't have a white box around it
- Figures placed on colored backgrounds in posters or talks
- General cleanliness — the figure background matches whatever it's placed on

**The matplotlibrc files in this repo already set:**
```
savefig.format       : pdf
savefig.bbox         : tight    ← trims whitespace
savefig.dpi          : 500      ← affects rasterized elements (images in figures)
savefig.pad_inches   : 0.1      ← small padding inside the tight boundary
```

So `plt.savefig("../pdf/fig_01.pdf")` will use all these settings automatically. I pass `transparent=True` explicitly because I want it to be visible in the notebook cell, not hidden in the rcParams.

**For PNG (slides, web):** In general, I don't recommend plotting figures as PNG since it is a raster format. However, sometimes you need small figure sizes for slides or the web. To make sure it still renders sufficiently well, you need to set a high DPI:
```python
fig.savefig("../pdf/fig_01_slides.png", dpi=300, transparent=True)
```
300 DPI at the displayed size (e.g. 5 inches wide) gives 1500 px, which is sharp on standard and retina screens.

### 3.6 Integrating figures into LaTeX

Rather than composing multi-panel figures in Python using `svgutils` (as the [mackelab tutorial](https://github.com/mackelab/figure_tutorial) shows), I assemble subfigures entirely in LaTeX. This approach has important advantages:

- **Panels can be updated independently**: if one panel changes, replace one PDF file. The LaTeX layout updates automatically.
- **Pure vector output**: the entire assembled figure — panels, insets, subfigure labels (a), (b) — is rendered as vector graphics by LaTeX's PDF engine.
- **Layout changes are one-line edits**: swapping the order of panels or adjusting spacing is a change to the LaTeX code, not a Python re-run.
- **Overlays in LaTeX coordinate space**: inset figures, legend boxes, and text annotations can be placed precisely on top of another PDF using LaTeX commands, without any Python composition.

**Required preamble:**
```latex
\usepackage{subfig}       % for \subfloat
\usepackage{stackengine}  % for \stackinset (overlaying content on a figure)
```

**Single full-width figure:**
```latex
\begin{figure}[t]
    \centering
    \includegraphics[width=\textwidth]{figures/fig_01.pdf}
    \caption{Caption here.}
    \label{fig:fig1}
\end{figure}
```

**Two-panel figure spanning both columns** (use `figure*` for full text width in two-column journals like PRL):
```latex
\begin{figure*}[t]
    \begin{minipage}[t]{.48\textwidth}
        \subfloat{
            \stackinset{l}{0cm}{t}{0cm}{\textbf{a}}{
                \includegraphics[width=\textwidth]{figures/fig_02a.pdf}
            }
        }
    \end{minipage}
    \hfill
    \begin{minipage}[t]{.48\textwidth}
        \subfloat{
            \stackinset{l}{0cm}{t}{-0.2cm}{\textbf{b}}{
                \includegraphics[width=\textwidth]{figures/fig_02b.pdf}
            }
        }
    \end{minipage}
    \caption{(a) Left panel narrative. (b) Right panel narrative.}
    \label{fig:main}
\end{figure*}
```

The `\stackinset{anchor_h}{offset_h}{anchor_v}{offset_v}{overlay}{base}` command places `overlay` on top of `base` at the specified position. Panel labels (**a**, **b**) are placed this way which means they use the paper's font and are part of the compiled PDF, not baked into the Python figure. This makes it easy to re-arrange subplots without having to regenerate the figure in Python.

**Advanced: overlaying multiple PDFs on one panel.** When a panel contains insets (e.g. a corner plot together with a skymap and a separate legend saved as its own PDF), nest multiple `\stackinset` calls:

```latex
\begin{minipage}[t]{.48\textwidth}
    \subfloat{
        \stackinset{l}{0cm}{t}{0cm}{\textbf{a}}{%        ← panel label
        \stackinset{l}{3cm}{t}{0cm}{Annotation text}{%   ← text overlay
        \stackinset{l}{2.8cm}{t}{0.16cm}{%               ← legend inset
            \includegraphics[width=0.28\textwidth]{figures/fig_03a_legend.pdf}%
        }{%
        \stackinset{l}{4.8cm}{t}{0.2cm}{%                ← skymap inset
            \includegraphics[width=0.4\textwidth]{figures/fig_03a_skymap.pdf}%
        }{%
            \includegraphics[width=\textwidth]{figures/fig_03a_corner.pdf}%  ← base
        }}}}%
    }
\end{minipage}
```

Each `\stackinset` wraps the previous one. The innermost (deepest nesting) is always the base figure; everything else is layered on top. This way a panel that visually shows a corner plot, a skymap inset, a separate legend, a text annotation, and a panel label is still just four independent PDF files where each can be updated on its own.

**Key insight for font size matching:** When you save a figure at exactly `\textwidth` width (or `0.48\textwidth` for a half-width panel) and include it with `\includegraphics[width=\textwidth]{...}` at the same fraction, the LaTeX compiler scales it by a factor of 1. The font size in the figure (e.g. 9 pt) will be exactly 9 pt in the compiled PDF. This only works if you set the figure width in Python to match the journal's column width. See [section 3.3](#33-getting-the-right-figure-size).

---

[← 2. Plan how you plot: the workflow](02_workflow.md) · [↑ Back to overview](../README.md) · [4. Multiple versions →](04_multiple_versions.md)
