# states
# black, red, white, in_drawer
def black():
    # experience state
    print("Light is OFF")
    # collect input
    current_input = input("You can click press (c), hold press (h), or do nothing (n) or put it away (p). Which one do you want? ")
    # transition to the next state
    # handle each input
    if current_input == "c":
        white()
    elif current_input == "h":
        red()
    elif current_input == "n":
        black()
    elif current_input == "p":
        in_drawer()
    else:
        print(f"Error! I don't recognize the input {current_input}")
        black()

def white():
    # experience state
    print("White light is ON")
    # collect input
    current_input = input("You can click press (c), hold press (h), or do nothing (n) or put it away (p). Which one do you want? ")
    # transition to the next state
    if current_input == "c":
        black()
    elif current_input == "h":
        red()
    elif current_input == "n":
        white()
    elif current_input == "p":
        in_drawer()
    else:
        print(f"Error! I don't recognize the input {current_input}")
        white()

def red():
    # experience state
    print("Red light is ON")
    # collect input
    current_input = input("You can click press (c), hold press (h), or do nothing (n) or put it away (p). Which one do you want? ")
    # transition to the next state
    if current_input == "c":
        black()
    elif current_input == "h":
        white()
    elif current_input == "n":
        red()
    elif current_input == "p":
        in_drawer()
    else:
        print(f"Error! I don't recognize the input {current_input}")
        red()

# ending states
def in_drawer():
    #experience state
    print("All done")

# starting state
black()