import curses
import operations

menu = [
    "Addition (+)",
    "Subtraction (-)",
    "Multiplication (*)",
    "Division (/)",
    "Modulo (%)",
    "Floor Division (//)",
    "Power (x^y)",
    "Square Root (√x)",
    "Factorial (n!)",
    "Absolute Value (|x|)",
    "Exit"
]

def run_ui(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_CYAN)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)

    current_row = 0

    while True:
        stdscr.clear()
        h, w = stdscr.getmaxyx()

        title = "🧮 Python Calculator"
        stdscr.attron(curses.A_BOLD)
        stdscr.addstr(1, w//2 - len(title)//2, title)
        stdscr.attroff(curses.A_BOLD)

        for idx, row in enumerate(menu):
            x = w//2 - len(row)//2
            y = 3 + idx
            if idx == current_row:
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(y, x, row)
                stdscr.attroff(curses.color_pair(1))
            else:
                stdscr.attron(curses.color_pair(2))
                stdscr.addstr(y, x, row)
                stdscr.attroff(curses.color_pair(2))

        stdscr.refresh()
        key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(menu) - 1:
            current_row += 1
        elif key in [curses.KEY_ENTER, 10, 13]:
            if current_row == len(menu) - 1:
                break
            else:
                stdscr.clear()
                stdscr.addstr(2, 2, f"Selected: {menu[current_row]}")
                
                # Single-input operations
                single_input_ops = [7, 8, 9]  # sqrt, factorial, absolute
                if current_row in single_input_ops:
                    stdscr.addstr(4, 2, "Enter number: ")
                    curses.echo()
                    x = stdscr.getstr(4, 18, 10).decode("utf-8")
                    curses.noecho()

                    try:
                        x = float(x)
                        if current_row == 7: result = operations.sqrt(x)
                        elif current_row == 8: result = operations.factorial(x)
                        elif current_row == 9: result = operations.absolute(x)
                    except ValueError:
                        result = "❌ Invalid input!"
                
                else:
                    # Two-input operations
                    stdscr.addstr(4, 2, "Enter first number: ")
                    curses.echo()
                    x = stdscr.getstr(4, 25, 10).decode("utf-8")

                    stdscr.addstr(5, 2, "Enter second number: ")
                    y = stdscr.getstr(5, 26, 10).decode("utf-8")
                    curses.noecho()

                    try:
                        x, y = float(x), float(y)
                        if current_row == 0: result = operations.add(x, y)
                        elif current_row == 1: result = operations.sub(x, y)
                        elif current_row == 2: result = operations.mul(x, y)
                        elif current_row == 3: result = operations.div(x, y)
                        elif current_row == 4: result = operations.mod(x, y)
                        elif current_row == 5: result = operations.floordiv(x, y)
                        elif current_row == 6: result = operations.power(x, y)
                    except ValueError:
                        result = "❌ Invalid input!"

                stdscr.addstr(7, 2, f"✅ Result: {result}")
                stdscr.addstr(9, 2, "Press any key to return to menu...")
                stdscr.refresh()
                stdscr.getch()
