import tkinter as tk

def on_click(event):
    text = event.widget.cget("text")
    if text == "=":
        calculate_result()
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

def calculate_result():
    try:
        expr = entry.get()
        expr = expr.replace(',', '.')
        result = eval(expr)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

root = tk.Tk()
root.title("Calculator")
root.geometry("500x500")
root.resizable(False, False) 
root.configure(bg='#fcd4f8') 

entry = tk.Entry(root, width=34, font=("Arial", 18), bd=10, insertwidth=2, justify='right', bg='white')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="we")

root.bind('<Return>', lambda event: calculate_result())

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '(', ')', '+',
    '0', '.', '='
]

row = 1
col = 0
for button_text in buttons:
    button = tk.Button(root, text=button_text, width=8, height=3, font=("Arial", 12), bg='#FF69B4', fg='white', activebackground='#FF1493', activeforeground='white')
    button.grid(row=row, column=col, padx=5, pady=5)
    button.bind("<Button-1>", on_click)
    col += 1
    if col > 3:
        col = 0
        row += 1

footer = tk.Label(root, text="Игнатчик Ульяна Сергеева, 3 курс, 11 группа, 2024", 
                  font=("Arial", 12, "italic"), bg='white', fg='#FF69B4')
footer.grid(row=row+1, column=0, columnspan=4, pady=20, sticky="s")

root.mainloop()