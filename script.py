import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

vertices = (
    ( 1, -1, -1),   # node0
    ( 1,  1, -1),   # node1
    (-1,  1, -1),   # node2
    (-1, -1, -1),   # node3
    ( 1, -1,  1),   # node4
    ( 1,  1,  1),   # node5
    (-1, -1,  1),   # node6
    (-1,  1,  1)    # node7
)

edges = (
    (0, 1),     # edge from node 0 to node 1
    (0, 3),     # edge from node 0 to node 3
    (0, 4),     # edge from node 0 to node 4
    (2, 1),     # edge from node 2 to node 1
    (2, 3),     # edge from node 2 to node 3
    (2, 7),     # edge from node 2 to node 7
    (6, 3),     # edge from node 6 to node 3
    (6, 4),     # edge from node 6 to node 4
    (6, 7),     # edge from node 6 to node 7
    (5, 1),     # edge from node 5 to node 1
    (5, 4),     # edge from node 5 to node 4
    (5, 7)      # edge from node 5 to node 7
)


def Cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0, 0.0, -5.0)

    glRotatef(0, 0, 0, 0)

    while (True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cube()
        pygame.display.flip()
        pygame.time.wait(10)


main()
