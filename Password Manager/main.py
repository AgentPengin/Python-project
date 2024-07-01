import tkinter
from tkinter import messagebox
import random
import pyperclip
END = tkinter.END

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_letters = [random.choice(letters) for x in range(nr_letters)]
    password_symbols = [random.choice(symbols) for x in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for x in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0,END)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():

    if (len(website_entry.get()) == 0 or len(password_entry.get()) == 0):
        messagebox.showinfo(title = "Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title = website_entry.get(), message = f"There are the details entered: \nEmail: {email_entry.get()} \nPassword: "
                                                                 f"{password_entry.get()} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as f:
                f.write(f"{email_entry.get()} | {password_entry.get()} | {website_entry.get()}")
                f.write('\n')
                password_entry.delete(0,END)
                website_entry.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx = 50, pady = 50)

#Image
canvas = tkinter.Canvas(width = 200, height = 200, highlightthickness = 0)
logo_img = tkinter.PhotoImage(file = "logo.png")
canvas.create_image(100,100, image = logo_img)
canvas.grid(row = 0,column = 1)

#Label
website_label = tkinter.Label(text = "Website: ", font = ("Arial",10))
website_label.grid(row = 1, column = 0)
email_label = tkinter.Label(text = "Email/Username: ", font = ("Arial",10))
email_label.grid(row = 2,column = 0)
password_label = tkinter.Label(text = "Password: ", font = ("Arial",10))
password_label.grid(row = 3,column = 0)

#Buttons
genpass_button = tkinter.Button(text = "Generate Password", font = ("Arial",10), command = generate_password)
genpass_button.grid(row = 3,column = 2)
add_button = tkinter.Button(text = "Add", font = ("Arial", 10),width = 36,command = save_password)
add_button.grid(row = 4, column = 1, columnspan = 2)

#Entries
website_entry = tkinter.Entry(width = 35)
website_entry.grid(row = 1,column = 1,columnspan = 2)
website_entry.focus()

email_entry = tkinter.Entry(width = 35)
email_entry.grid(row = 2,column = 1,columnspan = 2)
email_entry.insert(0, "example@gmail.com")

password_entry = tkinter.Entry(width = 21)
password_entry.grid(row = 3,column = 1)

window.mainloop()
