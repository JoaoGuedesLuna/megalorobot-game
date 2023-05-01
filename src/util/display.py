import os


# Classe utilitária que disponibiliza um método de limpar a tela
class Display:

    # Limpa a tela do console
    @staticmethod
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')
