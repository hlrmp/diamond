import pygame
from pygame.locals import * 
from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()

display = (1280,720)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
pygame.display.set_caption("Emerald")

gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
glTranslatef(0,0,-30)
glScale(1,1,1)
def draw_cube():

    glBegin(GL_TRIANGLES)
 

# top box
    
    #side 1
    glColor(0.6, 0.5, 1)
    glVertex3f(0, 0, -1)
    glVertex3f(1.5, 1.5, -0.5)
    glVertex3f(1.5, -1.5, -0.5)

    #side 2
    glColor(0.6, 0.5, 1)
    glVertex3f(0, 0, -1)
    glVertex3f(1.5, -1.5, -0.5)
    glVertex3f(-1.5, -1.5, -0.5)

    #side 3
    glColor(0.6, 0.5, 1)
    glVertex3f(0, 0, -1)
    glVertex3f(-1.5, -1.5, -0.5)
    glVertex3f(-1.5, 1.5, -0.5)

    #side 4
    glColor(0.6, 0.5, 1)
    glVertex3f(0, 0, -1)
    glVertex3f(1.5, 1.5, -0.5)
    glVertex3f(-1.5, 1.5, -0.5)


# top sides small
    
    # side 1
    glColor(0.31, 0.78, 1)
    glVertex3f(1.5, -1.5, -0.5)
    glVertex3f(3, -2, 0)
    glVertex3f(2, -3, 0)

    # side 2
    glColor(0.31, 0.78, 1)
    glVertex3f(1.5, 1.5, -0.5)
    glVertex3f(2, 3, 0)
    glVertex3f(3, 2, 0)

    # side 3
    glColor(0.31, 0.78, 1)
    glVertex3f(-1.5, -1.5, -0.5)
    glVertex3f(-2, -3, 0)
    glVertex3f(-3, -2, 0)

    # side 4
    glColor(0.31, 0.78, 1)
    glVertex3f(-1.5, 1.5, -0.5)
    glVertex3f(-2, 3, 0)
    glVertex3f(-3, 2, 0)


# top sides large
    
    # box 1
    glColor(1, 0.78, 1)
    glVertex3f(-1.5, -1.5, -0.5)
    glVertex3f(-1.5, 1.5, -0.5)
    glVertex3f(-3, -2, 0)
    
    glColor(1, 0.78, 1)
    glVertex3f(-3, -2, 0)
    glVertex3f(-3, 2, 0)
    glVertex3f(-1.5, 1.5, -0.5)

    # box 2
    glColor(1, 0.78, 1)
    glVertex3f(-2, 3, 0)
    glVertex3f(1.5, 1.5, -0.5)
    glVertex3f(-1.5, 1.5, -0.5)

    glColor(1, 0.78, 1)
    glVertex3f(1.5, 1.5, -0.5)
    glVertex3f(2, 3, 0)
    glVertex3f(-2, 3, 0)

    # box 3
    glColor(1, 0.78, 1)
    glVertex3f(-2, -3, 0)
    glVertex3f(-1.5, -1.5, -0.5)
    glVertex3f(1.5, -1.5, -0.5)

    glColor(1, 0.78, 1)
    glVertex3f(1.5, -1.5, -0.5)
    glVertex3f(2, -3, 0)
    glVertex3f(-2, -3, 0)

    # box 4
    glColor(1, 0.78, 1)
    glVertex3f(3, -2, 0)
    glVertex3f(1.5, -1.5, -0.5)
    glVertex3f(1.5, 1.5, -0.5)

    glColor(1, 0.78, 1)
    glVertex3f(1.5, 1.5, -0.5)
    glVertex3f(3, 2, 0)
    glVertex3f(3, -2, 0)






    # side 8
    glColor(0.31, 1, 1)
    glVertex3f(0, 0, 3)
    glVertex3f(3, 2, 0)
    glVertex3f(2, 3, 0)

    # side 7
    glColor(0.31, 0.78, 0.47)
    glVertex3f(0, 0, 3)
    glVertex3f(3, 2, 0)
    glVertex3f(3, -2, 0)

    # side 6
    glColor(0.31, 1, 1)
    glVertex3f(0, 0, 3)
    glVertex3f(3, -2, 0)
    glVertex3f(2, -3, 0)

    # side 5
    glColor(0.31, 0.78, 0.47)
    glVertex3f(0, 0, 3)
    glVertex3f(2, -3, 0)
    glVertex3f(-2, -3, 0)

    # side 4
    glColor(0.31, 1, 1)
    glVertex3f(0, 0, 3)
    glVertex3f(-2, -3, 0)
    glVertex3f(-3, -2, 0)

    # side 3
    glColor(0.31, 0.78, 0.47)
    glVertex3f(0, 0, 3)
    glVertex3f(-3, -2, 0)
    glVertex3f(-3, 2, 0)

    
    # side 2
    glColor(0.31, 1, 1)
    glVertex3f(0, 0, 3)
    glVertex3f(-3, 2, 0)
    glVertex3f(-2, 3, 0)

    # side 1
    glColor(0.31, 0.78, 0.47)
    glVertex3f(0, 0, 3)
    glVertex3f(2, 3, 0)
    glVertex3f(-2, 3, 0)





    glEnd()

def controls():
    if event.type == pygame.KEYDOWN:

        if event.key == pygame.K_a:
            glTranslatef(-1,0,0)
        if event.key == pygame.K_s:
            glRotatef(45.0, 0.0, 1.0, 0.0)
            glTranslatef(0,-1,0)
        if event.key == pygame.K_d:
            glTranslatef(1,0,0)
        if event.key == pygame.K_w:
            glRotatef(90.0, 0.0, 1.0, 0.0)
            glTranslatef(0,1,0)
        


while True:
    for event in pygame.event.get():
        controls()
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glEnable(GL_DEPTH_TEST)
    glRotate(1,1,0,0)
    draw_cube()
   


    pygame.display.flip()
    pygame.time.wait(15)
















