from src.model.robot import Robot
from src.skill.attack_skill import AttackSkill
from src.util.color import Color


# Representa um robô do tipo Marauder
class Marauder(Robot):

    def __init__(self, color=Color.magenta):
        art = [
            f'{Color.bold}{color}               ^                {Color.reset}',
            f'{Color.bold}{color}             (/U\)              {Color.reset}',
            f'{Color.bold}{color}             \___/     /        {Color.reset}',
            f'{Color.bold}{color}         --  _|||_  --/         {Color.reset}',
            f'{Color.bold}{color}        //\\\\/ ___ \/,/\\        {Color.reset}',
            Color.bold + color + "        \\\\////_^_\\\\\/'/         " + Color.reset,
            f'{Color.bold}{color}         -///-/_\-\/\-          {Color.reset}',
            f'{Color.bold}{color}        |||/_______\|||         {Color.reset}',
            f'{Color.bold}{color}      ,/|||\  |O|  /|||\,       {Color.reset}',
            f'{Color.bold}{color}     /  |_\\\\/-___-\//_|  \\     {Color.reset}',
            f'{Color.bold}{color}    / ,/.--/-------\--.\, \\    {Color.reset}',
            Color.bold + color + "   /\/  | / ||`|'|| \ |  \/\\   " + Color.reset,
            Color.bold + color + "  / /    ||=|`---'|=||    \ \\  " + Color.reset,
            f'{Color.bold}{color} |\/     |--|     |--|     \/|  {Color.reset}',
            f'{Color.bold}{color}/()\     \__/     \__/     /()\\{Color.reset}',
            f'{Color.bold}{color}\__/     /  \     /  \     \__/ {Color.reset}',
            f'{Color.bold}{color}|  |     ||||     ||||     |  | {Color.reset}',
            f'{Color.bold}{color}|==|     ||||     ||||     |==| {Color.reset}',
            f'{Color.bold}{color}         \__/     \__/          {Color.reset}',
            f'{Color.bold}{color}         /  \     /  \\         {Color.reset}',
            f'{Color.bold}{color}         ||||     ||||          {Color.reset}',
            f'{Color.bold}{color}       ,/|__|\   /|__|\,        {Color.reset}',
            f'{Color.bold}{color}      /--|__|-\ /-|__|--\\      {Color.reset}',
            f'{Color.bold}{color}     |___|  |_| |_|  |___|      {Color.reset}'
        ]
        lore = [
            "____________________________________",
            "|                                  |",
            "| Marauder é um robô  de segurança |",
            "| projetado      para     proteger |",
            "| instalações            militares |",
            "| estratégicas.  Ele  possui   uma |",
            "| inteligência artificial avançada |",
            "| capaz  de  detectar   ameaças  e |",
            "| tomar   decisões   rápidas    em |",
            "| situações  de   crise.  ele está |",
            "| disposto  a  sacrificar-se  para |",
            "| proteger aqueles  que  estão sob |",
            "| sua proteção.                    |",
            "|__________________________________|"
        ]
        attack_skills = [
            AttackSkill(
                'DIZIMAR',
                [
                    "___________________________________",
                    "|             DIZIMAR             |",
                    "|---------------------------------|",
                    "| A habilidade permite ao usuário |",
                    "| causar uma grande destruição em |",
                    "| uma área específica,  dizimando |",
                    "| tudo o que estiver ao redor.    |",
                    "|_________________________________|"
                ],
                15,
                12
            ),
            AttackSkill(
                'LIÇÃO DURA',
                [
                    "___________________________________",
                    "|            LIÇÃO DURA           |",
                    "|---------------------------------|",
                    "| A habilidade permite ao usuário |",
                    "| infligir uma  lição  dura em um |",
                    "| alvo  específico,  deixando uma |",
                    "| mensagem clara para o inimigos. |",
                    "|_________________________________|"
                ],
                30,
                18
            ),
            AttackSkill(
                'EFEITO COLATERAL',
                [
                    "___________________________________",
                    "|         EFEITO COLATERAL        |",
                    "|---------------------------------|",
                    "| Essa habilidade causa um efeito |",
                    "| indesejado  em   um  adversário |",
                    "| específico,  prejudicando-o  de |",
                    "| alguma forma.                   |",
                    "|_________________________________|"
                ],
                60,
                24
            )
        ]
        super().__init__('MARAUDER', art, color, lore, attack_skills)
