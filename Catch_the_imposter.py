import random
import timer
print("""
     Hello Gamer!!!, Hope you're having a great day!
      So wanna make it a Better one, Lets get started
             Welcome to the chor-police game
                So lets get to the rules
          This is just a basic killer-cops game
There are 10 characters in all from which you'll have to choose 1
      You will be either a cop, a killer or a civilian
*****************************************************************
                        🔪🔪KILLER🔪🔪
=================================================================
1. You have to try and kill all the civilians 1 by 1
2. If you try to kill a cop you get caught
3. If all the civilians get killed then killers win
*****************************************************************
*****************************************************************
                        👮👮👮COP👮👮👮
=================================================================
1. You have to try and catch all the killers before civilians die
2. You have to check if you want to catch character civilians have
   suspected
3. If all the killers get caught then cops and civilians win
*****************************************************************
*****************************************************************
                      🧒🧒CIVILIANS🧒🧒
=================================================================
1. You just have to suspect a killer and help cops catch them
2. If all the killers get caught then cops and civilians win
*****************************************************************

*****************************************************************
            😊😊😊HOPE YOU ENJOY THE GAME😊😊😊
*****************************************************************""")
characters={1:'Adam',2:'Charls',3:'Lucy',4:'Rocky',5:'Spiky',6:'Jullie',7:'Rita',8:'Drake',9:'Dan',10:'Dory'}
print(characters)
while True:
    try:
        myself=characters[int(input("Enter the number(key) of character you want to be:"))]
        print(f"Hello {myself}!!!")
        break
    except KeyError:
        print("Key an integer between (1,10)\n")
while True:
    num_killer=int(input("\nEnter number of killers(1/2):"))
    num_cop=int(input("\nEnter number of Cops(1/2):"))
    if 0<num_cop<3 and 0<num_killer<3:
        break
    print("""
🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴
Both number of killer and number of cops must be (1 or 2)
🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴""")
players_cop_dummy=list(characters.values())
players_cop=players_cop_dummy[:]
players_killer=players_cop_dummy[:]
civilians=players_cop_dummy[:]
players=players_cop_dummy[:]
killer=[]
cops=[]
while num_killer:
    a=random.choice(civilians)
    players_killer.remove(a)
    civilians.remove(a)
    killer.append(a)
    if a==myself:
        print("You are an Killer!!")
    num_killer-=1
while num_cop:
    b=random.choice(civilians)
    players_cop.remove(b)
    civilians.remove(b)
    cops.append(b)
    if b==myself:
        print("You are a COP!")
    num_cop-=1
def imposter(killer,cops,players_killer,players):
    if myself in killer and myself in players:
        k=input("enter player you want to kill:")
        while True:
            try:
                if k in players:
                    if k in cops:
                        print("You were caught")
                        killer.remove(myself)
                        players.remove(myself)
                    else:
                        print(f"You killed {k}")
                        players_killer.remove(k)
                        players.remove(k)
                break
            except: 
                print(f"kill a player from {players_killer}")
    else:
        k=random.choice(players_killer)
        if k in cops:
            print("killer tried to kill the cop but was caught")
            rem=killer.pop(0)
            players.remove(rem)
        else:
            players_killer.remove(k)
            players.remove(k)
def civilian():
    if myself in civilians and myself in players:
        sus=input(f"Do you suspect anyone from {players} or Skip:")
        if sus in players:
            return (sus)
        else:
            pass
    else:
        sus=random.choice(players)
        return sus
def cop(killer,cops,players_cop,players):
    civil_sus=civilian()
    if myself in cops and myself in players:
        choose=input(f"Civilians suspect {civil_sus} do you want remove them??(y|n):")
        if choose == 'y' or choose=='Y':
            if civil_sus in killer:
                print("You caught the killer")
                killer.remove(civil_sus)
                players.remove(civil_sus)
                players_cop.remove(civil_sus)
            else:
                print(f"{civil_sus} was not the killer")
                players_cop.remove(civil_sus)
                players.remove(civil_sus)
        else:
            while True:
                k=input("enter player you suspect or type No if you dont wanna suspect  any one:")
                if k in killer:
                    print("You caught the killer")
                    killer.remove(k)
                    players_cop.remove(k)
                    players.remove(k)
                    break
                elif k in players_cop:
                    print(f"{k} was not the killer")
                    players_cop.remove(k)
                    players.remove(k)
                    break
                elif k=='no' or k=='No' or k=='NO':
                    break
                else:
                    print(f"""
🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴
Enter a sus form {players_cop} or type No if you dont suspect anyone
🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴""")                
    else:
        k=random.choice(players_killer)
        if k in killer:
            print("killer was caught")
            rem=killer.pop(0)
            players_cop.remove(rem)
            players.remove(rem)
        else:
            players_cop.remove(k)
            players.remove(k)
if myself in civilians:
    print("You are a civilian")
while True:
    if killer==[]:
        print("Cops/civilians win")
        break
    elif players_killer==cops:
        print("Killers win")
        break
    else:
        pass
    imposter(killer,cops,players_killer,players)
    cop(killer,cops,players_killer,players)
print("hope you enjoyed the game")


