#12/02/26: Roll the dice V1
from easygui import *
import random

player_num = 0

for i in range (0,2):
    die_1 = random.randint(1,6)
    die_2 = random.randint(1,6)
    total = die_1 + die_2
    player_num += 1
    msgbox("Player " + str(player_num) + " you rolled: \n\n" + str(die_1) + " and " + str(die_2) + "\n\nTotal:" + str(total))

    

    
    

    
    
    
