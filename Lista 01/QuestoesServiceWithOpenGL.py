import OpenGL.GL as gl
import OpenGL.GLUT as glut
import numpy as np

def calcularMaxEMin(listaPontos):
    max_valor = 5
    min_valor = 0
    for lista in listaPontos:
        for valor in lista:
            max_valor = (valor + 2) if valor >= max_valor else max_valor
            min_valor = (valor - 2) if valor <= min_valor else min_valor
    return [min_valor, max_valor]

class Questao01:
    def resolucao(ponto_x, ponto_y):
        glut.glutInit()
        glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGBA | glut.GLUT_DEPTH)
        glut.glutInitWindowSize(400, 400)
        glut.glutCreateWindow("Ponto em OpenGL".encode('utf-8'))
        gl.glClearColor(1.0, 1.0, 1.0, 1.0)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
        gl.glLoadIdentity()

        # Desenha o ponto vermelho
        gl.glPointSize(8)
        gl.glColor3f(1.0, 0.0, 0.0)
        gl.glBegin(gl.GL_POINTS)
        gl.glVertex2f(ponto_x, ponto_y)
        gl.glEnd()

        glut.glutSwapBuffers()

class Questao02:
    def resolucao(ponto_a, ponto_b):
        escala = calcularMaxEMin([ponto_a, ponto_b])
        glut.glutInit()
        glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGBA | glut.GLUT_DEPTH)
        glut.glutInitWindowSize(400, 400)
        glut.glutCreateWindow("Questao02 em OpenGL".encode('utf-8'))
        gl.glClearColor(1.0, 1.0, 1.0, 1.0)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
        gl.glLoadIdentity()

        # Desenha os pontos
        gl.glPointSize(8)
        gl.glColor3f(0.0, 1.0, 0.0)  # Cor verde para o ponto A
        gl.glBegin(gl.GL_POINTS)
        gl.glVertex2f(ponto_a[0], ponto_a[1])
        gl.glEnd()

        gl.glColor3f(0.0, 0.0, 1.0)  # Cor azul para o ponto B
        gl.glBegin(gl.GL_POINTS)
        gl.glVertex2f(ponto_b[0], ponto_b[1])
        gl.glEnd()

        glut.glutSwapBuffers()

class Questao03:
    def resolucao(ponto_a, ponto_b):
        escala = calcularMaxEMin([ponto_a, ponto_b])
        glut.glutInit()
        glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGBA | glut.GLUT_DEPTH)
        glut.glutInitWindowSize(400, 400)
        glut.glutCreateWindow("Questao03 em OpenGL".encode('utf-8'))
        gl.glClearColor(1.0, 1.0, 1.0, 1.0)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
        gl.glLoadIdentity()

        # Desenha os pontos
        gl.glPointSize(8)
        gl.glColor3f(0.0, 0.0, 1.0)  # Cor azul para o ponto A
        gl.glBegin(gl.GL_POINTS)
        gl.glVertex2f(ponto_a[0], ponto_a[1])
        gl.glEnd()

        gl.glColor3f(1.0, 0.0, 0.0)  # Cor vermelha para o ponto B
        gl.glBegin(gl.GL_POINTS)
        gl.glVertex2f(ponto_b[0], ponto_b[1])
        gl.glEnd()

        # Desenha a linha AB
        gl.glColor3f(0.0, 0.0, 0.0)  # Cor preta para a linha AB
        gl.glBegin(gl.GL_LINES)
        gl.glVertex2f(ponto_a[0], ponto_a[1])
        gl.glVertex2f(ponto_b[0], ponto_b[1])
        gl.glEnd()

        glut.glutSwapBuffers()

class Questao04:
    def resolucao(ponto_a, ponto_b, ponto_c):
        escala = calcularMaxEMin([ponto_a, ponto_b, ponto_c])

        glut.glutInit()
        glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGBA | glut.GLUT_DEPTH)
        glut.glutInitWindowSize(400, 400)
        glut.glutCreateWindow("Triangulo ABC em OpenGL".encode('utf-8'))
        gl.glClearColor(1.0, 1.0, 1.0, 1.0)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
        gl.glLoadIdentity()

        # Define a escala da cena
        gl.glOrtho(escala[0], escala[1], escala[0], escala[1], -1.0, 1.0)

        # Desenha o ponto A
        gl.glColor3f(0.0, 0.0, 1.0)  # Azul para o ponto A
        gl.glPointSize(8)
        gl.glBegin(gl.GL_POINTS)
        gl.glVertex2f(ponto_a[0], ponto_a[1])
        gl.glEnd()

        # Desenha o ponto B
        gl.glColor3f(1.0, 0.0, 0.0)  # Vermelho para o ponto B
        gl.glBegin(gl.GL_POINTS)
        gl.glVertex2f(ponto_b[0], ponto_b[1])
        gl.glEnd()

        # Desenha o ponto C
        gl.glColor3f(0.0, 1.0, 0.0)  # Verde para o ponto C
        gl.glBegin(gl.GL_POINTS)
        gl.glVertex2f(ponto_c[0], ponto_c[1])
        gl.glEnd()

        # Desenha o triângulo ABC
        gl.glColor3f(0.0, 0.0, 0.0)  # Preto para as linhas do triângulo
        gl.glBegin(gl.GL_LINE_LOOP)
        gl.glVertex2f(ponto_a[0], ponto_a[1])
        gl.glVertex2f(ponto_b[0], ponto_b[1])
        gl.glVertex2f(ponto_c[0], ponto_c[1])
        gl.glEnd()

        glut.glutSwapBuffers()
        glut.glutMainLoop()

class Questao05:
    def resolucao(ponto_a, ponto_b, ponto_c, translacao):
        figura, eixo = plot.subplots()

        npA = np.append(ponto_a, 1)
        npB = np.append(ponto_b, 1)
        npC = np.append(ponto_c, 1)

        a = np.dot(translacao, npA)
        b = np.dot(translacao, npB)
        c = np.dot(translacao, npC)

        escala = calcularMaxEMin([a, b, c])

        glut.glutInit()
        glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGBA | glut.GLUT_DEPTH)
        glut.glutInitWindowSize(400, 400)
        glut.glutCreateWindow("Triangulo ABC com Translação em OpenGL".encode('utf-8'))
        gl.glClearColor(1.0, 1.0, 1.0, 1.0)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
        gl.glLoadIdentity()

        # Define a escala da cena
        gl.glOrtho(escala[0], escala[1], escala[0], escala[1], -1.0, 1.0)

        # Desenha o ponto A
        gl.glColor3f(0.0, 0.0, 1.0)  # Azul para o ponto A
        gl.glPointSize(8)
        gl.glBegin(gl.GL_POINTS)
        gl.glVertex2f(a[0], a[1])
        gl.glEnd()

        # Desenha o ponto B
        gl.glColor3f(1.0, 0.0, 0.0)  # Vermelho para o ponto B
        gl.glBegin(gl.GL_POINTS)
        gl.glVertex2f(b[0], b[1])
        gl.glEnd()

        # Desenha o ponto C
        gl.glColor3f(0.0, 1.0, 0.0)  # Verde para o ponto C
        gl.glBegin(gl.GL_POINTS)
        gl.glVertex2f(c[0], c[1])
        gl.glEnd()

        # Desenha o triângulo ABC
        gl.glColor3f(0.0, 0.0, 0.0)  # Preto para as linhas do triângulo
        gl.glBegin(gl.GL_LINE_LOOP)
        gl.glVertex2f(a[0], a[1])
        gl.glVertex2f(b[0], b[1])
        gl.glVertex2f(c[0], c[1])
        gl.glEnd()

        glut.glutSwapBuffers()
        glut.glutMainLoop()

class Questao06:
    def resolucao(ponto_a, ponto_b, ponto_c, translacao):
        Questao05.resolucao(ponto_a, ponto_b, ponto_c, translacao)