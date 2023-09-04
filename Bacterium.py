class Bacterium:
    def __init__(self, x=0, y=0, species="Escherichea coli", gram_negative=True, resistant=['penicillin'], hp=10, damage=1):
        self.x = x
        self.y = y
        self.species = species
        self.gram_negative = gram_negative
        self.resistant = resistant
        self.hp = hp
        self.damage = damage




# Create 3 instances
enemy1 = Bacterium(200, 300, "Staphilococcus aureus", False, [None], 20, 5)
enemy2 = Bacterium(140, 47, "Bacillus subtilis", False, ["penicillin", "cephalosporins"], 30, 11)
enemy3 = Bacterium(23, 310, "Vibrio cholerae", False, [None], 13, 7)