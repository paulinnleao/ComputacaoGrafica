import OpenGL.GL as gl
import OpenGL.GLUT as glut
import QuestoesService as qs

class Questao01:
    @staticmethod
    def resolucao(ponto_x, ponto_y):
        escala = qs.calcularMaxEMin([ponto_x, ponto_y])
        gl.glColor3f(1.0, 0.0, 0.0)
        gl.glPointSize(8)
        gl.glBegin(gl.GL_POINTS)
        gl.glVertex2f(ponto_x[0], ponto_y[0])
        gl.glEnd()

# def main():
#     glut.glutInit()
#     glut.glutInitDisplayMode(glut.GLUT_RGBA)
#     glut.glutInitWindowSize(720, 720)
#     glut.glutCreateWindow(b"Ponto em OpenGL")
#     glut.glutDisplayFunc(lambda: Questao01.resolucao([5], [5]))  # Usando uma função anônima (lambda) para passar os parâmetros
#     gl.glClearColor(1.0, 1.0, 1.0, 1.0)
#     glut.glutMainLoop()

# main()

def draw_point():
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)
    gl.glPointSize(8)
    gl.glColor3f(1.0, 0.0, 0.0)  # Vermelho
    gl.glBegin(gl.GL_POINTS)
    gl.glVertex2f(5, 5)
    gl.glEnd()
    gl.glFlush()

def main():
    glut.glutInit()
    glut.glutInitDisplayMode(glut.GLUT_SINGLE | glut.GLUT_RGBA)
    glut.glutInitWindowSize(720, 720)
    glut.glutCreateWindow(b"Ponto em OpenGL")
    glut.glutDisplayFunc(draw_point)
    gl.glClearColor(1.0, 1.0, 1.0, 1.0)  # Define a cor de fundo como branco
    glut.glutMainLoop()

main()