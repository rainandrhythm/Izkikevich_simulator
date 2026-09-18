# Izkikevich_simulator

Interactive Python simulator of Izhikevich spiking neuron models to see how firing dynamics change across established neuron types and input currents. The simulator allows users to select different neuronal firing types, adjust the input current, and visualize the resulting membrane potential over time.

**Features**

Simulates 7 neuronal firing patterns

Adjustable input current

Generates membrane-potential (voltage) traces

Calculates neuronal firing rate

Interactive graphical interface built with Python

Custom artwork and visual design

**Established Neuron Types**

Regular Spiking

Intrinsically Bursting

Chattering

Fast Spiking

Thalamocortical

Resonator

Low-Threshold Spiking

Each firing pattern is generated using a different set of Izhikevich model parameters.

**The Izhikevich Model**

The Izhikevich model is a computational model of neuronal dynamics that combines the biological plausibility of more complex neuron models with relatively low computational cost.

The model describes membrane potential using:

[{dv}/{dt} = 0.04v^2 + 5v + 140 - u + I]

and a recovery variable:

[{du}/{dt} = a(bv-u)]

When the membrane potential reaches the spike threshold, the model resets according to:

[v --> c]

[u --> u+d]

The parameters a, b, c, and d control the recovery dynamics and reset behavior, allowing the model to reproduce a range of experimentally observed neuronal firing patterns.


**Technologies**

Python

NumPy — numerical computation

Matplotlib — voltage-trace visualization

Tkinter — graphical user interface

Pillow — image handling

Git/GitHub — version control and project sharing

**Purpose**

This project combines computational neuroscience with scientific programming and data visualization. It demonstrates my experience with:

Translating mathematical models of neuronal dynamics into Python

Implementing numerical simulations

Working with parameterized dynamical systems

Visualizing time-series neural data

Building an interactive scientific application

Communicating computational neuroscience concepts through an accessible interface

Future Development

**Future Work?**

Additional neuron models (e.g., Hodgkin-Huxley, Fitz-Hugh Nagumo, Wilson-Cowan, etc.)

Raster plots for populations of neurons

Firing-rate versus input-current (F-I) curves

Interactive parameter adjustment for a, b, c, and d

Additional measures of neuronal activity (e.g., bursting, synchrony, oscillatory power, etc.)
