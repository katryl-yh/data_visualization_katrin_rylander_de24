# --- Global Variables ---
from taipy.gui import Gui
import taipy.gui.builder as tgb
import plotly.express as px
import pandas as pd
import random
import numpy as np

# Initial sliders
slider_num_dice = 5
slider_num_throws = 101
theoretical_mean = 3.5


# Simulate df with dice throws
def generate_data(num_dice=slider_num_dice, num_throws=slider_num_throws):
    df = pd.DataFrame(columns=[f"Die {i+1}" for i in range(num_dice)])
    for throw in range(num_throws):
        df.loc[throw] = [random.randint(1, 6) for _ in range(num_dice)]
    calculated_mean = df.to_numpy().mean()
    return df, calculated_mean

# Calculate start values
df, calculated_mean = generate_data()
difference = np.abs(theoretical_mean - calculated_mean)
hist_chart = px.histogram(
    df.mean(axis=1),
    nbins=20,
    labels={"value": "Mean per throw"},
    title="Histogram of throw means",
)  

def create_histogram(df):

    fig = px.histogram(
        df.mean(axis=1),
        nbins=20,
        labels={"value": "Mean per throw"},
        title="Histogram of throw means",
    )
    return fig

def perform_simulation(state):
    df, calculated_mean = generate_data(
        state.slider_num_dice, state.slider_num_throws
    )
    state.df = df
    state.calculated_mean = calculated_mean
    state.difference = np.abs(theoretical_mean - calculated_mean)
    state.hist_chart = create_histogram(state.df)


# ----------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------

with tgb.Page() as page:
    with tgb.part(class_name="container card"):
        tgb.text("# Dice Simulation", mode="md")

        with tgb.layout(columns="1 1"):
            with tgb.part(class_name="card"):
                tgb.table("{df}", rebuild=True, page_size=10)
                tgb.slider(value="{slider_num_dice}", min=1, max=10, step=1)
                tgb.text("Dices: {slider_num_dice}")
                tgb.slider(value="{slider_num_throws}", min=1, max=1001, step=100)
                tgb.text("Throws: {slider_num_throws}")
                tgb.button("SIMULATE", on_action=perform_simulation)

            with tgb.part(class_name="card"):

                with tgb.layout(columns="1 1 1"):
                    with tgb.part(class_name="card"):
                        tgb.text("Theoretical mean", class_name = 'small-text')
                        tgb.text("{theoretical_mean:.2f}")
                    with tgb.part(class_name="card"):
                        tgb.text("Calculated mean", class_name = 'small-text')
                        tgb.text("{calculated_mean:.2f}")
                    with tgb.part(class_name="card"):
                        tgb.text("Difference", class_name = 'small-text')
                        tgb.text("{difference:.2f}")
                with tgb.part(class_name="card"):
                    tgb.chart(figure="{hist_chart}")
                    tgb.text(
                    "The histogram have been calculated through taking mean values for each throw"
                    )

# ----------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------

if __name__ == "__main__":
    Gui(page, css_file="assets/main.css").run(dark_mode=False, use_reloader=False)
