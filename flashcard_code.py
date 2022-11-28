import random
import pandas
import tkinter as tk
import pandas as pd


def dictionary_words():
    pass


def pop_up():
    # this sets up the pop-up window
    window = tk.Tk()  # an instance of the window
    window.title('Study Flashcards')
    window.geometry('700x500')
    window.configure(bg='blue')

    # this prints the text out in black.
    definition = tk.Label(window, text="Put definition Here",font=("Helvetica",36)) #change text to a variable
    definition.configure(bg='blue')
    definition.pack(padx=15, pady=90)

    # this makes the text area for typing
    answer_entry = tk.Entry(window)
    answer_entry.grid(row=3,column=10)
    answer_entry.pack(padx=15, pady=30)
    answer_entry.config(text="") # missing one more step....

    # this makes the button to check if the text is correct.
    button_frame = tk.Frame(window)
    button_frame.pack(padx=15,pady=10)
    answer_button = tk.Button(button_frame, text="Answer")
    answer_button.grid(row=4,column=10)
    #missing on response


pop_up()
