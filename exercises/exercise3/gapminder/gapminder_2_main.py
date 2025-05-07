import taipy.gui.builder as tgb
from taipy.gui import Gui
import pandas as pd
import plotly.express as px

df = gapminder = px.data.gapminder()
# group per continent and year
df_continent = (
    gapminder.groupby(["year", "continent"])
    .agg({"pop": "sum", "lifeExp": "mean", "gdpPercap": "mean"})
    .reset_index().rename(columns={
        "pop": "Population",
        "lifeExp": "Life Expectancy",
        "gdpPercap": "GDP Per Capita"
    })
)


def filter_metric(df, metric, year):
    return df.query("year == @year")[["continent", metric]]


def filter_data(state):
    try:
        df_filtered = filter_metric(
            state.df_continent, state.selected_metric, state.selected_year
        )

        state.bar_chart = px.bar(
            df_filtered,
            x="continent",
            y=state.selected_metric,
            title=f"{state.selected_metric.capitalize()} by Continent in {state.selected_year}",
            labels={
                "continent": "Continent",
                state.selected_metric: state.selected_metric.capitalize(),
            },
        )
    except Exception as e:
        print(f"Error updating chart: {e}")
        state.bar_chart = None  # or you could assign an empty figure if preferred


selected_year = 2007
selected_metric = "Population"

try:
    df_filtered = filter_metric(df_continent, selected_metric, selected_year)

    bar_chart = px.bar(
        df_filtered,
        x="continent",
        y=selected_metric,
        title=f"{selected_metric.capitalize()} by Continent in {selected_year}",
        labels={
            "continent": "Continent",
            selected_metric: selected_metric.capitalize(),
        },
    )
except Exception as e:
    print(f"Error creating initial chart: {e}")
    bar_chart = None


# --------------------------------------------------------------
# --------------------------------------------------------------

with tgb.Page() as page:
    with tgb.part(class_name="container card"):
        tgb.text("# Gapminder continents", mode="md")

        with tgb.layout(columns="2 1"):
            with tgb.part(class_name="card"):
                tgb.text("Graph")
                tgb.chart(figure="{bar_chart}")

            with tgb.part(class_name="card"):
                tgb.text("## Filtrer data", mode="md")
                tgb.text("Select year", mode="md")

                tgb.slider(
                    "{selected_year}",
                    min = df_continent["year"].min(),
                    max = df_continent["year"].max(),
                    continuous=False,
                )

                tgb.text("Select metric", mode="md")
                tgb.selector(
                    "{selected_metric}",
                    lov = ["Population", "Life Expectancy", "GDP Per Capita"],
                    dropdown = True,
                )

                tgb.button("FILTRER DATA", class_name="plain", on_action=filter_data)

        #with tgb.part(class_name="card"):
        #    tgb.text("Raw data")
        #    tgb.table("{df}")


# --------------------------------------------------------------
# --------------------------------------------------------------

if __name__ == "__main__":
    Gui(page).run(dark_mode=False, use_reloader=False, port=8080)
