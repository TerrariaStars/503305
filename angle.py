import tkinter as tk
import math
def radian(event=None):
    radian = float(entry_1.get())
    entry.delete(0, tk.END)
    entry.insert(0, str(round(math.degrees(radian), 2)))
    draw_angle_deg()
def calculate_trigonometry(event=None):
    try:
        angle = float(entry.get())
        radians = math.radians(angle)
        if 89.99 < angle < 90.11:
            tangent = "-"
            cotangent = 0
            cosine = 0
            sine = 1
        elif 359.99 < angle < 359.999:
            tangent = 0
            cotangent = '-'
            cosine = 1
            sine = 0
        elif 359.9 < angle < 360:
            tangent = 0
            cotangent = '-'
            cosine = 1
            sine = 0
        elif 0 < angle < 0.11:
            tangent = 0
            cotangent = '-'
            cosine = 1
            sine = 0
        elif angle == 0:
            tangent = 0
            cotangent = '-'
            cosine = 1
            sine = 0
        elif 269.99 < angle < 270.11:
            tangent = '-'
            cotangent = 0
            cosine = 0
            sine = -1
        elif 179.99 < angle < 180.11:
            tangent = 0
            cotangent = '-'
            cosine = -1
            sine = 0

        else:
            cosine = round(math.cos(radians), 4)
            sine = round(math.sin(radians), 4)
            tangent = round(math.tan(radians), 4)
            cotangent = round(1 / tangent, 4)

        tangent_label.config(text=f"Тангенс: {tangent}", font=("Arial", 14, "bold"))
        cotangent_label.config(text=f"Котангенс: {cotangent}", font=("Arial", 14, "bold"))
        cosine_label.config(text=f"Косинус: {cosine}", font=("Arial", 14, "bold"))
        sine_label.config(text=f"Синус: {sine}", font=("Arial", 14, "bold"))
    except ZeroDivisionError:
        print('(')
def draw_angle_deg(event=None):
    draw_angle(float(entry.get()))
def draw_angle(angle_degrees):
    center_x = 200
    center_y = 200
    radius = 150

    angle_rad = math.radians(angle_degrees)
    x = center_x + radius * math.cos(angle_rad)
    y = center_y + radius * math.sin(angle_rad)

    entry.delete(0, tk.END)
    entry.insert(0, str(round(angle_degrees, 2)))
    entry_1.delete(0, tk.END)
    entry_1.insert(0, str(round(math.radians(angle_degrees), 4)))
    calculate_trigonometry()
    move_radius(x, y)
    move_angle_text(x, y, angle_degrees)

def get_angle(event):
    angle_degrees = ((math.degrees(math.atan2(event.y - 200, event.x - 200)) + 360) % 360)
    draw_angle(angle_degrees)


def move_radius(x, y):
    canvas.coords(radius, 200, 200, x, y)

def move_angle_text(x, y, angle):
    angle_text_x = x + 10
    angle_text_y = y - 10
    canvas.coords(angle_text, angle_text_x, angle_text_y)
    canvas.itemconfig(angle_text, text=f"{round(angle, 2)}°", font=("Arial", 12, "bold"))

root = tk.Tk()
root.title("Изменения тригонаметрических характеристик(by Terraria_Stars)")
root.geometry("640x500+100+100")

canvas = tk.Canvas(root, width=400, height=350)
canvas.pack()
canvas.create_oval(50, 50, 350, 350, outline="black", width=2)
canvas.create_line(200, 200, 350, 200, width=2)

entry = tk.Entry(root, width=10, font=("Arial", 16))
entry.pack(side="bottom")
entry.bind("<Return>", draw_angle_deg) 
label = tk.Label(root, text="Градусы", font=("Arial", 14, "bold"))
label.pack(side="bottom", padx=10, pady=10)

entry_1 = tk.Entry(root, width=10, font=("Arial", 16))
entry_1.pack(side="bottom")
entry_1.bind("<Return>", radian)
label = tk.Label(root, text="Радианы", font=("Arial", 14, "bold"))
label.pack(side="bottom", padx=10, pady=10)

tangent_label = tk.Label(root, text="Тангенс: ", font=("Arial", 14, "bold"))
tangent_label.place(x=10, y=10)

cotangent_label = tk.Label(root, text="Котангенс: ", font=("Arial", 14, "bold"))
cotangent_label.place(x=10, y=40)

cosine_label = tk.Label(root, text="Косинус: ", font=("Arial", 14, "bold"))
cosine_label.place(x=10, y=70)

sine_label = tk.Label(root, text="Синус: ", font=("Arial", 14, "bold"))
sine_label.place(x=10, y=100)
entry.pack(side='bottom')

radius = canvas.create_line(200, 200, 200, 200, width=2)
angle_text = canvas.create_text(200, 190, text="°", font=("Arial", 12, "bold"))

canvas.bind("<Motion>", get_angle)

root.mainloop()