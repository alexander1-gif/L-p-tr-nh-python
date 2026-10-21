import tkinter as tk
from tkinter import messagebox

cua_so = tk.Tk()
cua_so.title("Máy tính bỏ túi")
cua_so.geometry("350x500")
cua_so.resizable(False, False)

man_hinh = tk.Entry(
    cua_so,
    font=("Arial", 24),
    justify="right",
    bd=5,
    relief="sunken"
)
man_hinh.grid(
    row=0,
    column=0,
    columnspan=4,
    padx=10,
    pady=20,
    ipady=10
)

def them_ky_tu(ky_tu):
    man_hinh.insert(tk.END, ky_tu)

def tinh():
    try:
        bieu_thuc = man_hinh.get()

        # Chỉ cho phép các ký tự cần thiết
        ky_tu_hop_le = "0123456789+-*/.() "

        if not all(ky_tu in ky_tu_hop_le for ky_tu in bieu_thuc):
            raise ValueError

        ket_qua = eval(bieu_thuc)

        man_hinh.delete(0, tk.END)
        man_hinh.insert(0, str(ket_qua))

    except:
        messagebox.showerror("Lỗi", "Biểu thức không hợp lệ!")

def xoa():
    man_hinh.delete(0, tk.END)

cac_nut = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3)
]

for (ten_nut, hang, cot) in cac_nut:

    if ten_nut == "=":
        lenh = tinh
    else:
        lenh = lambda x=ten_nut: them_ky_tu(x)

    tk.Button(
        cua_so,
        text=ten_nut,
        font=("Arial", 18),
        width=5,
        height=2,
        command=lenh
    ).grid(
        row=hang,
        column=cot,
        padx=5,
        pady=5
    )

tk.Button(
    cua_so,
    text="C",
    font=("Arial", 18),
    width=22,
    height=2,
    command=xoa
).grid(
    row=5,
    column=0,
    columnspan=4,
    padx=5,
    pady=10
)

# Chạy chương trình
cua_so.mainloop()