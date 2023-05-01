from src.model.robot import Robot
from src.skill.attack_skill import AttackSkill
from src.util.color import Color


# Representa um robô do tipo Madcat
class Madcat(Robot):

    def __init__(self, color=Color.green):
        art = [
            f'{Color.bold}{color}    |oooo|        |oooo|    {Color.reset}',
            f'{Color.bold}{color}    |oooo| .----. |oooo|    {Color.reset}',
            f'{Color.bold}{color}    |Oooo|/\_||_/\|oooO|    {Color.reset}',
            Color.bold + color + "    `----' / __ \ `----'    " + Color.reset,
            Color.bold + color + "    ,/ |#|/\/__\/\|#| \,    " + Color.reset,
            f'{Color.bold}{color}   /  \|#|| |/\| ||#|/  \\  {Color.reset}',
            f'{Color.bold}{color}  / \_/|_|| |/\| ||_|\_/ \\ {Color.reset}',
            f'{Color.bold}{color} |_\/    o\=----=/o    \/_| {Color.reset}',
            f'{Color.bold}{color} <_>      |=\__/=|      <_> {Color.reset}',
            f'{Color.bold}{color} <_>      |------|      <_> {Color.reset}',
            f'{Color.bold}{color} | |   ___|======|___   | | {Color.reset}',
            f'{Color.bold}{color}//\\  / |O|======|O| \  //\\{Color.reset}',
            f'{Color.bold}{color}|  |  | |O+------+O| |  |  |{Color.reset}',
            f'{Color.bold}{color}|\/|  \_+/        \+_/  |\/|{Color.reset}',
            f'{Color.bold}{color}\__/  _|||        |||_  \__/{Color.reset}',
            f'{Color.bold}{color}      | ||        || |      {Color.reset}',
            f'{Color.bold}{color}     [==|]        [|==]     {Color.reset}',
            f'{Color.bold}{color}     [===]        [===]     {Color.reset}',
            f'{Color.bold}{color}      >_<          >_<      {Color.reset}',
            f'{Color.bold}{color}     || ||        || ||     {Color.reset}',
            f'{Color.bold}{color}     || ||        || ||     {Color.reset}',
            f'{Color.bold}{color}     || ||        || ||     {Color.reset}',
            f'{Color.bold}{color}   __|\_/|__    __|\_/|__   {Color.reset}',
            f'{Color.bold}{color}  /___n_n___\  /___n_n___\\ {Color.reset}'
        ]
        lore = [
            "____________________________________",
            "|                                  |",
            "| Madcat  é  um  robô  de  combate |",
            "| altamente  avançado, criado para |",
            "| operações  especiais.  É  temido |",
            "| por seus  inimigos  devido a sua |",
            "| velocidade e  habilidade. Madcat |",
            "| possui     uma     personalidade |",
            "| independente e prefere trabalhar |",
            "| sozinho,    sendo    considerado |",
            "| um lobo  solitário  no campo  de |",
            "| batalha.                         |",
            "|__________________________________|"
        ]
        attack_skills = [
            AttackSkill(
                'DESINTEGRAR',
                [
                    "___________________________________",
                    "|           DESINTEGRAR           |",
                    "|---------------------------------|",
                    "| A habilidade permite ao usuário |",
                    "| lançar um  raio de  energia que |",
                    "| desintegra rapidamente tudo  em |",
                    "| seu caminho.                    |",
                    "|_________________________________|"
                ],
                15,
                12
            ),
            AttackSkill(
                'INCINERAR',
                [
                    "___________________________________",
                    "|            INCINERAR            |",
                    "|---------------------------------|",
                    "| Permite ao  usuário  lançar uma |",
                    "| chama capaz  de incinerar  tudo |",
                    "| em  seu   caminho,  causando um |",
                    "| grande dano em área.            |",
                    "|_________________________________|"
                ],
                30,
                18
            ),
            AttackSkill(
                'RAJADA',
                [
                    "___________________________________",
                    "|             RAJADA              |",
                    "|---------------------------------|",
                    "| A habilidade permite ao usuário |",
                    "| disparar uma  rajada  de  tiros |",
                    "| precisos  e  rápidos em direção |",
                    "| ao alvo.                        |",
                    "|_________________________________|"
                ],
                60,
                24
            )
        ]
        super().__init__('MADCAT', art, color, lore, attack_skills)
