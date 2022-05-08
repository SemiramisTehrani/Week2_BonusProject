# Bonus Project Week 2 
# You are Hercules, the greatest of the Greek Heroes! You have been tasked by King Eurystheus to 
# slay the vicious Nemean Lion, 
# defeat the impossible nine-headed Lernaean Hydra, 
# and capture the guard dog of the underworld—Cerberus.


# print("I am  Hercules, the greatest of the Greek Heroes! I have been tasked by King Eurystheus to slay ...the vicious Nemean Lion, defeat the impossible nine-headed Lernaean Hydra, and capture the guard dog of the underworld—Cerberus.")

# my version vefore Friday 101 meeting
# Hero = "Hercules"
# Enemy_List = ['Nemean_Lion' , 'Lernaean_Hydra' , 'Cerberus']
# Enemy_Attack_Names_List = ['vicious','Nine_Headed', 'Dog_gaurd_of_under_water']


# def Attack(Hercules_health, enemy_health) :
#     if Hercules_health or  enemy_health == False :  
#         outcome = print(" Hercules's or Enemy's health reached zero : fight is over ")
#     else:
#         outcome = print(" Hercules's or Enemy's health is Ok : fighting continues ")
#     return outcome


# print("Enter Hercules's health level  1 (strong) or 0 (weak) : ")

# Hercules_health = int(input())

# print("Enter Enemy's health level  1 (strong) or 0 (weak) : ")
# Enemy_health = int(input())

# Attack_health_result = Attack(Hercules_health, Enemy_health)



# my version after Friday 101 meeting

print("I am  Hercules, the greatest of the Greek Heroes! I have been tasked by King Eurystheus to slay ...the vicious Nemean Lion, defeat the impossible nine-headed Lernaean Hydra, and capture the guard dog of the underworld—Cerberus.")
Hero = "Hercules"
opponent_Name_List = ["Nemean_Lion" , "Lernaean_Hydra" , "Cerberus"]
opponent_NicName_List = ['vicious','Nine_Headed', 'Dog_gaurd_of_under_water']


Hercues_dic = {
    "attack_power_level" : 100, 
    "health_level"       : 200
    }

opponent_dic = {
    "attack_power_level" : 50, 
    "health_level"       : 110
    }

opponent_name_dic = {
   "Nemean_Lion"    : "vicious",
   "Lernaean_Hydra" : "Nine_Headed",
   "Cerberus"       : "Dog_gaurd_of_under_water"
}


# attacker : Hercules
# defender : three guys to be killed
def attack(attacker, defender) : 
    battle_result_health = defender["health_level"] - attacker["attack_power_level"]
    print(f" The defender's health is now {battle_result_health}")

def run_game() :attack(Hercues_dic, opponent_dic);attack(opponent_dic,Hercues_dic)

run_game()

