import datetime
import random as rnd
from aquarium import Aquarium
from mosquito import Mosquito
import matplotlib.pyplot as plt
import datetime

male_gene_percentage = 30
initial_mosquito = 10
# the percentage of males with the "male gene"
on = True
def the_simulator(run):
    day_counter = 1
    # in days
    simulation_length = 150
    male_gene_percentage1 = male_gene_percentage
    initial_mosquito1 = initial_mosquito
    # creating aqu'arium
    aquarium = Aquarium()
    aquarium.add_mosquito(initial_mosquito1, male_gene_percentage1)
    print(aquarium)


    # starting the simulation
    total_mosquito_list = []
    total_female = []
    day_counter_ls = []
    l_ratio_male_gene = []
    previous_day_amount = 0
    while day_counter <= simulation_length and len(aquarium.get_all_mosquito()) != 0:
        print("day number", day_counter)
        # Initialise the subplot function using number of rows and columns

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
        total_mosquito_list.append(aquarium.get_total_mosquito())
        total_female.append(aquarium.total_female)
        ratio = 0
        if aquarium.total_male > 0:
            ratio = aquarium.total_male_gene / aquarium.total_male
        l_ratio_male_gene.append(ratio)
        if day_counter>1:
            growth_ratio = len(total_mosquito_list)/previous_day_amount
        day_counter_ls.append(day_counter)
        day_counter += 1
        previous_day_amount = len(total_mosquito_list)
    # figure, axis = plt.subplots(1, 2)
    # figure = run
    # axis[0].plot(day_counter, aquarium.get_total_mosquito(), 'b.')

    # axis[0].set_title(my_title, fontsize=18, color='blue')
    if on:
        # graph 1
        plt.figure(str(run)+'-1')

        plt.plot(day_counter_ls, total_mosquito_list, 'b.')
        plt.plot(day_counter_ls, total_female, 'm.')
        plt.xlabel('day number', fontsize=12)
        plt.ylabel('total mosquitoes couter', fontsize=12)
        my_title = 'total mosquito (init =' + str(initial_mosquito1), 'male gene per =' + str(male_gene_percentage1)
        plt.title(my_title)
        plt.grid(True)

        date = datetime.datetime.now()
        plt.savefig('data/' + str(date) + '-init-' + str(initial_mosquito1) + '-per-' + str(male_gene_percentage1) + '-1.png',dpi = 300)

        # graph 2
        plt.figure(str(run)+'-2')

        plt.plot(day_counter_ls, l_ratio_male_gene, 'b.')
        plt.xlabel('day number', fontsize=12)
        plt.ylabel('ratio', fontsize=12)
        plt.ylim((male_gene_percentage1/100)-0.25,1)
        my_title = 'ratio between mosquito with gene to all male (init =' + str(initial_mosquito1), 'male gene per =' + str(male_gene_percentage)
        plt.title(my_title)
        plt.grid(True)

        date = datetime.datetime.now()
        plt.savefig('data/' + str(date) + '-init-' + str(initial_mosquito1) + '-per-' + str(male_gene_percentage1) + '-2.png',
                    dpi=300)

    # graph 3
    plt.figure(str(run) + '-3')

    plt.plot(l_ratio_male_gene, day_counter_ls, 'b.')
    plt.xlabel('male gene percentage', fontsize=12)
    plt.ylabel('days took to obliterate', fontsize=12)
    my_title = 'the effect of the male gene percentage on the amount of days that it takes the mosquitoes to obliterate (init =' + str(initial_mosquito1), 'male gene per =' + str(
        male_gene_percentage1)
    plt.title(my_title)
    plt.grid(True)

    date = datetime.datetime.now()
    plt.savefig('data/' + str(date) + '-init-' + str(initial_mosquito1) + '-per-' + str(male_gene_percentage1) + '-3.png',
                dpi=300)

for i in range (3):
    if not on:
        the_simulator(i)
    else:
        initial_mosquito += 10
        the_simulator(i)


