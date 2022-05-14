import datetime
import random as rnd
from aquarium import Aquarium
from mosquito import Mosquito
import matplotlib.pyplot as plt
import datetime


def the_simulator(run):
    day_counter = 1
    # in days
    simulation_length = 100
    initial_mosquito = 1000
    # the percentage of males with the "male gene"
    male_gene_percentage = 50
    # creating aquarium
    aquarium = Aquarium()
    aquarium.add_mosquito(initial_mosquito, male_gene_percentage)
    print(aquarium)
    # starting the simulation
    while day_counter <= simulation_length and len(aquarium.get_all_mosquito()) != 0:
        print("day number", day_counter)
        day_counter_ls = []
        plt.figure(run)
        plt.plot(day_counter, aquarium.get_total_mosquito(), 'b.')
        plt.plot(day_counter, aquarium.total_female, 'm.')
        # loop through all mosquitoes in the aquarium and connect between them
        mosquito_list = aquarium.get_all_mosquito()
        newborn_mosquito = []
        for mosquito in mosquito_list:
            # print("mosquito:",mosquito)
            newborn_mosquito = mosquito.meeting(rnd.choice(mosquito_list))
            aquarium.add_mosquitos_list(newborn_mosquito)

            mosquito.day_pass()
            if mosquito.life_span == 0:
                mosquito_list.remove(mosquito)
                aquarium.reduce_counters(mosquito)
        if day_counter % 5 == 0:
            print(aquarium)

        day_counter_ls.append(day_counter)
        day_counter += 1
    plt.xlabel('day number', fontsize=12)
    plt.ylabel('total mosquitoes couter', fontsize=12)
    plt.grid(True)
    my_title = 'total mosquito (init =' + str(initial_mosquito), 'male gene per =' + str(male_gene_percentage)
    plt.title(my_title, fontsize=18, color='blue')
    date = datetime.datetime.now()
    plt.savefig('data/' + str(date) + '-init-' + str(initial_mosquito) + '-per-' + str(male_gene_percentage) + '.png')

for i in range(3):
    the_simulator(i)
