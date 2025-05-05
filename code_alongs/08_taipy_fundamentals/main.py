from taipy.gui import Gui
import taipy.gui.builder as tgb
import plotly.express as px

df = px.data.gapminder()
fig = px.line(df.query("country == 'Sweden'"), x = "year", y = "pop")

slider_value = 20
selected_fruit = "avocado"
number1 = 5
number2 = 8

sum_ = number1 + number2
# TODO: add division, multiplication and subtracion

def perform_calculation(state):
    print(state.number1)

    state.sum_ = int(state.number1) + int(state.number2) # TODO: add try-except to handle errors properly

def clear_results(state):
    state.sum_ = ""

with tgb.Page() as page:
    with tgb.part(class_name="container card"):
        with tgb.layout(columns = "1 1 1"):
            with tgb.part() as column_fruit: 
                tgb.text("# Hello there taipy", mode ="md", class_name="color-primary")
                tgb.text("Welcome to the world ot reactive programming")

                # binds to slider_value and makes it dynamic
                tgb.slider(value = "{slider_value}", min = 1, max = 50, step = 5, continuous=False)
                tgb.text("Slider value is at {slider_value}")
                tgb.text("Slider value again is at {slider_value}")

                tgb.text("Select your favourite fruit", mode = "md")
                tgb.selector(
                    value="{selected_fruit}", 
                    lov=["tomato", "apple", "avocado", "banana"],
                    dropdown=True,
                )
                tgb.text("Yummy {selected_fruit}")
                tgb.image("assets/{selected_fruit}.jpg")

            with tgb.part() as column_calculator:
                tgb.text("## Coolu calculatoru", mode = "md")
                tgb.text("Type in a number")
                tgb.input("{number1}", on_change = clear_results)

                # on change -> this function will run when value is changed
                tgb.text("Type in another number")
                tgb.input("{number2}", on_change = clear_results)

                tgb.text("You have typed in {number1} and {number2}")

                tgb.button(label = "CALCULATU", class_name="plain", on_action=perform_calculation)

                tgb.text("{number1} + {number2} = {sum_}")
            
            with tgb.part() as column_data:
                tgb.table("{df}", page_size=10)

                tgb.chart(figure = "{fig}")


if __name__ == '__main__':
    Gui(page).run(dark_mode=False, use_reloader=False, port=8080)