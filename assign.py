import tkinter as tk
from tkinter import ttk, messagebox

students = []
deleted_stack = []   # Stack for undo delete

def add_student():
    student = {
        "id": id_entry.get(),
        "name": name_entry.get(),
        "program": program_entry.get(),
        "year": year_entry.get()
    }
    students.append(student)
    display_students()

def search_student():
    sid = id_entry.get()
    for s in students:
        if s["id"] == sid:
            messagebox.showinfo("Found", f"Student: {s['name']}")
            return
    messagebox.showerror("Error", "Student not found")

def update_student():
    sid = id_entry.get()
    for s in students:
        if s["id"] == sid:
            s["name"] = name_entry.get()
            s["program"] = program_entry.get()
            s["year"] = year_entry.get()
            display_students()
            messagebox.showinfo("Success", "Student updated")
            return
    messagebox.showerror("Error", "Student not found")

def delete_student():
    sid = id_entry.get()
    for s in students:
        if s["id"] == sid:
            students.remove(s)
            deleted_stack.append(s)  # save to stack
            display_students()
            messagebox.showinfo("Deleted", "Student removed")
            return
    messagebox.showerror("Error", "Student not found")

def undo_delete():
    if deleted_stack:
        student = deleted_stack.pop()  # last deleted comes back
        students.append(student)
        display_students()
        messagebox.showinfo("Undo", "Last deleted student restored")
    else:
        messagebox.showerror("Error", "Nothing to undo")

def display_students():
    for row in table.get_children():
        table.delete(row)

    for s in students:
        table.insert("", "end", values=(s["id"], s["name"], s["program"], s["year"]))

# GUI
root = tk.Tk()
root.title("Student Record Management System")

tk.Label(root, text="Student ID").pack()
id_entry = tk.Entry(root)
id_entry.pack()

tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Program").pack()
program_entry = tk.Entry(root)
program_entry.pack()

tk.Label(root, text="Year").pack()
year_entry = tk.Entry(root)
year_entry.pack()

tk.Button(root, text="Add Student", command=add_student).pack()
tk.Button(root, text="Search Student", command=search_student).pack()
tk.Button(root, text="Update Student", command=update_student).pack()
tk.Button(root, text="Delete Student", command=delete_student).pack()
tk.Button(root, text="Undo Delete", command=undo_delete).pack()
tk.Button(root, text="Display All", command=display_students).pack()

table = ttk.Treeview(root, columns=("ID","Name","Program","Year"), show="headings")
table.heading("ID", text="ID")
table.heading("Name", text="Name")
table.heading("Program", text="Program")
table.heading("Year", text="Year")
table.pack()

root.mainloop()