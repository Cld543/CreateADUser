import tkinter as tk
from tkinter import ttk
import ldap3

root = tk.Tk()
root.title = 'Create AD User'

userType = ''
labelUserType = tk.Label(root, text='User Type:')

labelUserType.grid(row= 0, column= 0, pady= 2, padx= 2)

root.mainloop()