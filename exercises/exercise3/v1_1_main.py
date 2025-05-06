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

# Simulate df with dice throws
def generate_df(num_dice = slider_num_dice, num_throws = slider_num_throws):
    df = pd.DataFrame(columns=[f"Die {i+1}" for i in range(num_dice)])
    for throw in range(num_throws):
        df.loc[throw] = [random.randint(1, 6) for _ in range(num_dice)]
    return df

df = generate_df()

# Calculate start values
throw_means = df.mean(axis=1)
theoretical_mean = 3.5
calculated_mean = df.to_numpy().mean()
difference = np.abs(theoretical_mean - calculated_mean)
fig = px.histogram(throw_means, nbins=20, labels={'value': 'Mean per throw'}, title='Histogram of throw means')


def perform_simulation(state):
    df = generate_df(state.slider_num_dice, state.slider_num_throws)
    
    state.throw_means = state.df.mean(axis=1)
    state.calculated_mean = state.df.to_numpy().mean()
    state.difference = np.abs(state.theoretical_mean - state.calculated_mean)
    state.fig = px.histogram(state.throw_means, nbins=20, labels={'value': 'Mean per throw'}, title='Histogram of throw means')


with tgb.Page() as page:
    with tgb.part():
        tgb.text("# Dice Simulation", mode="md")

        with tgb.layout(columns="1 1"):
            with tgb.part(class_name="container card"):
                tgb.table("{df}", rebuild=True, page_size=10)
                tgb.slider(value="{slider_num_dice}", min=1, max=10, step=1)
                tgb.text("Dices: {slider_num_dice}")
                tgb.slider(value="{slider_num_throws}", min=1, max=1001, step=100)
                tgb.text("Throws: {slider_num_throws}")
                tgb.button("SIMULATE", on_action=perform_simulation)

            with tgb.part(class_name="container card"):
                # TODO: check how to position widgets correctly!
                """
                with tgb.layout(columns="1 1 1"):
                    tgb.text("Theoretical mean\n{theoretical_mean:.2f}",rebuild=True)
                    tgb.text("Calculated mean\n{calculated_mean:.2f}",rebuild=True)
                    tgb.text("Difference\n{difference:.2f}",rebuild=True)
                """
                tgb.chart(figure = "{state.fig}")
                tgb.text("The histogram have been calculated through taking mean values for each throw")


if __name__ == '__main__':
    Gui(page).run(dark_mode=False, use_reloader=False)
