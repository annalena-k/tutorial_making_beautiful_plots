# Making beautiful plots for scientific papers

Disclaimer: I believe that the plots of a paper are like the blurb of a fantasy book. While the title and abstract convince the reader to click on the paper in the first place (like the cover design), the plots will decide whether they actually read, understand, and appreciate the paper.
Plots will either convince the reader of your claim or they will confuse them, cast doubt on your results, and leave them frustrated.

TL;DR: Your plots make or break your paper.

I hope this tutorial contains a few interesting details for everyone to improve their plotting game!
Let me know if you have things to add or if you do things differently.

**Just want Claude to follow these conventions without reading the whole tutorial?** Copy [`CLAUDE.md`](CLAUDE.md) into your project root. Claude Code picks it up automatically and will apply the plotting rules from this tutorial to every figure you make together. If your project already has a `CLAUDE.md`, paste the content in.

> This tutorial is inspired by [Michael Deistler](https://github.com/michaeldeistler)'s figure tutorial [mackelab/figure_tutorial](https://github.com/mackelab/figure_tutorial). I highly recommend checking it out in addition to this one. I wanted to prepare an extended version that covers the full workflow from data preparation to LaTeX integration, explains the reasoning behind each plotting choice more deeply, covers how plots evolve throughout a project, and includes a ready-to-use colorblind-friendly color palette package. The mackelab tutorial additionally explains how to sync your figures via git and how to compose multi-panel figures programmatically (using svgutils); I explain why I decided to do the latter in LaTeX instead.

---

## Contents of this repository

```
tutorial_making_beautiful_plots/
├── README.md                          ← this tutorial
├── CLAUDE.md                          ← drop this in your project to guide Claude Code
├── pyproject.toml                     ← pip install -e .
├── requirements.txt                   ← minimal dependencies (no pinned versions)
├── requirements_pinned.txt            ← exact pinned versions for reproducibility
├── cb_colors/                         ← colorblind-friendly color palettes
│   ├── __init__.py
│   └── palettes.py
├── cb_colors_overview/                ← all palettes visualized in one figure
│   ├── notebooks/plot_color_overview.ipynb
│   └── png/color_overview.png
├── matplotlibrc_ml                    ← style file for ML conferences (NeurIPS/ICML/ICLR)
├── matplotlibrc_physics               ← style file for physics journals (PRL, PRB, A&A)
└── example_plots/
    ├── 01_line_plot/                  ← method comparison over training
    │   ├── data/example_data.json
    │   ├── notebooks/plot_line_comparison.ipynb
    │   └── pdf/
    ├── 02_histogram/                  ← distribution comparison
    │   ├── data/example_data.json
    │   ├── notebooks/plot_histogram.ipynb
    │   └── pdf/
    ├── 03_scatter_with_errorbars/     ← predictions vs. ground truth
    │   ├── data/example_data.yaml
    │   ├── notebooks/plot_scatter.ipynb
    │   ├── pdf/
    │   └── png/
    └── z_backlog_plots/               ← plots that didn't make it into the paper
        └── exploratory_violin/
            ├── data/
            ├── notebooks/
            └── pdf/
```

## Quick start

```bash
git clone https://github.com/annalena-k/tutorial_making_beautiful_plots.git
cd tutorial_making_beautiful_plots

# Create and activate the dedicated plotting environment (see section 2.6 for why)
python3 -m venv venv_plotting
source venv_plotting/bin/activate      # on Windows: venv_plotting\Scripts\activate

# Install all plotting dependencies + the cb_colors package
pip install -e .

# Open a notebook
cd example_plots/01_line_plot/notebooks
jupyter lab
```

Then open `plot_line_comparison.ipynb` and run it. The figure is saved to `../pdf/fig_01.pdf`.

To recreate the exact same environment from the pinned lockfile:
```bash
python3 -m venv venv_plotting
source venv_plotting/bin/activate
pip install -r requirements_pinned.txt
```

---

## Sections

| Section | What you'll learn |
|---|---|
| [1. The philosophy of plotting](docs/01_philosophy.md) | What to ask before plotting; why clutter hurts; how to iterate with collaborators |
| [2. Plan how you plot: the workflow](docs/02_workflow.md) | Summary files, local plotting, version control, folder structure, notebooks, venv |
| [3. The plotting process and its details](docs/03_plotting_details.md) | matplotlibrc, fonts, figure size, colorblind-safe colors, saving, LaTeX integration |
| [4. Why you should make multiple versions](docs/04_multiple_versions.md) | The `VERSION` switch pattern for paper / slides / dark figures |
| [5. How plots evolve during paper writing](docs/05_evolution.md) | Exploration, iteration, rearrangement, backlog, referee revisions |
| [6. The example plots](docs/06_example_plots.md) | Line plot, histogram, scatter with error bars — what each example illustrates |
| [7. Citing papers and colormaps](docs/07_citations.md) | Citation table for every palette in `cb_colors` |
| [8. Further reading & LLM disclaimer](docs/08_further_reading.md) | Links, books, and a note on how this tutorial was made |
