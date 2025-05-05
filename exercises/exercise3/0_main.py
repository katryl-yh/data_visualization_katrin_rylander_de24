# 0. Palindrome game

from taipy.gui import Gui
import taipy.gui.builder as tgb
import plotly.express as px

user_input = "Anna"
result = "True"
counter = 0



def clear_results(state):
    state.result = ""

def is_palindrome(state):
    input_string = state.user_input.lower().replace(" ", "")
    print(f"current input: {input_string}")
    print(f"before results is: {state.result}")
    if input_string == input_string[::-1]:
        state.result = "True"
        state.counter +=1
    else:
        state.result = "False"
        state.counter -=1
    print(f"after results is {state.result}")


with tgb.Page() as page:
    tgb.text("# Palindrome game", mode ="md", class_name="color-primary")
    tgb.text(
        "A palindrome is a set of characters that is read the same backwards as forwards.  \n"
        "Example of palindromes (case-insensitive and ignoring spaces):  \n"
        "- Anna  \n"
        "- Otto", mode="md"
    )
    tgb.text("Each correct answer = ⭐  \nEach incorrect answer = 😭", mode="md")

    # on change -> this function will run when value is changed
    tgb.text("Type in your set of characters")
    tgb.input("{user_input}", on_change = clear_results)

    tgb.text("You have typed in {user_input}")

    tgb.button(label = "CHECK", class_name="plain", on_action=is_palindrome)

    tgb.text("The results is: {result}, current counter is: {counter} ")


if __name__ == '__main__':
    Gui(
        page
    ).run(dark_mode=False, use_reloader=False, port=8080)