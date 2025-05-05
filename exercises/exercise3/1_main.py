# 1.  App for simulating dices

from taipy.gui import Gui
import taipy.gui.builder as tgb
import plotly.express as px
import pandas as pd
import random
import numpy as np

slider_num_dice = 5
slider_num_throws = 101

df = pd.DataFrame()
fig = None
throw_means = pd.Series()

theoretical_mean = 3.5
calculated_mean = 0
difference = theoretical_mean - calculated_mean


def perform_simulation(state):
    # Initialize an empty DataFrame with column names corresponding to each die
    state.df = pd.DataFrame(columns=[f"Die {i+1}" for i in range(state.slider_num_dice)])

    # Simulate the dice throws and add a new row for each throw
    for throw in range(state.slider_num_throws):
        # Create a row with the results of all dice for the current throw
        state.df.loc[throw] = [random.randint(1, 6) for _ in range(state.slider_num_dice)]

    # Calculate the mean of all values
    state.throw_means = state.df.mean(axis=1)
    state.calculated_mean = state.df.to_numpy().mean()
    state.difference = np.abs(state.theoretical_mean-state.calculated_mean)

    state.fig = px.histogram(state.throw_means, nbins=20, labels={'value': 'Mean per throw'}, title='Histogram of throw means')


with tgb.Page() as page:
    tgb.text("# Dices simulation", mode ="md")
    with tgb.part():
        with tgb.layout(columns = "1 1"):
            with tgb.part(class_name="container card") as column_table: 
                # binds to slider_value and makes it dynamic
                tgb.table("{df}", rebuild = True, page_size=10)
                tgb.slider(value = "{slider_num_dice}", min = 1, max = 10, step = 1, continuous=False)
                tgb.text("Slider value is at {slider_num_dice}")
                tgb.slider(value = "{slider_num_throws}", min = 1, max = 1001, step = 100, continuous=False)
                tgb.text("Slider value is at {slider_num_throws}")
                tgb.button(label = "SIMULATE", class_name="plain", on_action=perform_simulation)

            with tgb.part(class_name="container card") as column_results: 
                tgb.text("Theoretical mean: {theoretical_mean:.2f}")
                tgb.text("Calculated mean:{calculated_mean:.2f}")
                tgb.text("Difference:  {difference:.2f}")
                tgb.text("Mean value of {slider_num_dice} dices for {slider_num_throws} throws")
                tgb.chart("{fig}")
                tgb.text("This histogram have been calculated through taking mean values for each throw")



if __name__ == '__main__':
    Gui(
        page
    ).run(dark_mode=False, use_reloader=False, port=8080)
