import random

# create a decorator that randomize the tts of the function
def randomize(func):
    def wrapper(*args, **kwargs):
        return random.choice(func(*args, **kwargs))
    return wrapper

@randomize
def random_not_auth_insert_name():
    return ["Não é permitido, mudares o teu nome neste momento",
            "Já tens um nome no jogo",
            "Já tens um nome no jogo, não podes mudar",
            "Não é permitido, mudares de nome enquanto estás numa sala de jogo",
            "Já tens um nome no jogo, não podes mudar enquanto estás numa sala de jogo",
    ]

@randomize
def random_not_create_room():
    return ["Não é permitido, criares uma sala neste momento",
            "Já tens uma sala criada",
            "Já te encontras numa sala", 
    ]

@randomize
def random_create_room():
    return ["Precisa de criar uma sala para poder jogar",
            "Não tens nenhuma sala criada",
            "Não te encontras numa sala", 
            "Não te encontras numa sala, cria uma sala para poderes jogar",
    ]

@randomize
def random_frase_dados():
    return [  "Já lançaste os dados", 
              "Já lançaste os dados, não sejas batoteiro",
              "Não sejas batoteiro, já lançaste os dados",
              "Nínguem gosta de um batoteiro",
              "Não é permitido, lançar os dados neste momento", 
              "Termina a tua ronda, e para de Trapacear",
              
    ]

@randomize
def random_frase_dados2():
    return [ "Não é a tua vez de Jogar", 
              "Espera pela tua jogada", 
                "Não é a tua vez de jogar, espera pela tua vez", 
                "Espera pela tua vez de jogar",
                "Estás a tentar jogar fora da tua vez",
                "Não podes jogar fora da tua vez",
                "Não podes jogar enquanto outro jogador não acabar a sua jogada",
    ]

@randomize
def random_frase_nao_entendi():
    return ["Não percebi o que disseste",
            "Não entendi o que disseste",
            "Não percebi o que disseste, por favor repita",
            "Podes repetir o que disseste",
            "Não percebi, podes repetir",
            "Não percebi, podes repetir por favor", 
            "Desculpa, não percebi o que disseste",
            "Desculpa, não percebi, podes repetir",
            "Repita por favor, não percebi o que disseste",
    ]