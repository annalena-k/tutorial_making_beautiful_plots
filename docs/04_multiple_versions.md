[← Back to overview](../README.md) · [5. How plots evolve →](05_evolution.md)

---

## 4. Why you should make multiple versions of a figure

A single figure typically needs to exist in several versions:
- **Paper version**: exact journal column width, small font, PDF
- **Slides version**: wider and taller, larger font (readable from the back of a room)
- **Dark background version**: for dark-themed presentations (requires white labels, ticks, spines, and legend)
- **Different journal format**: different column width and font size if you submit elsewhere

I manage this with a `VERSION` variable at the top of each notebook:

```python
VERSION = "paper"   # "paper" | "slides" | "dark"

if VERSION == "paper":
    FIGWIDTH    = 3.375   # PRL column width
    FONT_SIZE   = 9.0
    SUFFIX      = ""
    TRANSPARENT = True
elif VERSION == "slides":
    FIGWIDTH    = 5.0
    FONT_SIZE   = 14.0
    SUFFIX      = "_slides"
    TRANSPARENT = False
elif VERSION == "dark":
    FIGWIDTH    = 5.0
    FONT_SIZE   = 14.0
    SUFFIX      = "_dark"
    TRANSPARENT = True

matplotlib.rcParams.update({"font.size": FONT_SIZE})
```

Changing `VERSION` and re-running the notebook regenerates the figure for a different target. All versions live in `pdf/` with distinguishing suffixes:
```
pdf/
├── fig_01.pdf               ← paper version (no suffix = canonical)
├── fig_01_slides.pdf        ← slides version
└── fig_01_dark.pdf          ← dark background for talks
```

For the dark version, text and spine colors also need to change:
```python
if VERSION == "dark":
    BG = "#1c1c2e"
    FG = "white"
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(BG)
    ax.tick_params(colors=FG)
    ax.xaxis.label.set_color(FG)
    ax.yaxis.label.set_color(FG)
    for spine in ax.spines.values():
        spine.set_edgecolor(FG)
    # Update legend text color if needed:
    for text in ax.get_legend().get_texts():
        text.set_color(FG)
```

---

[← 3. The plotting process and its details](03_plotting_details.md) · [↑ Back to overview](../README.md) · [5. How plots evolve →](05_evolution.md)
