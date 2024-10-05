import tkinter as tk
from tkinter import messagebox, Listbox, Scrollbar
import subprocess

class AppRemover:
    def __init__(self, master):
        self.master = master
        master.title("Unwanted App Remover")

        self.label = tk.Label(master, text="Select apps to remove:")
        self.label.pack()

        # Create a listbox with a scrollbar
        self.listbox = Listbox(master, selectmode=tk.MULTIPLE, width=50, height=15)
        self.listbox.pack(side=tk.LEFT)

        self.scrollbar = Scrollbar(master)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)

        # Load installed apps into the listbox
        self.load_installed_apps()

        # Create the remove button
        self.remove_button = tk.Button(master, text="Remove Selected Apps", command=self.remove_apps)
        self.remove_button.pack()

    def load_installed_apps(self):
        # Get the list of installed packages
        result = subprocess.run(['dpkg', '--get-selections'], capture_output=True, text=True)
        installed_apps = [line.split()[0] for line in result.stdout.splitlines() if 'deinstall' not in line]
        
        for app in installed_apps:
            self.listbox.insert(tk.END, app)

    def remove_apps(self):
        selected_apps = [self.listbox.get(i) for i in self.listbox.curselection()]
        if not selected_apps:
            messagebox.showwarning("No Selection", "No apps selected for removal.")
            return
        
        # Confirm removal
        confirm = messagebox.askyesno("Confirm Removal", f"Are you sure you want to remove: {', '.join(selected_apps)}?")
        if confirm:
            # Remove selected packages
            subprocess.run(['sudo', 'apt', 'remove', '--purge'] + selected_apps)
            subprocess.run(['sudo', 'apt', 'autoremove'])
            messagebox.showinfo("Success", f"Removed the following packages: {', '.join(selected_apps)}")
            self.listbox.delete(0, tk.END)  # Clear the listbox
            self.load_installed_apps()  # Reload the apps list

if __name__ == "__main__":
    root = tk.Tk()
    app = AppRemover(root)
    root.mainloop()
