[← Back to overview](../README.md)

---

## 8. Further reading

- [**mackelab/figure_tutorial**](https://github.com/mackelab/figure_tutorial) — the tutorial that inspired this one; focuses on Python-based figure composition with svgutils, a different and complementary approach
- [**Paul Tol's colorblind-friendly palettes**](https://personal.sron.nl/~pault/data/colourschemes.pdf) — the reference for the `paul_tol_bright` and `paul_tol_muted` palettes in this repo
- [**Okabe & Ito colorblind palette**](https://jfly.uni-koeln.de/color/) — the original paper proposing the `okabe_and_ito` palette
- [**UCSB colorblind-safe schemes reference**](https://www.nceas.ucsb.edu/sites/default/files/2022-06/Colorblind%20Safe%20Color%20Schemes.pdf) — a useful overview of multiple palettes with visual comparisons
- [**Coblis: color blindness simulator**](https://www.color-blindness.com/coblis-color-blindness-simulator/) — paste your figure to see how it looks under different types of color vision deficiency
- [**matplotlib rcParams reference**](https://matplotlib.org/stable/tutorials/introductory/customizing.html) — full documentation for every setting in a matplotlibrc file
- **Tufte, E.R., *The Visual Display of Quantitative Information*** — the classic reference on data visualization design; chapter 4 ("Data-Ink and Graphical Redesign") is especially relevant to the "clutter is the enemy" principle above

---

## 9. LLM usage disclaimer

Claude code was used to iterate the structure of this tutorial, prepare the general examples (including the data), and improve some of the code that I use for plotting my own paper figures.
I gathered the points discussed in the tutorial myself, wrote an initial, incomplete draft, and instructed Claude to clean my writing, shorten it, and add small technical details that I wasn't aware of.
Claude Code was also used to implement the `cb_colors` package and verify the color values against published sources.

Since I have seen messy, uninteresting, and confusing LLM generated plots from students and colleagues, the goal of this tutorial is to give them a reference point for how to design great and beautiful figures.
If you decide to feed this tutorial into your favourite LLM, this is fine with me. I just hope it does improve your figure quality! xD

---

[← 7. Citing papers and colormaps](07_citations.md) · [↑ Back to overview](../README.md)
