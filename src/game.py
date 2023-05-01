from random import randint
from time import sleep
from src.draw import Draw
from src.model.mech import Mech
from src.model.catapult import Catapult
from src.model.madcat import Madcat
from src.model.marauder import Marauder
from src.model.rifleman import Rifleman
from src.model.atlas import Atlas
from src.util.color import Color
from src.util.constants import SCREEN_WIDTH
from src.util.display import Display


# Classe principal do jogo
class Game:

    # Construtor ca classe Game
    def __init__(self):
        self.playing = False
        self.robots = [Mech, Catapult, Madcat, Marauder, Rifleman, Atlas]

    # Inicia o jogo
    def start(self):
        self.playing = True
        Display.clear_screen()
        self.show_title_menu()
        self.show_rules_menu()
        while self.playing:
            user_option = self.show_options_menu()
            if user_option == 'X':
                self.playing = False
            elif user_option == '1':
                self.show_game_mode_menu()
            elif user_option == '2':
                self.show_character_menu()
        self.show_bye_bye_menu()

    # Exibe o menu de título do jogo
    def show_title_menu(self):
        Draw.draw_title_menu()
        input()
        Display.clear_screen()

    # Exibe um menu explicando as regras do jogo
    def show_rules_menu(self):
        Draw.draw_rules_menu()
        input()
        Display.clear_screen()

    # Exibe o menu de opções do jogo
    def show_options_menu(self):
        valid_options = "12X"
        while True:
            Draw.draw_options_menu()
            user_option = input().upper().strip()
            Display.clear_screen()
            if len(user_option) == 1 and user_option in valid_options:
                return user_option

    # Exibe um menu onde o usuário pode escolher o modo de jogo
    def show_game_mode_menu(self):
        valid_options = "12"
        user_option = "  "
        while len(user_option) != 1 or user_option not in valid_options:
            Draw.draw_game_mode_menu()
            user_option = input().upper().strip()
            Display.clear_screen()
        if user_option == "1":
            self.show_single_player_mode_robot_choice_menu()
        else:
            self.show_multiplayer_mode_robot_choice_menu()

    # Exibe o menu onde o usuário poderá escolher seu robô de combate para o modo jogo solo
    def show_single_player_mode_robot_choice_menu(self):
        user_robot = self.show_robot_choice_menu(Draw.draw_single_player_robot_choice_menu)
        machine_robot = self.robots[randint(0, len(self.robots) - 1)]
        while machine_robot == user_robot:
            machine_robot = self.robots[randint(0, len(self.robots) - 1)]
        self.show_battle_menu(user_robot(), machine_robot(), self.get_machine_option)

    # Exibe o menu onde os usuários poderão escolher o seu robô no modo multijogador
    def show_multiplayer_mode_robot_choice_menu(self):
        player1_robot = self.show_robot_choice_menu(Draw.draw_player_one_robot_choice_menu)
        player2_robot = self.show_robot_choice_menu(Draw.draw_player_two_robot_choice_menu)
        if player1_robot == player2_robot:
            player1_robot = player1_robot()
            player1_robot.name += " 1"
            colors_list = Color.list()
            player2_color = colors_list[randint(0, len(colors_list) - 1)]
            while player1_robot.color == player2_color:
                player2_color = colors_list[randint(0, len(colors_list) - 1)]
            player2_robot = player2_robot(player2_color)
            player2_robot.name += " 2"
        else:
            player1_robot = player1_robot()
            player2_robot = player2_robot()
        self.show_battle_menu(player1_robot, player2_robot, self.get_user_option)

    # Exibe o menu de escolha do robô e retorna uma referência para o tipo de robo escolhido
    def show_robot_choice_menu(self, draw_menu):
        valid_options = "123456"
        user_option = "  "
        while len(user_option) != 1 or user_option not in valid_options:
            draw_menu()
            user_option = input().upper().strip()
            Display.clear_screen()
        return self.robots[int(user_option) - 1]

    # Exibe o menu de batalha
    def show_battle_menu(self, robot1, robot2, method):
        current_option = ""
        round = 0
        while current_option != "X":
            Draw.draw_robots_status_bar(robot1, robot2)
            Draw.draw_robots_appearance(robot1, robot2)
            if not robot2.is_on():
                if method == self.get_machine_option:
                    self.show_you_won_message()
                else:
                    self.show_player_one_won_message(robot1.color)
                return
            elif not robot1.is_on():
                if method == self.get_machine_option:
                    self.show_you_lost_message()
                else:
                    self.show_player_two_won_message(robot2.color)
                return
            if round % 2 == 0:
                current_robot = robot1
                enemy_robot = robot2
                current_option = self.get_user_option(robot1)
            else:
                current_robot = robot2
                enemy_robot = robot1
                current_option = method(robot2)
            try:
                played = self.play_round(current_robot, enemy_robot, int(current_option))
                round = round + 1 if played else round
            except ValueError:
                pass
            print(f'|{" " * (SCREEN_WIDTH-2)}|')
            print("-" * SCREEN_WIDTH)
            input()
            Display.clear_screen()

    # Método que retorna a opção do usuário na rodada
    def get_user_option(self, user_robot):
        print(f'|{user_robot.name.center(SCREEN_WIDTH+8)}|')
        Draw.draw_battle_menu_options(user_robot)
        valid_options = "1234X"
        print(f'|{" " * (SCREEN_WIDTH-2)}|')
        user_options = input(f'|{"🎮 OPÇÃO: ".rjust(SCREEN_WIDTH//2 + 2)}').upper().strip()
        print(f'|{" " * (SCREEN_WIDTH-2)}|')
        if len(user_options) != 1 or user_options not in valid_options:
            print(f'|{"💢 OPÇÃO INVÁLIDA 💢".center(SCREEN_WIDTH-4)}|')
        return user_options

    # Método que retorna a opção da máquina na rodada
    def get_machine_option(self, machine_robot):
        print(f'|{machine_robot.name.center(SCREEN_WIDTH+8)}|')
        print(f'|{" " * (SCREEN_WIDTH - 2)}|')
        print(f'|{"🤖 MÁQUINA ATACANDO...".center(SCREEN_WIDTH-3)}|', end="")
        sleep(2)
        print(f'|{" " * (SCREEN_WIDTH-2)}|')
        machine_option = randint(1, 3 if machine_robot.energy == 100 else 4)
        if machine_option < 4:
            skill_attack = machine_robot.attack_skills[machine_option - 1]
            if skill_attack.energy_consumption > machine_robot.energy:
                machine_option = 4
        return machine_option

    # Método que calcula a jogada do robô
    def play_round(self, current_robot, enemy_robot, attack_option):
        if not 0 < attack_option < 5:
            return False
        if attack_option == 4:
            return current_robot.recharge_energy()
        attack_skill = current_robot.attack_skills[attack_option - 1]
        if attack_skill.energy_consumption > current_robot.energy:
            warning = f'🔌 {current_robot.name} NÃO TEM ENERGIA SUFICIENTE PARA ESSE ATAQUE 🔌'
            print(f'|{warning.center(SCREEN_WIDTH+6)}|')
            return False
        rand = randint(0, 100)
        if attack_option == 1:
            if rand <= 25:
                return current_robot.attack(enemy_robot, attack_skill)
            if rand <= 60:
                return enemy_robot.defend(current_robot, attack_skill)
            return enemy_robot.dodge(current_robot, attack_skill)
        elif attack_option == 2:
            if rand <= 15:
                return current_robot.attack(enemy_robot, attack_skill)
            if rand <= 45:
                return enemy_robot.defend(current_robot, attack_skill)
            return enemy_robot.dodge(current_robot, attack_skill)
        else:
            if rand <= 5:
                return current_robot.attack(enemy_robot, attack_skill)
            if rand <= 30:
                return enemy_robot.defend(current_robot, attack_skill)
            return enemy_robot.dodge(current_robot, attack_skill)

    # Exibe uma mensagem de vitória
    def show_you_won_message(self):
        Draw.draw_you_won_message()
        input()
        Display.clear_screen()

    # Exibe uma mensagem de derrota
    def show_you_lost_message(self):
        Draw.draw_you_lost_message()
        input()
        Display.clear_screen()

    # Exibe uma mensagem de que o jogador 1 venceu
    def show_player_one_won_message(self, color):
        Draw.draw_player_one_won_message(color)
        input()
        Display.clear_screen()

    # Exibe uma mensagem de que o jogador 2 venceu
    def show_player_two_won_message(self, color):
        Draw.draw_player_two_won_message(color)
        input()
        Display.clear_screen()

    # Exibe um menu onde o usuário pode escolher qual personagem ele deseja ver as informações
    def show_character_menu(self):
        robot = self.show_robot_choice_menu(Draw.draw_robots_options_menu)
        Draw.draw_robot_information(robot())
        input()
        Display.clear_screen()

    # Exibe o menu de despedida do jogo
    def show_bye_bye_menu(self):
        Draw.draw_bye_bye_menu()
