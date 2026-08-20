[← Back to overview](../README.md) · [7. Citing papers →](07_citations.md)

---

## 6. The example plots

The three examples in `example_plots/` are not just toy demos — each was chosen to represent a distinct plot type that comes up in almost every ML or physics paper, and each illustrates a specific set of design challenges.

**01 — Line plot: method comparison over training**  
`01_line_plot/` shows multiple methods plotted against a shared x-axis (e.g. training epochs or time). This is arguably the most common figure type in machine learning papers. The design challenges here are: choosing colors that remain distinguishable at small print sizes, placing the legend without it overlapping the curves, and picking axis ranges that focus attention on the relevant regime rather than on uninformative tails.

**02 — Histogram: distribution comparison**  
`02_histogram/` compares two overlapping distributions. Histograms are deceptively tricky: the bin width dramatically changes what the reader sees, alpha blending must be chosen carefully for overlapping fills, and the legend placement becomes important when both distributions occupy the same region. This example also illustrates how to summarize raw samples into a small JSON file (bin edges + density values) so that re-plotting is instant.

**03 — Scatter plot with error bars: predictions vs. ground truth**  
`03_scatter_with_errorbars/` shows model predictions against ground truth with uncertainty estimates, a reference diagonal, and a separate residual panel below. This represents the "result summary" figure that often carries the main claim of the paper. The key design choices here are: using a reference line that communicates the ideal outcome without dominating the figure, error bars that are visible but not distracting, and matching axis ranges across the two panels.

![Example scatter plot with error bars](../example_plots/03_scatter_with_errorbars/png/fig_03_preview.png)

Each notebook contains a `VERSION` switch at the top (`"paper"` / `"slides"` / `"dark"`) so you can regenerate the same figure in different formats with a single variable change. See [section 4](04_multiple_versions.md) for the rationale.

---

[← 5. How plots evolve during paper writing](05_evolution.md) · [↑ Back to overview](../README.md) · [7. Citing papers →](07_citations.md)
