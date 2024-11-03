import tkinter as tk
import random
from PIL import ImageTk,Image

# Function to load jokes from a file
def load_jokes(): 
    with open(r"/Users/mac/Desktop/exercise/randomJokes.txt") as file:
        return [line.strip() for line in file if line.strip()] #  strip() removes leading/trailing whitespace

# Function to display a random joke
def tell_joke(): 
    joke = random.choice(jokes) #   random.choice() returns a random element from the list
    setup, punchline = joke.split("?", 1)  #  split() it will splits a string into a list where each word is  listed  in item
    setup_label.config(text=f"Setup: {setup}?") #   config() is used to change the configuration of a widget
    punchline_label.config(text="") 
    global current_punchline #   global keyword is used to indicate that a variable is global
    current_punchline = punchline.strip()  #  strip() removes leading/trailing whitespace
    show_button.config(state=tk.NORMAL)  #   config() is used to change the configuration of a widget

# Function to show the punchline
def show_punchline():
    punchline_label.config(text=f"Punchline: {current_punchline}") 
    show_button.config(state=tk.DISABLED)   #   config() is used to change the configuration of a widget

# Creating the main window
root = tk.Tk()
root.title("Alexa tell me a Joke")  #   title() is used to set the title of the window 
root.geometry("400x500") #    geometry() is used to set the size and position of the window
root.configure(background="#e5ebc5") 


# function to load jokes
jokes = load_jokes() #    load_jokes() is a function that loads jokes from a file
current_punchline = "" #    current_punchline is a global variable that stores the current punchline

# Creating labels and buttons
setup_label = tk.Label(root, text="", fg='Red',bg='#e5ebc5', wraplength=300, font=("Times New Roman", 16)) #   we use  Label()  to create a label widget to show jokes 
setup_label.pack(pady=20)

punchline_label = tk.Label(root, text="", fg='green',bg='#e5ebc5', wraplength=300, font=("Times New Roman", 16))   # this Label() is to used to show  the punchline
punchline_label.pack(pady=20)

show_button = tk.Button(root, text="Show Punchline",fg='Black',bg='yellow',font=("Gill Sans", 14) , command=show_punchline, state=tk.DISABLED)   #   we use  Button() to create a button widget to show the punchline when its clicked
show_button.pack(pady=10)

speak_button = tk.Button(root, text="Alexa tell me a Joke", fg='black',bg='light blue',font=("Gill Sans", 14) , command=tell_joke) #    we use  Button() to create a button widget to tell a joke when its clicked
speak_button.pack(pady=10) 

exit_button = tk.Button(root, text="Exit", fg='black', bg='light yellow',font=("Gill Sans", 12), command=root.quit) #    we use  Button() to create a button widget to exit the application.
exit_button.pack(pady=10) #    pack() is used to add a widget to the window and fix its size accordingly 


# now Run the application
root.mainloop()
