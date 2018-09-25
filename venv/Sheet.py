from tkinter import *

def display_prof():
    profVar.set(int((float(lvl_spinBox.get()) - 1) / 4) + 2)


def str_modifier():
    str_var.set(int((int(str_spinBox.get()) - 10 )/2))


def dex_modifier():
    dex_var.set(int((int(dex_spinBox.get()) - 10 )/2))


def const_modifier():
    const_var.set(int((int(const_spinBox.get()) - 10 )/2))


def int_modifier():
    int_var.set(int((int(int_spinBox.get()) - 10 )/2))


def wis_modifier():
    wis_var.set(int((int(wis_spinBox.get()) - 10 )/2))


def char_modifier():
    char_var.set(int((int(char_spinBox.get()) - 10 )/2))


# Placement of objects within the window begins here
root = Tk()
Description_Frame = Frame(root)
Stats_Frame = Frame(root)
Items_Frame = Frame(root)
Spells_Frame = Frame(root)

Label_Name = Label(Description_Frame, text="Name")
Label_Class = Label(Description_Frame, text="Class")
Label_Lvl = Label(Description_Frame, text="Level")
Label_Race = Label(Description_Frame, text="Race")
Label_Age = Label(Description_Frame, text="Age")
Label_Ali = Label(Description_Frame, text="Alignment")
Label_Prof = Label(Description_Frame, text="Proficiency Bonus")
Label_Hp = Label(Description_Frame, text="Max Hit Points")
Label_Intiv = Label(Description_Frame, text="Initiative")
Label_Inspr = Label(Description_Frame, text="Inspiration")
Label_AC = Label(Description_Frame, text="Armour Class")
Label_Wpns = Label(Items_Frame, text="Weapons")
Label_Amr = Label(Items_Frame, text="Armour")
Label_spells = Label(Spells_Frame, text="Spells")
Label_str = Label(Stats_Frame, text="Strength")
Label_dex = Label(Stats_Frame, text="Dexterity")
Label_const = Label(Stats_Frame, text="Constitution")
Label_Int = Label(Stats_Frame, text="Intelligence")
Label_Wis = Label(Stats_Frame, text="Wisdom")
Label_Char = Label(Stats_Frame, text="Charisma")

entry_Name = Entry(Description_Frame)
entry_Class = Entry(Description_Frame)
entry_Lvl = Entry(Description_Frame)
entry_Age = Entry(Description_Frame)
entry_Hp = Entry(Description_Frame)
entry_Intiv = Entry(Description_Frame)
entry_Inspr = Entry(Description_Frame)
entry_AC = Entry(Description_Frame)

Weapon_Text = Text(Items_Frame, height=20, width=20)
Armour_Text = Text(Items_Frame, height=20, width=20)
Spell_Text = Text(Spells_Frame, height=20, width=60)

# Spinbox

lvl_spinBox = Spinbox(Description_Frame, command=display_prof, from_=1, to=20, width=5)
str_spinBox = Spinbox(Stats_Frame, command=str_modifier, from_=0, to=20, width=5)
dex_spinBox = Spinbox(Stats_Frame, command=dex_modifier, from_=0, to=20, width=5)
const_spinBox = Spinbox(Stats_Frame, command=const_modifier, from_=0, to=20, width=5)
int_spinBox = Spinbox(Stats_Frame, command=int_modifier, from_=0, to=20, width=5)
wis_spinBox = Spinbox(Stats_Frame, command=wis_modifier, from_=0, to=20, width=5)
char_spinBox = Spinbox(Stats_Frame, command=char_modifier, from_=0, to=20, width=5)

# Dropdown Menus

Races = {'Human', 'Elf', 'Dwarf', 'Gnome'}
Alignments = {'Good', 'Neutral', 'Evil'}
Class = {'Ranger':6, 'Barbarian':8, 'Paladin':6}
tkvar_R = StringVar(Description_Frame)
tkvar_A = StringVar(Description_Frame)
tkvar_C = StringVar(Description_Frame)

tkvar_R.set('')
tkvar_A.set('')
tkvar_C.set('')
Race_Menu = OptionMenu(Description_Frame, tkvar_R, *Races)
Alignment_Menu = OptionMenu(Description_Frame, tkvar_A, *Alignments)
Class_Menu = OptionMenu(Description_Frame, tkvar_C, *Class)

# Description Frame Code
Label_Name.grid(row=0, column=0, sticky=W)
Label_Class.grid(row=0, column=2, sticky=W)
Label_Lvl.grid(row=0, column=4, sticky=W)

entry_Name.grid(row=0, column=1)
Class_Menu.grid(row=0, column=3)
lvl_spinBox.grid(row=0, column=5)

Label_Race.grid(row=1, column=0)
Race_Menu.grid(row=1, column=1)

Label_Ali.grid(row=1, column=2)
Alignment_Menu.grid(row=1, column=3)

Label_Prof.grid(row=2, column=0, sticky=W)

# proficency Code
# Will need to format this correctly so there is a + sign before the number
profVar = StringVar()
profVar.set('2')

Proficency_Label = Label(Description_Frame, textvariable=profVar).grid(row=2, column=1)

Label_Hp.grid(row=2, column=2, sticky=W)
#Max Hit Code
HpVar = StringVar()
HpVar.set('0')

Max_Hit_Label = Label(Description_Frame,textvariable=HpVar).grid(row=2,column=3)

#entry_Hp.grid(row=2, column=3)

Label_Intiv.grid(row=2, column=4, sticky=W)
entry_Intiv.grid(row=2, column=5)

Label_Inspr.grid(row=3, column=0, sticky=W)
entry_Inspr.grid(row=3, column=1)

Label_AC.grid(row=3, column=2, sticky=W)
entry_AC.grid(row=3, column=3)

# Stats Frame Code
Label_str.grid(row=0, column=0)
Label_dex.grid(row=1, column=0)
Label_const.grid(row=2, column=0)
Label_Int.grid(row=3, column=0)
Label_Wis.grid(row=4, column=0)
Label_Char.grid(row=5, column=0)

str_spinBox.grid(row=0, column=1)
dex_spinBox.grid(row=1, column=1)
const_spinBox.grid(row=2, column=1)
int_spinBox.grid(row=3, column=1)
wis_spinBox.grid(row=4, column=1)
char_spinBox.grid(row=5, column=1)

# Modifiers for the Stats
str_var = StringVar()
dex_var = StringVar()
const_var = StringVar()
int_var = StringVar()
wis_var = StringVar()
char_var = StringVar()

str_var.set('-5')
dex_var.set('-5')
const_var.set('-5')
int_var.set('-5')
wis_var.set('-5')
char_var.set('-5')

str_mod_Label = Label(Stats_Frame, textvariable=str_var).grid(row=0, column=2)
dex_mod_Label = Label(Stats_Frame, textvariable=dex_var).grid(row=1, column=2)
const_mod_Label = Label(Stats_Frame, textvariable=const_var).grid(row=2, column=2)
int_mod_Label = Label(Stats_Frame, textvariable=int_var).grid(row=3, column=2)
wis_mod_Label = Label(Stats_Frame, textvariable=wis_var).grid(row=4, column=2)
char_mod_Label = Label(Stats_Frame, textvariable=char_var).grid(row=5, column=2)

# Item Frame Code
Label_Wpns.grid(row=0, column=0)
Label_Amr.grid(row=0, column=2)

Wpn_Button = Button(Items_Frame,text='+')
Wpn_Button.grid(row=0,column=1)

Amr_Button = Button(Items_Frame,text='+')
Amr_Button.grid(row=0,column=3)

Weapon_Text.grid(row=1, column=0,columnspan=2)
Armour_Text.grid(row=1, column=2,columnspan=2)

# Spell Frame Code

Label_spells.grid(row=0, column=0)
Spell_Text.grid(row=1, column=1)

Description_Frame.grid(row=0, column=0, columnspan=2)
Stats_Frame.grid(row=1, column=0, rowspan=2)
Items_Frame.grid(row=1, column=1)
Spells_Frame.grid(row=2, column=1)

root.mainloop()
