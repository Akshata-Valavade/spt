import tkinter as tk
import time
import threading
import random
from PIL import ImageTk, Image


class TypeSpeedGUI:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Speed Typing Test")
        self.root.geometry("600x800")
        self.root.configure(bg="teal")
        img = Image.open("Screenshot (149).png")
        bg = ImageTk.PhotoImage(img)

        self.texts = open("test.txt", "r").read().split("\n")

        self.frame = tk.Frame(self.root)

        self.sample_label = tk.Label(self.root, text="            \t\t----Speed Typing Test----\t\t          ", font=("Times New Roman", 56), bg="orange", highlightthickness=5)
        self.sample_label.config(highlightbackground="white", highlightcolor="white")
        self.sample_label.place(x=0, y=0)

        self.sample_label = tk.Label(self.frame, image=bg, highlightthickness=2)
        self.sample_label.config(highlightbackground="black", highlightcolor="black")
        self.sample_label.place(x=0, y=0)

        self.sample_label = tk.Label(self.frame, text=random.choice(self.texts), font=("Times New Roman", 50),  fg="white", bg="purple", highlightthickness=5)
        self.sample_label.config(highlightbackground="black", highlightcolor="black")
        self.sample_label.grid(row=0, column=0, columnspan=2, padx=5, pady=10)

        self.input_entry = tk.Entry(self.frame, width=40, font=("Times New Roman", 45), highlightthickness=5)
        self.input_entry.grid(row=3, column=0, columnspan=2, padx=5, pady=10)
        self.input_entry.config(highlightbackground="brown", highlightcolor="brown")
        self.input_entry.bind("<KeyRelease>", self.start)

        self.speed_label = tk.Label(self.frame, text="Speed: \n0.00 CPS\t\t0.00 CPM\n0.00 WPS\t0.00 WPM", font=("Arial", 35), fg="dark blue", bg="cyan",  highlightthickness=5)
        self.speed_label.config(highlightbackground="black", highlightcolor="black")
        self.speed_label.grid(row=6, column=0, columnspan=2, padx=5, pady=10)

        self.reset_button = tk.Button(self.frame, text="Reset", command=self.reset, font=("Times New Roman", 30), bg="red", fg="white")
        self.reset_button.grid(row=9, column=0, columnspan=2, padx=5, pady=10)

        self.frame.pack(expand=True)

        self.counter = 0
        self.running = False

        self.root.mainloop()

    def start(self, event):
        if not self.running:
            if event.keycode not in [8, 16, 17, 18]:
                self.running = True
                t = threading.Thread(target=self.time_thread)
                t.start()
        if not self.sample_label.cget('text').startswith(self.input_entry.get()):
            self.input_entry.config(fg="red")
        else:
            self.input_entry.config(fg="black")
        if self.input_entry.get() == self.sample_label.cget('text'):
            self.running = False
            self.input_entry.config(fg="green")

    def time_thread(self):
        while self.running:
            time.sleep(0.1)
            self.counter += 0.1
            cps = len(self.input_entry.get()) / self.counter
            cpm = cps * 60
            wps = len(self.input_entry.get().split(" ")) / self.counter
            wpm = wps * 60
            self.speed_label.config(text=f"Speed: \n{cps:.2f} CPS\t\t{cpm:.2f} CPM\n{wps:.2f} WPS\t{wpm:.2f} WPM")

    def reset(self):
        self.running = False
        self.counter = 0
        self.speed_label.config(text="Speed: \n0.00 CPS\t\t0.00 CPM\n0.00 WPS\t0.00 WPM")
        self.sample_label.config(text=random.choice(self.texts))
        self.input_entry.delete(0, tk.END)


TypeSpeedGUI()
