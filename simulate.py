import random as rnd
from aquarium import Aquarium
import matplotlib.pyplot as plt
import datetime

ls_graph_result = []
ls_graph_result_mosquito = []
male_gene_percentage = 0
initial_mosquito = 50
# the percentage of males with the "male gene"

def the_simulator(run_num):
    day_counter = 1
    # in days
    simulation_length = 150
    max_mosquito = 0
    # creating aqu'arium
    aquarium = Aquarium()
    aquarium.add_mosquito(initial_mosquito, male_gene_percentage)
    print(aquarium)
    print(male_gene_percentage)

    # starting the simulation
    total_mosquito_list = []
    total_female = []
    day_counter_ls = []
    l_ratio_male_gene = []
    while day_counter <= simulation_length and len(aquarium.get_all_mosquito()) != 0:
        print("day number", day_counter)
        # Initialise the subplot function using number of rows and columns

        mosquito_list = aquarium.get_all_mosquito()
        newborn_mosquito = []
        for mosquito in mosquito_list:
            # print("mosquito:",mosquito)
            newborn_mosquito = mosquito.meeting(rnd.choice(mosquito_list))
            aquarium.add_mosquitos_list(newborn_mosquito)

            mosquito.day_pass()
            if mosquito.life_span <= 0:
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
        day_counter_ls.append(day_counter)
        if max_mosquito < len(aquarium.l_mosquito):
            max_mosquito = len(aquarium.l_mosquito)
        day_counter += 1
    ls_graph_result_mosquito.append(max_mosquito)
    ls_graph_result.append({'x': day_counter_ls,'y': total_mosquito_list})
    # graph 1
    plt.figure(str(run_num)+'-1')

    plt.plot(day_counter_ls, total_mosquito_list, 'b.')
    plt.plot(day_counter_ls, total_female, 'm.')
    plt.xlabel('day number', fontsize=12)
    plt.ylabel('total mosquitoes couter', fontsize=12)
    my_title = 'total mosquito (init =' + str(initial_mosquito), 'male gene per =' + str(male_gene_percentage)
    plt.title(my_title)
    plt.grid(True)

    date = datetime.datetime.now()
    plt.savefig('data/' + str(date) + '-init-' + str(initial_mosquito) + '-per-' + str(male_gene_percentage) + '-1.png',dpi = 300)

    # graph 2
    plt.figure(str(run_num)+'-2')

    plt.plot(day_counter_ls, l_ratio_male_gene, 'b.')
    plt.xlabel('day number', fontsize=12)
    plt.ylabel('ratio', fontsize=12)
    plt.ylim((male_gene_percentage/100)-0.25,1)
    my_title = 'ratio between mosquito with gene to all male (init =' + str(initial_mosquito), 'male gene per =' + str(male_gene_percentage)
    plt.title(my_title)
    plt.grid(True)

    date = datetime.datetime.now()
    plt.savefig('data/' + str(date) + '-init-' + str(initial_mosquito) + '-per-' + str(male_gene_percentage) + '-2.png',
                dpi=300)
    plt.close()


for i in range (1):
    the_simulator(i)


plt.figure('summary')
plt.hist(ls_graph_result_mosquito, )
plt.xlabel('max mosquitoes', fontsize=12)
plt.ylabel('amount of simulations', fontsize=12)
my_title = 'max mosquitoes per simulation (init =' + str(initial_mosquito), 'male gene per =' + str(male_gene_percentage)
plt.title(my_title)
plt.grid(True)

date = datetime.datetime.now()
plt.savefig('data/' + str(date) + '-init-' + str(initial_mosquito) + '-per-' + str(male_gene_percentage) + '-3.png',
            dpi=300)
print(ls_graph_result_mosquito)