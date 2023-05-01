from src.util.color import Color
from src.util.constants import SCREEN_WIDTH


# Essa classe representa um robô
class Robot:

    # Construtor da classe robô
    def __init__(self, name, appearance, color, lore, attack_skills):
        self.name = color + name + Color.reset
        self.appearance = appearance
        self.color = color
        self.lore = lore
        self.attack_skills = attack_skills
        self.shield = 100
        self.life = 100
        self.energy = 100

    # Método onde o robô ataca um adversário de acordo com o tipo do ataque
    def attack(self, enemy_robot, attack_skill):
        if attack_skill.energy_consumption > self.energy:
            warning = f'🔌 {self.name} NÃO TEM ENERGIA SUFICIENTE PARA ESSE ATAQUE 🔌'
            print(f'|{warning.center(SCREEN_WIDTH+6)}|')
            return False
        enemy_robot.life -= min(enemy_robot.life, attack_skill.damage)
        self.energy -= attack_skill.energy_consumption
        warnings = [
            f'✅ {self.name} ACERTOU O ATAQUE ✅',
            f'💥 {enemy_robot.name} SOFREU {attack_skill.damage} DE DANO 💥',
            f'⏬ {self.name} CONSUMIU {attack_skill.energy_consumption} DE ENERGIA ⏬'
        ]
        for warning in warnings:
            print(f'|{warning.center(SCREEN_WIDTH+6)}|')
        return True

    # Método onde o robô defende um ataque do adversário
    def defend(self, enemy_robot, attack_skill):
        warnings = []
        damage = attack_skill.damage // 2
        energy_consumption = damage / 2
        warnings.append(f'🚫 {self.name} DEFENDEU O ATAQUE 🚫')
        # sem escudo ou sem energia
        if self.shield == 0 or self.energy == 0:
            self.life -= min(self.life, damage)
            warnings.append(f'💥 {self.name} SOFREU {damage} DE DANO 💥')
        else:
            # proporção de mais escudo que energia ou proporção igual
            if self.shield >= self.energy * 2:
                energy_consumption = min(self.energy, energy_consumption)
                damage_shield = int(energy_consumption * 2)
                energy_consumption = int(energy_consumption)
            # proporção de mais energia que escudo
            else:
                damage_shield = min(self.shield, damage)
                energy_consumption = damage_shield // 2
            self.shield -= damage_shield
            self.energy -= energy_consumption
            warnings.append(f'🤖 {self.name} PERDEU {damage_shield} DE ESCUDO 🤖')
            warnings.append(f'⏬ {self.name} GASTOU {energy_consumption} DE ENERGIA PARA ARMAR O ESCUDO ⏬')
            damage_life = damage - damage_shield
            if damage_life != 0:
                self.life -= min(self.life, damage_life)
                warnings.append(f'💥 {self.name} SOFREU {damage_life} DE DANO 💥')
        enemy_robot.energy -= attack_skill.energy_consumption
        warnings.append(f'⏬ {enemy_robot.name} CONSUMIU {attack_skill.energy_consumption} DE ENERGIA ⏬')
        for warning in warnings:
            print(f'|{warning.center(SCREEN_WIDTH+6)}|')
        return True

    # Método onde o robô esquiva do ataque do inimigo
    def dodge(self, enemy_robot, attack_skill):
        enemy_robot.energy -= attack_skill.energy_consumption
        warnings = [
            f'💨 {self.name} ESQUIVOU DO ATAQUE 💨',
            f'⏬ {enemy_robot.name} CONSUMIU {attack_skill.energy_consumption} DE ENERGIA ⏬'
        ]
        for warning in warnings:
            print(f'|{warning.center(SCREEN_WIDTH+6)}|')
        return True

    # Método onde o robô recarrega suas energias
    def recharge_energy(self):
        if self.energy == 100:
            warning = f'🔋 SUA ENERGIA JÁ ESTÁ NO MÁXIMO. NÃO É POSSIVÉL CARREGÁ-LA. 🔋'
            print(f'|{warning.center(SCREEN_WIDTH-4)}|')
            return False
        recharge_load = min((100 - self.energy), 20)
        self.energy += recharge_load
        warning = f'🔋 {self.color + self.name + Color.reset} CARREGOU {recharge_load} DE ENERGIA 🔋'
        print(f'|{warning.center(SCREEN_WIDTH+16)}|')
        return True

    # Verifica se a vida e a energia do robô são maior que zero
    def is_on(self):
        return self.energy > 0 and self.life > 0
