import tkinter as tk
contacts = []


def save():
    name = name_box.get()
    phone = phone_box.get()
    if name and phone:
        contacts.append(f"{name} - {phone}")
        name_box.delete(0, tk.END)
        phone_box.delete(0, tk.END)
        msg.set("Contact saved!")
    else:
        msg.set("Enter name and phone number")

def show_all():
    listbox.delete(0, tk.END)
    for c in contacts:
        listbox.insert(tk.END, c)

def search():
    key = search_box.get().lower()
    listbox.delete(0, tk.END)
    for c in contacts:
        if c.lower().startswith(key):
            listbox.insert(tk.END, c)
            return
    listbox.insert(tk.END, "Not found")

# To delete a contact
def remove():
    key = delete_box.get().lower()
    for c in contacts:
        if c.lower().startswith(key):
            contacts.remove(c)
            msg.set("Deleted")
            show_all()
            return
    msg.set("Not found")

# Setup GUI
win = tk.Tk()
win.title("Contact Book")
win.geometry("300x400")

tk.Label(win, text="Name").pack()
name_box = tk.Entry(win)
name_box.pack()

tk.Label(win, text="Phone").pack()
phone_box = tk.Entry(win)
phone_box.pack()

tk.Button(win, text="Add", command=save).pack(pady=5)
tk.Button(win, text="View", command=show_all).pack()

tk.Label(win, text="Search Name").pack()
search_box = tk.Entry(win)
search_box.pack()
tk.Button(win, text="Search", command=search).pack()

tk.Label(win, text="Delete Name").pack()
delete_box = tk.Entry(win)
delete_box.pack()
tk.Button(win, text="Delete", command=remove).pack()

listbox = tk.Listbox(win, width=40)
listbox.pack(pady=10)

msg = tk.StringVar()
tk.Label(win, textvariable=msg).pack()

win.mainloop()
