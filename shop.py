import sqlite3 as sq
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

class Connect_db:
    def __init__(self, db_name):
        self.db_name = db_name
        self.con = sq.connect(self.db_name)
        self.cursor = self.con.cursor()

    def execute_sql(self, sql_text):
        try:
            self.sql_text = sql_text
            return self.cursor.execute(self.sql_text)
        except:
            messagebox.showerror("Ошибка!", "Невозможно получить данные")

    def close_sql(self):
        self.con.commit()
        self.cursor.close()
        self.con.close()


class My_window:
    def __init__(self):
        self.win = Tk()
        self.win.geometry('900x400')
        self.win.title('СТО')
        self.create_frames()
        self.win.mainloop()

    def create_frames(self):
        self.notebook = Notebook()

        style = Style()

        style.configure('TFrame0', background='lightblue')
        self.notebook.pack(expand=True, fill=BOTH)


        self.frame1 = Frame(self.notebook)
        self.frame2 = Frame(self.notebook)
        self.frame3 = Frame(self.notebook)

        self.frame1.pack(fill=BOTH, expand=True)
        self.frame2.pack(fill=BOTH, expand=True)
        self.frame3.pack(fill=BOTH, expand=True)

        self.notebook.add(self.frame1, text="Товары")
        self.notebook.add(self.frame2, text="Купить")
        self.notebook.add(self.frame3, text="Продать")

        self.tovar()
        self.buy()
        self.sell()

    def tovar(self):
        self.table_tov = Treeview(self.frame1, columns=['tovar', 'price'], show='headings')
        self.table_tov.heading('tovar', text='Товар')
        self.table_tov.heading('price', text='Цена')
        self.table_tov.column('tovar', width=150, anchor='c')
        self.table_tov.column('price', width=150, anchor='c')
        self.table_tov.place(x=10, y=10)

        self.tovar_name = StringVar()
        self.lb_name = Label(self.frame1, text='Наименование товара', font='Arial 12', background='lightblue')
        self.lb_name.place(x = 350, y = 20)

        self.entry_name = Entry(self.frame1, textvariable=self.tovar_name, font='Arial 12')
        self.entry_name.place(x=350, y = 60)

        self.tovar_price = DoubleVar()
        self.lb_name = Label(self.frame1, text='Цена товара', font='Arial 12', background='lightblue')
        self.lb_name.place(x = 350, y = 100)

        self.entry_price = Entry(self.frame1, textvariable=self.tovar_price, font='Arial 12')
        self.entry_price.place(x=350, y = 140)

        self.btn_new_tov = Button(self.frame1, text='Добавить новый товар')
        self.btn_new_tov.place(x=600, y=60)

        self.btn_delete_tov = Button(self.frame1, text='Удалить товар')
        self.btn_delete_tov.place(x=600, y=100)

        self.btn_update_tov = Button(self.frame1, text='Изменить товар')
        self.btn_update_tov.place(x=600, y=140)

    def buy(self):
        pass
    def sell(self):
        pass

new_win = My_window()
