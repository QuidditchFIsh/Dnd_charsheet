from tkinter import *
from tkinter import ttk
import json

# First create application class


class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)

        self.pack()
        self.create_widgets()

    # Create main GUI window
    def create_widgets(self):
        self.search_var = StringVar()
        self.search_var.trace("w", self.update_list)
        self.select_var = StringVar()
        self.entry = Entry(self, textvariable=self.search_var, width=13)
        self.select = Entry(self,textvariable=self.select_var,width=13)
        self.lbox = Listbox(self, width=45, height=15)
        self.lbox.bind("<Double-Button-1>", self.OnDouble)
        self.Text_Box = Text(self,height=20,width=20)
        self.Text_Box.grid(row=2,column=0,columnspan=2)

        self.entry.grid(row=0, column=0, padx=10, pady=3)
        self.select.grid(row=0,column=1,padx=10,pady=3)
        self.lbox.grid(row=1, column=0, padx=10, pady=3,columnspan =2)

        # Function for updating the list/doing the search.
        # It needs to be called here to populate the listbox.
        self.update_list()

    def update_list(self, *args):
        search_term = self.search_var.get()

        with open('C:/Users/nye42/PycharmProjects/dnd/dnd5-weapons-json-master/json/martialMeleeWeapons.json') as f:
            data = json.load(f)
        self.weapons = []
        self.cost=[]
        self.damage=[]
        self.weight=[]
        self.properties=[]

        for weapon in data['Melee_Weapons']:
            self.weapons.append(weapon['Name'])
            self.cost.append(weapon['Cost'])
            self.damage.append(weapon['Damage'])
            self.weight.append(weapon['Weight'])
            self.properties.append(weapon['Properties'])

        self.lbox.delete(0, END)

        for item in self.weapons:
                if search_term.lower() in item.lower():
                    self.lbox.insert(END, item)
        print(self.weapons)

    def OnDouble(self, event):
        widget = event.widget
        selection=widget.curselection()
        value = widget.get(selection[0])
        #self.select_var.set(value)
        location = self.weapons.index(value)
        print(self.weapons[location] + " " + self.damage[location])
        self.Text_Box.insert('1.0',self.weapons[location] + " " + self.damage[location] + "\n")






root = Tk()
root.title('Filter Listbox Test')
app = Application(master=root)
print('Starting mainloop()')
app.mainloop()