import padding
import sorter
import tkinter as tk
import tkinter.filedialog as tkf

def print_choice_list(choices, window_name):
    """
    choices: a list with the choices to print
    window_name: the window on which you print the choices
    """
    variable = tk.StringVar(window_name)

    # Setting up the default value printed on the window
    variable.set(choices[0])

    w = tk.OptionMenu(window_name, variable, *choices)
    w.pack()

def ask_file_path():
    """
    Function that can be triggered (with a button for example) to
    select a file. Initial directory will be the current one
    """
    filetypes = (("Excel files", "*.xls"),
                 ("Csv files", "*.csv"),
                 ("All files", "*"))
    file_path = tkf.askopenfilename(filetypes = filetypes, initialdir="./")


def main():
    """
    main function
    """
    # Create the main window
    root = tk.Tk()
    root.geometry("700x350")
    
    # Basic title
    title = tk.Label(root, text="Welcome in this sorter program !", padx=10, pady=10)
    title.pack()

    # Create a button to browse files
    title = tk.Label(root, text="Choose file: ", padx=10, pady=10)
    title.pack()

    button = tk.Button(root, text="Browse", command=ask_file_path, padx=10, pady=10)
    button.pack()

    # Create a dropdown menu for selecting padding
    title = tk.Label(root, text="Choose your padding function below: ", padx=10, pady=10)
    title.pack()

    padding_choice = [name + " padding" for name in padding.define_paddings().keys()]
    print_choice_list(padding_choice, root)
    
    button = tk.Button(root, text="Run !", command=sorter.main, padx=10, pady=10)   
    button.pack()

    root.mainloop()


if __name__ == "__main__":
    main()
