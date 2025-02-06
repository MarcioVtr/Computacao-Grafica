from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

window_height = 300
window_width = 300
window_title = b"Reta com Relevos - OpenGL"


def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Cor de fundo (preto)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, window_width, 0, window_height)  # Sistema de coordenadas 2D


def funcao_reta_com_relevos(x1, y1, x2, y2):
    glBegin(GL_POINTS)

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    x, y = x1, y1
    step_x = 1 if x1 < x2 else -1
    step_y = 1 if y1 < y2 else -1
    count = 0

    while x != x2:
        glVertex2f(x, y)
        x += step_x

        if count % 5 == 0:
            y += step_y * random.randint(1, 3)
        elif count % 10 == 0:
            y -= step_y * random.randint(1, 2)

        count += 1

    glEnd()


def render():
    glClear(GL_COLOR_BUFFER_BIT)  # Limpa a tela
    glColor3f(1.0, 1.0, 1.0)  # Define a cor da linha (branco)

    funcao_reta_com_relevos(50, 50, 250, 200)

    glFlush()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(window_width, window_height)
    glutCreateWindow(window_title)
    init()
    glutDisplayFunc(render)
    glutMainLoop()


if __name__ == "__main__":
    main()
