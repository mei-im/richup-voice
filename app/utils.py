import random


def random_frase_dados():
    frases = ["Lançaste os dados", 
              "Já lançaste os dados", 
              "Já lançaste os dados, não sejas batoteiro",
              "Não sejas batoteiro, já lançaste os dados",
              "Nínguem gosta de um batoteiro",
              "Não é permitido, lançar os dados neste momento", 
              "Termina a tua ronda, e para de Trapacear"
    ]
    return random.choice(frases)

def random_frase_nao_entendi():
    frase= ["Não percebi o que disseste",
            "Não entendi o que disseste",
            "Não percebi o que disseste, por favor repita",
            "Podes repetir o que disseste",
            "Não percebi, podes repetir",
            "Não percebi, podes repetir por favor", 
            "Desculpa, não percebi o que disseste",
            "Desculpa, não percebi, podes repetir",
            "Repita por favor, não percebi o que disseste",
    ]

    return random.choice(frase)