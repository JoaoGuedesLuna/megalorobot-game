# Classe que representa uma habilidade de ataque
class AttackSkill:

    # Construtor da classe Habilidade de Ataque
    def __init__(self, name, description, damage, energy_consumption):
        self.name = name
        self.description = description
        self.damage = damage
        self.energy_consumption = energy_consumption
