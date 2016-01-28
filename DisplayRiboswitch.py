'''# In[making the matrix --> and practicing]:

import os

FoldList = os.popen('ls -p /home/flucas/Documents/Bioinformatics/week3/Riboswitch_sequences/llmg_0079 | grep /').read().split()

matrix=[]
for i in range(len(FoldList)):
    os.chdir("/home/flucas/Documents/Bioinformatics/week3/Riboswitch_sequences/llmg_0079/{0}".format(FoldList[i]))
    pngList = os.popen('ls | grep png').read().split()
    if len(pngList) == 0:
        continue
    else:
        matrix.append(pngList)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=" ")
    print()'''

# In[Display Result with the pygame lib]:

'''use as a base to write a scritp that can change the folders.'''
"""
Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/
"""
import pygame
import os

 # Define some colors in RGB format
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

#make the matrix here to prevent doing this 60* per sec in the main while loop
FoldList = os.popen('ls -p /home/flucas/Documents/Bioinformatics/week3/Riboswitch_sequences/llmg_0079 | grep /').read().split()
matrix=[]
for i in range(len(FoldList)):
    os.chdir("/home/flucas/Documents/Bioinformatics/week3/Riboswitch_sequences/llmg_0079/{0}".format(FoldList[i]))
    pngList = os.popen('ls | grep png').read().split()
    if len(pngList) == 0:
        continue
    else:
        matrix.append(pngList)

#draw matrix function. to draw one pic when defined here image should be called only once instead of 60* per sec
def draw_matrix(i, j):
    background_image = pygame.image.load("/home/flucas/Documents/Bioinformatics/week3/Riboswitch_sequences/llmg_0079/{0}{1}".format(FoldList[i+10], matrix[i][j])).convert()
    screen.blit(background_image, [0,0])

# Setup pygame 
pygame.init()
# Set the width and height of the screen [width,height]
size = [591, 800]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Bioinformatics project")
# Loop until the user clicks the close button.
done = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
# Hide the mouse cursor
pygame.mouse.set_visible(True)
# base speed of changing images
iadd = 0
jadd = 0
# start of image in the list
i = 0
j = 0
drawinfo = 0
# -------- Main Program Loop -----------\
while not done:
# --- Event Processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        # User pressed down on a key
        elif event.type == pygame.KEYDOWN:
        # Figure out if it was an arrow key. If so adjust image.
            if event.key == pygame.K_LEFT:
                iadd = -1
            elif event.key == pygame.K_RIGHT:
                iadd = 1
            elif event.key == pygame.K_UP:
                jadd = 1
            elif event.key == pygame.K_DOWN:
                jadd = -1
            elif event.key == pygame.K_j:
                drawinfo = 1
        # User let up on a key'''
        elif event.type == pygame.KEYUP:
        # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                iadd = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                jadd = 0
            elif event.key == pygame.K_j:
                drawinfo = 0
                
    # --- Program Logic
    # change pos in list.
    i = i + iadd
    if i <= 0:
        i = 0
    if i >= (len(matrix)-1):
        i = (len(matrix)-1)
    j = j + jadd
    if j <= 0:
        j = 0
    if j >= (len(matrix[i])-1):
        j = (len(matrix[i])-1)
    # --- Drawing Code
    # First, clear the screen to WHITE. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)
    draw_matrix(i, j)
    
    #showng where you are in the list and which file it is
    font = pygame.font.SysFont('Calibri', 20, True, False)
    text1 = font.render("SeqLen: {0}/{1}".format(i,(len(matrix)-1)),True, BLACK)
    text2 = font.render("Fold: {0}/{1}".format(j,(len(matrix[i])-1)),True, BLACK)
    text3 = font.render("{0}".format(FoldList[i + 10]),True, BLACK)
    screen.blit(text1, [350,2])
    screen.blit(text2, [350,24])
    screen.blit(text3, [350,46])
    #draw additional info of sequence, nothing important yet
    if drawinfo == 1:
        pygame.draw.rect(screen, BLACK, [0, 600, 591, 800])
        text4 = font.render("info about this folding, gene, locus tag",True, WHITE)
        text5 = font.render("additional info: calculated structures e.g. basenr-basnr = terminator",True, WHITE)
        screen.blit(text4, [10, 610])
        screen.blit(text5, [10, 635])
    # update the screen with what we've drawn.
    pygame.display.flip()
    # Limit frames per second
    clock.tick(10)
# Close the window and quit.
pygame.quit()
