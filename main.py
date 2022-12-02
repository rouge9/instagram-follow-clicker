from tkinter import *
from tkinter import messagebox

from instagram_follower import InstaFollower

bot = InstaFollower()

# ---------------------------- Instagram Follow Automation ------------------------------- #
def caller():
    try:
        bot.login(user=USERNAME.get(), passw=PASSWORD.get())
        bot.follow(sim_account=SIMILAR_ACCOUNT.get())
    except Exception as e:
        messagebox.showerror(title="Error", message=e)
        print(e)
        return


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Instagram follow clicker")
window.config(pady=50, padx=200)

canvas = Canvas(width=200, height=200)
label_instagram = Label(
    text="Instagram Follow Clicker",
    font=("Arial", 12, "bold"),
)
label_instagram.grid(row=0, column=0)
logo = PhotoImage(file="assets/logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=0)


label_website = Label(text="username")
label_website.grid(row=1, column=2)
label_email = Label(text="password")
label_email.grid(row=2, column=2)
label_password = Label(text="Instagram channal name")
label_password.grid(row=3, column=2)

USERNAME = Entry(width=35)
USERNAME.grid(row=1, column=3)
USERNAME.focus()
PASSWORD = Entry(width=35)
PASSWORD.grid(row=2, column=3)
SIMILAR_ACCOUNT = Entry(width=35)
SIMILAR_ACCOUNT.grid(row=3, column=3)

button_add = Button(text="Follow", width=10, command=caller)
button_add.grid(row=5, column=3, columnspan=2)

window.mainloop()
