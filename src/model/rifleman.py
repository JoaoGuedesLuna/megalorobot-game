from src.model.robot import Robot
from src.skill.attack_skill import AttackSkill
from src.util.color import Color


# Representa um robô do tipo Rifleman
class Rifleman(Robot):

    def __init__(self, color=Color.red):
        art = [
            f'{Color.bold}{color}      ______________      {Color.reset}',
            Color.bold + color + "     `--------------'     " + Color.reset,
            f'{Color.bold}{color}  _.  .--./|  |\.--.  ._  {Color.reset}',
            f'{Color.bold}{color} //|  |--||----||--|  |\\ {Color.reset}',
            f'{Color.bold}{color}||__\_|  ||____||  |_/__||{Color.reset}',
            f'{Color.bold}{color}||_() |___||--||___| ()_||{Color.reset}',
            f'{Color.bold}{color}||||  |---||__||---|  ||||{Color.reset}',
            f'{Color.bold}{color} \|| /|___||__||___|\_||/ {Color.reset}',
            f'{Color.bold}{color} |||_| \.||||||||./ |_||| {Color.reset}',
            f'{Color.bold}{color} \ _ /   \--==--/   \ _ / {Color.reset}',
            f'{Color.bold}{color}  <_>  /----------\  <_>  {Color.reset}',
            f'{Color.bold}{color}  ||| _\__ |  | __/_ |||  {Color.reset}',
            f'{Color.bold}{color}  ||| \  |\|  |/|  / |||  {Color.reset}',
            f'{Color.bold}{color}  ||| |  |_|__|_|  | |||  {Color.reset}',
            f'{Color.bold}{color}  ||| [--+ \  / +--] |||  {Color.reset}',
            f'{Color.bold}{color}  ||| |--+-/  \-+--| |||  {Color.reset}',
            f'{Color.bold}{color}  ||| |  ||    ||  | |||  {Color.reset}',
            f'{Color.bold}{color}  / \ |---|    |---| / \\ {Color.reset}',
            f'{Color.bold}{color}  |=| | | |    | | | |=|  {Color.reset}',
            f'{Color.bold}{color}  \ / |___|    |___| \ /  {Color.reset}',
            f'{Color.bold}{color}   = (| | ||  || | |) =   {Color.reset}',
            f'{Color.bold}{color}     _|_#__|  |__#_|_     {Color.reset}',
            f'{Color.bold}{color}    /______\  /______\\   {Color.reset}',
            f'{Color.bold}{color}   |________||________|   {Color.reset}'
        ]
        lore = [
            "____________________________________",
            "|                                  |",
            "| Rifleman é um robô de suporte de |",
            "| infantaria que fornece cobertura |",
            "| e apoio  às  tropas em  batalha. |",
            "| Ele é equipado  com um  rifle de |",
            "| precisão  de   última   geração, |",
            "| capaz de atingir alvos a longas  |",
            "| distâncias.  Apesar    de   sua  |",
            "| ofensiva, ele também é  capaz de |",
            "| prestar assistência   médica  de |",
            "| emergência  às  tropas  feridas, |",
            "| tornando-se um elemento  crucial |",
            "| para o sucesso da missão.        |",
            "|__________________________________|"
        ]
        attack_skills = [
            AttackSkill(
                'MUNIÇÃO FLAMEJANTE',
                [
                    "___________________________________",
                    "|        MUNIÇÃO FLAMEJANTE       |",
                    "|---------------------------------|",
                    "| A habilidade permite ao usuário |",
                    "| disparar  munições que explodem |",
                    "| em  chamas  ao  acertar o alvo, |",
                    "| causando um dano crucial.       |",
                    "|_________________________________|"
                ],
                15,
                12
            ),
            AttackSkill(
                'METRALHADORA',
                [
                    "___________________________________",
                    "|           METRALHADORA          |",
                    "|---------------------------------|",
                    "| A habilidade permite ao usuário |",
                    "| disparar uma  metralhadora  com |",
                    "| alta taxa de fogo,  causando um |",
                    "| dano significativo no combate.  |",
                    "|_________________________________|"
                ],
                30,
                18
            ),
            AttackSkill(
                'BARRAGEM DE MÍSSEIS',
                [
                    "___________________________________",
                    "|       BARRAGEM DE MÍSSEIS       |",
                    "|---------------------------------|",
                    "| A habilidade permite ao usuário |",
                    "| lançar uma barragem de  mísseis |",
                    "| numa área específica,  causando |",
                    "| um grande dano em área.         |",
                    "|_________________________________|"
                ],
                60,
                24
            )
        ]
        super().__init__('RIFLEMAN', art, color, lore, attack_skills)
