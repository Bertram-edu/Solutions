import tkinter as tk
from tkinter import ttk

import danskcargo_data as dcd
import danskcargo_sql as dcsql

# region global constants
padx = 8
pady = 4
rowheight = 24
treeview_background = "#eeeeee"
treeview_foreground = "black"
treeview_selected = "#206030"
oddrow = "#dddddd"
evenrow = "#cccccc"

# endregion global constants

# region container functions

# endregion container functions

# region common functions

# endregion common functions

# region common widgets

main_window = tk.Tk()  # Define the main window
main_window.title('AspIT S2: DanskCargo')  # Text shown in the top window bar
main_window.geometry("500x500")  # window size

style = ttk.Style()
style.theme_use("default")


# Configure treeview colors and formatting. A treeview is an object that can contain a data table.
style.configure("Treeview", background=treeview_background, foreground=treeview_foreground, rowheight=rowheight, fieldbackground=treeview_background)
style.map('Treeview', background=[('selected', treeview_selected)])  # Define color of selected row in treeview

# endregion common widgets

# region container widgets

# Define Labelframe which contains all container related GUI objects (data table, labels, buttons, ...)
frame_container = tk.LabelFrame(main_window, text="Container")
frame_container.grid(row=0, column=0, padx=padx, pady=pady, sticky=tk.N)

tree_frame_container = tk.Frame(frame_container)
tree_frame_container.grid(row=0, column=0, padx=padx, pady=pady)
tree_scroll_container = tk.Scrollbar(tree_frame_container)
tree_scroll_container.grid(row=0, column=1, padx=0, pady=pady, sticky="ns")
tree_container = ttk.Treeview(tree_frame_container, yscrollcommand=tree_scroll_container.set, selectmode="browse")
tree_container.grid(row=0, column=0, padx=0, pady=pady)
tree_scroll_container.config(command=tree_container.yview)

# Define the data table's formatting and content
tree_container["columns"] = ("id", "weight", "destination")
tree_container.column("#0", width=0, stretch=tk.NO)
tree_container.column("id", anchor=tk.E, width=40)
tree_container.column("weight", anchor=tk.E, width=80)
tree_container.column("destination", anchor=tk.W, width=200)
tree_container.heading("#0", text="", anchor=tk.W)
tree_container.heading("id", text="Id", anchor=tk.CENTER)
tree_container.heading("weight", text="Weight", anchor=tk.CENTER)
tree_container.heading("destination", text="Destination", anchor=tk.CENTER)
tree_container.tag_configure("oddrow", background=oddrow)
tree_container.tag_configure("evenrow", background=evenrow)

# Define Frame which contains Labels entires and buttons
controls_frame_container = tk.Frame(frame_container)
controls_frame_container.grid(row=3, column=0, padx=padx, pady=pady)

# Define Frame which contains Labels (text fields) and entries (input fields)
edit_frame_container = tk.Frame(controls_frame_container)
edit_frame_container.grid(row=0, column=0, padx=padx, pady=pady)

# label and entry for container id
label_container_id = tk.Label(edit_frame_container, text="Id")
label_container_id.grid(row=0, column=0, padx=padx, pady=pady)
entry_container_id = tk.Entry(edit_frame_container, width=4, justify="right")
entry_container_id.grid(row=1, column=0, padx=padx, pady=pady)

# label and entry for container weight
label_container_weight = tk.Label(edit_frame_container, text="Weight")
label_container_weight.grid(row=0, column=1, padx=padx, pady=pady)
entry_container_weight = tk.Entry(edit_frame_container, width=8, justify="right")
entry_container_weight.grid(row=1, column=1, padx=padx, pady=pady)

# label and entry for container destination
label_container_destination = tk.Label(edit_frame_container, text="Destination")
label_container_destination.grid(row=0, column=2, padx=padx, pady=pady)
entry_container_destination = tk.Entry(edit_frame_container, width=20)
entry_container_destination.grid(row=1, column=2, padx=padx, pady=pady)

# label and entry for container wheater
label_container_weather = tk.Label(edit_frame_container, text="Weather")
label_container_weather.grid(row=0, column=3, padx=padx, pady=pady)
entry_container_weather = tk.Entry(edit_frame_container, width=14)
entry_container_weather.grid(row=1, column=3, padx=padx, pady=pady)

# Define Frame which contains buttons
button_frame_container = tk.Frame(controls_frame_container)
button_frame_container.grid(row=1, column=0, padx=padx, pady=pady)
# Define buttons
button_create_container = tk.Button(button_frame_container, text="Create")
button_create_container.grid(row=0, column=1, padx=padx, pady=pady)
button_update_container = tk.Button(button_frame_container, text="Update")
button_update_container.grid(row=0, column=2, padx=padx, pady=pady)
button_delete_container = tk.Button(button_frame_container, text="Delete")
button_delete_container.grid(row=0, column=3, padx=padx, pady=pady)
button_clear_boxes = tk.Button(button_frame_container, text="Clear Entry Boxes")
button_clear_boxes.grid(row=0, column=4, padx=padx, pady=pady)


# endregion container widgets

# region main program

if __name__ == "__main__":  # Executed when invoked directly. We use this so main_window.mainloop() does not keep our unit tests from running.
    main_window.mainloop()  # Wait for button clicks and act upon them

# endregion main program
