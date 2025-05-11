# Exercise 0

## Task 2. Theory questions

---

**a) When can you make line charts and when can't you make line charts?**

### Use line charts when:

- Data is continuous and has a logical order (usually over time).

  - Example: stock prices over a month, temperature changes during a day.

- You're showing trends or patterns over time.

  - Example: website traffic each day for a week.

- You want to compare multiple series of continuous data.

  - Example: comparing sales of two products over 12 months.

- Your x-axis represents something measurable or sequential, like:

  - Time (days, months, years)

  - Distance

  - Experimental steps

### Avoid line charts when:

- Data is categorical with no natural order.

Bad Example: plotting “Red”, “Blue”, “Green” as x-axis categories.

Why? Line charts suggest continuity, but colors aren’t sequential.

- You're showing individual values, not trends.

Better: use bar charts or scatter plots for discrete comparisons.

- Data points are not connected in meaning.

Connecting unrelated data with lines can mislead the viewer.

- You have too much noise or many lines, making it hard to read.

If your chart has 10+ lines and it's messy, consider breaking it into smaller charts.

### Quick Rule of Thumb:

- Use line charts for **time series** and **trends**.

- Don’t use them for **categories**, **unrelated points**, or **isolated data**.

---

**b) Whats wrong with this chart?**

<img src="theory_figures/bar_no_zero.png"  width="500">

Y-axis does not start at zero: it begins at 75, not 0.

- This can distort the visual interpretation of the data.

- It exaggerates differences between bars that might actually be small.

**Why it's an issue:**
Even though the actual difference between, say, 85% and 90% is just 5 percentage points, the visual gap looks huge because the y-axis is cut off.

This can unintentionally mislead viewers into thinking the changes are more dramatic than they are.

---

**c) Whats wrong with this chart?**

<img src="theory_figures/line_categorical.png"  width="500">

- The x-axis shows car brands (Volkswagen, Volvo, etc.), which are categorical, not continuous.

- Line charts are meant to show trends over continuous data (like time or measurements).

- Using a line chart here suggests a progression or connection between brands, which doesn’t make sense—there’s no natural order or “flow” from Volkswagen to Peugeot.

**A bar chart is the better choice because:**

- It clearly shows the quantity for each brand.

- It doesn’t imply any connection or trend between categories.

---

**d) What is the difference between OOP approach and plt approach in drawing graphs.**

The OOP approach and the plt approach in Matplotlib both let you draw graphs—but they work a bit differently under the hood.

### plt Approach (Pyplot Interface)

Also called the state-based interface, this is the simpler and more intuitive way to create plots, especially for beginners.

🧠 How it works:

- Think of it like a “drawing mode”: every plt.plot() or plt.title() affects the current figure.

- It’s like using a whiteboard where each new command updates what’s on it.

✅ Pros:

- Very easy and fast for small plots.

- Great for quick visualizations or learning.

❌ Cons:

- Can get messy or hard to control with multiple subplots or complex layouts.

- Less explicit = harder to debug or customize in big projects.

🔍 Example:

```py
import matplotlib.pyplot as plt 
plt.plot([1, 2, 3], [4, 5, 6]) 
plt.title("Simple Plot") 
plt.xlabel("X") plt.ylabel("Y") 
plt.show()
```


### OOP Approach (Object-Oriented Programming)

This is a more flexible and powerful way, especially useful when building complex or professional plots.

🧠 How it works:

- You explicitly create figure and axes objects, then call methods on them.

- You're not relying on the "current state" of the plot—you're managing everything directly.

✅ Pros:

- Better control over multiple subplots, axes, and figures.

- More readable and organized for complex visualizations.

❌ Cons:

- Slightly more code.

- A bit more advanced for beginners.

🔍 Example:

```py
import matplotlib.pyplot as plt

fig, ax = plt.subplots()  # Create figure and axes
ax.plot([1, 2, 3], [4, 5, 6])
ax.set_title("Simple Plot")
ax.set_xlabel("X")
ax.set_ylabel("Y")
plt.show()
```

| Feature               | plt (State-Based)       | OOP (Figure & Axes Objects)       |
| --------------------- | ----------------------- | --------------------------------- |
| Simplicity            | ✅ Easier for beginners | ❌ Slightly more complex          |
| Control & Flexibility | ❌ Limited for subplots | ✅ Excellent for complex layouts  |
| Best For              | Quick plots, learning   | Dashboards, professional projects |
| Explicit Structure    | ❌ Implicit             | ✅ Very clear and organized       |


---
**e) How do you draw an arrow in matplotlib?**

1. Basic Arrow with plt.arrow()
This is the simplest way to draw a straight arrow on a plot.

Example:
```py
import matplotlib.pyplot as plt

plt.figure()
plt.xlim(0, 10)
plt.ylim(0, 10)
# Draw arrow from (2, 2) pointing 3 units right and 4 units up
plt.arrow(2, 2, 3, 4, head_width=0.5, head_length=0.7, fc='blue', ec='blue')

plt.grid(True)
plt.show()
```
 Notes:
- plt.arrow(x, y, dx, dy, ...)

- It draws an arrow from point (x, y) to (x+dx, y+dy).

- Not always ideal for annotations or adjusting size with figure scaling.

2. Better Arrow with ax.annotate()
This is the recommended and more powerful method, especially for labeling or pointing at stuff.

Example:

```py
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot([1, 2, 3], [4, 5, 6])

# Annotate with an arrow
ax.annotate('Here!', xy=(2, 5), xytext=(1.5, 6),
             arrowprops=dict(facecolor='black', arrowstyle='->'))

plt.show()
```

Why it's better:
- You can control arrow style, direction, labels, etc.

- Works well with both text and shapes.

- Handles coordinate transforms better than plt.arrow().

# Exercise 1

## Task 4. Theory questions

---

**a) Why is it good to use the proximity principle when designing visuals?**

- The proximity principle comes from Gestalt psychology, and it says that elements that are close together are perceived as related.

- In data visualization, using proximity helps people instantly understand relationships between items without needing extra explanations.

- It reduces cognitive load because viewers can group related data points or labels easily and interpret the chart faster and more accurately.

- In short: Proximity = Clear structure = Faster understanding.

**b) What is clutter and why is it undesirable?**

- Clutter is when there are too many visual elements (e.g., too many colors, lines, labels, decorations, or unrelated data) that distract the viewer from the main message.

- Clutter makes visuals harder to read, slower to understand, and can confuse or overwhelm the audience.

- In data visualization, the goal is clarity and focus. Clutter buries important insights under unnecessary noise.

- Think of it like this: Clutter hides the story you want to tell.

**c) Why should you spend time on data storytelling when there is a lot of things that needs to be explored and cleaned in the data?**

- Even if data is messy, storytelling is what makes insights meaningful.

- Data exploration and cleaning help prepare the data, but storytelling is what translates technical findings into understandable narratives for others.

- Spending time on storytelling ensures that after all the hard work of cleaning, you don’t just throw facts at people, but you guide them to the important conclusions.

- Without storytelling, even the cleanest, richest data can fail to engage or persuade your audience.


**d) Data storytelling is very subjective in terms of which story to tell. How could you or your team craft a compelling story to tell?**

- Start by knowing your audience: Understand what they care about or need to decide.

- Explore the data carefully: Look for patterns, anomalies, trends that could be interesting or important.

- Choose a clear angle: Pick one main insight or narrative rather than trying to cover everything at once.

- Use structure: Frame your story with a beginning (context), middle (key findings), and end (implications or actions).

- Make it visual and focused: Support your story with simple, clean visuals that highlight the main message.

- Test it: Share the draft story with teammates for feedback — does it make sense, is it compelling, does it answer "so what?"

### In short: 
**Good storytelling = Audience-centered + Insight-driven + Visually clear + Actionable.**


# Exercise 2

## Task 4. Theory questions

---

**a)  What is the difference between Plotly Graph Objects and Plotly Express?**

#### Plotly Express → Quick and easy way to make charts.
It’s like a “shortcut” — you just give it your data, and it figures out most of the layout and style for you.

Example:
```python
import plotly.express as px
df = px.data.iris()
fig = px.scatter(
    df, 
    x='sepal_width', 
    y='sepal_length', 
    color='species')
fig.show()
```
#### Plotly Graph Objects → More control and customization.
You build the figure step by step: define traces (data series), layout, and then combine them.

Example:
```python
import plotly.graph_objects as go
fig = go.Figure()
fig.add_trace(
  go.Scatter(
    x=[1, 2, 3], 
    y=[4, 5, 6], 
    mode='lines+markers'
    )
  )
fig.update_layout(title='Simple Line Plot')
fig.show()
```

##### Summary:

- Use Plotly Express for fast plotting.

- Use Graph Objects when you need more detailed control (like adding multiple layers, custom legends, etc.).

---
**b) How do you customize the hover in your visualizations?**

One can change hover info (what shows up when you hover over points) using:

- hover_data (Plotly Express)

- hovertemplate or hoverinfo (Graph Objects)

##### Example with Plotly Express:

```python
fig = px.scatter(
  df, 
  x='sepal_width', 
  y='sepal_length', 
  color='species',
  hover_data=['petal_length', 'petal_width']
  )
fig.show()
```

##### Example with Graph Objects:

```python
fig = go.Figure()
fig.add_trace(go.Scatter(
    x=[1, 2, 3],
    y=[4, 5, 6],
    mode='markers',
    hovertemplate='X: %{x}<br>Y: %{y}<extra></extra>'
))
fig.show()
```
---

**c) When should you use Plotly vs Matplotlib?**

##### Matplotlib:

- Best for static plots (like in PDFs, reports, papers)

- Good when you want simple, quick plots with full control over appearance

- Not interactive

##### Plotly:

- Best for interactive plots (hovering, zooming, tooltips)

- Great for dashboards, web apps, or sharing online

- Easier to explore big or complex datasets interactively

##### Example:

- Report figure → Matplotlib

- Interactive dashboard → Plotly

# Exercise 3

## Task 3. Theory questions

---

**a) What are some differences between streamlit and taipy?**

#####  Streamlit and Taipy are both tools for building web apps using Python, but they have different focuses:

- Streamlit is simpler and quicker for making dashboards and prototypes.

- Taipy is more advanced, designed for full applications with features like pipelines, scenarios, and better control over user interaction and data flow.

Example:

- Use Streamlit if you want to build a quick dashboard from a DataFrame.

- Use Taipy if you want to build a full app that runs a process (like a prediction model), tracks user input, and displays multiple outputs.

---
**b) What is the state variable used for?**

The state variable in Taipy stores the current values of variables (like user input or data) and keeps track of changes. It helps the app know when to update the UI.

##### Example:

```python
def on_button_click(state):
    state.counter += 1
```

If you click a button, the counter will increase and the app will show the new value, thanks to the state.

---
**c) How do you style Taipy apps?**

You can style Taipy apps using:

- CSS (custom styles)

- Taipy's style properties (like style="color:red;")

- Themes (light/dark modes)

---
**d) What is a KPI?**

KPI stands for Key Performance Indicator. It's a value that shows how well something is performing.

Example:

- In a sales dashboard, a KPI might be "Total Sales: $10,000"

- In Taipy, you can show this using a gui.kpi component.

---
**e) How do you integrate Plotly graphs into Taipy?**

You can create a Plotly chart and pass it to a Taipy gui.plotly component.

##### Example:

```python
import taipy.gui.builder as tgb
from taipy.gui import Gui
import plotly.express as px

# load data
df_gapminder_Sweden = px.data.gapminder().query("country == 'Sweden'")

# Create a Plotly figure
bar_chart = px.line(
    df_gapminder_Sweden,
    x="year",
    y="pop",
    title="Population change",
    labels={
        "pop": "Population",
    }
)

with tgb.Page() as page:
    with tgb.part(class_name="card"):
        tgb.text("Graph")
        tgb.chart(figure="{bar_chart}")


if __name__ == "__main__":
    Gui(page).run(dark_mode=False, use_reloader=False, port=8080)
```

This shows a line chart inside your Taipy app.

---
**f) What is the difference between Python-syntax and Markdown syntax in Taipy?**

Python syntax is used in your .py files, like normal Python code.

##### Example:

```python
gui.Text("Hello from Python!")
```

Markdown syntax is used in .py or .md files to define layout using text formatting and embedded Taipy variables/components.

```python
# Hello from Markdown!
<|Text|label=Welcome|>
```

You can mix both in a Taipy app depending on how you want to structure your code and layout.

