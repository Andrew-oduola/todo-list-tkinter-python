import tkinter  as tk
from tkinter import messagebox, filedialog

class ToDoApp:
    def __init__(self, root) -> None:
        self.root = root
        self.root.title("Todo List App")
        self.root.geometry("400x400")

        # Title Label
        self.title_label = tk.Label(root, text="To-Do List", font=("Helcetica", 16))
        self.title_label.pack(pady=10)

        # Task Entry 
        self.task_entry = tk.Entry(root, width=35, font=("Helvatica", 14))
        self.task_entry.pack(pady=10)
        self.task_entry.bind("<Return>", self.add_task)

        # Add Task Button
        self.add_task_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_task_button.pack(pady=5)

        # Frame to hold the tasklist and it scrollbar
        self.task_listframe = tk.Frame(root)
        self.task_listframe.pack()

        # Task Listbox
        self.task_listbox = tk.Listbox(self.task_listframe, width=34, height=9, font=("Helvatica", 14))
        self.task_listbox.pack(pady=10, side=tk.LEFT)

        # Scrollbar for Listbox
        self.scrollbar = tk.Scrollbar(self.task_listframe)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)

        # Delete Button
        self.delete_task_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_task_button.pack(pady=5)

        # Menu bar setup
        self.menu = tk.Menu(root)
        root.config(menu=self.menu)

        # File Menu
        self.file_menu = tk.Menu(self.menu, tearoff=False)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Save Tasks", command=self.save_tasks)
        self.file_menu.add_command(label="Load Tasks", command=self.load_tasks)

        # File Menu
        self.help_menu = tk.Menu(self.menu, tearoff=False)
        self.menu.add_cascade(label="Help", menu=self.help_menu)
        self.help_menu.add_command(label="About", command=self.show_about)


    # Fucntion to add task
    def add_task(self, event=None):
        task = self.task_entry.get()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task")


    # Function to delete the selected task from the list
    def delete_task(self):
        try: 
            selected_task_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_task_index)
        except:
            messagebox.showwarning("Warning", "You must select a task to delete")


    # Function to save task to file
    def save_tasks(self):
        tasks = self.task_listbox.get(0, tk.END)
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", 
                                                 filetypes=[("Text Files", "*.txt")])
        
        if file_path:
            with open(file_path, 'w') as file:
                for task in tasks:
                    file.write(f"{task}\n")

    # Function to load tasks from a file
    def load_tasks(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, 'r') as file:
                tasks = file.readlines()
                self.task_listbox.delete(0, tk.END)
                for task in tasks:
                    self.task_listbox.insert(tk.END, task.strip())

    # Function to show about dialog
    def show_about(self):
        messagebox.showinfo("About", "To-Do List App\nCreated with Tkinter by Drex")





if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()