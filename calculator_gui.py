import tkinter as tk
import operations  # import your existing math functions
import random

root = tk.Tk()
root.title("Pink Lily Calculator 🌸")
root.geometry("400x650")
root.config(bg="#ffe6f0")

current_input = ""   # current number being typed
operand1 = None      # first number
operator = None      # chosen operator
display_var = tk.StringVar()

# ---------------- DISPLAY ----------------
display = tk.Entry(root, textvariable=display_var,
                   font=("Comic Sans MS", 24), bd=8, relief="ridge",
                   justify="right", bg="white")
display.pack(pady=20, padx=10, fill="x")

# ---------------- FUNCTIONS ----------------
def press(key):
    """Handle digits and dot input"""
    global current_input
    current_input += str(key)
    display_var.set(current_input)

def set_operator(op):
    """Handle +, -, ×, ÷"""
    global operand1, operator, current_input
    if current_input != "":
        operand1 = float(current_input)
        operator = op
        current_input = ""  # clear for second number
        display_var.set("")  # don’t show operand1 op, just clear screen


def sci_function(func):
    """Handle scientific functions from operations.py"""
    global current_input
    try:
        num = float(current_input) if current_input != "" else float(display_var.get())

        if func == "sqrt": result = operations.sqrt(num)
        elif func == "pow": result = operations.pow(num, 2)   # default square
        elif func == "fac": result = operations.fac(int(num))
        elif func == "a_val": result = operations.a_val(num)

        elif func == "sin": result = operations.sin(num)
        elif func == "cos": result = operations.cos(num)
        elif func == "tan": result = operations.tan(num)

        elif func == "asin": result = operations.asin(num)
        elif func == "acos": result = operations.acos(num)
        elif func == "atan": result = operations.atan(num)

        elif func == "n_log": result = operations.n_log(num)
        elif func == "log": result = operations.log(num)
        elif func == "exp": result = operations.exp(num)

        else: result = "Err"

        display_var.set(result)
        current_input = str(result)

    except:
        display_var.set("Error")
        current_input = ""

def clear():
    """Reset everything"""
    global operand1, operator, current_input
    operand1, operator, current_input = None, None, ""
    display_var.set("")

def calculate():
    """Perform calculation using operations.py"""
    global operand1, operator, current_input
    if operand1 is not None and operator and current_input != "":
        operand2 = float(current_input)
        try:
            if operator == "+":
                result = operations.add(operand1, operand2)
            elif operator == "-":
                result = operations.sub(operand1, operand2)
            elif operator == "×":
                result = operations.mul(operand1, operand2)
            elif operator == "÷":
                result = operations.div(operand1, operand2)
            else:
                result = "Error"

            display_var.set(result)
            # Reset so result can be chained
            operand1, current_input, operator = result, "", None

        except Exception as e:
            display_var.set("Error")
            operand1, operator, current_input = None, None, ""

# ---------------- BUTTONS ----------------
btns_frame = tk.Frame(root, bg="#ffe6f0")
btns_frame.pack()

# scientific buttons
sci_buttons = [
    ["sqrt", "pow", "fac", "a_val"],
    ["sin", "cos", "tan"],
    ["asin", "acos", "atan"],
    ["n_log", "log", "exp"]
]

for row in sci_buttons:
    row_frame = tk.Frame(root, bg="#ffe6f0")
    row_frame.pack(pady=2)
    for btn in row:
        action = lambda x=btn: sci_function(x)
        tk.Button(row_frame, text=btn, font=("Comic Sans MS", 12, "bold"),
                  bg="#ffb3d9", fg="white", width=6, height=2,
                  command=action, relief="raised", bd=3).pack(side="left", padx=3)

# basic calculator buttons
buttons = [
    ["7", "8", "9", "÷"],
    ["4", "5", "6", "×"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
    ["CA"]
]

for row in buttons:
    row_frame = tk.Frame(btns_frame, bg="#ffe6f0")
    row_frame.pack(side="top", pady=5)
    for btn in row:
        if btn in ["+", "-", "×", "÷"]:
            action = lambda x=btn: set_operator(x)
        elif btn == "=":
            action = calculate
        elif btn == "CA":
            action = clear
        else:
            action = lambda x=btn: press(x)

        tk.Button(row_frame, text=btn, font=("Comic Sans MS", 18, "bold"),
                  bg="#ff99cc" if btn not in ["=", "CA"] else "#ff4d88",
                  fg="white", width=5, height=2, command=action,
                  relief="raised", bd=3).pack(side="left", padx=5)

# ---------------- LILY FLOWER ANIMATION 🌸 ----------------
canvas = tk.Canvas(root, width=400, height=100, bg="#ffe6f0", highlightthickness=0)
canvas.pack(fill="both", expand=True)

flowers = []
for _ in range(6):
    x, y = random.randint(10, 390), random.randint(10, 90)
    flower = canvas.create_text(x, y, text="🌸", font=("Arial", 18))
    flowers.append(flower)

def animate():
    for flower in flowers:
        canvas.move(flower, 0, 1)
        x, y = canvas.coords(flower)
        if y > 100:
            canvas.coords(flower, random.randint(10, 390), 0)
    root.after(100, animate)

animate()
root.mainloop()
