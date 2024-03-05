import matplotlib.pyplot as plot

def calcularMaxEMin(ponto_a: list, ponto_b: list):
    max: float = 5
    min: float = -5
    for value in ponto_a:
        max = (value + 2) if value >= max else max
        min = (value - 2) if value <= min else min

    for value in ponto_b:
        max = (value + 2) if value >= max else max
        min = (value - 2) if value <= min else min

    return [min, max]

class Questao01:
    def resolucao(ponto_x: float, ponto_y: float):
        figura, eixo = plot.subplots()
        eixo.set_xlim(0, 10)
        eixo.set_ylim(0, 10)
        eixo.grid()
        eixo.text(ponto_x, ponto_y, 'O', fontsize=8, color='red')
        plot.show()

class Questao02:
    def resolucao(ponto_a: list, ponto_b: list):
        escala: list = calcularMaxEMin(ponto_a, ponto_b)
        figura, eixo = plot.subplots()

        eixo.set_xlim(escala[0], escala[1])
        eixo.set_ylim(escala[0], escala[1])
        eixo.grid()

        eixo.text(ponto_a[0], ponto_a[1], 'O', fontsize=8, color='green')
        eixo.text(ponto_b[0], ponto_b[1], '+', fontsize=8, color='blue')

        plot.show()

class Questao03:
    def resolucao(ponto_a: list, ponto_b: list):
        escala: list = calcularMaxEMin(ponto_a, ponto_b)
        figura, eixo = plot.subplots()

        eixo.set_xlim(escala[0], escala[1])
        eixo.set_ylim(escala[0], escala[1])
        eixo.grid()

        eixo.plot(ponto_a[0], ponto_a[1], 'bo', label = 'Ponto A')
        eixo.plot(ponto_b[0], ponto_b[1], 'ro', label = 'Ponto B')

        eixo.plot([ponto_a[0], ponto_b[0]], [ponto_a[1], ponto_b[1]], 'k-', label='Linha AB')
        plot.show()

