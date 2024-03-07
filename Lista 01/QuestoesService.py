import matplotlib.pyplot as plot
import numpy as np

def calcularMaxEMin(listaPontos: list):
    max: float = 5
    min: float = 0
    for lista in listaPontos:
        for value in lista:
            max = (value + 2) if value >= max else max
            min = (value - 2) if value <= min else min

    return [min, max]

def separaPontosXY(listaPontos: list):
    listaX: list
    listaY: list

    for lista in listaPontos:
        for value in lista:
            listaX.append(value[0])
            listaY.append(value[1])

    return listaX, listaY

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
        escala: list = calcularMaxEMin([ponto_a, ponto_b])
        figura, eixo = plot.subplots()

        eixo.set_xlim(escala[0], escala[1])
        eixo.set_ylim(escala[0], escala[1])
        eixo.grid()

        eixo.text(ponto_a[0], ponto_a[1], 'O', fontsize=8, color='green')
        eixo.text(ponto_b[0], ponto_b[1], '+', fontsize=8, color='blue')

        plot.show()

class Questao03:
    def resolucao(ponto_a: list, ponto_b: list):
        escala: list = calcularMaxEMin([ponto_a, ponto_b])
        figura, eixo = plot.subplots()

        eixo.set_xlim(escala[0], escala[1])
        eixo.set_ylim(escala[0], escala[1])
        eixo.grid()

        eixo.plot(ponto_a[0], ponto_a[1], 'bo', label = 'Ponto A')
        eixo.plot(ponto_b[0], ponto_b[1], 'ro', label = 'Ponto B')

        eixo.plot([ponto_a[0], ponto_b[0]], [ponto_a[1], ponto_b[1]], 'k-', label='Linha AB')
        plot.show()

class Questao04:
    def resolucao(ponto_a: list, ponto_b: list, ponto_c: list):
        escala: list = calcularMaxEMin([ponto_a, ponto_b, ponto_c])
        figura, eixo = plot.subplots()

        eixo.set_xlim(escala[0], escala[1])
        eixo.set_ylim(escala[0], escala[1])
        eixo.grid()

        eixo.plot(ponto_a[0], ponto_a[1], 'bo', label = 'Ponto A')
        eixo.plot(ponto_b[0], ponto_b[1], 'ro', label = 'Ponto B')
        eixo.plot(ponto_c[0], ponto_c[1], 'go', label = 'Ponto C')

        eixo.plot([ponto_a[0], ponto_b[0], ponto_c[0], ponto_a[0]], [ponto_a[1], ponto_b[1], ponto_c[1], ponto_a[1]], 'k-', label='Triangulo ABC')
        plot.show()

class Questao05:
    def resolucao(ponto_a: list, ponto_b: list, ponto_c: list, translacao: list):
        figura, eixo = plot.subplots()

        npA: list = np.append(ponto_a, 1)
        npB: list = np.append(ponto_b, 1)
        npC: list = np.append(ponto_c, 1)

        a: list = np.dot(translacao, npA)
        b: list = np.dot(translacao, npB)
        c: list = np.dot(translacao, npC)


        escala: list = calcularMaxEMin([a, b, c])
        
        eixo.set_xlim(escala[0], escala[1])
        eixo.set_ylim(escala[0], escala[1])
        eixo.grid()

        eixo.plot(a[0], a[1], 'bo', label = 'Ponto A')
        eixo.plot(b[0], b[1], 'ro', label = 'Ponto B')
        eixo.plot(c[0], c[1], 'go', label = 'Ponto C')

        eixo.plot([a[0], b[0], c[0], a[0]], [a[1], b[1], c[1], a[1]], 'k-', label='Triangulo ABC')
        plot.show()

class Questao06:
    def resolucao(ponto_a: list, ponto_b: list, ponto_c: list, translacao: list):
        Questao05.resolucao(ponto_a, ponto_b, ponto_c, translacao)