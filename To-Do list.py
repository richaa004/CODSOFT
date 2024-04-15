import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import font as tkfont
from tkinter import ttk

class TodoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.root.geometry("400x400")


        # Define colors
        self.bg_color = "black"  # white background for the root window
        self.widget_bg_color = "grey"  # light blue background for widgets
        self.button_color = "cream"
        self.font_color = "#333333"

        # Set background color for root window
        self.root.configure(bg=self.bg_color)

        # Set custom font
        self.custom_font = tkfont.Font(family="Helvetica", size=12)

        # Create listbox to display tasks
        self.task_listbox = tk.Listbox(root, width=40, height=10, bg=self.widget_bg_color, font=self.custom_font)
        self.task_listbox.pack(pady=10)

        # Entry widget to enter new tasks
        self.new_task_entry = ttk.Entry(root, width=30, font=self.custom_font)
        self.new_task_entry.pack(pady=5)

        # Buttons to add and delete tasks
        self.add_task_btn = ttk.Button(root, text="Add Task", command=self.add_task)
        self.add_task_btn.pack(pady=5)

        self.delete_task_btn = ttk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_task_btn.pack(pady=5)

        # Additional buttons
        self.clear_all_btn = ttk.Button(root, text="Clear All Tasks", command=self.clear_all_tasks)
        self.clear_all_btn.pack(pady=5)

        self.mark_done_btn = ttk.Button(root, text="Mark as Done", command=self.mark_as_done)
        self.mark_done_btn.pack(pady=5)

        # Initialize tasks list
        self.tasks = []

    def add_task(self):
        new_task = self.new_task_entry.get()
        if new_task:
            self.tasks.append(new_task)
            self.task_listbox.insert(tk.END, new_task)
            self.new_task_entry.delete(0, tk.END)
            

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_index]
            self.task_listbox.delete(selected_index)
        except IndexError:
            messagebox.showinfo("Error", "Please select a task to delete.")

    def clear_all_tasks(self):
        self.task_listbox.delete(0, tk.END)
        self.tasks = []


    def mark_as_done(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            selected_task = self.tasks[selected_index]
            confirmed = messagebox.askyesno("Mark as Done", f"Mark '{selected_task}' as done?")
            if confirmed:
                self.task_listbox.delete(selected_index)
                del self.tasks[selected_index]
           
        except IndexError:
            messagebox.showinfo("Error", "Please select a task to mark as done.")


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()
