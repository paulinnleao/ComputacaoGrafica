import OpenGL.GL as gl
import OpenGL.GLUT as glut
import QuestoesService as qs
class Questao01:
    def resolucao(ponto_x: list, ponto_y: list):
        escala: list = qs.calcularMaxEMin([ponto_x, ponto_y])
        gl.glColor3f(1.0, 0.0, 0.0)
        gl.glPointSize(8)
        gl.glBegin(gl.GL_POINTS)
def draw_point(x, y):
    gl.glColor3f(1.0, 0.0, 0.0)  # Define a cor vermelha
    gl.glPointSize(8)  # Define o tamanho do ponto
    gl.glBegin(gl.GL_POINTS)  # Inicia o desenho de pontos
    gl.glVertex2f(x, y)  # Define as coordenadas do ponto
    gl.glEnd()  # Finaliza o desenho de pontos
def draw_scene():
    gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
    gl.glLoadIdentity()

    # Desenhar linha do eixo x (abscissas)
    gl.glColor3f(0.0, 0.0, 0.0)  # Cor preta
    gl.glBegin(gl.GL_LINES)
    gl.glVertex2f(0.0, 0.0)  # Ponto inicial (origem)
    gl.glVertex2f(10.0, 0.0)  # Ponto final (extremidade direita)
    gl.glEnd()

    # Desenhar linha do eixo y (ordenadas)
    gl.glBegin(gl.GL_LINES)
    gl.glVertex2f(0.0, 0.0)  # Ponto inicial (origem)
    gl.glVertex2f(0.0, 10.0)  # Ponto final (extremidade superior)
    gl.glEnd()

    # Desenhar ponto
    draw_point(5, 5)

    glut.glutSwapBuffers()

def main():
    glut.glutInit()  # Inicializa o GLUT
    glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGBA | glut.GLUT_DEPTH)  # Configura o modo de exibição
    glut.glutInitWindowSize(400, 400)  # Define o tamanho da janela
    glut.glutCreateWindow(b"Ponto em OpenGL")  # Cria a janela com o título especificado
    glut.glutDisplayFunc(draw_scene)  # Define a função de desenho da cena
    gl.glClearColor(1.0, 1.0, 1.0, 1.0)  # Define a cor de fundo da janela como branco
    glut.glutMainLoop()  # Inicia o loop principal do GLUT

if __name__ == "__main__":
    main()
