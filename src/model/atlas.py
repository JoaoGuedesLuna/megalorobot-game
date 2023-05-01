from src.model.robot import Robot
from src.skill.attack_skill import AttackSkill
from src.util.color import Color


# Representa um robô do tipo Atlas
class Atlas(Robot):

    def __init__(self, color=Color.black):
        art = [
            f'{Color.bold}{color}          0 _____             {Color.reset}',
            f'{Color.bold}{color}           X_____\\           {Color.reset}',
            f'{Color.bold}{color}   .-^-.  ||_| |_||  .-^-.    {Color.reset}',
            f'{Color.bold}{color}  /_\_/_\_|  |_|  |_/_\_/_\\  {Color.reset}',
            f'{Color.bold}{color}  ||(_)| __\_____/__ |(_)||   {Color.reset}',
            f'{Color.bold}{color}  \/| | |::|\```/|::| | |\/   {Color.reset}',
            Color.bold + color + "  /`---_|::|-+-+-|::|_---'\\  " + Color.reset,
            f'{Color.bold}{color} / /  \ |::|-|-|-|::| /  \ \\ {Color.reset}',
            Color.bold + color + "/_/   /|`--'-+-+-`--'|\   \_\\" + Color.reset,
            f'{Color.bold}{color}| \  / |===/_\ /_\===| \  / | {Color.reset}',
            f'{Color.bold}{color}|  \/  /---/-/-\-\  o\  \/  | {Color.reset}',
            f'{Color.bold}{color}| ||| | O / /   \ \   | ||| | {Color.reset}',
            f'{Color.bold}{color}| ||| ||----\ | /----|o|||| | {Color.reset}',
            f'{Color.bold}{color}| _|| ||-----|||-----|o|||_ | {Color.reset}',
            f'{Color.bold}{color}\/|\/  |     |||     |o|\/|\/ {Color.reset}',
            Color.bold + color + "\_o/   |----|||||----|-' \o_/ " + Color.reset,
            f'{Color.bold}{color}       |##  |   |  ##|        {Color.reset}',
            f'{Color.bold}{color}       ||__ |   | __||        {Color.reset}',
            Color.bold + color + "      [|`--'|] [|`--'|]       " + Color.reset,
            f'{Color.bold}{color}      /|__| |\ /| |__|\\      {Color.reset}',
            f'{Color.bold}{color}      ||__|_|| ||_|__||       {Color.reset}',
            f'{Color.bold}{color}      \|----|/ \|----|/       {Color.reset}',
            f'{Color.bold}{color}      /______\ /______\\      {Color.reset}',
            f'{Color.bold}{color}      |__||__| |__||__|       {Color.reset}'
        ]
        lore = [
            "____________________________________",
            "|                                  |",
            "| Atlas é um robô  de   construção |",
            "| projetado  para realizar tarefas |",
            "| pesadas  em terrenos acidentados |",
            "| e  perigosos.  Ele   possui  uma |",
            "| estrutura reforçada e  poderosos |",
            "| motores que o permitem  carregar |",
            "| grandes   cargas   e  enfrentar  |",
            "| condições  climáticas  extremas. |",
            "| Atlas  também  é  equipado  com  |",
            "| sensores avançados que o permite |",
            "| detectar    materiais   valiosos |",
            "| e recursos  naturais, tornando-o |",
            "| uma ferramenta importante para a |",
            "| exploração de novos territórios. |",
            "|__________________________________|"
        ]
        attack_skills = [
            AttackSkill(
                'PUNHO AVASSALADOR',
                [
                    "___________________________________",
                    "|         PUNHO AVASSALADOR       |",
                    "|---------------------------------|",
                    "| A habilidade permite ao usuário |",
                    "| desferir um golpe poderoso  com |",
                    "| o punho,  causando dano ao alvo |",
                    "| e lançando-o para longe.        |",
                    "|_________________________________|"
                ],
                15,
                12
            ),
            AttackSkill(
                'DEVASTAR',
                [
                    "___________________________________",
                    "|             DEVASTAR            |",
                    "|---------------------------------|",
                    "| Causa uma grande  destruição em |",
                    "| uma  área  ampla, causando dano |",
                    "| em massa aos inimigos e objetos |",
                    "| próximos.                       |",
                    "|_________________________________|"
                ],
                30,
                18
            ),
            AttackSkill(
                'CATACLISMA',
                [
                    "___________________________________",
                    "|            CATACLISMA           |",
                    "|---------------------------------|",
                    "| Provoca  um  grande cataclisma, |",
                    "| causando danos  extremos em uma |",
                    "| grande área ao redor do usuário |",
                    "| podendo  até alterar o terreno. |",
                    "|_________________________________|"
                ],
                60,
                24
            )
        ]
        super().__init__('ATLAS', art, color, lore, attack_skills)
