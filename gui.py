import tkinter as tk
import svm_gui

# text = list("")
# def click(user_input, input_arr):
#     input_arr.clear()
#     for i in range(0, len(user_input)):
#         input_arr.append(user_input[i].get())
#         print(input_arr)

window = tk.Tk()
window.title("Micro:bit Temperature Predictor")
window.configure(bg="#161616")

tk.Label(window, text="file that contains the temperature data of your micro:bit:", bg="#161616", fg="#f7f7f7", font="none 12 bold").grid(row=0, column=0, sticky=tk.W)
file_name = tk.Entry(window, width=20, bg="#f7f7f7")
file_name.grid(row=1, column=0, sticky=tk.W)

tk.Label(window, text="Delimiter used:", bg="#161616", fg="#f7f7f7", font="none 12 bold").grid(row=2, column=0, sticky=tk.W)
delimiter = tk.Entry(window, width=20, bg="#f7f7f7")
delimiter.grid(row=3, column=0, sticky=tk.W)

tk.Label(window, text="Name of the y column:", bg="#161616", fg="#f7f7f7", font="none 12 bold").grid(row=4, column=0, sticky=tk.W)
predict = tk.Entry(window, width=20, bg="#f7f7f7")
predict.grid(row=5, column=0, sticky=tk.W)


# https://stackoverflow.com/questions/6920302/how-to-pass-arguments-to-a-button-command-in-tkinter
tk.Button(window,text="Submit", width=6,
command=lambda: svm_gui.svm_gui(window, file_name.get(), delimiter.get(), predict.get())).grid(row=7, column=0, sticky=tk.W) # click([file_name, delimiter, predict], text)"""

window.mainloop()