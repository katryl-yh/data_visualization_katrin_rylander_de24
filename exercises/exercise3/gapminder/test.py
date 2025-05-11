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