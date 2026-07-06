import tkinter as tk
from tkinter import ttk
import math

# الثوابت
GRADES = {"S235JR": 0.02466, "API X42/52": 0.02467, "API X60/70": 0.02468}
STDS = {"API 5L": (13.0, 1.6, 5.0), "EN 10219": (10.0, 2.0, 6.0), "DIN 2458": (10.0, 2.0, 6.0)}

def calculate():
    try:
        D, t, L = float(e1.get()), float(e2.get()), float(e3.get())
        Ws, V = float(e4.get()), float(e5.get())
        
        factor = GRADES[c1.get()]; d_tol, end_tol, end_c_tol = STDS[c2.get()]
        
        mod_D = D + (t * 2); circ = math.pi * mod_D; cos_a = Ws / circ
        alpha = math.degrees(math.acos(cos_a))
        weight = ((D - t) * t * factor * L) / 1000
        strip_len = (1 / cos_a) * L
        strip_per_meter = 1 / cos_a
        weld_width = t + 4
        cap_height = t * 0.8
        
        # التنسيق: كل نتيجة في سطر مستقل
        res = f"Angle: {alpha:.2f} Degrees\n"
        res += f"Weight: {weight:.3f} Tons\n"
        res += f"Strip/m: {strip_per_meter:.3f} m\n"
        res += f"Total Strip: {strip_len:.2f} m\n"
        res += f"Weld Width: {weld_width:.1f} mm\n"
        res += f"Cap Height: {cap_height:.1f} mm\n\n"
        res += f"--- QUALITY LIMITS ---\n"
        res += f"Body OD: {D-d_tol:.1f} to {D+d_tol:.1f}\n"
        res += f"End OD: {D-end_tol:.1f} to {D+end_tol:.1f}\n"
        res += f"End Circ: {circ-end_c_tol:.1f} to {circ+end_c_tol:.1f}"
        
        txt.config(state='normal'); txt.delete(1.0, tk.END); txt.insert(tk.END, res); txt.config(state='disabled')
    except:
        txt.config(state='normal'); txt.delete(1.0, tk.END); txt.insert(tk.END, "Check Inputs!"); txt.config(state='disabled')

root = tk.Tk(); root.title("Khorshed SPM Tech"); root.configure(bg="#2e2e2e")

# العنوان الزخرفي (ذهبي)
title_lbl = tk.Label(root, text="★ KHORSHED SPM TECH ★", font=("Helvetica", 14, "bold"), 
                     bg="#2e2e2e", fg="#FFD700") # Gold Color
title_lbl.pack(pady=10)

labels = ["OD (mm)", "Thickness", "Length (m)", "Width (mm)", "Speed (m/min)"]
entries = []
for i, l in enumerate(labels):
    ttk.Label(root, text=l, background="#2e2e2e", foreground="white").pack(pady=(2, 0))
    e = ttk.Entry(root, width=30); e.pack(pady=2); entries.append(e)
e1, e2, e3, e4, e5 = entries

c1 = ttk.Combobox(root, values=list(GRADES.keys()), width=28); c1.pack(pady=5); c1.set("S235JR")
c2 = ttk.Combobox(root, values=list(STDS.keys()), width=28); c2.pack(pady=5); c2.set("API 5L")

tk.Button(root, text="CALCULATE", command=calculate, bg="#007acc", fg="white", 
          font=("Arial", 10, "bold"), relief="raised").pack(pady=15, fill='x', padx=20)

# مربع النتائج متناسب مع الحجم
txt = tk.Text(root, height=12, width=30, font=("Helvetica", 10), bg="#1e1e1e", fg="#FFFFFF", state='disabled')
txt.pack(pady=10, padx=20, fill='both', expand=True)

root.mainloop()
