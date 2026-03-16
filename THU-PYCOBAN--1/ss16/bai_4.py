import tkinter as tk
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
#KQ
display = tk.Entry(root, font=("Arial", 20), bd=10, relief="sunken", justify="right")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")
display.insert(0, "0")
buttons = [
    ['C', '√', 'x^y', '%'],
    ['1', '2', '3', '+'],
    ['4', '5', '6', '-'],
    ['7', '8', '9', '*'],
    ['0', '.', '=', '/']
]
#nút
for i, row in enumerate(buttons):
    for j, text in enumerate(row):
        btn = tk.Button(root, text=text, font=("Arial", 14), width=5, height=2)
        btn.grid(row=i+1, column=j, padx=5, pady=5, sticky="nsew")
#hàng
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)
root.mainloop()