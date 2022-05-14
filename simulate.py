import random as rnd
from aquarium import Aquarium
from fish import Fish
day_counter = 1
#in days
simulation_length = 2
initial_mosquito = 50
#creating aquarium
aquarium = Aquarium()
aquarium.add_fish(initial_mosquito)
print(aquarium)
#starting the simulation
while(day_counter<=simulation_length):
    print("day number",day_counter)
    #loop through all mosquitoes in the aquarium and connect between them
    fish_list = aquarium.get_all_fish()
    for fish in fish_list:
        print("fish:",fish)
        newborn_fish = fish.meeting(rnd.choice(fish_list))
        print("after a meeting, the number of new fish is:", len(newborn_fish))
        fish_list.extend(newborn_fish)
        print(len(fish_list))
    day_counter+=1


