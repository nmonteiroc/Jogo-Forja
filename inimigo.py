import random
from entidade import Entidade
class Inimigo(Entidade):
    def agir (self):
        return random.choice(['atacar', 'defender'])
    