import gene_utils as gu
import random as rnd

class Fish:
    species = "Canis familiaris"

    def __init__(self, sex='XX', age=0, spotting='B', fin_color='G', tail_shape='F', tail_color='T'):
        self.sex = sex
        self.age = age
        self.spotting = spotting
        self.fin_color = fin_color
        self.tail_shape = tail_shape
        self.tail_color = tail_color

    def __str__(self):
        return f"{self.sex}, {self.age}, {self.spotting}, {self.fin_color}, {self.tail_shape}, {self.tail_color}"

    def newborn(self, fish):
        if self.sex != fish.sex:
            newfish = Fish()
            # sex proccess
            if rnd.random > 0.5:
                newfish.sex = 'XY'

    gu.calc_newborn_gene('B', 'b')
