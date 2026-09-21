game_over = False
health = 10

print("WOULD YOU LIKE TO ENTER THE DUNGEON?")
enter_dungeon = input("(yes/no):")
if enter_dungeon == "yes":
    print("You step under the archway, led by flickering candles deeper into the dark.")
    level = 1
if enter_dungeon == "no":
    print("You turn away from the dungeon. 'Oh hell nah', and head back to your village. (basically you're a loser)")
    game_over = True
if game_over == True:
    print("GAME OVER (get a life moron)")

if level == 1:
    print("You descend down a dark staircase, into a room with a large bottomless pit in the middle.")
    method_over_pit = input("How do you get across? (jump, climb, rope)")
if method_over_pit == "jump":
    print("You step back and take a running start, jumping over the pit. You land hard on your shoulder and roll to a stop. Take 1 damage asshole.")
    health = health - 1
    print("health = ", health, "(fuck you)")
if method_over_pit == "climb":
    print("You try to climb across using the ivy thick on the walls, but you slip and nearly fall into the void. You manage to grab the ledge and pull youreself up at the last minute. (your lucky I'm feeling gracious today)")
if method_over_pit == "rope":
    print("You tie your rope into a lasso and throw it across the pit, where it catches on a rock. The rock slips slightly as you pull yourself up, but you make it across in one piece.")

level = 2
print("You make your way through a door and into a room where the floor is covered in old human bones. As you step inside, the bones shift and move together, attachign themselves to form a human skeleton. It grabs a sword and turns towards you, flames lighting up it's eye sockets.")
print("The skeleton lunges forward and swings it's sword around, slashing through your flesh. You take two damage.")
health = health - 2
print("health = ", health, "(ouchie! go cry about it!)")
skeleton_health = 5
first_action_skeleton_vulnerable = False
first_action_vulnerable = False
first_action_parry = False
skeleton_battle_first_move = input("You're move! (attack, defend, run, heal, flirt)")
if skeleton_battle_first_move == "attack":
    print("You jab your sword at the skeleton, but your blade passes through its rib cage. It looks down at your sword and then up at you in dissapointment at your stupidity.")
    first_action_vulnerable = True
if skeleton_battle_first_move == "defend":
    print("You raise your sword in a defenseive position, ready to parry his next attack.")
    first_action_parry = True
if skeleton_battle_first_move == "run":
    print("You turn like a coward, scream like a baby, and trip over a rock like an idiot, landing face first on the floor as the skeleton descends upon you.")
    first_action_vulnerable = True
if skeleton_battle_first_move == "heal":
    print("You reach into your bag and pull out a healing potion, popping the cork and gulping it down. Congratulations you get health and stuff... exciting")
    health = health + 2
    print("health = ", health, "(You know I'm a little dissapointed, I wanted to see you die a lot quicker.)")
    first_action_vulnerable = True
if skeleton_battle_first_move == "flirt":
    print("You wink and trace the front of your pants suggestively. The skeleton drops his sword and his jaw hangs open. If he had a dick it would be up.")
    first_action_skeleton_vulnerable = True

if first_action_skeleton_vulnerable == True:
    print("The skeleton is distracted by your flirtatious behavior, and is too captivated to move.")
if first_action_parry == True: 
    print("The skeleton swings his sword down at your, but you parry it, sparks flying off your blade as you block it.")
if first_action_vulnerable == True:
    print("The skeleton swings his sword down at you, completely caught off guard, and you take... yeesh... 3 points of damage.")
    health = health - 3
    print("health = ", health, "(thats just embarrasing)")
