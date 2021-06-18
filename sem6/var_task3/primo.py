# Реализация графического интерфейса и формы для приложения
# «Гостевая книга» с возможностью сохранения данных из полей формы в
# файл. Сформировать отчет по выполненной самостоятельной работе и
# опубликовать его в портфолио.
import tkinter as tk


def handle_submit(author_filed, text_field):
    author = author_filed.get()
    msg = text_field.get("1.0", "end-1c")
    with open("data.bd", "at") as file:
        file.write(f"{author}: {msg}\n")

    author_filed.delete(0, "end")
    text_field.delete("1.0", tk.END)


root = tk.Tk()
author_entry = tk.Entry(root)
text = tk.Text(root)
submit = tk.Button(root, text="Отправить", command=lambda: handle_submit(author_entry, text))

author_entry.pack()
text.pack()
submit.pack()

root.mainloop()
