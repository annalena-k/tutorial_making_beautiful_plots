[← Back to overview](../README.md) · [6. Example plots →](06_example_plots.md)

---

## 5. How plots evolve during paper writing

It was important for me to realize that the final figures in a paper look nothing like the first plots I made during a project. Understanding this helped me not get discouraged early on and allowed me to organize my work so I can find things later.

### Early exploration: many plots, most discarded

At the start of a project, you don't know what the final figures will be. You make many exploratory plots which are different representations of the same data, different aspects to highlight, different hypotheses just to test how they look like. Most of these plots will never appear in the paper.

This is expected and healthy. Each plot teaches you something about the data. I keep some of them in `z_backlog_plots/` because I might need them later, they might spark an idea, or they document a dead end that saves someone (including future me) from repeating it.

### Many versions of the same plot: iteration is the process

For a single figure that ends up in the paper, you will likely make 10–15 different versions before settling on the right visualization. Maybe you start with a scatter plot, try a line plot, realize a histogram communicates the point better, then spend three sessions adjusting the binning, axis range, color scheme, and label positions.
Once you think you are done, a colleague suggests removing a certain category from the plot because it doesn't fit the story and you have to redo the figure from this new perspective. 

It's easy to get frustrated, but these iteration will make your plot better. The `pdf/` folder will accumulate these versions. Keep them. Use suffixes like `_v1`, `_v2` or the date in the filename if you want to track the evolution. Remove old versions when you are certain you don't need them.

### Figures get rearranged

As the paper narrative develops, figures move around. What was Figure 2 becomes Figure 4, and a new Figure 2 is created. Panels get combined or split. A figure that was one plot becomes a two-panel comparison.

The numbered folder names may no longer match the paper figure numbers — that's fine. I recommend, you rename the folder when convenient, but don't waste time on perfect bookkeeping during active writing. The key is that each folder clearly describes what it contains (`02_histogram`, `03_scatter_with_errorbars`) so you can find things by description, not just by number.

### Some plots never make the final paper

Sadly, this happens on every project. A visualization you spent hours on doesn't convey the point clearly enough, or it shows something the paper doesn't need to show, or the paper gets reorganized and the figure no longer fits the narrative. 
If you have space constraints, don't hesitate to move supportive or less relevant results to the Appendix. You can still reference these plots, but you need to distill which message/figure deserves a spotlight in the main text.
If a figure isn't relevant enough for the Appendix, move it to `z_backlog_plots/` and don't feel bad about it, it might help you in the future (e.g. when preparing slides).

The backlog is not a trash folder but a summary of not-important-enough figures. Referees sometimes ask for additional analyses that you already explored and plotted, but didn't deem relevant enough; the backlog lets you find that work quickly.

### Figures in slides

When you give a talk about the paper, you often need different figures. Conference talks need slides-format versions (wider, larger font, possibly fewer panels or none at all). Tutorial talks might need simplified versions showing fewer curves. Sometimes a visualization that works beautifully in a paper (dense information, small font) fails on a slide, and you need to redesign it.

These presentation-specific figures either live alongside the paper figures (with `_slides` or `_talk` suffixes in the `pdf/` folder) or in a separate `presentations/` folder alongside `example_plots/`.

### Referee revisions

Referees will ask for additional analyses, replotted comparisons with new baselines, or modified visualizations. Having the data and code organized in a clean folder structure means these revisions are fast: find the folder, update the data file or adjust the notebook, regenerate. If the figures are in git, you can also compare the before-and-after trivially.

---

[← 4. Why you should make multiple versions](04_multiple_versions.md) · [↑ Back to overview](../README.md) · [6. Example plots →](06_example_plots.md)
