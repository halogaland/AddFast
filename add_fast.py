# AddFast
# Test your skill in adding two numbers

import pygame, sys
from pygame.locals import *
from random import randint

# set up pygame
pygame.init()

# set up the window
windowSurface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('addFast')

# set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
LIGHT_BLUE = (128, 128, 255)

# set up fonts
basicFont = pygame.font.SysFont('Arial', 50)
smallFont = pygame.font.SysFont('Arial', 20)

progress_width = 0.001

time_frame = 0.001

rate = 1.0

#game states
start = 0
play = 1
restart = 2

game_state = start

#strings
start_str = ''
question_str = ''
input_str = ''
response_str = ''
stats_str = ''
restart_str = ''

# set up start screen
start_str = 'Hit Enter to Start'

# set up question
question_input_a = randint(0 , 9)
question_input_b = randint(0 , 9)
question_str = str(question_input_a) + ' + ' + str(question_input_b)

# set up input
num_num_keys = 0

# Set up stats
num_of_qs = 0
num_of_right_ans = 0
stats_str = str(num_of_right_ans) + ' / ' + str(num_of_qs)

# Set up restart
restart_str = "Restart? Hit y / n"

# set up the start screen text
start_text = basicFont.render(start_str, True, BLACK)
start_text_x = 100
start_text_y = 200

# set up the question text
question_text = basicFont.render(question_str, True, GREEN)
question_text_x = 50
question_text_y = 50

# set up the input text
input_text = basicFont.render(input_str, True, BLUE)
input_text_x = 50
input_text_y = 120

# set up the computer response text
response_text = smallFont.render(response_str, True, RED)
response_text_x = 50
response_text_y = 190

# set up the stats text
stats_text = basicFont.render(stats_str, True, BLACK)
stats_text_x = 50
stats_text_y = 260

# set up the restart text
restart_text = basicFont.render(restart_str, True, BLACK)
restart_text_x = 100
restart_text_y = 200

def increaseRate() :
    global rate
    rate = rate * 1.2

def decreaseRate() :
    global rate
    rate = rate / 1.2

def startHandleEvents() :
    global game_state

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN :
            if event.key == K_RETURN :
                game_state = play


def startDraw() :
    global start_text

    windowSurface.fill(WHITE)
    start_text = basicFont.render(start_str, True, BLACK)
    windowSurface.blit(start_text, (start_text_x, start_text_y))


def playHandleEvents() :
    global num_num_keys, input_str, game_state, response_str, question_input_a, question_input_b
    global num_of_right_ans, question_str, num_of_qs, stats_str, time_frame, rate

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
                
        if event.type == pygame.KEYDOWN :
            if (ord('0') <= event.key) and (event.key <= ord('9')) :
                # It is a number
                if num_num_keys < 2 :
                    num_num_keys += 1
                    input_str += chr(event.key)
    
            if event.key == ord('p') :
                game_state = restart
    
            if event.key == K_RETURN :
                if input_str :
                    response_str = 'You entered : ' + input_str
                    if (question_input_a + question_input_b) == int(input_str) :
                        response_str += '. Great! Next question.'
                        num_of_right_ans += 1 # Update stats
                        increaseRate()
                    else :
                        response_str += '. Wrong! Next question.'
                        decreaseRate()

                    # update question
                    question_input_a = randint(0, 9)
                    question_input_b = randint(0, 9)
                    question_str = str(question_input_a) + ' + ' + str(question_input_b)
                    # update state
                    num_of_qs += 1
                    stats_str = str(num_of_right_ans) + ' / ' + str(num_of_qs)
                    # update input
                    input_str = ''
                    num_num_keys = 0
                    # reset time
                    time_frame = 0.001
def playDraw() :
    global question_text, input_text, response_text, stats_text, time_frame, num_of_qs, stats_str, input_str, num_num_keys
    global question_input_a, question_input_b, question_str, response_str, rate
    
    # draw the white background onto the surface
    windowSurface.fill(WHITE)
    
    # put all text on screen
    question_text = basicFont.render(question_str, True, GREEN)
    input_text = basicFont.render(input_str, True, BLUE)
    response_text = smallFont.render(response_str, True, RED)
    stats_text = basicFont.render(stats_str, True, BLACK)
    
    windowSurface.blit(question_text, (question_text_x, question_text_y))
    windowSurface.blit(input_text, (input_text_x, input_text_y))
    windowSurface.blit(response_text, (response_text_x, response_text_y))
    windowSurface.blit(stats_text, (stats_text_x, stats_text_y))
    
    progress_width = int(478 * time_frame)

    time_bar = pygame.Surface((480, 20))
    time_bar.fill(WHITE)
    pygame.draw.rect(time_bar, BLACK, (1, 1, 478, 18), 1)
    pygame.draw.rect(time_bar, GREEN, (2, 2, progress_width, 16))
    
    windowSurface.blit(time_bar, (10, 370))

    time_frame += 0.0001 * rate
    
    # reset question if time is up
    if time_frame >= 1 :
        # update response
        response_str = "Time up! Next question"
        decreaseRate()
        # update question
        question_input_a = randint(0, 9)
        question_input_b = randint(0, 9)
        question_str = str(question_input_a) + ' + ' + str(question_input_b)
        # update stats
        num_of_qs += 1
        stats_str = str(num_of_right_ans) + ' / ' + str(num_of_qs)
        # update input
        input_str = ''
        num_num_keys = 0
        time_frame = 0.001

def restartHandleEvents() :
    global input_str, response_str, question_input_a, question_input_b, question_str, num_num_keys, num_of_qs, num_of_right_ans
    global stats_str, time_frame, game_state
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN :
            if event.key == ord('y') :
                # re initialize
                # reset strings
                input_str = ''
                response_str = ''
                # reset question
                question_input_a = randint(0 , 9)
                question_input_b = randint(0 , 9)
                question_str = str(question_input_a) + ' + ' + str(question_input_b)
                # reset input
                num_num_keys = 0
                # reset stats
                num_of_qs = 0
                num_of_right_ans = 0
                stats_str = str(num_of_right_ans) + ' / ' + str(num_of_qs)
                time_frame = 0.001
                game_state = play
                
            if event.key == ord('n') :
                game_state = play

def restartDraw() :
    # draw the white background onto the surface
    windowSurface.fill(WHITE)
    # put all text on screen
    restart_text = basicFont.render(restart_str, True, BLACK)

    windowSurface.blit(restart_text, (restart_text_x, restart_text_y))

# run the game loop
while True:
    if game_state == start :
        startHandleEvents()
        startDraw()

    elif game_state == play :
        playHandleEvents()
        playDraw()
        
    elif game_state == restart :
        restartHandleEvents()
        restartDraw()
        
	# draw the window onto the screen
    pygame.display.update()
