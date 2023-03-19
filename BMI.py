import tkinter as tk

def calculate_bmi():
    height = float(height_entry.get())
    weight = float(weight_entry.get())
    bmi = weight / (height ** 2)
    result_label.config(text=f"BMI: {bmi:.2f}")

#Initialize window & set properties
root = tk.Tk()
root.title("BMI Calc")
root.configure(bg="#2596be")
root.resizable(False, False)

image_icon=tk.PhotoImage(file="icon.png")
root.iconphoto(False,image_icon)

logo = tk.PhotoImage(file='logo.png')
tk.Label(root, image=logo, bg='#2596be').place(x=200, y=140)

#set height
height_label = tk.Label(root, text="Height (m):", font='Exo', bg="#2596be")
height_label.grid(row=0, column=0, padx=10, pady=10)

height_entry = tk.Entry(root, bg="white")
height_entry.grid(row=0, column=1, padx=10, pady=10)

#set weight
weight_label = tk.Label(root, text="Weight (kg):", font='Exo', bg="#2596be")
weight_label.grid(row=1, column=0, padx=10, pady=10)

weight_entry = tk.Entry(root, bg="white")
weight_entry.grid(row=1, column=1, padx=10, pady=10)

#calculate button
calculate_button = tk.Button(root, text="Calculate", font= 'Exo', command=calculate_bmi, bg="#e28743", fg="white")
calculate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

result_label = tk.Label(root, text="", font='Exo', bg="#2596be")
result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
