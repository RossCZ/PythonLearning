from structural_rope_dynamic import run_simulation
from customtkinter import *
import customtkinter
import tkinter as tk

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


class RopeApp:
    def __init__(self):
        self.length = StringVar(value="100.0")
        self.step = StringVar(value="0.001")
        self.no_nodes = StringVar(value="50")
        self.k = StringVar(value="5e2")
        self.weight_per_length = StringVar(value="1.0")
        self.damping = StringVar(value="0.4")

    def get_settings(self):
        return {
            "step": float(self.step.get()),
            "length": float(self.length.get()),
            "no_nodes": int(self.no_nodes.get()),
            "k": float(self.k.get()),
            "g": -9.81,
            "weight_per_length": float(self.weight_per_length.get()),
            "damping": float(self.damping.get()),
        }

    def run(self):
        try:
            print(self.get_settings())
        except:
            tk.messagebox.showerror(title="Error", message="Wrong format!")
        run_simulation(self.get_settings())


# Create the main application window
root = CTk()
root.geometry("300x500")
root.title("Structural rope")

# Create control elements and bind them to settings class
rope_app = RopeApp()
CTkLabel(master=root, text="Settings", font=CTkFont(size=18, weight="bold")).pack(pady=10)

frame = CTkFrame(master=root)
frame.pack(pady=10, padx=30, fill="both", expand=True)

CTkLabel(master=frame, text="Step [s]").pack()
CTkEntry(master=frame, textvariable=rope_app.step).pack()

CTkLabel(master=frame, text="Length [m]").pack()
CTkEntry(master=frame, textvariable=rope_app.length).pack()

CTkLabel(master=frame, text="Nodes [-]").pack()
CTkEntry(master=frame, textvariable=rope_app.no_nodes).pack()

CTkLabel(master=frame, text="Stiffness K [N/m]").pack()
CTkEntry(master=frame, textvariable=rope_app.k).pack()

CTkLabel(master=frame, text="Weight per unit length [kg/m]").pack()
CTkEntry(master=frame, textvariable=rope_app.weight_per_length).pack()

CTkLabel(master=frame, text="Damping [kg/s]").pack()
CTkEntry(master=frame, textvariable=rope_app.damping).pack()

CTkButton(master=root, text="Run", command=rope_app.run).pack(pady=10)

# Start the application main loop
root.mainloop()
