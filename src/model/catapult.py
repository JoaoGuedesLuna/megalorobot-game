from src.model.robot import Robot
from src.skill.attack_skill import AttackSkill
from src.util.color import Color


# Representa um robô do tipo Catapult
class Catapult(Robot):

    def __init__(self, color=Color.blue):
        art = [
            f'{Color.bold}{color}   _____             _____   {Color.reset}',
            f'{Color.bold}{color}  |_____|___________|_____|  {Color.reset}',
            f'{Color.bold}{color}  |_____| / _____ \ |_____|  {Color.reset}',
            f'{Color.bold}{color}  |_____|/ /\___/\ \|_____|  {Color.reset}',
            f'{Color.bold}{color} /|====|__/_/___\_\__|====|\\ {Color.reset}',
            f'{Color.bold}{color} ||====|  _/_\_/_\_  |====|| {Color.reset}',
            f'{Color.bold}{color} \|====| | \ ... / | |====|/ {Color.reset}',
            Color.bold + color + "       |__\ `---' /__|       " + Color.reset,
            f'{Color.bold}{color}        |==\_____/==|        {Color.reset}',
            f'{Color.bold}{color}        |===|===|===|        {Color.reset}',
            f'{Color.bold}{color}        |===|+-+|===|        {Color.reset}',
            f'{Color.bold}{color}        >|||<   >|||<        {Color.reset}',
            f'{Color.bold}{color}        |---|   |---|        {Color.reset}',
            f'{Color.bold}{color}        || ||   || ||        {Color.reset}',
            f'{Color.bold}{color}        || ||   || ||        {Color.reset}',
            f'{Color.bold}{color}        >= =<   >= =<        {Color.reset}',
            f'{Color.bold}{color}        |===|   |===|        {Color.reset}',
            f'{Color.bold}{color}        >---/   \---<        {Color.reset}',
            f'{Color.bold}{color}        ||#|     |#||        {Color.reset}',
            f'{Color.bold}{color}        ||-|\   /|-||        {Color.reset}',
            f'{Color.bold}{color}        ||+||   ||+||        {Color.reset}',
            f'{Color.bold}{color}        ||_|\   /|_||        {Color.reset}',
            f'{Color.bold}{color}     ___|/-\/   \/-\|___     {Color.reset}',
            f'{Color.bold}{color}    /________\ /________\\    {Color.reset}'
        ]
        lore = [
            "____________________________________",
            "|                                  |",
            "| Catapult  é  um  robô construído |",
            "| para  fins  militares,  capaz de |",
            "| lançar    projéteis    a   longa |",
            "| distância com precisão incrível. |",
            "| Ele era altamente respeitado por |",
            "| suas habilidades de combate e se |",
            "| destacava   por   sua   lealdade |",
            "| inabalável  aos  seus   aliados. |",
            "| Catapult sofreu  um dano crítico |",
            "| e foi deixado para trás pelo seu |",
            "| esquadrão. Incapaz de se  mover, |",
            "| Catapult   foi   capturado  pelo |",
            "| inimigo   e   reprogramado  para |",
            "| lutar   contra   seus   próprios |",
            "| criadores.                       |",
            "|__________________________________|"
        ]
        attack_skills = [
            AttackSkill(
                'PUNIÇÃO',
                [
                    "___________________________________",
                    "|             PUNIÇÃO             |",
                    "|---------------------------------|",
                    "| Punição  é  uma habilidade  que |",
                    "| permite ao usuário infligir uma |",
                    "| punição avassaladora em um alvo |",
                    "| , causando um grande dano.      |",
                    "|_________________________________|"
                ],
                15,
                12
            ),
            AttackSkill(
                'PULVERIZAR',
                [
                    "___________________________________",
                    "|            PULVERIZAR           |",
                    "|---------------------------------|",
                    "| A habilidade permite ao usuário |",
                    "| atacar um alvo  com  uma  força |",
                    "| esmagadora,  pulverizando-o  em |",
                    "| pedaços ou destroços.           |",
                    "|_________________________________|"
                ],
                30,
                18
            ),
            AttackSkill(
                'EXECUÇÃO PERFEITA',
                [
                    "___________________________________",
                    "|        EXECUÇÃO PERFEITA        |",
                    "|---------------------------------|",
                    "| Essa   habilidade   permite  ao |",
                    "| usuário executar um golpe letal |",
                    "| preciso em um alvo  vulnerável, |",
                    "| causando muito dano.            |",
                    "|_________________________________|"
                ],
                60,
                24
            )
        ]
        super().__init__('CATAPULT', art, color, lore, attack_skills)
