from tkinter import *
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if len(website) ==0 or len(username) ==0 or len(password) ==0 :
        messagebox.showinfo(title="Oops", message="Please make sure you haven't "
                                                    "left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, 
                                    message=f"These are the details entered: "
                                    f"\nUsername: {username}" 
                                    f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("Test_passwords.txt", "a") as file:
                file.write(f" Website: {website} | Username: {username} | Password: {password}\n")
                website_entry.delete(0,END)
                username_entry.delete(0,END)
                password_entry.delete(0,END)
                username_entry.insert(0, "your_email@gmail.com") 
                website_entry.focus()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Lables
website_lable = Label(text="Website:")
website_lable.grid(row=1, column=0)

username_lable = Label(text="Email/Username:")
username_lable.grid(row=2, column=0)

password_lable = Label(text="Password:")
password_lable.grid(row=3, column=0)

# Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2, sticky="EW", padx=(5,0),  ) 
website_entry.focus() 

username_entry = Entry(width=35)
username_entry.grid(row=2, column=1, columnspan=2, sticky="EW", padx=(5,0), pady=2)
username_entry.insert(END, "your_email@gmail.com") 

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky="EW", padx=(5,0), pady=2)

# Buttons
generate_password_button = Button(text="Generate Password")
generate_password_button.grid(row=3, column=2, sticky="EW", padx=(5,0), pady=2) 

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW", padx=(5,0), pady=2)


window.mainloop()
