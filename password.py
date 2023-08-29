from tkinter import *
import random
import string
import hashlib

def generator():
    length = int(entry_length.get())
    user_input = entry_user_input.get()

    hash = hashlib.sha256()
    hash.update(user_input.encode())
    hash_value = hash.hexdigest()

    random.seed(hash_value)

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    label_result.config(text=" " + password)

win = Tk()
win.geometry("500x200+500+100")
win.title("PASSWORD GENERATOR")
win.config(bg="#545050")

label_input = Label(win, text="ENTER YOUR CHARACTERS:")
label_input.grid(row=0, column=0, padx=10, pady=5)

label_length = Label(win, text="ENTER PASSWORD LENGTH:")
label_length.grid(row=1, column=0, padx=10, pady=5)


entry_user_input = Entry(win)
entry_user_input.grid(row=0, column=1, padx=10, pady=5)

entry_length = Entry(win)
entry_length.grid(row=1, column=1, padx=10, pady=5)


generate_button = Button(win, text="Generate Password",bg="#bdb4b3", activebackground="#05ad3a",command=generator)
generate_button.grid(row=2, columnspan=2, padx=10, pady=10)


label_result = Label(win, text="", width=30, height=2, bg="white",fg="#ed0c2e")
label_result.grid(row=3, columnspan=2, padx=10, pady=5)

win.mainloop()
