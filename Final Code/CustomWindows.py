import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk
import DataLog as log


class DisplayWindow(tk.Tk):
    def __init__(self, title, detail):
        tk.Tk.__init__(self)
        self.title(title)
        self.title = title
        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()
        self.geometry('%sx%s' % (width, height))
        self.resizable(False, False)
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)

        button_frame = tk.Frame(self)
        button_frame.grid(row=0, column=0)
        button_frame.columnconfigure(0, weight=1)
        button_frame.columnconfigure(1, weight=1)

        text_frame = tk.Frame(self)
        text_frame.grid(row=1, column=0, padx=(1, 1), pady=(1, 1) ,sticky="nsew")
        text_frame.rowconfigure(0, weight=1)
        text_frame.columnconfigure(0, weight=1)

        ttk.Button(button_frame, text="Close", command=self.destroy).grid(row=0, column=0)
        ttk.Label(button_frame, text="Search: ").grid(row=0, column=1)
        self.E1 = ttk.Entry(button_frame)
        ttk.Button(button_frame, text="Go", command=self.start_search).grid(row=0, column=3)
        self.E1.grid(row=0, column=2)

        # scrolling text box for entire contents of files
        self.textbox = tk.Text(text_frame, height=6)
        self.textbox.insert("1.0", detail)
        self.textbox.config(state="normal")
        self.scrollb = tk.Scrollbar(text_frame, command=self.textbox.yview)
        self.textbox.config(yscrollcommand=self.scrollb.set)
        self.textbox.grid(row=0, column=0, sticky='nsew')
        self.scrollb.grid(row=0, column=1, sticky='nsew')
        self.resizable(True, True)
        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()
        self.geometry('%sx%s' % (width, height))
        self.mainloop()

    def start_search(self):
        target = self.E1.get()
        lower_target = target.lower()
        result = log.search(self.title, lower_target)
        if result == "Search not found. Please try again.":
            number = 0
        else:
            number = len(result)
        message = "Found {} results for {}".format(number, target)
        SearchResultBox("Search Result", message, result)
        
        
class SearchResultBox(tk.Toplevel):
    def __init__(self, title, message, detail):
        tk.Toplevel.__init__(self)
        self.title(title)
        self.title = title
        self.geometry('900x600')
        self.resizable(True, True)
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)

        button_frame = tk.Frame(self)
        button_frame.grid(row=0, column=0, columnspan=2, pady=(7, 7))
        button_frame.columnconfigure(0, weight=0)

        text_frame = tk.Frame(self)
        text_frame.grid(row=1, column=0, padx=(1, 1), pady=(1, 1) ,sticky="nsew")
        text_frame.rowconfigure(0, weight=1)
        text_frame.columnconfigure(0, weight=1)

        ttk.Label(button_frame, text=message).grid(row=0, column=0)
        ttk.Button(button_frame, text="OK", command=self.destroy).grid(row=1, column=0)
        
        self.textbox = tk.Text(text_frame, height=6)
        self.textbox.insert("1.0", detail)
        self.textbox.config(state="normal")
        self.scrollb = tk.Scrollbar(text_frame, command=self.textbox.yview)
        self.textbox.config(yscrollcommand=self.scrollb.set)
        self.textbox.config(yscrollcommand=self.scrollb.set)
        self.textbox.grid(row=0, column=0, sticky='nsew')
        self.scrollb.grid(row=0, column=1, sticky='nsew')
        self.resizable(True, True)
        self.geometry('900x600')
               
        self.mainloop()