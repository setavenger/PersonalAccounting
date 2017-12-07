from tkinter import *
import datetime
from tkinter import ttk
import sqlite3 as sql
# root Window

root = Tk()


# def createtable():
#    conn = sql.connect('Money')
#    c = conn.cursor()
#    c.execute("CREATE TABLE IF NOT EXISTS accounttest (value REAL, keyword TEXT)")

class App:
    def __init__(self, master):
        self.master = master
#        master.geometry('800x600')
        master.title("Project X")

        self.label_0 = Label(master, text="User")
        self.label_0.pack()

        self.date = Label(master, text=datetime.date.today())
        self.date.pack()

        self.tree = ttk.Treeview(master, columns=('Transaction', 'Value', 'Instance', 'Comments'))
        self.tree.heading('#0', text="Transaction Number")
        self.tree.heading('#1', text='Value')
        self.tree.heading('#2', text='Instance')
        self.tree.heading('#3', text="Comment")
        self.tree.heading('#4', text='Dates')
        self.tree.column('#1', stretch=TRUE)
        self.tree.column('#2', stretch=TRUE)
        self.tree.column('#0', stretch=TRUE)
        self.tree.column('#3', stretch=TRUE)
        self.tree.pack(fill=Y)
        self.tree['height'] = 15
        self.treeview = self.tree

        self.update_button = Button(master, pady=3, text="Update Table", command=self.update_table)
        self.update_button.pack()
        self.show_instancebutton = Button(master, pady=3, text="select Instance", command=self.show_instance)
        self.show_instancebutton.pack()

        self.get_data()
        self.tree.column("#0", anchor=E)
        self.tree.column("#1", anchor=E)
        self.tree.column("#2", anchor=E)
        self.tree.column("#3", anchor=E)
        self.tree.column("#4", anchor=E)

        # Setup Menu

        self.menu = Menu(master, tearoff=0)
        master.config(menu=self.menu)
        self.subMenu_0 = Menu(self.menu)
        self.menu.add_cascade(label="File", menu=self.subMenu_0)
        self.subMenu_0.add_command(label="Add a Transaction", command=self.popup)
        self.subMenu_0.add_command(label="Quit", command=root.destroy)
        self.subMenu_0.add_command(label="Useless?", command=self.donothing)

        self.subMenu_1 = Menu(self.menu)
        self.menu.add_cascade(label="Input", menu=self.subMenu_1)
        self.subMenu_1.add_command(label="Name", command=self.account)

        self.show_balance = Button(master, pady=3, text="Show total Balance", command=self.show_totalBalance)
        self.show_balance.pack()

    def rootlayoutchanges(self):
        self.label_0.config(text=str(self.firstname + " " + str(self.lastname)))

    def donothing(self):
        top = Toplevel()
        top.title("Hihi")
        label_0 = Label(top, text="Told ya nothing would happen or have I...")
        label_0.pack()
        button = Button(top, text="Dismiss", command=top.destroy)
        button.pack()

    def account(self):
        self.top = Toplevel()
        self.top.title("About You")

        Label(self.top, text="First Name").grid(row=0)
        Label(self.top, text="Last Name").grid(row=1)

        self.e0 = Entry(self.top)
        self.e1 = Entry(self.top)

        self.e0.grid(row=0, column=1)
        self.e1.grid(row=1, column=1)

        Dismissbutton = Button(self.top, text="Dismiss", command=self.top.destroy)
        Dismissbutton.grid(row=3, column=1)

        ConfirmButton = Button(self.top, text="Confirm", command=self.get_input)
        ConfirmButton.grid(row=3, column=0)

    def get_input(self):
        self.firstname = self.e0.get()
        self.lastname = self.e1.get()
        self.top.destroy()
        self.greetings()
        self.rootlayoutchanges()

    def greetings(self):
        top = Toplevel()
        top.title("Greetings")

        label_0 = Label(top, text="Hello" + " " + str(self.firstname) + " " + str(self.lastname) + ", nice to see you")
        label_0.pack()

        button = Button(top, text="Dismiss", command=top.destroy)
        button.pack()

    def popup(self):
        #create widgets

        top = Toplevel()
        self.entervalue = Entry(top)
        self.entercomment = Entry(top)
        self.enterDate = Entry(top)
        label = Label(top, text="Insert Value")
        label1 = Label(top, text="Add comment")
        label2 = Label(top, text="Enter Date")
        FSbutton = Button(top, text="FS", command=self.insertFS)
        parentsbutton = Button(top, text="parents", command=self.insertparents)
        mebutton = Button(top, text="Kfw", command=self.insertkfw)

        #place widgets
        self.entervalue.grid(row=1,column=2, columnspan=2)
        self.entercomment.grid(row=2, column=2, columnspan=2)
        self.enterDate.grid(row=3, column=2, columnspan=2)
        label.grid(row=1, column=1)
        label1.grid(row=2, column=1)
        label2.grid(row=3, column=1)
        FSbutton.grid(row=4, column=1, ipadx=20)
        parentsbutton.grid(row=4, column=2, ipadx=5)
        mebutton.grid(row=4, column=3, ipadx=17)

    def insertFS(self):
        conn = sql.connect("/Users/setor/PycharmProjects/Project_X/Optimizing")
        c = conn.cursor()
        c.execute('PRAGMA FOREIGN_KEYS = ON')
        conn.commit()

        keyword = "FS"
        comment = self.entercomment.get()
        value = self.entervalue.get()
        Dates = self.enterDate.get()
        c.execute("INSERT INTO Accounting (value, keyword, comment, Dates) VALUES (?, ?, ?, ?)",
                  (value, keyword, comment, Dates))
        conn.commit()
        c.close()
        conn.close()

    def insertparents(self):
        conn = sql.connect("/Users/setor/PycharmProjects/Project_X/Optimizing")
        c = conn.cursor()
        c.execute('PRAGMA FOREIGN_KEYS = ON')
        conn.commit()

        keyword = "parents"
        comment = self.entercomment.get()
        value = self.entervalue.get()
        Dates = self.enterDate.get()
        c.execute("INSERT INTO Accounting (value, keyword, comment, Dates) VALUES (?, ?, ?, ?)",
                  (value, keyword, comment, Dates))
        conn.commit()
        c.close()
        conn.close()

    def insertkfw(self):
        conn = sql.connect("/Users/setor/PycharmProjects/Project_X/Optimizing")
        c = conn.cursor()
        c.execute('PRAGMA FOREIGN_KEYS = ON')
        conn.commit()

        keyword = "Kfw"
        comment = self.entercomment.get()
        value_0 = self.entervalue.get()
        value = round(float(value_0), 2)
        Dates = self.enterDate.get()
        c.execute("INSERT INTO Accounting (value, keyword, comment, Dates) VALUES (?, ?, ?, ?)",
                  (value, keyword, comment, Dates))
        conn.commit()
        c.close()
        conn.close()

    def get_data(self):

        conn = sql.connect('/Users/setor/PycharmProjects/Project_X/Optimizing')
        c = conn.cursor()
        c.execute('SELECT * FROM Accounting')
        data = c.fetchall()
        for row in data:
            self.treeview.insert("", "end", text="Trans_" + str(row[0]), values=(str(row[1])+"€",
                                                                                 row[2], row[3], row[4]))
        c.close()
        conn.close()

    def update_table(self):
        self.tree.delete(*self.tree.get_children())
        conn = sql.connect('/Users/setor/PycharmProjects/Project_X/Optimizing')
        c = conn.cursor()
        c.execute('SELECT * FROM Accounting')
        data = c.fetchall()
        for row in data:
            self.treeview.insert('', 'end', text="Trans_" + str(row[0]), values=(str(row[1])+"€",
                                                                                 row[2], row[3], row[4]))

        c.close()
        conn.close()

    def show_instance(self):
        top = Toplevel()
        label = Label(top, text="Which instance would you like to view?")
        button0 = Button(top, text="FS", command=self.get_FS)
        button1 = Button(top, text="parents", command=self.get_parents)
        button2 = Button(top, text="Kfw", command=self.get_kfw)

        label.grid(row=0, column=0, columnspan=3)
        button0.grid(row=1, column=0, ipadx=17)
        button1.grid(row=1, column=1, ipadx=4)
        button2.grid(row=1, column=2, ipadx=14)

    def get_FS(self):
        sumFS = []
        top = Toplevel()
        tree = ttk.Treeview(top, columns=('Transaction Number', 'Value', 'Instance', 'comment'))
        tree.heading('#0', text="Transaction Number")
        tree.heading('#1', text='Value')
        tree.heading('#2', text='Instance')
        tree.heading('#3', text='Comment')
        tree.heading('#4', text='Dates')
        tree.column('#1', stretch=TRUE)
        tree.column('#2', stretch=TRUE)
        tree.column('#0', stretch=TRUE)
        tree.pack()
        treeview_1 = tree
        conn = sql.connect('/Users/setor/PycharmProjects/Project_X/Optimizing')
        c = conn.cursor()
        c.execute("SELECT * FROM main.Accounting WHERE keyword = 'FS' ")
        data = c.fetchall()
        for row in data:
            treeview_1.insert('', 'end', text="Trans_" + str(row[0]), values=(str(row[1])+"€", row[2], row[3], row[4]))

        for row in data:
            sumFS.append(row[1])

        treeview_1.insert('', 'end', text="SumFS", values=(str(sum(sumFS))+"€"))
        c.close()
        conn.close()

    def get_parents(self):
        sumparents = []
        top = Toplevel()
        tree = ttk.Treeview(top, columns=("Transaction Number", 'Value', 'Instance', 'Comments'))
        tree.heading('#0', text="Transaction Number")
        tree.heading('#1', text='Value')
        tree.heading('#2', text='Instance')
        tree.heading('#3', text='comment')
        tree.heading('#4', text='Dates')
        tree.column('#1', stretch=TRUE)
        tree.column('#2', stretch=TRUE)
        tree.column('#0', stretch=TRUE)
        tree.pack()
        treeview_1 = tree
        conn = sql.connect('/Users/setor/PycharmProjects/Project_X/Optimizing')
        c = conn.cursor()
        c.execute("SELECT * FROM main.Accounting WHERE keyword = 'parents' ")
        data = c.fetchall()
        for row in data:
            treeview_1.insert('', 'end', text="Trans_" + str(row[0]), values=(str(row[1])+"€", row[2], row[3], row[4]))

        for row in data:
            sumparents.append(row[1])
        treeview_1.insert('', 'end', text="Sum Parents", values=(str(sum(sumparents))+"€"))
        c.close()
        conn.close()

    def get_kfw(self):
        sum_kfw = []
        top = Toplevel()
        tree = ttk.Treeview(top, columns=('Transaction Number', 'Value', 'Instance', 'Comment'))
        tree.heading('#0', text="Transaction Number")
        tree.heading('#1', text='Value')
        tree.heading('#2', text='Instance')
        tree.heading('#3', text='Comment')
        tree.heading('#4', text="Dates")
        tree.column('#1', stretch=TRUE)
        tree.column('#2', stretch=TRUE)
        tree.column('#0', stretch=TRUE)
        tree.pack()
        treeview_1 = tree

        conn = sql.connect('/Users/setor/PycharmProjects/Project_X/Optimizing')
        c = conn.cursor()
        c.execute("SELECT * FROM main.Accounting WHERE keyword = 'Kfw' ")
        data = c.fetchall()
        for row in data:
            treeview_1.insert('', 'end', text="Trans_" + str(row[0]), values=(str(row[1])+"€", row[2], row[3], row[4]))
        for row in data:
            sum_kfw.append(row[1])
        treeview_1.insert('', 'end', text="Sum Kfw", values=(str(sum(sum_kfw))+"€"))

        c.close()
        conn.close()

    def show_totalBalance(self):
        conn = sql.connect('/Users/setor/PycharmProjects/Project_X/Optimizing')
        c = conn.cursor()
        c.execute("SELECT * FROM main.Accounting")
        data = c.fetchall()

        inflow = []
        outflow = []

        for row in data:
            if row[1] >= 0:
                inflow.append(row[1])
            elif row[1] < 0:
                outflow.append(row[1])

        sumInflow = round(sum(inflow), 3)
        sumOutflow = round(sum(outflow), 3)
        Balance = round(round(sum(inflow), 3) + round(sum(outflow), 3), 4)

        top = Toplevel()
        tree = ttk.Treeview(top, columns=('Transaction Number', 'Outflow', ""))
        tree.heading('#0', text='Transaction Number')
        tree.heading('#1', text='Outflow')
        tree.heading('#2', text='Inflow')
        tree.heading('#3', text='Dates')
        tree.column('#0', stretch=TRUE)
        tree.column('#1', stretch=TRUE)
        tree.column('#2', stretch=TRUE)
        tree['height'] = 13
        tree.column("#0", anchor=E)
        tree.column("#1", anchor=E)
        tree.column("#2", anchor=E)
        tree.column("#3", anchor=E)

        labelInflow = Label(top, text=('Total Inflow = ' + str(sumInflow)+"€"))
        labelOutflow = Label(top, text=('Total Outflow = ' + str(sumOutflow) + "€"))
        labelBalance = Label(top, text=('The Balance = '+str(Balance)+"€"))

        tree.grid(row=1, column=1, columnspan=3)
        labelOutflow.grid(row=2, column=2)
        labelInflow.grid(row=2, column=3)
        labelBalance.grid(row=3, column=3)

        for row in data:
            #inflow
            if row[1] >= 0:
                tree.insert('', 'end', text="Trans_" + str(row[0]),
                                values=('', str(row[1]) + "€", row[4]))
            #outflow
            elif row[1] < 0:
                tree.insert('', 'end', text="Trans_" + str(row[0]),
                                values=(str(row[1]) + "€", "", row[4]))
        c.close()
        conn.close()


App(root)
root.mainloop()
