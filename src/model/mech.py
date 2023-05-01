from src.model.robot import Robot
from src.skill.attack_skill import AttackSkill
from src.util.color import Color


# Representa um robô do tipo Mech
class Mech(Robot):

    def __init__(self, color=Color.black):
        art = [
            f'{Color.bold}{color}           ___                                {Color.reset}',
            f'{Color.bold}{color}          |_|_|                               {Color.reset}',
            f'{Color.bold}{color}          |_|_|              _____            {Color.reset}',
            f'{Color.bold}{color}          |_|_|     ____    |*_*_*|           {Color.reset}',
            f'{Color.bold}{color} _______   _\__\___/ __ \____|_|_   _______   {Color.reset}',
            f'{Color.bold}{color}/ ____  |=|      \  <_+>  /      |=|  ____ \\ {Color.reset}',
            f'{Color.bold}{color}~|    |\|=|======\\\\______//======|=|/|    |~  {Color.reset}',
            f'{Color.bold}{color} |_   |    \      |      |      /    |    |   {Color.reset}',
            f'{Color.bold}{color}  \==-|     \     |  2D  |     /     |----|~~/{Color.reset}',
            f'{Color.bold}{color}  |   |      |    |      |    |      |____/~/ {Color.reset}',
            f'{Color.bold}{color}  |   |       \____\____/____/      /    / /  {Color.reset}',
            f'{Color.bold}{color}  |   |         {{----------}}       /____/ /   {Color.reset}',
            f'{Color.bold}{color}  |___|        /~~~~~~~~~~~~\     |_/~|_|/    {Color.reset}',
            f'{Color.bold}{color}   \_/        |/~~~~~||~~~~~\|     /__|\\     {Color.reset}',
            f'{Color.bold}{color}   | |         |    ||||    |     (/|| \\)    {Color.reset}',
            f'{Color.bold}{color}   | |        /     |  |     \       \\\\      {Color.reset}',
            f'{Color.bold}{color}   |_|        |     |  |     |                {Color.reset}',
            f'{Color.bold}{color}              |_____|  |_____|                {Color.reset}',
            f'{Color.bold}{color}              (_____)  (_____)                {Color.reset}',
            f'{Color.bold}{color}              |     |  |     |                {Color.reset}',
            f'{Color.bold}{color}              |     |  |     |                {Color.reset}',
            f'{Color.bold}{color}              |/~~~\|  |/~~~\|                {Color.reset}',
            f'{Color.bold}{color}              /|___|\  /|___|\\               {Color.reset}',
            f'{Color.bold}{color}             <_______><_______>               {Color.reset}'
        ]
        lore = [
            "____________________________________",
            "|                                  |",
            "| Mech é um robô  construído com a |",
            "| mais alta tecnologia para ajudar |",
            "| na   exploração   espacial.  Ele |",
            "| possui     uma      inteligência |",
            "| artificial avançada  que permite |",
            "| que  aprenda  com  suas próprias |",
            "| experiências. Durante uma missão |",
            "| em um planeta distante, Mech foi |",
            "| danificado e sua programação foi |",
            "| corrompida. A partir daí, ele se |",
            "| rebelou contra seus  criadores e |",
            "| decidiu  explorar o universo por |",
            "| conta própria, em busca  de  sua |",
            "| verdadeira       identidade    e |",
            "| propósito.                       |",
            "|__________________________________|"
        ]
        attack_skills = [
            AttackSkill(
                'PUNHO DO PODER',
                [
                    "___________________________________",
                    "|          PUNHO DO PODER         |",
                    "|---------------------------------|",
                    "| Punho do poder é uma habilidade |",
                    "| que permite ao usuário carregar |",
                    "| seu ataque e  desferir um golpe |",
                    "| devastador em um único alvo.    |",
                    "|_________________________________|"
                ],
                15,
                12
            ),
            AttackSkill(
                'AVANÇO UMBRAL',
                [
                    "___________________________________",
                    "|          AVANÇO UMBRAL          |",
                    "|---------------------------------|",
                    "| Permite ao usuário aumentar sua |",
                    "| velocidade   e  força   por  um |",
                    "| curto  período,  permitindo  um |",
                    "| avanço  rápido  e  poderoso.    |",
                    "|_________________________________|"
                ],
                30,
                18
            ),
            AttackSkill(
                'ANIQUILADOR DE MUNDOS',
                [
                    "___________________________________",
                    "|      ANIQUILADOR DE MUNDOS      |",
                    "|---------------------------------|",
                    "| Aniquilador de Mundos causa uma |",
                    "| explosão massiva  capaz de des- |",
                    "| truir tudo ao  seu  redor, ani- |",
                    "| quilando mundos inteiros.       |",
                    "|_________________________________|"
                ],
                60,
                24
            )
        ]
        super().__init__('MECH', art, color, lore, attack_skills)
