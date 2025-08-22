import curses
from ui import run_ui

def main():
    curses.wrapper(run_ui)

if __name__ == "__main__":
    main()
