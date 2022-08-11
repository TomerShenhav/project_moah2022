from mosquito import Mosquito


class Aquarium:
    l_mosquito = []
    total_male = 0
    total_female = 0
    total_male_gene = 0

    def __init__(self):
        self.l_mosquito = []
        self.total_male_gene = 0
        self.total_male = 0
        self.total_female = 0

    def __str__(self):
        mystr = '====================\nMy Aquarium'

        ratio = 0
        if self.total_male > 0:
            ratio = self.total_male_gene / self.total_male
        mystr = mystr + f'\nNumber of mosquito in aquarium:' + str(len(self.l_mosquito)) + f'\nNumber of males:' + str(
            self.total_male) + f'\nNumber of males with the "male gene":' + str(
            self.total_male_gene) +' ('+ str('{0:.2f}'.format(ratio))+f') is the ration between males with male gene to total males' + f'\nNumber of females:' + str(self.total_female)

        return mystr

    def update_counters(self,mylist):
        for mos in mylist:
            if mos.sex == 'XX':
                self.total_female += 1
            else:
                if mos.male_gene == 'M':
                    self.total_male_gene += 1
                self.total_male += 1

    def add_mosquito(self, amount_of_mosquito, male_gene_percetage):
        for i in range(amount_of_mosquito):
            self.l_mosquito.append(Mosquito.random_mosquito(male_gene_percetage))
        self.total_male = 0
        self.total_female = 0
        self.total_male_gene = 0
        self.update_counters(self.l_mosquito)

    def get_all_mosquito(self):
        return self.l_mosquito

    def get_total_mosquito(self):
        return(len(self.l_mosquito))

    def add_mosquitos_list(self, newborn_mosquito):
        self.l_mosquito.extend(newborn_mosquito)
        self.update_counters(newborn_mosquito)

    def reduce_counters(self,mos):
        if mos.sex == 'XX':
            self.total_female -= 1
        else:
            if mos.male_gene == 'M':
                self.total_male_gene -= 1
            self.total_male -= 1

