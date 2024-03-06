""" Opgave "GUI step 4":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Bruge det, du har lært i GUI-eksempelfilerne, og byg den GUI, der er afbildet i images/gui_2040.png

Genbrug din kode fra "GUI step 3".

Fyld treeview'en med testdata.
Leg med farveværdierne. Find en farvekombination, som du kan lide.

Funktionalitet:
    Klik på knappen "clear entry boxes" sletter teksten i alle indtastningsfelter (entries).
    Hvis du klikker på en datarække i træoversigten, kopieres dataene i denne række til indtastningsfelterne.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""


import tkinter as tk
from tkinter import ttk

import random


def clear_all_entry_boxes():
    print("all entries emptied")
    id_entry1.delete(0, tk.END)
    weight_entry1.delete(0, tk.END)
    destination_entry1.delete(0, tk.END)
    weather_entry1.delete(0, tk.END)

# fix this styling doesn't work for some reason
def read_table(tree):
    count = 0
    for record in data_list:
        if count % 2 == 0:  # even
            tree.insert(parent='', index='end', text='', values=record, tags=('evenrow',))
        else:  # odd
            tree.insert(parent='', index='end', text='', values=record, tags=('oddrow',))
        count += 1

def edit_record(event, tree):
    index_selected = tree.focus()
    values = tree.item(index_selected, "values")
    id_entry1.delete(0, tk.END)
    weight_entry1.delete(0, tk.END)
    destination_entry1.delete(0, tk.END)
    id_entry1.insert(0, values[0])
    weight_entry1.insert(0, values[1])
    destination_entry1.insert(0, values[2])





padx = 8
pady = 4

# rows odd or even
oddrow = "#cccccc"
evenrow = "#dddddd"

# row height
treeview_rowheight = 24

# treeview's style
treeview_background = "#eeeeee"
treeview_foreground = "black"
treeview_selected = "#773333"


data_list = []



main_window = tk.Tk()
main_window.title("my first GUI")
main_window.geometry("500x500")

style = ttk.Style()
style.theme_use("default")
style.configure("Treeview", background=treeview_background, foreground=treeview_foreground, rowheight=treeview_rowheight, fieldbackground=treeview_background)
style.map("Treeview", background=[("selected", treeview_selected)])









labelframe1 = tk.LabelFrame(main_window, padx=padx, pady=pady, text="Container")
labelframe1.grid(row=0, column=0, padx=padx, pady=pady)

# treeview and scrollbar frame
treeview_and_scrollbar_frame1 = tk.Frame(labelframe1)
treeview_and_scrollbar_frame1.grid(row=0, column=0, padx=padx, pady=pady)

# treeview and scrollbar
tree_1_scrollbar = tk.Scrollbar(treeview_and_scrollbar_frame1)
tree_1_scrollbar.grid(row=0, column=1, padx=0, pady=pady, sticky="ns")
tree_1 = ttk.Treeview(treeview_and_scrollbar_frame1, yscrollcommand=tree_1_scrollbar.set, selectmode="browse")
tree_1.grid(row=0, column=0, padx=0, pady=pady)
tree_1_scrollbar.config(command=tree_1.yview)

# treeview columns

tree_1["columns"] = ("id", "weight", "destination")
tree_1.column("#0", width=0, stretch=tk.NO)
tree_1.column("id", anchor=tk.E, width=40)
tree_1.column("weight", anchor=tk.W, width=80)
tree_1.column("destination", anchor=tk.W, width=200)

# treeview columns headings

tree_1.heading("#0", text="", anchor=tk.W)
tree_1.heading("id", text="Id", anchor=tk.CENTER)
tree_1.heading("weight", text="Weight", anchor=tk.CENTER)
tree_1.heading("destination", text="Destination", anchor=tk.CENTER)

# treeview tags

tree_1.tag_configure("oddrow", background=oddrow)
tree_1.tag_configure("evenrow", background=evenrow)

tree_1.bind("<ButtonRelease-1>", lambda event: edit_record(event, tree_1))

# labels and entries
labels_and_entries_frame1 = tk.Frame(labelframe1)
labels_and_entries_frame1.grid(row=1, column=0, padx=padx, pady=pady)

# id
id_label1 = tk.Label(labels_and_entries_frame1, text="Id")
id_label1.grid(row=0, column=0, padx=padx, pady=pady)
id_entry1 = tk.Entry(labels_and_entries_frame1, width=4)
id_entry1.grid(row=1, column=0, padx=padx, pady=pady)

# weight
weight_label1 = tk.Label(labels_and_entries_frame1, text="Weight")
weight_label1.grid(row=0, column=1, padx=padx, pady=pady)
weight_entry1 = tk.Entry(labels_and_entries_frame1, width=8)
weight_entry1.grid(row=1, column=1, padx=padx, pady=pady)

# destination
destination_label1 = tk.Label(labels_and_entries_frame1, text="Destination")
destination_label1.grid(row=0, column=2, padx=padx, pady=pady)
destination_entry1 = tk.Entry(labels_and_entries_frame1, width=20)
destination_entry1.grid(row=1, column=2, padx=padx, pady=pady)

# weather
weather_label1 = tk.Label(labels_and_entries_frame1, text="Weather")
weather_label1.grid(row=0, column=3, padx=padx, pady=pady)
weather_entry1 = tk.Entry(labels_and_entries_frame1, width=14)
weather_entry1.grid(row=1, column=3, padx=padx, pady=pady)

# buttons

buttons_frame1 = tk.Frame(labelframe1)
buttons_frame1.grid(row=2, column=0, padx=padx, pady=pady)

create_button = tk.Button(buttons_frame1, text="Create")
create_button.grid(row=0, column=0, padx=padx, pady=pady)

update_button = tk.Button(buttons_frame1, text="Update")
update_button.grid(row=0, column=1, padx=padx, pady=pady)

delete_button = tk.Button(buttons_frame1, text="Delete")
delete_button.grid(row=0, column=2, padx=padx, pady=pady)

clear_entry_boxes = tk.Button(buttons_frame1, text="Clear Entry Boxes", command=clear_all_entry_boxes)
clear_entry_boxes.grid(row=0, column=3, padx=padx, pady=pady)

read_table(tree_1)

if __name__ == "__main__":
    main_window.mainloop()
