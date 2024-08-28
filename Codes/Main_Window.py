import os
from tkinter import *
from tkinter import messagebox
from tkinter import PhotoImage
import sys
import Codes.Start_Threading
from Codes.Start_Sorting import *
from Codes.Start_Searching import *

# Main Window
class Window:
    def __init__(self, root):
        # Main Window
        self.root = root
        self.root.protocol("WM_DELETE_WINDOW", self.Close)

        # Full-Screen Window
        self.root.attributes('-fullscreen', True)
        self.root.config(bg="#282C34")

        # Title And Icon
        self.root.title("Algorithm Visualizer")
        try:
            # Using .png file as an icon
            img = PhotoImage(file=os.path.join(sys.path[0], "Images", "algorithm.png"))
            self.root.tk.call('wm', 'iconphoto', self.root._w, img)
        except Exception as e:
            print(f"Error setting icon: {e}")

        # Heading of the main window
        self.MainLabel = Label(self.root, text='Algorithm Visualizer', bg="#61AFEF", fg="#282C34",
                               font=("Arial", 28, "bold"))
        self.MainLabel.pack(pady=30)

        # Dictionary On types of Algorithms and their lists
        self.Algo = {'Searching': ['Linear Search', 'Binary Search'],
                     'Sorting': ['Selection Sort', 'Insertion Sort', 'Bubble Sort', 'Merge Sort', 'Quick Sort',
                                 'Heap Sort', 'Radix Sort'],
                    }

        # Dropdown menus configurations
        self.AlgoTypeVar = StringVar()
        self.AlgoNameVar = StringVar()
        self.AlgoTypeVar.trace('w', self.update_options)

        # Algorithm Type Dropdown
        self.AlgoTypeList = OptionMenu(self.root, self.AlgoTypeVar, *self.Algo.keys())
        self.AlgoTypeList.config(bg="#98C379", fg="#282C34", activebackground="#61AFEF", cursor="hand2",
                                 font=("Arial", 14), width=20)
        self.AlgoTypeVar.set("Select Algorithm Type")
        self.AlgoTypeList.pack(pady=10)

        # Algorithm Name Dropdown
        self.AlgoNameList = OptionMenu(self.root, self.AlgoNameVar, 'None')
        self.AlgoNameList.config(bg="#98C379", fg="#282C34", activebackground="#61AFEF", cursor="hand2",
                                 font=("Arial", 14), width=20)
        self.AlgoNameVar.set("Select Algorithm")
        self.AlgoNameList.pack(pady=10)

        # Next button
        self.NextButton = Button(self.root, text="Next >", bg="#E5C07B", fg="#282C34", activebackground="#D19A66",
                                 font=("Arial", 16, "bold"), command=self.Run1)
        self.NextButton.pack(pady=40)

    # For automatic update on the 2nd list if something is chosen on the 1st list
    def update_options(self, *args):
        algo_list = self.Algo.get(self.AlgoTypeVar.get(), ["None"])
        self.AlgoNameVar.set("Select Algorithm")
        menu = self.AlgoNameList['menu']
        menu.delete(0, 'end')
        for algo in algo_list:
            menu.add_command(label=algo, command=lambda x=algo: self.AlgoNameVar.set(x))

    # Exit button
    def Exit(self):
        self.root.destroy()

    # Close warning
    def Close(self):
        if messagebox.askokcancel("Exit", "Do you want to exit?"):
            self.root.destroy()
            exit()

    # For running the algorithms
    def Run2(self):
        if self.AlgoTypeVar.get() == "Sorting":
            # Create a new full-screen window for sorting algorithm
            sort_window = Toplevel(self.root)
            sort_window.attributes('-fullscreen', True)
            sort_window.config(bg="#282C34")
            Sorting(sort_window, self.AlgoNameVar.get())
            sort_window.mainloop()
        elif self.AlgoTypeVar.get() == "Searching":
            # Create a new full-screen window for searching algorithm
            search_window = Toplevel(self.root)
            search_window.attributes('-fullscreen', True)
            search_window.config(bg="#282C34")
            Searching(search_window, self.AlgoNameVar.get())
            search_window.mainloop()

    # For running the secondary window
    def Run1(self):
        if self.AlgoTypeVar.get() == "Select Algorithm Type":
            messagebox.showerror("Error!", "Please select Algorithm Type.")
        else:
            self.Run2()

# Driver Code
if __name__ == "__main__":
    root = Tk()
    app = Window(root)
    root.mainloop()
