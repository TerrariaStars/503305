import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

root = tk.Tk()
root.title("Рисование параболы")
frame_graph = tk.Frame(root)
frame_graph.pack(side=tk.LEFT)
frame_sliders = tk.Frame(root)
frame_sliders.pack(side=tk.RIGHT)

fig = plt.Figure(figsize=(5, 5))
ax = fig.add_subplot(111)
canvas = FigureCanvasTkAgg(fig, master=frame_graph)
canvas.get_tk_widget().pack()
slider_a = tk.Scale(frame_sliders, orient=tk.HORIZONTAL, label="a", from_=-10, to=10, resolution=0.01)
slider_b = tk.Scale(frame_sliders, orient=tk.HORIZONTAL, label="b", from_=-25, to=25, resolution=0.01)
slider_c = tk.Scale(frame_sliders, orient=tk.HORIZONTAL, label="c", from_=-50, to=50, resolution=0.01)

slider_a.pack()
slider_b.pack()
slider_c.pack()

def update_graph(event):
    a = slider_a.get()
    b = slider_b.get()
    c = slider_c.get()
    
    ax.clear()
    ax.set_xlim(-100, 100)
    ax.set_ylim(-100, 100)
    x = np.linspace(-100, 100, 1000)
    y = a * x**2 + b * x + c
    ax.plot(x, y)
    canvas.draw()
    
slider_a.config(command=update_graph)
slider_b.config(command=update_graph)
slider_c.config(command=update_graph)
root.mainloop()
