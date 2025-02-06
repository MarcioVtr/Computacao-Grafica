from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

def funcao_circunferencia_bresenham(x1, y1, x2, y2):
    raio = math.sqrt((x2 - x1)*2 + (y2 - y1)*2)
    t = 0
    delta_t = 0.0001

    glBegin(GL_POINTS)
    while t < 0.7854:
        x = int(raio * math.cos(t))
        y = int(raio * math.sin(t))

        glVertex2i(x + x1, y + y1)
        glVertex2i(-x + x1, y + y1)
        glVertex2i(-x + x1, -y + y1)
        glVertex2i(x + x1, -y + y1)
        glVertex2i(y + x1, x + y1)
        glVertex2i(y + x1, -x + y1)
        glVertex2i(-y + x1, -x + y1)
        glVertex2i(-y + x1, x + y1)

        t += delta_t
    glEnd()
    glFlush()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)  # Define a cor como branca

    x1, y1 = 0, 0
    x2, y2 = 100, 100
    funcao_circunferencia_bresenham(x1, y1, x2, y2)

    glutSwapBuffers()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(400, 400)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Funcao Circunferencia - Bresenham")

    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-200, 200, -200, 200)

    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()