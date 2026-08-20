[← Back to overview](../README.md) · [2. The workflow →](02_workflow.md)

---

## 1. The philosophy of plotting

Before touching any code, it's worth thinking hard about why and what you're plotting. A figure in a scientific paper is not just data, it is an argument designed to convince the reader of your story. The most technically correct plot can fail as a figure if it doesn't communicate effectively what you want to say.

### What to ask yourself before plotting

**What is the one message I want this plot to convey?**
Every good figure makes exactly one point which should be obvious to the reader just from looking at your plot. Choosing 
1.  the message you want to get across, and 
2. the plot design that supports your claim 
are incredibly important, but oftentimes people "just start plotting".  

Especially since LLM tools can quickly generating myriads of different plots for you, it is essential that you know what you actually want to see and why. 
There are different strategies to get there: Some people might let their favourite LLM generate five different plots and pick the best for their message; I however need to sit down with pen and paper and sketch the figure myself while thinking through its design (Type of plot? Axes? Legend? Different colors or separate subplots? ...).

**Does this plot actually support my claim?**
Once you have an initial figure draft, it is easy to believe that the plot shows what you think it shows. Before finalizing a figure, ask a collaborator how they interpret the plot. Let them think on their own and don't provide explanations. The figure needs to stand on its own. If they read a different message than you intended, or if they need explanations from you to get it, the figure doesn't work.
In this case, zou need to go back to the drawing board and start from scratch, but I'm sure your colleague has ideas for you!

**Would I need a lot of explanation to make the reader understand?**
If yes, that's a sign the plot is too complex, the visual encoding is unclear, or the wrong type of chart was chosen. The best figures are largely self-contained: axes are clearly labeled with units, the legend is unambiguous, and the visual hierarchy guides the eye without narration.
If you find yourself with a plot that needs half a paragraph of caption before the reader can understand it, the plot isn't working. The best figures communicate their main message within seconds and also don't contain too much information. If you have multiple messages, consider whether they belong in separate panels, separate figures, or whether these messages are important at all for your storyline.

**Does careful presentation make the reader trust my results more?**
Yes. Sloppy plots (misaligned axes, clashing colors, unreadable font sizes, too many elements crammed in) make readers skeptical, even if the underlying science is correct. Beautiful, carefully made figures signal that the work behind them was equally careful. If you say "Why should I spend time making the figure beautiful, as long as it conveys the result, that's fine.", I can assure you that people enjoy looking at your figure more and for longer if it is pleasing to the eye. For example, I never use the standard matplotlib colors. Everyone knows them, sees them every day, and is simply bored by them. Intentionally choosing colors (which can be a time-consuming process) has always been worth it and I have received compliments for such choices. Making your figure beautiful also tells the reviewer: "This is not a preliminary result, but something ready for publication. I have so much faith into this result that I invested a significant amount of time into presenting it nicely. This is why you also should take it seriously and eventually trust the result."
Presentation is not superficial: it directly affects how your results are received.

### Clutter is the enemy
A common issue I have with peliminary (often LLM made) plots is that they contain each and every pieace of information, resulting in a lot of unnecessary clutter.
I believe that every element on a plot must earn its place. You can ask yourself: "What can I remove without losing information?" and remove it. This will make your plot cleaner, less confusing, and sharpen the message you want to convey.

Examples: 
- Grid lines often don't help the reader since the axes contain the same information. 
- Top and right spines are usually for decoration and are irrelevant, but add another line to the plot that the reader's brain must process. I always remove them (the matplotlibrc files in this repo do this by default). 
- Basically everything that competes for the reader's attention: Unnecessary tick marks that clutter the axes, the same legend in every subplot, overly detailed axis labels that are confusing, ...
  
All these things force the reader to spend their brain power on processing the details of the plot itself, instead of focussing on the message that you want to convey.

### Every choice matters

**Chart type**: "How do I want to show the data?" A line plot implies continuity. A bar chart implies discrete categories. A scatter plot suggests a relationship between two variables. Choosing the wrong type sends the wrong signal, even before the reader looks at the data.

**Axis ranges**: "What ranges make sense for my data?" Not only the maximal and minimal value matter, but also the scale: linear, log10, or ln can help to emphasize the feature you want to show. Think about what your reader needs to see.

**Labels and units**: Axis labels must include units where applicable and should be chosen to reflect the standard in the community of the target audience. Legend labels should be concise but unambiguous. Ideally, you can avoid abbreviations that require an explanation in the caption.

**Reference lines and guides**: A diagonal dashed line in a scatter plot comparing predictions to ground truth immediately tells the reader "perfect prediction lies on this line." Such guides can replace a sentence of caption. Use them when they help, but don't add lines without a reason.

**Colors and line styles**: See [section 3.4](03_plotting_details.md#34-choosing-colorblind-friendly-colors). Color is one of the most powerful visual channels in scientific figures. Different line styles not only help color-blind people, but they are also important when someone prints your paper in black and white.

### Iterate with collaborators

After making a plot, show it to at least one other person before including it in the paper. 
Ask:
- "What does this plot tell you?" (don't explain it first)
- "What's confusing?"
- "How could the plot be improved?"

You'll often find that colleagues immediately notice things you've stopped seeing because you've been staring at the figure for hours. They might read a subtly different message than you intended. This feedback is invaluable and much cheaper to act on before submission than after. Ask your supervisor, a labmate, or a friend who knows the field. The goal is to get ideas for improvement.

---

[↑ Back to overview](../README.md) · [2. The workflow →](02_workflow.md)
