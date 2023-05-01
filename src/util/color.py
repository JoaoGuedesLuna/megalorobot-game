# Classe utilitária que contém atributos para formatação de string's, como cor, negrito, sublinhado...
class Color:

    black = '\x1b[90m'
    blue = '\x1b[94m'
    cyan = '\x1b[96m'
    green = '\x1b[92m'
    magenta = '\x1b[95m'
    red = '\x1b[91m'
    white = '\x1b[97m'
    yellow = '\x1b[93m'
    bold = '\033[1m'
    underline = '\033[4m'
    reset = '\x1b[00m'

    # Retorna uma lista contendo cada atributo cor da classe Color
    @staticmethod
    def list():
        return [
            Color.black,
            Color.blue,
            Color.cyan,
            Color.green,
            Color.magenta,
            Color.red,
            Color.white,
            Color.yellow
        ]
