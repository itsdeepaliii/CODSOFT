from tkinter import *
import random
tk=Tk()
tk.title("Password Generator")
tk.geometry('300x300')
tk.configure(background='gainsboro')

# To store/retrieve the string value entered by user
password=StringVar()

# To store/retrieve the Integer value entered by user
pas=IntVar()
pas.set("")

# Function to generate a random password
def password_generator():
    characters='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 !@#$%^&*()'
    Password=''
    if pas.get()>=8:
        for i in range(pas.get()):
            Password+=random.choice(characters)
        password.set(Password)


# Label to display the primary instruction to user to enter the length of passwod he requires
Label(tk, text="Enter the length of the password \n (Minimum length should be 8)",bg='darkolivegreen4',fg='white').pack(pady=3)

# To store the entry of user
Entry(tk, textvariable=pas).pack(pady=3)

# To generate Random password and confirmation by the button click
Button(tk, text="Generate Password", command=password_generator,bg='darkolivegreen4',fg='white').pack(pady=7)
Entry(tk, textvariable=password).pack(pady=3)

tk.mainloop()