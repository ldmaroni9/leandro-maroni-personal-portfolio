from tkinter import *
from tkinter import messagebox
import random
import pandas
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def password_generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    random_letter = [random.choice(letters) for n in range(random.randint(8, 10))]
    random_symbol = [random.choice(symbols) for n in range(random.randint(2, 4))]
    random_number = [random.choice(numbers) for n in range(random.randint(2, 4))]

    password_list = random_letter + random_symbol + random_number
    random.shuffle(password_list)

    password = ''.join(password_list)
    pass_website.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
saved_user = []
saved_website = []
saved_passwords = []

def website_button_clicked():
    website = input_website.get()
    password = pass_website.get()
    email = user_website.get()
    new_dict = {
        website: {
            "email": email,
            "password": password,
            "website": website,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any blank fields.")
    else:
        try:
            with open("data.json", "r") as data_file:
                #Reading old data
                data = json.load(data_file)
        except FileNotFoundError or KeyboardInterrupt:
            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(new_dict, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_dict)
            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            pass_website.delete(0, END)
            input_website.delete(0, END)
        # saved_user.append(user_website.get())
        # saved_website.append(website)
        # saved_passwords.append(password)

        #saved_data = pandas.DataFrame.from_dict({"user": saved_user, "website": saved_website, "password": saved_passwords})
        #print(saved_data)
        #key.append(input_website.get())
        #value.append(user_website.get())
        #saved_data.to_csv('data.txt', sep='\t', index=False)
    #print(saved_data)

# ---------------------------- WEBSITE SEARCH ------------------------------- #


def website_search():
    try:
        with open("data.json", "r") as data_file:
            # Reading old data
            data = json.load(data_file)
            searched_site = input_website.get()
            output = data.get(searched_site)
            extract_user = output.get("email")
            extract_pass = output.get("password")
            messagebox.showinfo(title="Match!", message=f"The user is: {extract_user}\nThe password is: {extract_pass}")
    except FileNotFoundError:
        messagebox.showinfo(title="No files...", message=f"File not found.")
    except AttributeError:
        messagebox.showinfo(title="Not found :(", message=f"There's no details for that website.")

    #            users = [user["email"] for user in data_file[searched_site]]
 #           print(users)
            # for item in data:
            #     if item == searched_site:
            #         for key in data.keys():
            #             print(key)
#                    print(matching_keys[0], matching_keys[1])
#            print(data)
#            print(matching_item)
#            searched_website = data[website]
    except FileNotFoundError:
        # win = Tk()
        # top = TopLevel(win)
        Label(canvas, text="Error. Site not found.")
        #print("There's no data")
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=70, pady=70)

canvas = Canvas(width=200, height=200, highlightthickness=0)

logo_img = PhotoImage(file="logo.png")
logo_image = Label(image=logo_img)
logo_image.grid(column=1, row=0)

#logo_image = canvas.create_image(100,100, image=logo_img)
#canvas.pack()

#Texts
website_text = Label(text="Website:")
website_text.grid(column=0, row=1)

user_text = Label(text="Email/Username:")
user_text.grid(column=0, row=2)

pass_text = Label(text="Password:")
pass_text.grid(column=0, row=3)

#Buttons
generate_button = Button(text="Generate Password", width=14, command=password_generate)
generate_button.grid(column=2, row=3)
add_button = Button(text="Add", width=36, command=website_button_clicked)
add_button.grid(column=1, row=4, columnspan=2)
search_button = Button(text="Search", width=14, command=website_search)
search_button.grid(column=2, row=1)

#Entries
input_website = Entry(width=24)
input_website.grid(column=1, row=1)
input_website.focus()

user_website = Entry(width=42)
user_website.grid(column=1, row=2, columnspan=2)
user_website.insert(0, "leandrodmaroni@gmail.com")

pass_website = Entry(width=24)
pass_website.grid(column=1, row=3)

window.mainloop()
