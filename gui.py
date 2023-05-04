import pandas as pd
import tkinter as tk
from tkinter import ttk

def create_table(headers, data):
    df = pd.DataFrame(data, columns=headers)
    
    root = tk.Tk()
    root.title("Tabla de Datos")
    
    table = ttk.Treeview(root)
    
    table['columns'] = headers
    for header in headers:
        table.column(header, width=100)
        table.heading(header, text=header)
    
    for i, row in df.iterrows():
        table.insert('', i, text=str(i), values=tuple(row))
    
    table.pack(expand=True, fill='both')
    
    root.mainloop()
