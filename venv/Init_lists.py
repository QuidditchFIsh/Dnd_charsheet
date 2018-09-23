import json
import Char

Path_to_Spells = 'C:/Users/nye42/PycharmProjects/dnd/dnd-spells-master/spells.json'
Path_to_Martial_Melee_Weapons = 'C:/Users/nye42/PycharmProjects/dnd/dnd5-weapons-json-master/json/martialMeleeWeapons.json'
Path_to_Martial_Ranged_Weapons = 'C:/Users/nye42/PycharmProjects/dnd/dnd5-weapons-json-master/json/martialRangedWeapons.json'
Path_to_Firearms = 'C:/Users/nye42/PycharmProjects/dnd/dnd5-weapons-json-master/json/firearms.json'
Path_to_Simple_Melee_Weapons = 'C:/Users/nye42/PycharmProjects/dnd/dnd5-weapons-json-master/json/simpleMeleeWeapons.json'
Path_to_Simple_Ranged_Weapons = 'C:/Users/nye42/PycharmProjects/dnd/dnd5-weapons-json-master/json/simpleRangedWeapons.json'
Path_to_Levels = 'C:/Users/nye42/PycharmProjects/dnd/Levels.json'
with open(Path_to_Spells, encoding='utf-8') as file:
    spell_data = json.load(file)
with open(Path_to_Levels, encoding='utf-8') as level_file:
    level_data = json.load(level_file)

'''
    level up data
 
    each of the lists in this lists will be a level
    within the lists the elements will be the description for each class in the order given in the phb
    Order of classes 
    Barbarian
    Bard
    Cleric
    Druid
    Fighter
    Monk
    Paladin
    Ranger
    Rouge
    Sorcerer
    Warlock
    Wizard
    '''

level_up_descp = []

for i in range(0,19):
    level_up_descp.append([])

for cls in level_data['Levels']:
    for i in range (1,20):
        level_up_descp[i-1].append(cls[str(i)])

#spells by class

Ranger_spells = []
Barbarian_spells = []
Paladin_spells = []
Bard_spells = []
Cleric_spells = []
Druid_spells = []
Fighter_spells = []
Monk_spells = []
Rouge_spells = []
Sorcerer_spells = []
Warlock_spells = []
Wizard_spells = []



for spell in spell_data['spells']:
    a = spell['class']
    for c in a.split(', '):
        if(c == 'Ranger'):
             Ranger_spells.append(spell['name'])
        elif(c=='Barbarian'):
            Barbarian_spells.append(spell['name'])
        elif(c=='Paladin'):
            Paladin_spells.append(spell['name'])
        elif(c=='Bard'):
            Bard_spells.append(spell['name'])
        elif (c == 'Cleric'):
            Cleric_spells.append(spell['name'])
        elif (c == 'Druid'):
            Druid_spells.append(spell['name'])
        elif (c == 'Fighter'):
            Fighter_spells.append(spell['name'])
        elif (c == 'Monk'):
            Monk_spells.append(spell['name'])
        elif (c == 'Rouge'):
            Rouge_spells.append(spell['name'])
        elif (c == 'Sorcerer'):
            Sorcerer_spells.append(spell['name'])
        elif (c == 'Warlock'):
            Warlock_spells.append(spell['name'])
        elif (c == 'Wizard'):
            Wizard_spells.append(spell['name'])

#spells by level
spell_name = []

spell_lvl_1=[]
spell_lvl_2=[]
spell_lvl_3=[]
spell_lvl_4=[]
spell_lvl_5=[]
spell_lvl_6=[]
spell_lvl_7=[]
spell_lvl_8=[]

for spell in spell_data['spells']:
    if(spell['level'] == '1st-level'):
        spell_lvl_1.append(spell['name'])
    elif(spell['level'] == '2nd-level'):
        spell_lvl_2.append(spell['name'])
    elif(spell['level'] == '3rd-level'):
        spell_lvl_3.append(spell['name'])
    elif(spell['level'] == '4th-level'):
        spell_lvl_4.append(spell['name'])
    elif(spell['level'] == '5th-level'):
        spell_lvl_5.append(spell['name'])
    elif(spell['level'] == '6th-level'):
        spell_lvl_6.append(spell['name'])
    elif(spell['level'] == '7th-level'):
        spell_lvl_7.append(spell['name'])
    elif(spell['level'] == '8th-level'):
        spell_lvl_8.append(spell['name'])

#combined weapons

