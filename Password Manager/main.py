import tkinter
from tkinter import messagebox
import random
import pyperclip
import json
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

    password = password_entry.get()
    website = website_entry.get()
    email = email_entry.get()
    new_data = {
        website : {
            "email" : email,
            "password" : password,
        }
    }

    if (len(website) == 0 or len(password) == 0):
        messagebox.showinfo(title = "Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title = website, message = f"There are the details entered: \nEmail: {email} \nPassword: "
                                                                 f"{password} \nIs it ok to save?")
        if is_ok:
            data = {}
            try:
                with open("data.json","r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                pass
            except json.decoder.JSONDecodeError:
                data = {}
                with open("data.json","w") as data_file:
                    json.dump(new_data, data_file, indent = 4)
            else:
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent = 4)
            finally:
                password_entry.delete(0,END)
                website_entry.delete(0,END)

def search_password():
    website = website_entry.get()
    try:
        with open("data.json","r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title = "Oops", message = "No data file found")
    except json.decoder.JSONDecodeError:
        messagebox.showinfo(title = "Oops", message = "No data file found")
    else:
        have_data = False
        for info in data:
            if info == website:
                have_data = True
                messagebox.showinfo(title = website, message = f"Email: {data[info]["email"]}\nPassword: {data[info]["password"]}")
                break
        if have_data == False:
            messagebox.showinfo(title = "Oops", message = "No details for the website exist")

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
genpass_button.grid(row = 3,column = 2, sticky = "w")
search_button= tkinter.Button(text = "Search", font = ("Arial",10), width = 14, command = search_password)
search_button.grid(row = 1, column = 2, sticky = "w")
add_button = tkinter.Button(text = "Add", font = ("Arial", 10),width = 40,command = save_password)
add_button.grid(row = 4, column = 1, columnspan = 2)


#Entries
website_entry = tkinter.Entry(width = 32, justify = "left")
website_entry.grid(row = 1,column = 1,columnspan = 2, sticky = "w")
website_entry.focus()

email_entry = tkinter.Entry(width = 54)
email_entry.grid(row = 2,column = 1,columnspan = 2, sticky = "w")
email_entry.insert(0, "example@gmail.com")

password_entry = tkinter.Entry(width = 32)
password_entry.grid(row = 3,column = 1, sticky = "w")

window.mainloop()
