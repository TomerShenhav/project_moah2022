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

    def create_newborn(self, fish):
        if self.sex != fish.sex:
            newfish = Fish()
            # sex process
            if rnd.random() > 0.5:
                newfish.sex = 'XY'
            newfish.spotting = gu.calc_newborn_gene(self.spotting, fish.spotting)
            newfish.fin_color = gu.calc_newborn_gene(self.fin_color, fish.fin_color)
            newfish.tail_shape = gu.calc_newborn_gene(self.tail_shape, fish.tail_shape)
            newfish.tail_color = gu.calc_newborn_gene(self.tail_color, fish.tail_color)
            return newfish
