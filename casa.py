from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    gluOrtho2D(-10.0, 10.0, -10.0, 10.0)

def draw_house():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.0, 1.0)

    # Base da casa
    glBegin(GL_LINE_LOOP)
    glVertex2f(-5, -5)
    glVertex2f(5, -5)
    glVertex2f(5, 5)
    glVertex2f(-5, 5)
    glEnd()

    # Telhado
    glBegin(GL_LINE_LOOP)
    glVertex2f(-6, 5)
    glVertex2f(0, 9)
    glVertex2f(6, 5)
    glEnd()

    # Porta
    glBegin(GL_LINE_LOOP)
    glVertex2f(-2, -5)
    glVertex2f(2, -5)
    glVertex2f(2, 2)  # Aumentei a altura da porta
    glVertex2f(-2, 2)
    glEnd()

    # Janela
    glBegin(GL_LINE_LOOP)
    glVertex2f(2.5, 0)  # Mais próxima à porta
    glVertex2f(4.5, 0)
    glVertex2f(4.5, 2)
    glVertex2f(2.5, 2)
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(3.5, 0)
    glVertex2f(3.5, 2)
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(2.5, 1)
    glVertex2f(4.5, 1)
    glEnd()

    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Casa com OpenGL")
    init()
    glutDisplayFunc(draw_house)
    glutMainLoop()

if __name__ == "__main__":
    main()
