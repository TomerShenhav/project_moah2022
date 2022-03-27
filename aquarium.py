from fish import Fish


class Aquarium:
    l_fish = []

    def __str__(self):
        mystr = 'My Aquarium\n===================='
        for fish in self.l_fish:
            mystr = mystr + '\n' + str(fish)

        mystr = mystr + f'\nNumber od Fish in aquarium: {len(self.l_fish)}'
        return mystr

    def add_fish(self, amount_of_fish):
        for i in range(amount_of_fish):
            self.l_fish.append(Fish.random_fish())
