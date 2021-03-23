import tkinter as tk
import svm_gui

window = tk.Tk()
window.title("Micro:bit Temperature Predictor")
error_or_output_label = tk.Label()
window.configure(bg="#161616")
window.geometry("550x450")
window.iconbitmap("")

tk.Label(window, text="File that contains the temperature data of your micro:bit", bg="#161616", fg="#f7f7f7", font="none 12 bold").grid(row=0, column=0, sticky=tk.W)
file_name = tk.Entry(window, width=20, bg="#191919", fg="#f7f7f7")
file_name.grid(row=1, column=0, sticky=tk.W)

tk.Label(window, text="Delimiter used", bg="#161616", fg="#f7f7f7", font="none 12 bold").grid(row=2, column=0, sticky=tk.W)
delimiter = tk.Entry(window, width=20, bg="#191919", fg="#f7f7f7")
delimiter.grid(row=3, column=0, sticky=tk.W)

tk.Label(window, text="Name of the y column", bg="#161616", fg="#f7f7f7", font="none 12 bold").grid(row=4, column=0, sticky=tk.W)
predict = tk.Entry(window, width=20, bg="#191919", fg="#f7f7f7")
predict.grid(row=5, column=0, sticky=tk.W)


# https://stackoverflow.com/questions/6920302/how-to-pass-arguments-to-a-button-command-in-tkinter
tk.Button(window, text="Submit", width=6, bg="#161616", fg="#f7f7f7", 
command=lambda: svm_gui.svm_gui(window, file_name.get(), delimiter.get(), predict.get(), error_or_output_label)
).grid(row=9, column=0, stick=tk.SW, pady=9)

window.mainloop()