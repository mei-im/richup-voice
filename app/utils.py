import random

# create a decorator that randomize the tts of the function
def randomize(func):
    def wrapper(*args, **kwargs):
        return random.choice(func(*args, **kwargs))
    return wrapper

@randomize
def random_not_understand():
    return ["Não percebi o que disseste",
            "Não entendi o que disseste",
            "Não percebi o que disseste, por favor repita",
            "Podes repetir o que disseste",
            "Não percebi, podes repetir",
            "Não percebi, podes repetir por favor", 
            "Desculpa, não percebi o que disseste",
            "Desculpa, não percebi, podes repetir",
            "Repita por favor, não percebi o que disseste",
            "Repita por favor, não percebi",
    ]

@randomize
def random_not_understand_name():
    return ["Não percebi o nome que disseste, por favor repita",
            "Podes repetir o nome, não percebi",
            "Por favor, repita o nome",
            "Por favor, repita o nome com que quer ser identificado",
            "Não percebi o nome, podes repetir",
            "Não entendi o nome com que quer ser identificado, podes repetir",
            "Por favor, diga o nome com que quer ser identificado",
            "Desculpa, não percebi com que nome quer jogar",
            "Desculpa, não percebi, podes repetir",
            "Repita por favor, não percebi o nome com que quer ser identificado",
    ]

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
            "Não é permitido, criares uma sala enquanto estás numa sala de jogo",
            "Já tens uma sala criada, não podes criar outra sala enquanto estás numa sala",
            "Desculpa, mas não é permitido criares uma sala enquanto estás noutra sala",
            "Desculpa, mas não é permitido criares uma sala neste momento",
    ]

@randomize
def random_create_room():
    return ["Precisa de criar uma sala para poder jogar",
            "Não tens nenhuma sala criada",
            "Não te encontras numa sala", 
            "Não te encontras numa sala, cria uma sala para poderes jogar",
            "Precisa de criar uma sala para poder jogar",
    ]

@randomize
def random_not_valid_color():
    return ["Escolhe uma cor válida",
            "A cor que escolheste não é válida",
            "A cor que escolheste não é válida, se não sabes as cores disponíveis, pergunta-me",
            "A cor que escolheste não é válida, pergunta-me as cores disponíveis",
            "Escolhe uma cor válida, se não sabes as cores disponíveis, pergunta-me",
            "Escolhe uma cor válida, se necessitares de ajuda, pergunta-me",
            "A cor que escolheste não é válida, se necessitares de ajuda, pergunta-me"
    ]

@randomize
def random_not_understand_color():
    return ["Não percebi a cor que disseste, por favor repita",
            "Podes repetir a cor, não percebi",
            "Por favor, repita a cor",
            "Por favor, repita a cor com que quer jogar",
            "Por favor, repita a cor com que quer ser identificado durante o jogo",
            "Não percebi a cor, podes repetir",
            "Não entendi a cor com que quer jogar, podes repetir",
            "Por favor, diga a cor com que quer jogar",
            "Por favor, diga a cor com que quer ser identificado durante o jogo",
            "Desculpa, não percebi com que cor quer jogar",
            "Desculpa, não percebi, podes repetir",
            "Repita por favor, não percebi a cor com que quer jogar",
    ]

@randomize
def random_roll_dice_in_turn():
    return [  "Já lançaste os dados", 
              "Já lançaste os dados, não sejas batoteiro",
              "Não sejas batoteiro, já lançaste os dados",
              "Nínguem gosta de um batoteiro",
              "Não é permitido, lançar os dados neste momento", 
              "Termina a tua ronda, e para de Trapacear",
              
    ]

@randomize
def random_roll_dice_not_auth():
    return [ "Não é a tua vez de Jogar", 
              "Espera pela tua jogada", 
                "Não é a tua vez de jogar, espera pela tua vez", 
                "Espera pela tua vez de jogar",
                "Estás a tentar jogar fora da tua vez",
                "Não podes jogar fora da tua vez",
                "Não podes jogar enquanto outro jogador não acabar a sua jogada",
    ]

@randomize
def random_roll_dice():
    return [ "Os dados foram lançados",
            "Os dados foram lançados, espera pelo resultado",
            "Aguarda pelo resultado",
            "A sua jogada foi realizada",
            "A sua peça já se moveu",
            "Lançaste os dados, espera pela peça se mover",
    ]


@randomize
def random_end_turn_other_player():
    return [ "Não é a tua vez de acabar a ronda",
            "Não é a tua de jogar",
            "Não é a tua vez de jogar, espera pela tua vez",
            "Não podes acabar a ronda fora da tua vez",
            "Deixa os outros jogarem",
            "Não podes acabar a ronda enquanto outro jogador não acabar a sua jogada",
            "Outro jogador ainda não acabou a sua ronda",
            "Outro jogador ainda está a jogar, espera pela tua vez",
            "Outro jogador ainda não acabou a sua ronda, espera pela tua vez",
    ]

@randomize
def random_end_turn():
    return [ "A tua ronda terminou",
            "A tua ronda terminou, espera pela tua proxima jogada",
            "Aguarda pela tua próxima jogada",
            "Agora é a vez de outro jogador",
            "Agora é a vez de outro jogador, espera pela tua vez"
    ]

@randomize
def random_end_turn_not_auth():
    return ["É a tua vez de jogar",
            "É a tua vez de jogar, termina a tua ronda depois",
            "Faz a tua jogada, e depois acaba a ronda",
            "Não podes acabar a ronda agora, faz a tua jogada",
            "Não podes acabar a ronda agora, faz a tua jogada primeiro",
            "Faz a tua jogada primeiro",
            "Não podes acabar a ronda agora",
            "Não podes acabar a ronda agora, faz a tua jogada primeiro",]