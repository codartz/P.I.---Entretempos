import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_cabecalho():
    limpar_tela()
    print("=" * 90)
    exibir_logo()
    print("=" * 90 + "\n")

def exibir_logo():

    print(r"""
  ______       _              _______                   
 |  ____|     | |            |__   __|                  
 | |__   _ __ | |_ _ __ ___     | | ___ _ __ ___  _ __   ___  ___
 |  __| | '_ \| __| '__/ _ \    | |/ _ \ '_ ` _ \| '_ \ / _ \/ __|
 | |____| | | | |_| | |  __/    | |  __/ | | | | | |_) | (_) \__ \
 |______|_| |_|\__|_|  \___|    |_|\___|_| |_| |_| .__/ \___/|___/
                                                  | |
                                                  |_|
    """)