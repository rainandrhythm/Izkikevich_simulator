#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 18:32:43 2026

@author: Allison
"""

import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# NEURON TYPES

neuron_names = [
    "Regular Spiking",
    "Intrinsically Bursting",
    "Chattering",
    "Fast Spiking",
    "Thalamocortical",
    "Resonator",
    "Low-Threshold Spiking"
]

a_values = [0.02, 0.02, 0.02, 0.1, 0.02, 0.1, 0.02]
b_values = [0.2, 0.2, 0.2, 0.2, 0.25, 0.26, 0.25]
c_values = [-65, -55, -50, -65, -65, -65, -65]
d_values = [8, 4, 2, 2, 0.05, 2, 2]

# SIMULATION

def simulate_neuron(a, b, c, d, I, duration=200, dt=0.1):

    time = np.arange(0, duration, dt)

    v = np.zeros(len(time))
    u = np.zeros(len(time))

    v[0] = -65
    u[0] = b * v[0]

    spike_times = []

    for i in range(len(time) - 1):

        dv = (0.04 * v[i]**2 + 5 * v[i] + 140 - u[i] + I)

        du = a * (b * v[i] - u[i])

        v[i + 1] = v[i] + dv * dt
        u[i + 1] = u[i] + du * dt

        if v[i + 1] >= 30:

            spike_times.append(time[i + 1])

            v[i + 1] = c
            u[i + 1] = u[i + 1] + d

    return time, v, spike_times

def run_simulation():

    # Get selected neuron
    neuron_number = neuron_names.index(neuron_var.get())

    # Get input current
    I = I_var.get()

    # Run simulation
    time, voltage, spikes = simulate_neuron(
        a_values[neuron_number],
        b_values[neuron_number],
        c_values[neuron_number],
        d_values[neuron_number],
        I
    )

    # Update plot
    ax.clear()
    ax.plot(time, voltage)

    ax.set_xlabel("Time (ms)")
    ax.set_ylabel("Membrane potential (mV)")
    ax.set_title(neuron_names[neuron_number])

    canvas.draw()

    # Calculate firing rate
    firing_rate = len(spikes) / (200 / 1000)

    firing_rate_label.config(
        text=f"Firing Rate: {firing_rate:.2f} Hz"
    )
    
root = tk.Tk()
root.title("Izhikevich Playground")
root.geometry("900x700")

# Background
background = Image.open("images/background.jpg")

background_label = tk.Label(root)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


def resize_background(event):
    
    # Get current window size
    width = event.width
    height = event.height
    
    # Resize background to match window
    resized_background = background.resize((width, height))
    
    # Create new Tkinter image
    background_image = ImageTk.PhotoImage(resized_background, master=root)
    
    # Update background
    background_label.config(image=background_image)
    
    # Keep reference so image doesn't disappear
    background_label.image = background_image

# Resize background whenever window size changes
root.bind("<Configure>", resize_background)

# Top section
top_frame = tk.Frame(root)
top_frame.pack(pady=10)

# Action potential image
image = Image.open("images/cat_potential.jpg")
image = image.resize((200, 150))

cat_potential_image = ImageTk.PhotoImage(image, master=root)

image_label = tk.Label(top_frame, image=cat_potential_image)
image_label.pack(side="left", padx=20)

# Controls
control_frame = tk.Frame(top_frame)
control_frame.pack(side="left", padx=20)

neuron_var = tk.StringVar()
neuron_var.set(neuron_names[0])

ttk.Label(
    control_frame,
    text="Neuron Type"
).pack()

neuron_dropdown = ttk.Combobox(
    control_frame,
    textvariable=neuron_var,
    values=neuron_names,
    state="readonly"
)

neuron_dropdown.pack()

ttk.Label(
    control_frame,
    text="Input current (I):"
).pack()

I_var = tk.DoubleVar(value=10)

I_entry = ttk.Entry(
    control_frame,
    textvariable=I_var
)

I_entry.pack()

run_button = ttk.Button(
    control_frame,
    text="Run",
    command=run_simulation
)

run_button.pack()

# Graph section
graph_frame = tk.Frame(root, bg="white", padx=10, pady=10)
graph_frame.pack(pady=20)
graph_frame.pack(pady=20)

fig, ax = plt.subplots(figsize=(8, 4))

canvas = FigureCanvasTkAgg(fig, master=graph_frame)
canvas.get_tk_widget().pack()

firing_rate_label = ttk.Label(
    graph_frame,
    text="Firing Rate: -- Hz"
)
firing_rate_label.pack(pady=5)

root.mainloop()
