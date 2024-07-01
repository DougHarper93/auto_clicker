import tkinter as tk
import pyautogui
import threading
import time

class AutoClicker:
    def __init__(self, root):
        self.root = root
        self.root.title("Auto Clicker")
        self.root.geometry("300x200")

        self.running = False
        self.delay = tk.DoubleVar(value=1.0)

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Delay (seconds):").pack(pady=10)

        self.delay_entry = tk.Entry(self.root, textvariable=self.delay)
        self.delay_entry.pack(pady=5)

        self.start_button = tk.Button(self.root, text="Start", command=self.start_clicking)
        self.start_button.pack(pady=10)

        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_clicking, state='disabled')
        self.stop_button.pack(pady=10)

    def start_clicking(self):
        self.running = True
        self.start_button.config(state='disabled')
        self.stop_button.config(state='normal')
        threading.Thread(target=self.click).start()

    def stop_clicking(self):
        self.running = False
        self.start_button.config(state='normal')
        self.stop_button.config(state='disabled')

    def click(self):
        while self.running:
            pyautogui.click()
            time.sleep(self.delay.get())

if __name__ == "__main__":
    root = tk.Tk()
    app = AutoClicker(root)
    root.mainloop()
