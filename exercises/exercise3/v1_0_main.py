# 0. Palindrome game

from taipy.gui import Gui
import taipy.gui.builder as tgb
import plotly.express as px

# State variables
user_input = "Anna"
result = "True"
counter = 0
status_icons = ""
pictures = ["fake_sad_rabbit.png", "fake_cat.png"]
pic_pointer = 1

# Clear result when input changes
def clear_results(state):
    state.result = ""

# Palindrome check logic
def is_palindrome(state):
    input_string = state.user_input.lower().replace(" ", "")
    print(f"current input: {input_string}")
    print(f"before results is: {state.result}")
    
    if input_string == input_string[::-1]:
        state.result = True
        state.counter += 1
        state.pic_pointer = 1
    else:
        state.result = "False"
        state.counter -= 1
        state.pic_pointer = 0

    # Update status_icons based on counter
    if state.counter >= 0:
        state.status_icons = "⭐" * state.counter
    else:
        state.status_icons = "😭" * abs(state.counter)

    print(f"after results is {state.result}")
    print(f"picture to show: {pictures[state.pic_pointer]}")

# UI Page definition
with tgb.Page() as page:
    with tgb.part(class_name="container card"):
        tgb.text("# Palindrome game", mode="md", class_name="color-primary")
        tgb.text(
            "A palindrome is a set of characters that is read the same backwards as forwards.  \n"
            "Example of palindromes (case-insensitive and ignoring spaces):  \n"
            "- Anna  \n"
            "- Otto", mode="md"
        )
        tgb.text("Each correct answer = ⭐  \nEach incorrect answer = 😭", mode="md")

        tgb.text("Type in your set of characters")
        tgb.input("{user_input}", on_change=clear_results)

        tgb.text("You have typed in {user_input}")

        tgb.button(label="CHECK", class_name="plain", on_action=is_palindrome)

        tgb.text("Progress: {status_icons}")

        tgb.image("assets/{pictures[pic_pointer]}")

# Run the GUI
if __name__ == '__main__':
    Gui(page).run(dark_mode=False, use_reloader=False, port=8080)
