import tkinter as tk
from tkinter import messagebox

def calculate_discount():
    try:
        price = float(price_entry.get())
        discount_percent = float(discount_entry.get())

        # Apply discount only if it's 20% or more
        if discount_percent >= 20:
            final_price = price - (price * (discount_percent / 100))
            result_label.config(text=f"✅ Discount applied!\nFinal price: KES {final_price:,.2f}", fg="green")
        else:
            result_label.config(text=f"❌ No discount applied.\nPrice remains: KES {price:,.2f}", fg="red")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numeric values for price and discount.")

# Create main window
root = tk.Tk()
root.title("Kenyan Shilling Discount Calculator 🇰🇪")
root.geometry("450x350")
root.config(bg="#e0f7fa")  # Light blue background

# Title Label
title_label = tk.Label(root, text="🛒 Discount Calculator (KES)", font=("Arial", 18, "bold"), bg="#e0f7fa", fg="#00796b")
title_label.pack(pady=10)

# Price Input
tk.Label(root, text="Enter Original Price (KES):", font=("Arial", 12), bg="#e0f7fa").pack()
price_entry = tk.Entry(root, font=("Arial", 14), width=20)
price_entry.pack(pady=5)

# Discount Input
tk.Label(root, text="Enter Discount (%) :", font=("Arial", 12), bg="#e0f7fa").pack()
discount_entry = tk.Entry(root, font=("Arial", 14), width=20)
discount_entry.pack(pady=5)

# Calculate Button
calculate_button = tk.Button(root, text="Calculate Discount", font=("Arial", 14, "bold"), bg="#00796b", fg="white", command=calculate_discount)
calculate_button.pack(pady=15)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 14), bg="#e0f7fa")
result_label.pack(pady=10)

# Run the Tkinter loop
root.mainloop()
