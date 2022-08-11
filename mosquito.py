import gene_utils as gu
import random as rnd


class Mosquito:
    species = "Canis familiaris"
    NEWBORN_EGGS = 4

    def __init__(self, sex='XX', age=0, male_gene='m', life_span=0, birth_cycle =2):
        self.life_span = life_span
        self.sex = sex
        self.age = age
        self.male_gene = male_gene
        self.birth_cycle = birth_cycle

    @classmethod
    def random_mosquito(new_mosquito, male_gene_percentage):
        new_mosquito = Mosquito()
        if rnd.random() > 0.5:
            new_mosquito.sex = 'XY'
        new_mosquito.age = int(rnd.uniform(0, 20))
        new_mosquito.life_span = abs(int(rnd.uniform(14, 28)) - new_mosquito.age)
        # life span is 2-4 weeks
        if rnd.random() < male_gene_percentage / 100 and new_mosquito.sex == 'XY':
            new_mosquito.male_gene = 'M'
            new_mosquito.age = 12
            new_mosquito.life_span = rnd.uniform(18,28)-new_mosquito.age
        else:
            new_mosquito.male_gene = 'm'
        return new_mosquito

    def __str__(self):
        return f"{self.sex}, {self.age},  {self.male_gene}, {self.life_span}, {self.birth_cycle}"

    def create_mosquito(self):
        new_mosquito = Mosquito()
        # sex process
        new_mosquito.life_span = int(rnd.uniform(14, 28))
        if rnd.random() <= 0.5:
            new_mosquito.sex = 'XX'
        else:
            new_mosquito.sex = 'XY'
        new_mosquito.male_gene = 'm'
        return new_mosquito

    def creatre_mosquito_with_male_gene(self):
        new_mosquito = Mosquito()
        # sex process
        new_mosquito.life_span = int(rnd.uniform(14, 28))
        new_mosquito.sex = 'XY'
        new_mosquito.male_gene = 'M'
        return new_mosquito

    def meeting(self, mosquito):
        all_new_mosquito = []

        if self.sex != mosquito.sex and (self.age >= 12 and mosquito.age >= 12):
            if self.birth_cycle <= 0 and mosquito.birth_cycle <= 0:
                if (self.sex == 'XY' and self.male_gene == 'M') or (mosquito.sex == 'XY' and mosquito.male_gene == 'M'):
                    for i in range(int(Mosquito.NEWBORN_EGGS / 2)):
                        new_mosquito = self.creatre_mosquito_with_male_gene()
                        all_new_mosquito.append(new_mosquito)
                else:
                    for i in range(Mosquito.NEWBORN_EGGS):
                        new_mosquito = self.create_mosquito()
                        all_new_mosquito.append(new_mosquito)
                if self.sex == 'XX':
                    self.birth_cycle = 3
                    mosquito.birth_cycle = 1
                else:
                    self.birth_cycle = 1
                    mosquito.birth_cycle = 3

        return all_new_mosquito
    def day_pass(self):
        self.life_span -= 1
        self.birth_cycle -= 1
        self.age += 1
