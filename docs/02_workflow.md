[← Back to overview](../README.md) · [3. Plotting details →](03_plotting_details.md)

---

## 2. Plan how you plot: the workflow

### 2.1 Summarize your data into small files

Don't plot directly on the cluster from raw model outputs or large simulation results. Instead, extract exactly the numbers you need and save them into small, human-readable summary files.

**Formats:** JSON, YAML, CSV, and plain TXT work well for scalars, lists, and tables. For larger arrays (samples, time series, images), HDF5 is a good choice. The key criterion is: the file should contain only what you actually plot, nothing more.

**Why:**
- Running your data pipeline or simply reading a large file from disk might take several minutes or hours. But a plot tweak (e.g changing the axis range, the color, the label) should take seconds. If plotting code loads the full model output, every tweak forces a long wait which quickly becomes frustrating and takes the fun out of making a beautiful plot.
- Summary files force you to explicitly think about about what you need to save for the plot. This is excellent reflection since it makes you think clearly about what the figure contains and what to compute in advance.
- Small files can be committed to git and therefore version controlled (more on this later).
- You can run all plotting locally, not on the cluster. This enables a fast, interactive iteration cycle (plus you don't block cluster resources).

**What to include in a summary file:** The data you actually plot, plus any metadata needed to reproduce the file. If you return to a project six months later, you should be able to understand what the file contains by reading it.

**Example:** Instead of loading 10 GB of samples to plot a histogram, compute the histogram on the cluster, save the bin edges and density values as a 2 KB JSON file, and plot that locally. The `02_histogram` example in this repo illustrates exactly this pattern.

### 2.2 Don't plot on the cluster

HPC clusters are optimized for computation, not visualization. Plotting there is painful:
- You typically don't have a display, so interactive debugging is impossible/difficult, requires tunneling, or a complicated setup.
- Matplotlib needs a non-interactive backend (Agg), and errors are hard to diagnose.
- The feedback loop is slow: submit job → wait in queue → job runs → download output → discover the axis label was wrong → repeat.
- You need a stable internet connection to access the cluster which means you can't quickly re-do the plot on the (German) train.
- You cannot iterate quickly, which means you settle for "fine" rather than improving the plot until it is "great."
- If the cluster is shut down for maintenance or some files cannot be accessed because a node got fried (This happened to me when I was writing a paper!), you cannot redo the plot because you can't access the data. This can be devastating if you have a submission deadline coming up.

From my experience of previous projects, results are updated very rarely while plots are updated often until all people on the paper are happy with them. I would estimate that in one of my projects, I updated the underlying data for one plot maybe four times, but iterated the plot at least 100 times. It is definitely worth it making these 100 iterations as quick and easy as possible.

Therefore, I can recommend doing all heavy computation on the cluster, extracting summary files, copying them to your local machine (or a shared folder), and doing all plotting there. A fast feedback loop where you see results immediately when you change something, is what makes iterative refinement of figures fun.

### 2.3 Version control data, code, and figures
Paper submissions are always stressful and it can leave you in shock when important things unexpectedly fail (which they will because of Murphy's law... sorry).
For example, the cluster could be down for maintenance, you accidentally deleted a notebook which contained plotting code you have already spent days on, or you tried to improve the figure, but now it looks worse and you already deleted the code. 
All these things are likely to happen and they can set you back significantly. This is the reason why I version control my plotting code and I want to recommend you the following:

Your plotting repository should be a git repository containing:
- The summary data files
- The plotting notebooks
- The output figures (PDFs)

**Yes, commit the PDFs.** PDF files are small (vector graphics, typically a few hundred KB), and having them in git means:
- You can always return to a previous version of any figure, without having to re-run the notebook.
- Collaborators can see the current state of all figures without running any code.
- When a referee asks "What was Figure 3 in the original submission?", you can answer immediately.

If your project has many or large binary files, you might not be properly constructing your summary files and it could be helpful to go back to [section 2.1](#21-summarize-your-data-into-small-files). If you really need these large files, consider git LFS. For typical PDF figures, regular git is fine.

**Tipp:** The plotting data (summary files), plotting code (notebooks), and figures (PDFs) should all be committed together. If you change the notebook and regenerate a figure, commit the new PDF at the same time. This keeps the repository consistent.

### 2.4 Folder structure

Each figure (or closely related group of figures) gets its own folder with the same internal structure:

```
{number}_{descriptive_name}/
├── data/           # summary data files — what goes into the figure
├── notebooks/      # one or more plotting notebooks
└── pdf/            # output PDFs — commit these to git
```

Number the top-level folders to match the figure numbers in the paper: `01_`, `02_`, etc. This makes it immediately clear where each paper figure comes from. For figures with labeled sub-panels (3a, 3b), use the subfolder naming `03a_`, `03b_`.

A `z_backlog_plots/` folder at the end (the `z_` prefix makes it sort last) should contain plots that didn't make it into the paper. It's always a good idea to just move a plotting folder into the backlog when it is deemed not important enough, but I would never delete them — see [section 5](05_evolution.md) for details.

### 2.5 Why I plot in notebooks

Jupyter notebooks are excellent for iterative figure making:
- The figure appears inline, immediately below the code that generated it. You can see the result of every change without leaving the editing environment.
- You can run individual cells without re-running everything. Tweak the color in one cell, re-run just that cell.
- The notebook serves as living documentation: you can add markdown cells explaining what you tried, why a particular choice was made, or what a failed approach looked like.
- Multiple versions of a cell (commented out) let you preserve the history of your decisions.

I recommend only using one notebook per figure (or per closely related group of figures) because this keeps everything clear and simple. You only load the essential data files and make the one essential plot.
At the beginning, I thought that this is would generate a lot of notebooks with little content, but I was surprised how long the notebooks got over time (different versions of the same plot, cross-checks, small tweaks, ...). The notebook lives in `notebooks/` inside the figure folder and saves its output to `pdf/`.

> **Note on LLM tools:** Coding assistants like Claude are changing how quickly one can iterate on figures since you can describe what you want, get working code immediately, and refine from there. In the future, this might shift the workflow toward plain Python scripts over notebooks. For now, the interactive notebook workflow remains excellent for the exploratory, visual work of making figures which allows manual editing when needed.

### 2.6 Use a dedicated virtual environment

**Use a separate Python virtual environment for plotting and version-control the pinned package list.**

This sounds like extra overhead, and early in a project it feels that way. But it matters since it can take quite some time from first plots to published paper.

**Why:** Plotting libraries (like `matplotlib`, `numpy`, `seaborn`) release new versions that change default behaviors, color cycles, layout algorithms, and font rendering. A figure you made in `matplotlib==3.7` can look noticeably different when re-run in `matplotlib==3.9`: tick spacing shifts, default colors change, font metrics differ slightly. If you have a single shared Python environment that you update constantly, your plots will silently drift. By the time you submit the reviewed version of the paper, the figures in the PDF may not match what you had included in your initial submission (This could be >6 months later!).

**The solution:** Create a dedicated venv for plotting, install everything once, and freeze the exact versions:

```bash
python3 -m venv venv_plotting
source venv_plotting/bin/activate
pip install -e .                          # installs dependencies from pyproject.toml
pip freeze > requirements_pinned.txt      # pin all exact versions
```

Commit `requirements_pinned.txt` to git. Do **not** commit `venv_plotting/` itself (it's in `.gitignore`). Anyone who clones the repo and wants to reproduce exactly what you saw can run:

```bash
python3 -m venv venv_plotting
source venv_plotting/bin/activate
pip install -r requirements_pinned.txt
```

**When to update:** When you want a new package version, update explicitly, re-test your figures, and commit the new `requirements_pinned.txt`. That way the update is a deliberate, documented change and not a silent drift.

**In JupyterLab:** Select the venv as the kernel by name (`venv_plotting`). If it doesn't appear, you can register it via:
```bash
source venv_plotting/bin/activate
pip install ipykernel
python -m ipykernel install --user --name venv_plotting --display-name "venv_plotting"
```

---

[← 1. The philosophy of plotting](01_philosophy.md) · [↑ Back to overview](../README.md) · [3. Plotting details →](03_plotting_details.md)
