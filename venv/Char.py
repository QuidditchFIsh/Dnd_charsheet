#script to store all the data about the character instead of using a file. This data can then be used to write out to
#the save file

Name = 'None'
clss  = 'None'
level = 1
race  = 'None'
alignment = 'None'
current_hit_points = 0
max_hit_points = 0
AC = 0
str = 0
dex = 0
const = 0
wis = 0
int = 0
char = 0
weapons = 'None'
armour = 'None'
spells = 'None'

def save():
    try:
        file = open("Saves/" + Name + ".txt", "w")
        file.write("hellooo")
        file.write(str(Name) + ',' + str(clss) + ',' + str(level) +
                   ',' + str(race) + ',' + str(alignment) + ',' + str(max_hit_points)
                   + ',' + str(AC) + ',' + str(str) + ',' + str(dex) + ',' + str(const)+ ',' + str(int)+ ',' + str(char)
                   + ',' + str(weapons)+ ',' + str(armour)+ ',' + str(spells))
        file.close()
    except:
        print("The File Doesn't Exist")





#need to add a save method to this file



