import tkinter as tk
from datetime import datetime, timedelta


class TimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Timer App")

        self.is_running = False
        self.start_time = None
        self.elapsed_time = timedelta()

        self.time_label = tk.Label(root, text="00:00:00", font=("Helvetica", 48))
        self.start_button = tk.Button(root, text="Start", command=self.start_timer, padx=20)
        self.stop_button = tk.Button(root, text="Stop", command=self.stop_timer, padx=20)
        self.reset_button = tk.Button(root, text="Reset", command=self.reset_timer, padx=20)

        self.time_label.grid(row=0, column=0, columnspan=3, pady=20)
        self.start_button.grid(row=1, column=0)
        self.stop_button.grid(row=1, column=1)
        self.reset_button.grid(row=1, column=2)

        self.update_display()

    def start_timer(self):
        if not self.is_running:
            self.is_running = True
            self.start_time = datetime.now() - self.elapsed_time
            self.update_timer()

    def stop_timer(self):
        if self.is_running:
            self.is_running = False

    def reset_timer(self):
        self.is_running = False
        self.elapsed_time = timedelta()
        self.update_display()

    def update_timer(self):
        if self.is_running:
            self.elapsed_time = datetime.now() - self.start_time
            self.update_display()
            self.root.after(1000, self.update_timer)

    def update_display(self):
        time_str = str(self.elapsed_time).split(".")[0]
        self.time_label.config(text=time_str)


if __name__ == "__main__":
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()
