import tkinter as tk
from math import sqrt

class XPConverter:
    def __init__(self, master):
        self.master = master
        master.title("XP to Level Converter")
        master.configure(background="#EFDFCC")  # fondo claro

        # XP to Level Converter
        self.xp_frame = tk.Frame(master, bg="#EFDFCC")
        self.xp_frame.pack(padx=10, pady=10)
        self.xp_label = tk.Label(self.xp_frame, text="Enter XP:", font=("Arial", 12), fg="#333", bg="#BA8E7A")
        self.xp_label.pack(side=tk.LEFT)
        self.xp_entry = tk.Entry(self.xp_frame, width=10, font=("Arial", 12), fg="#333")
        self.xp_entry.pack(side=tk.LEFT)
        self.xp_to_level_btn = tk.Button(self.xp_frame, text="Convert XP to Level", font=("Arial", 12), fg="#333", bg="#66796B", command=self.xp_to_level)
        self.xp_to_level_btn.pack(side=tk.LEFT, padx=10)
        self.level_label = tk.Label(self.xp_frame, text="Level:", font=("Arial", 12), fg="#333", bg="#D7A184")
        self.level_label.pack(side=tk.LEFT)
        self.level_output = tk.Label(self.xp_frame, text="0", font=("Arial", 12), fg="#333", bg="#D7A184")
        self.level_output.pack(side=tk.LEFT)

        # Level to XP Converter
        self.level_frame = tk.Frame(master, bg="#EFDFCC")
        self.level_frame.pack(padx=10, pady=10)
        self.level_label = tk.Label(self.level_frame, text="Enter Level:", font=("Arial", 12), fg="#333", bg="#BA8E7A")
        self.level_label.pack(side=tk.LEFT)
        self.level_entry = tk.Entry(self.level_frame, width=10, font=("Arial", 12), fg="#333")
        self.level_entry.pack(side=tk.LEFT)
        self.level_to_xp_btn = tk.Button(self.level_frame, text="Convert Level to XP", font=("Arial", 12), fg="#333", bg="#66796B", command=self.level_to_xp)
        self.level_to_xp_btn.pack(side=tk.LEFT, padx=10)
        self.xp_label = tk.Label(self.level_frame, text="XP:", font=("Arial", 12), fg="#333", bg="#D7A184")
        self.xp_label.pack(side=tk.LEFT)
        self.xp_output = tk.Label(self.level_frame, text="0", font=("Arial", 12), fg="#333", bg="#D7A184")
        self.xp_output.pack(side=tk.LEFT)

    def xp_to_level(self):
        xp = float(self.xp_entry.get())
        if xp <= 0:
            level = 0.0
        elif xp <= 352:
            level = sqrt(xp + 9) - 3
        elif xp <= 1507:
            level = 8.1 + sqrt(0.4 * (xp - 195.975))
        else:
            level = (325/18) + sqrt((2/9) * (xp - (54215/72)))
        self.level_output.config(text=f"{level:.2f}")

    def level_to_xp(self):
        level = float(self.level_entry.get())
        if level <= 0:
            xp = 0.0
        elif level <= 16:
            xp = level**2 + 6 * level
        elif level <= 31:
            xp = 2.5 * level**2 - 40.5 * level + 360
        else:
            xp = 4.5 * level**2 - 162.5 * level + 2220
        self.xp_output.config(text=f"{xp:.2f}")

root = tk.Tk()
root.resizable(False, False)
root.config(bg="#EFDFCC")
my_gui = XPConverter(root)
root.mainloop()