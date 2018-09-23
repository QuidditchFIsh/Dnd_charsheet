import tkinter as tk
from tkinter import ttk
import random as rand
from PIL import ImageTk, Image
import json
import Char as char
import Init_lists as lists


LARGE_FONT = ("Verdana",12)

#Can put inheritance into these parathemcies
class dnd_char_Sheet(tk.Tk):
#init method is initalisation class. When the class runs this will imidately will run
    def __init__(self):
        #initalise tkinter as well
        tk.Tk.__init__(self)
        self.container = tk.Frame(self)

        self.container.pack(side='top', fill='both',expand=True)

        self.container.grid_rowconfigure(0,weight=1)
        self.container.grid_columnconfigure(0,weight=1)

        self.menubar = tk.Menu(self.container)
        self.filemenu = tk.Menu(self.menubar,tearoff=0)
        self.filemenu.add_command(label="Save Settings")
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit",command=quit)


        self.char_menu = tk.Menu(self.menubar,tearoff=0)
        self.char_menu.add_command(label="Edit Hit Points")



        self.spell_menu = tk.Menu(self.menubar,tearoff=0)
        self.lvl_menu = tk.Menu(self.spell_menu,tearoff=0)
        self.class_menu = tk.Menu(self.spell_menu, tearoff=0)

        for i in range(0,8):
            self.lvl_menu.add_command(label=i)


        for i in ['Ranger', 'Barbarian', 'Paladin','Bard','Cleric','Druid','Fighter','Monk','Rouge','Sorcerer','Warlock','Wizard']:
            self.class_menu.add_command(label=i)


        self.class_menu.add_command(label="hello")
        self.spell_menu.add_cascade(label="By Level",menu=self.lvl_menu)
        self.spell_menu.add_cascade(label="By Class",menu=self.class_menu)

        self.menubar.add_cascade(label="File",menu=self.filemenu)
        self.menubar.add_cascade(label="Edit")
        self.menubar.add_cascade(label="Character",menu=self.char_menu)
        self.menubar.add_cascade(label="Spells",menu=self.spell_menu)

        self.menubar.entryconfigure("Character",state="disabled")
        self.menubar.entryconfigure("Spells",state="disabled")


        tk.Tk.config(self,menu=self.menubar)

        self.frames = {}

        for F in (StartPage,Page_One):
            self.init_frames(F)



        self.show_frame(StartPage)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()

    def init_frames(self,page):
        frame = page(self.container, self)
        self.frames[page] = frame
        frame.grid(row=0, column=0, sticky="nsew")

    def show_page(self,page):
        frame = page(self.container, self)
        self.frames[page] = frame

    def show_char_sheet(self):
        self.init_frames(Page_Two)
        self.show_frame(Page_Two)
        self.spell_menu.add_command(label="Spells", command=lambda :self.show_page(Spell_Page))
        #self.char_menu.add_command(label="Level Up",command = lambda :self.show_page(level_up_page))
        self.menubar.entryconfigure("Character",state="normal")
        self.menubar.entryconfigure("Spells", state="normal")




class StartPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text="DnD Character Sheet and Database",font=LARGE_FONT)
        label.grid(padx=10,pady=10,row=0,column=2)

        Button1 = ttk.Button(self,text="New Char Sheet",command=lambda :controller.show_frame(Page_One))
        Button1.grid(padx=10,pady=10,row=1,column=2)

        Button2 = ttk.Button(self,text="Load Char Sheet",command=lambda :controller.show_page(test_page))
        Button2.grid(padx=10,pady=10,row=2,column=2)

        Button3 = ttk.Button(self,text="Weapons DataBase",command=lambda :controller.show_page(Weapons_Page))
        Button3.grid(padx=10,pady=10,row=3,column=2)

        Button5 = ttk.Button(self, text="Spells DataBase",command=lambda :controller.show_page(Spell_Page))
        Button5.grid(padx=10, pady=10,row=4,column=2)

        Button4 = ttk.Button(self,text="Dice",command=lambda :controller.show_page(Dice_Page))
        Button4.grid(padx=10,pady=10,row=5,column=2)

    def load(self):
        print("Need to implement loading a charsheet")

class Weapons_Page(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        win=tk.Toplevel()

class Dice_Page(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        win=tk.Toplevel()


class Spell_Page(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        win=tk.Toplevel()
        search_Box_Frame = tk.Frame(win)
        spell_List_Frame = tk.Frame(win)
        spell_Description_Frame= tk.Frame(win)

        self.spell_search_var=tk.StringVar()
        self.spell_search_var.trace("w",self.update_spell_list)
        self.Search_Box = ttk.Entry(search_Box_Frame, textvariable=self.spell_search_var)
        self.spell_lbox = tk.Listbox(spell_List_Frame, width=20, height=30)
        self.Search_Label = tk.Label(search_Box_Frame, text='Enter Spell Name Here')
        self.Search_Label.grid(row=0,column=0)
        self.spell_lbox.bind("<Double-Button-1>",self.OnDouble_Spell)

        self.spell_lbox.grid(row=0,column=0)
        self.Search_Box.grid(row=0,column=1)

        self.name_var = tk.StringVar()
        self.name_var.set('')
        spell_Name_label = tk.Label(spell_Description_Frame,text="Name")
        spell_Name_label.grid(row=0,column=0)

        spell_Name_Entry = ttk.Entry(spell_Description_Frame,textvariable=self.name_var)
        spell_Name_Entry.grid(row=0,column=1)

        spell_Description_label = tk.Label(spell_Description_Frame,text='Description')
        spell_Description_label.grid(row=1,column=0,columnspan=2)
        self.spell_Description_Box = tk.Text(spell_Description_Frame,width=20,height=10)
        self.spell_Description_Box.grid(row=2,column=0,columnspan=2)
        self.spell_Description_Box.config(wrap=tk.WORD)

        spell_Materials_label = tk.Label(spell_Description_Frame,text='Materials')
        spell_Materials_label.grid(row=8,column=0,columnspan=2)
        self.spell_Materials_Box = tk.Text(spell_Description_Frame,width=20,height=10)
        self.spell_Materials_Box.grid(row=9,column=0,columnspan=2)
        self.spell_Materials_Box.config(wrap=tk.WORD)

        self.range_var = tk.StringVar()
        self.range_var.set('')
        spell_Range_label = tk.Label(spell_Description_Frame,text="Range")
        spell_Range_label.grid(row=3,column=0)

        spell_Range_Entry = ttk.Entry(spell_Description_Frame,textvariable=self.range_var)
        spell_Range_Entry.grid(row=3,column=1)

        spell_Duration_label = tk.Label(spell_Description_Frame,text="Duration")
        spell_Duration_label.grid(row=4,column=0)

        self.duration_var=tk.StringVar()
        self.duration_var.set('')
        spell_Duration_Entry = ttk.Entry(spell_Description_Frame,textvariable=self.duration_var)
        spell_Duration_Entry.grid(row=4,column=1)

        spell_Level_label = tk.Label(spell_Description_Frame,text="Level")
        spell_Level_label.grid(row=5,column=0)

        self.lvl_var=tk.StringVar()
        self.lvl_var.set('')
        spell_Level_Entry = ttk.Entry(spell_Description_Frame,textvariable=self.lvl_var)
        spell_Level_Entry.grid(row=5,column=1)

        self.concentration_var = tk.IntVar()
        self.concentration_chk_box = tk.Checkbutton(spell_Description_Frame,text="Concentration",variable=self.concentration_var)
        self.concentration_chk_box.grid(row=6,column=0,columnspan=2)

        spell_Casting_label = tk.Label(spell_Description_Frame,text="Casting Time")
        spell_Casting_label.grid(row=7,column=0)

        self.casting_var = tk.StringVar()
        self.casting_var.set('')
        spell_Casting_Entry = ttk.Entry(spell_Description_Frame,textvariable=self.casting_var)
        spell_Casting_Entry.grid(row=7,column=1)

        search_Box_Frame.grid(row=0,column=0,columnspan=2,pady=10)
        spell_List_Frame.grid(row=1,column=0,padx=10)
        spell_Description_Frame.grid(row=1,column=1,padx=10)

        self.update_spell_list()

    def update_spell_list(self,*args):
        search_term = self.spell_search_var.get()

        with open("C:/Users/nye42/PycharmProjects/dnd/dnd-spells-master/spells.json", encoding='utf-8') as file:
            spell_data = json.load(file)
        self.spells = []
        self.desc = []
        self.range = []
        self.duration=[]
        self.lvl=[]
        self.concentration=[]
        self.casting=[]
        self.materials=[]

        for spell in spell_data['spells']:
            self.spells.append(spell['name'])
            self.desc.append(spell['desc'])
            self.range.append(spell['range'])
            self.duration.append(spell['duration'])
            self.lvl.append(spell['level'])
            self.concentration.append(spell['concentration'])
            self.casting.append(spell['casting_time'])
            try:
                self.materials.append(spell['material'])
            except Exception:
                self.materials.append('No Materials Required')


        self.spell_lbox.delete(0, tk.END)

        for item in self.spells:
                if search_term.lower() in item.lower():
                    self.spell_lbox.insert(tk.END, item)

    def OnDouble_Spell(self,event):
        widget = event.widget
        selection = widget.curselection()
        value = widget.get(selection[0])
        location = self.spells.index(value)
        self.name_var.set(self.spells[location])
        self.range_var.set(self.range[location])
        self.duration_var.set(self.duration[location])
        self.casting_var.set(self.casting[location])
        self.lvl_var.set(self.lvl[location])
        self.spell_Description_Box.insert('1.0',self.desc[location])
        self.spell_Materials_Box.insert('1.0',self.materials[location])
        if(self.concentration[location] == 'yes'):
            self.concentration_var.set('1')
        else:
            self.concentration_var.set('0')



class Page_One(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.create_page(controller)

    def create_page(self,controller):
        label = ttk.Label(self,text="Enter The info About your Character",font=LARGE_FONT)
        label.grid(row=0,column=0,columnspan=2,padx=30)

        Label_Name = ttk.Label(self,text="Name")
        Label_Name.grid(row=1,column=0)
        self.Entry_Name = ttk.Entry(self)
        self.Entry_Name.grid(row=1,column=1)

        Races = {'Half Elf','Gnome','Half Orc','DragonBorn','Tiefling','Dwarf'
            , 'Elf','Halfling','Human'}
        Alignments = {'Lawful Good', 'Neutral Good', 'Chaotic Good ','Lawful neutral','True neutral',
                      'Chaotic neutral','Lawful evil','Neutral evil','Chaotic evil'}
        Class = {'Ranger': 6, 'Barbarian': 8, 'Paladin': 6 ,'Bard': 5,'Cleric':5
        , 'Druid':5,'Fighter':6,'Monk':5,'Rouge':5,'Sorcerer':4,
                 'Warlock':5,'Wizard':4}
        self.tkvar_R = tk.StringVar()
        self.tkvar_A = tk.StringVar()
        self.tkvar_C = tk.StringVar()

        self.tkvar_R.set('')
        self.tkvar_A.set('')
        self.tkvar_C.set('')

        #put a trace on te class variable to check when it changes

        Label_Class = tk.Label(self,text="Class")
        Label_Class.grid(row=2,column=0)
        Class_Menu = ttk.OptionMenu(self, self.tkvar_C, *Class)
        Class_Menu.grid(row=2,column=1)
        #self.img=ImageTk.PhotoImage(Image.open("C:/Users/nye42/PycharmProjects/dnd/Class_icons/Ranger.jpg"))
        #Label_Class_Img = ttk.Label(self,image = self.img)
        #Label_Class_Img.image = self.img
        #Label_Class_Img.grid(row=2,column=2)

        Label_Race = tk.Label(self,text="Race")
        Label_Race.grid(row=3,column=0)
        Race_Menu = ttk.OptionMenu(self, self.tkvar_R, *Races)
        Race_Menu.grid(row=3,column=1)

        Label_Alignment = tk.Label(self,text="Alignment")
        Label_Alignment.grid(row=4,column=0)
        Alignment_Menu = ttk.OptionMenu(self, self.tkvar_A, *Alignments)
        Alignment_Menu.grid(row=4,column=1)

        Label_str = ttk.Label(self, text="Strength")
        Label_dex = ttk.Label(self, text="Dexterity")
        Label_const = ttk.Label(self, text="Constitution")
        Label_int = ttk.Label(self, text="Intelligence")
        Label_wis = ttk.Label(self, text="Wisdom")
        Label_char = ttk.Label(self, text="Charisma")

        self.Entry_str = ttk.Entry(self)
        self.Entry_dex = ttk.Entry(self)
        self.Entry_const = ttk.Entry(self)
        self.Entry_int = ttk.Entry(self)
        self.Entry_wis = ttk.Entry(self)
        self.Entry_char = ttk.Entry(self)

        Label_str.grid(row=5,column=0)
        self.Entry_str.grid(row=5,column=1)
        Label_dex.grid(row=6, column=0)
        self.Entry_dex.grid(row=6, column=1)
        Label_const.grid(row=7, column=0)
        self.Entry_const.grid(row=7, column=1)
        Label_int.grid(row=8, column=0)
        self.Entry_int.grid(row=8, column=1)
        Label_wis.grid(row=9, column=0)
        self.Entry_wis.grid(row=9, column=1)
        Label_char.grid(row=10, column=0)
        self.Entry_char.grid(row=10, column=1)

        Button2 = ttk.Button(self,text="Back",command=lambda:controller.show_frame(StartPage))
        Button2.grid(row=11,column=0)

        Button_new = ttk.Button(self,text="Make new Character",command=lambda :Page_One.save(self,Page_One,controller))
        Button_new.grid(row=11,column=2)

        Button_roll = ttk.Button(self,text="Roll for Stats",command =lambda:Page_One.roll(self,Page_One))
        Button_roll.grid(row=11,column=1)

    def roll(self,page):
        rolls = []
        results = []
        sum = 0
        for i in range(0, 6):
            for i in range(0, 4):
                rolls.append(rand.randint(1, 6))
                sum += rolls[i]
            sum = sum - min(rolls)
            results.append(sum)
            rolls = []
            sum = 0
        self.Entry_str.delete(0,100)
        self.Entry_str.insert(0,str(results[0]))
        self.Entry_dex.delete(0,100)
        self.Entry_dex.insert(0,str(results[1]))
        self.Entry_const.delete(0,100)
        self.Entry_const.insert(0,str(results[2]))
        self.Entry_int.delete(0,100)
        self.Entry_int.insert(0,str(results[3]))
        self.Entry_wis.delete(0,100)
        self.Entry_wis.insert(0,str(results[4]))
        self.Entry_char.delete(0,100)
        self.Entry_char.insert(0,str(results[5]))

    def save(self,page,controller):
        '''
        Structure of File will be
        Name,Class,Race,Alignment,str,dex,const,int,wis,char
        '''
        file = open("Data_File.txt","w")
        file.write(str(self.Entry_Name.get()) + ',' + str(self.tkvar_C.get()) + ',' + str(self.tkvar_R.get()) +
                   ',' + str(self.tkvar_A.get()) + ',' + str(self.Entry_str.get())+ ',' + str(self.Entry_dex.get())
                   + ',' + str(self.Entry_const.get())+ ',' + str(self.Entry_int.get())+ ',' + str(self.Entry_wis.get())
                   + ',' + str(self.Entry_char.get()))
        char.Name = self.Entry_Name.get()
        char.clss = self.tkvar_C.get()
        char.race = self.tkvar_R.get()
        char.alignment = self.tkvar_R.get()
        char.str = self.Entry_str.get()
        char.dex = self.Entry_dex.get()
        char.const = self.Entry_const.get()
        char.int = self.Entry_int.get()
        char.wis = self.Entry_wis.get()
        char.char = self.Entry_char.get()

        file.close()
        controller.show_char_sheet()

class Page_Two(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        Frame1 = tk.Frame(self) #Description Frame
        Frame2 = tk.Frame(self) #Stats Frame
        Frame3 = tk.Frame(self) #Items Frame
        Frame4 = tk.Frame(self) #Spells Frame


        #Description of the Character
        Label_Name = tk.Label(Frame1,text="Name").grid(row=0,column=0)
        self.Name_var = tk.StringVar()
        self.Name_var.set('Holder')
        self.Name = tk.Label(Frame1,textvariable=self.Name_var).grid(row=0,column=1)
        self.Char_Data = []

        Label_Class = tk.Label(Frame1,text="Class").grid(row=0,column=2)
        self.Class_var = tk.StringVar()
        self.Class_var.set(char.clss)
        self.Class = tk.Label(Frame1,textvariable=self.Class_var).grid(row=0,column=3)

        Label_Level = tk.Label(Frame1,text="Level").grid(row=0,column=4)
        self.lvl_var = tk.StringVar()
        self.lvl_var.set(char.level)
        self.Level = tk.Label(Frame1,textvariable = self.lvl_var).grid(row=0,column=5)
        self.lvl_up_button = tk.Button(Frame1,text="Level Up",command=lambda :Page_Two.lvlup(self))
        self.lvl_up_button.grid(row=0,column=6)

        Label_Race = tk.Label(Frame1, text="Race").grid(row=1, column=0)
        self.race_var = tk.StringVar()
        self.race_var.set('Holder')
        self.Race = tk.Label(Frame1, textvariable=self.race_var).grid(row=1, column=1)

        Label_Alignment = tk.Label(Frame1, text="Alignment").grid(row=1, column=2)
        self.Alig_var = tk.StringVar()
        self.Alig_var.set('Holder')
        self.Alignment = tk.Label(Frame1, textvariable=self.Alig_var).grid(row=1, column=3)

        Label_Proficiency = tk.Label(Frame1, text="Proficiency").grid(row=2, column=0)
        self.Prof_var = tk.StringVar()
        self.Prof_var.set('Holder')
        self.Prof = tk.Label(Frame1, textvariable=self.Prof_var).grid(row=2, column=1)

        Label_HP = tk.Label(Frame1, text="Hit Points" ).grid(row=2, column=2)
        self.HP_var = tk.StringVar()
        self.HP_var.set('Holder')
        self.HP = tk.Label(Frame1, textvariable=self.HP_var).grid(row=2, column=3)

        Label_Init = tk.Label(Frame1, text="Initiative").grid(row=2, column=4)
        self.init_Entry = ttk.Entry(Frame1)
        self.init_Entry.grid(row=2,column=5)

        Label_Insipr = tk.Label(Frame1, text="Inspiration").grid(row=3, column=0)
        self.Insipr_Entry = ttk.Entry(Frame1)
        self.Insipr_Entry.grid(row=3,column=1)

        Label_AC = tk.Label(Frame1, text="Armour Class").grid(row=3, column=2)
        self.AC_Entry = ttk.Entry(Frame1)
        self.AC_Entry.grid(row=3,column=3)

        #Stats Code

        Label_str = tk.Label(Frame2, text="Strength").grid(row=0,column=0,pady=30)
        Label_dex = tk.Label(Frame2, text="Dexterity").grid(row=1,column=0,pady=30)
        Label_const = tk.Label(Frame2, text="Constitution").grid(row=2,column=0,pady=30)
        Label_Int = tk.Label(Frame2, text="Intelligence").grid(row=3,column=0,pady=30)
        Label_Wis = tk.Label(Frame2, text="Wisdom").grid(row=4,column=0,pady=30)
        Label_Char = tk.Label(Frame2, text="Charisma").grid(row=5,column=0,pady=30)

        self.str_var = tk.StringVar()
        self.dex_var = tk.StringVar()
        self.const_var = tk.StringVar()
        self.int_var = tk.StringVar()
        self.wis_var = tk.StringVar()
        self.char_var = tk.StringVar()

        self.str_var.set('Holder')
        self.dex_var.set('Holder')
        self.const_var.set('Holder')
        self.int_var.set('Holder')
        self.wis_var.set('Holder')
        self.char_var.set('Holder')

        self.str_var_mod = tk.StringVar()
        self.dex_var_mod = tk.StringVar()
        self.const_var_mod = tk.StringVar()
        self.int_var_mod = tk.StringVar()
        self.wis_var_mod = tk.StringVar()
        self.char_var_mod = tk.StringVar()

        self.str_var_mod.set('0')
        self.dex_var_mod.set('0')
        self.const_var_mod.set('0')
        self.int_var_mod.set('0')
        self.wis_var_mod.set('0')
        self.char_var_mod.set('0')

        Label_str_stat = tk.Label(Frame2, textvariable=self.str_var).grid(row=0,column=1)
        Label_dex_stat = tk.Label(Frame2, textvariable=self.dex_var).grid(row=1,column=1)
        Label_const_stat = tk.Label(Frame2, textvariable=self.const_var).grid(row=2,column=1)
        Label_Int_stat = tk.Label(Frame2, textvariable=self.int_var).grid(row=3,column=1)
        Label_Wis_stat = tk.Label(Frame2, textvariable=self.wis_var).grid(row=4,column=1)
        Label_Char_stat = tk.Label(Frame2, textvariable=self.char_var).grid(row=5,column=1)

        Label_str_mod = tk.Label(Frame2, textvariable=self.str_var_mod).grid(row=0,column=2)
        Label_dex_mod = tk.Label(Frame2, textvariable=self.dex_var_mod).grid(row=1,column=2)
        Label_const_mod = tk.Label(Frame2, textvariable=self.const_var_mod).grid(row=2,column=2)
        Label_Int_mod = tk.Label(Frame2, textvariable=self.int_var_mod).grid(row=3,column=2)
        Label_Wis_mod = tk.Label(Frame2, textvariable=self.wis_var_mod).grid(row=4,column=2)
        Label_Char_mod = tk.Label(Frame2, textvariable=self.char_var_mod).grid(row=5,column=2)

        #Items and weapons code

        Label_Wpns = tk.Label(Frame3, text="Weapons").grid(row=0,column=0)
        Label_Amr = tk.Label(Frame3, text="Armour").grid(row=0,column=2)

        self.Weapon_Text = tk.Text(Frame3, height=20, width=20)
        self.Armour_Text = tk.Text(Frame3, height=20, width=20)

        self.Weapon_Text.config(wrap=tk.WORD)
        self.Armour_Text.config(wrap=tk.WORD)

        self.Weapon_Text.grid(row=1,column=0,columnspan=2)
        self.Armour_Text.grid(row=1,column=2,columnspan=2)

        Wpn_Button = ttk.Button(Frame3, text='+',command=lambda :Page_Two.add_wpn(self))
        Wpn_Button.grid(row=0, column=1)

        Amr_Button = ttk.Button(Frame3, text='+',command=lambda : Page_Two.add_amr(self))
        Amr_Button.grid(row=0, column=3)

        #spell code

        Label_Spells = tk.Label(Frame4, text="Spells").grid(row=0,column=0)
        Spells_Text = tk.Text(Frame4, height=20, width=40)
        Spells_Text.grid(row=1,column=0)
        Spells_Text.config(wrap=tk.WORD)

        spell_Button = tk.Button(Frame4, text = "+",command = lambda : Page_Two.add_spell(self) )
        spell_Button.grid(row=0,column=1,sticky = tk.W)
        Page_Two.update(self)
        Frame1.grid(row=0,column=0,columnspan=2)
        Frame2.grid(row=1,column=0,rowspan=2)
        Frame3.grid(row=1,column=1)
        Frame4.grid(row=2,column=1)


        #update all of the stats for the characyer and save the hitpoints as they are not somthing whihc is set they
        #are calculated
        Page_Two.update_stat_mod(self)
        Page_Two.prof_update(self)
        Page_Two.HP_Set(self)

    def lvlup(self):
        lvl_win = tk.Toplevel()

        level = char.level + 1
        Title = tk.Label(lvl_win, text="Level Up")
        Title.grid(row=0, column=0, columnspan=2)
        msg = "Level:" + str(char.level) + " -> " + str(char.level + 1)
        message = tk.Label(lvl_win, text=msg)
        message.grid(row=1, column=0)

        # HP level up
        current_hp = char.max_hit_points
        const_mod = int((int(char.const) - 10) / 2)
        cls = char.clss
        roll = rand.randint(1, Page_Two.hp_switch(cls))
        new_hp = current_hp + const_mod + roll

        hp_msg = "Hit Points:" + str(current_hp) + " -> " + str(new_hp)
        hp_message = tk.Label(lvl_win, text=hp_msg)
        hp_message.grid(row=2, column=0)

        lvlup_desc = tk.Text(lvl_win, height=5, width=30)
        lvlup_desc.grid(row=3, column=0)
        lvlup_desc.insert(tk.INSERT, str(lists.level_up_descp[int(level) - 1][self.class_switch(cls)]))

        #if(level == 4 || )



        conf = tk.Button(lvl_win, text="Confirm", command=lambda :lvl_win.destroy())
        conf.grid(row=4, column=0)

        char.level = level
        char.max_hit_points = new_hp
        char.current_hit_points = new_hp

        self.level_up_update()
        print(self.HP_var.get())

    def class_switch(self,cls):
        #method which returns the location of a specific class within the level_desp list
        class_switcher = {'Barbarian':0 ,'Bard':1,'Cleric':2,'Druid':3,'Fighter':4,'Monk':5,'Paladin':6,'Ranger':7,
            'Rouge':8,'Sorcerer':9,'Warlock':10,'Wizard':11}
        return class_switcher.get(cls,"Nothing")

    def HP_Set(self):
        hp_base = Page_Two.hp_switch(self.Class_var.get())
        max = hp_base + int(self.const_var_mod.get())
        self.HP_var.set(str(max) + "/" + str(max))
        char.max_hit_points=max
        char.current_hit_points=max

    def hp_switch(player_class):
        switcher = {'Ranger': 10, 'Barbarian': 12, 'Paladin': 10, 'Bard': 8, 'Cleric': 8
            ,'Druid': 8, 'Fighter': 10, 'Monk': 8, 'Rouge': 8, 'Sorcerer': 6,'Warlock': 8, 'Wizard': 6}
        return switcher.get(player_class, "nothing")


    def prof_update(self):
        self.Prof_var.set(int((float(self.lvl_var.get()) - 1) / 4) + 2)

    def update_stat_mod(self):
        self.str_var_mod.set(int((int(self.str_var.get()) - 10 )/2))
        self.dex_var_mod.set(int((int(self.dex_var.get()) - 10 )/2))
        self.const_var_mod.set(int((int(self.const_var.get()) - 10 )/2))
        self.wis_var_mod.set(int((int(self.wis_var.get()) - 10 )/2))
        self.int_var_mod.set(int((int(self.int_var.get()) - 10 )/2))
        self.char_var_mod.set(int((int(self.char_var.get()) - 10 )/2))


    def add_wpn(self):
        # create child window
        win = tk.Toplevel()
        self.search_var = tk.StringVar()
        self.search_var.trace("w", self.update_wpn_list)
        self.entry = tk.Entry(win, textvariable=self.search_var, width=13)
        self.lbox = tk.Listbox(win, width=45, height=15)
        self.Search_Label = tk.Label(win,text="Enter Name of Weapon")
        self.lbox.bind("<Double-Button-1>", self.OnDouble)

        self.entry.grid(row=0, column=1, padx=10, pady=3)
        self.Search_Label.grid(row=0,column=0,padx=10,pady=3)
        self.lbox.grid(row=1, column=0, padx=10, pady=3,columnspan =2)

        self.update_wpn_list()


    def add_amr(self):
        # create child window
        win = tk.Toplevel()
        self.search_var = tk.StringVar()
        self.search_var.trace("w", self.update_amr_list)
        self.entry = tk.Entry(win, textvariable=self.search_var, width=13)
        self.lbox = tk.Listbox(win, width=45, height=15)
        self.Search_Label = tk.Label(win,text="Enter Name of Armour")
        self.lbox.bind("<Double-Button-1>", self.OnDouble_amr)

        self.entry.grid(row=0, column=1, padx=10, pady=3)
        self.Search_Label.grid(row=0,column=0,padx=10,pady=3)
        self.lbox.grid(row=1, column=0, padx=10, pady=3,columnspan =2)

        self.update_amr_list()

    def add_spell(self):
        # create child window
        win = tk.Toplevel()
        self.search_var = tk.StringVar()
        self.search_var.trace("w", self.update_amr_list)
        self.entry = tk.Entry(win, textvariable=self.search_var, width=13)
        self.lbox = tk.Listbox(win, width=45, height=15)
        self.Search_Label = tk.Label(win,text="Enter Name of Spell")
        self.lbox.bind("<Double-Button-1>", self.OnDouble_amr)

        self.entry.grid(row=0, column=1, padx=10, pady=3)
        self.Search_Label.grid(row=0,column=0,padx=10,pady=3)
        self.lbox.grid(row=1, column=0, padx=10, pady=3,columnspan =2)

    def update_wpn_list(self, *args):
        search_term = self.search_var.get()

        with open(lists.Path_to_Martial_Melee_Weapons, encoding='utf-8') as f:
            data = json.load(f)
        with open(lists.Path_to_Martial_Ranged_Weapons, encoding='utf-8') as f1:
            data1 = json.load(f1)
        with open(lists.Path_to_Firearms,encoding='utf-8') as f2:
            data2 = json.load(f2)
        with open(lists.Path_to_Simple_Melee_Weapons,encoding='utf-8') as f3:
            data3 = json.load(f3)
        with open(lists.Path_to_Simple_Ranged_Weapons,encoding='utf-8') as f4:
            data4 = json.load(f4)
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

        for weapon in data1['Ranged_Weapons']:
            self.weapons.append(weapon['Name'])
            self.cost.append(weapon['Cost'])
            self.damage.append(weapon['Damage'])
            self.weight.append(weapon['Weight'])
            self.properties.append(weapon['Properties'])

        for weapon in data2['firearms']:
            self.weapons.append(weapon['Name'])
            self.cost.append(weapon['Cost'])
            self.damage.append(weapon['Damage'])
            self.weight.append(weapon['Weight'])
            self.properties.append(weapon['Properties'])

        for weapon in data3['Simple_Melee']:
            self.weapons.append(weapon['Name'])
            self.cost.append(weapon['Cost'])
            self.damage.append(weapon['Damage'])
            self.weight.append(weapon['Weight'])
            self.properties.append(weapon['Properties'])

        for weapon in data4['Simple_Ranged_Weapons']:
            self.weapons.append(weapon['Name'])
            self.cost.append(weapon['Cost'])
            self.damage.append(weapon['Damage'])
            self.weight.append(weapon['Weight'])
            self.properties.append(weapon['Properties'])

        self.lbox.delete(0, tk.END)

        for item in self.weapons:
                if search_term.lower() in item.lower():
                    self.lbox.insert(tk.END, item)

    def update_amr_list(self, *args):
        search_term = self.search_var.get()

        self.armour = ['Padded','Leather','Studded Leather','Hide','Chain Shirt'
                       ,'Scale Mail','Breastplate','Half Plate','Ring Mail',
                       'Chain Mail','Splint','Plate','Sheild']

        self.lbox.delete(0, tk.END)

        for item in self.armour:
                if search_term.lower() in item.lower():
                    self.lbox.insert(tk.END, item)

    def OnDouble(self, event):
        widget = event.widget
        selection=widget.curselection()
        value = widget.get(selection[0])
        #self.select_var.set(value)
        location = self.weapons.index(value)
        self.Weapon_Text.insert('1.0',self.weapons[location] + " " + self.damage[location] + "\n")

    def OnDouble_amr(self, event):
        widget = event.widget
        selection=widget.curselection()
        value = widget.get(selection[0])
        #self.select_var.set(value)
        location = self.armour.index(value)
        self.Armour_Text.insert('1.0',self.armour[location] + "\n")

    def update(self):
        self.Name_var.set(char.Name)
        self.Class_var.set(char.clss)
        self.race_var.set(char.race)
        self.Alig_var.set(char.alignment)
        self.str_var.set(char.str)
        self.dex_var.set(char.dex)
        self.const_var.set(char.const)
        self.int_var.set(char.int)
        self.wis_var.set(char.wis)
        self.char_var.set(char.char)
        self.HP_var.set(char.max_hit_points)

    def level_up_update(self):
        self.str_var.set(char.str)
        self.dex_var.set(char.dex)
        self.const_var.set(char.const)
        self.int_var.set(char.int)
        self.wis_var.set(char.wis)
        self.char_var.set(char.char)
        self.HP_var.set(str(char.max_hit_points) + "/" + str(char.max_hit_points))
        self.lvl_var.set(char.level)


app = dnd_char_Sheet()
LEVEL = tk.StringVar()
LEVEL.set('1')
app.mainloop()
