""" Opgave "GUI step 2":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Bruge det, du har lært i GUI-eksempelfilerne, og byg den GUI, der er afbildet i images/gui_2020.png

Genbrug din kode fra "GUI step 1".

GUI-strukturen bør være som følger:
    main window
        labelframe
            frame
                labels and entries
            frame
                buttons

Funktionalitet:
    Klik på knappen "clear entry boxes" sletter teksten i alle indtastningsfelter (entries).

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""

import tkinter as tk

main_window = tk.Tk()
main_window.title("my first GUI")
main_window.geometry("500x500")

padx = 8
pady = 4


def clear_all_entry_boxes():
    id_entry1.delete(0, tk.END)
    weight_entry1.delete(0, tk.END)
    destination_entry1.delete(0, tk.END)
    weather_entry1.delete(0, tk.END)


labelframe1 = tk.LabelFrame(main_window, padx=padx, pady=pady, text="Container")
labelframe1.grid(row=0, column=0, padx=padx, pady=pady)

# labels and entries
labels_and_entries_frame1 = tk.Frame(labelframe1)
labels_and_entries_frame1.grid(row=0, column=0, padx=padx, pady=pady)

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
buttons_frame1.grid(row=1, column=0, padx=padx, pady=pady)

create_button = tk.Button(buttons_frame1, text="Create")
create_button.grid(row=0, column=0, padx=padx, pady=pady)

update_button = tk.Button(buttons_frame1, text="Update")
update_button.grid(row=0, column=1, padx=padx, pady=pady)

delete_button = tk.Button(buttons_frame1, text="Delete")
delete_button.grid(row=0, column=2, padx=padx, pady=pady)

clear_entry_boxes = tk.Button(buttons_frame1, text="Clear Entry Boxes", command=clear_all_entry_boxes)
clear_entry_boxes.grid(row=0, column=3, padx=padx, pady=pady)



if __name__ == "__main__":
    main_window.mainloop()
