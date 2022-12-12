import tkinter as tk


# Convert the gallons and miles to mpg
def calculate_gas(enter_gal, enter_mi, calc_mpg):
    gallons_used = float(enter_gal.get())
    miles_driven = float(enter_mi. get())
    miles_per_gallon = miles_driven / gallons_used
    calc_mpg["text"] = f"{round(miles_per_gallon, 2)} mpg"


def window_display():
    # Set up the window
    window = tk.Tk()
    window.title("Lab 12: Mileage GUI")
    window.resizable()

    # Create the miles & gallons entry frame with an Entry widget and label in it
    frm_entry = tk.Frame(master=window)
    lbl_temp = tk.Label(master=frm_entry, text='Enter the number of Gallons: ')
    lbl_temp2 = tk.Label(master=frm_entry, text='Enter the number of Miles: ')
    lbl_temp3 = tk.Label(master=frm_entry, text='Miles Per Gallon = ')
    ent_gallon = tk.Entry(master=frm_entry, width=7)
    ent_miles = tk.Entry(master=frm_entry, width=7)
    calc_result = tk.Label(master=frm_entry, text='mpg')

    # Create the conversion and quit Button
    btn_convert = tk.Button(
        master=frm_entry,
        text="Calculate MPG",
        command=lambda: calculate_gas(ent_gallon, ent_miles, calc_result)
    )
    btn_quit = tk.Button(
        master=frm_entry,
        text="Quit",
        command=lambda: quit()
    )

    # Set up the layout using the .grid() geometry manager
    frm_entry.grid(row=0, column=0)
    lbl_temp.grid(row=0, column=0)
    lbl_temp2.grid(row=1, column=0)
    lbl_temp3.grid(row=2, column=0)
    ent_gallon.grid(row=0, column=1)
    ent_miles.grid(row=1, column=1)
    calc_result.grid(row=2, column=1)
    btn_convert.grid(row=3, column=0)
    btn_quit.grid(row=3, column=1)

    # Run the application
    window.mainloop()


def main():
    window_display()


if __name__ == "__main__":
    main()
