import random
from pygame.locals import *
from sys import exit
import pygame
from enum import Enum

class Player_Option(Enum):
    ROCK = 0
    PAPER = 1
    SCISSORS = 2

class Ending_Option(Enum):
    DRAW = 0
    WIN = 1
    LOSE = 2

class Game_States(Enum):
    ANSWERING = 0
    CHOOSING = 1
    DRAW = 2
    WIN = 3
    LOSE = 4
    BEGINNING = 5
    SUBTITLE = 6

#doing maths
def calc_ypos(image_height, screen_height):
    half_height = image_height / 2
    ypos= (screen_height / 2) - half_height
    return ypos

def decision(player_choice, computer_choice):
    if player_choice == computer_choice:
        return Ending_Option.DRAW
    if player_choice == Player_Option.ROCK:
        if computer_choice == Player_Option.SCISSORS:
            return Ending_Option.WIN
        if computer_choice == Player_Option.PAPER:
            return Ending_Option.LOSE
    if player_choice == Player_Option.PAPER:
        if computer_choice == Player_Option.ROCK:
            return Ending_Option.WIN
        if computer_choice == Player_Option.SCISSORS:
            return Ending_Option.LOSE
    if player_choice == Player_Option.SCISSORS:
        if computer_choice == Player_Option.ROCK:
            return Ending_Option.LOSE
        if computer_choice == Player_Option.PAPER:
            return Ending_Option.WIN
    
def drawing_centre(input_image, input_screen):
        blit_width = input_image.get_rect().width
        blit_length = input_image.get_rect().height

        blit_pos_x = input_screen.get_width() / 2
        blit_pos_x -= blit_width / 2

        blit_pos_y = input_screen.get_height() / 2
        blit_pos_y -= blit_length / 2

        input_screen.blit(input_image, (blit_pos_x, blit_pos_y))

def end_displaying(screen_place, living_option, ai_option, reset_image):
    user_text = font_states.render("You chose:...", True, (255,69,0))
    computer_text = font_states.render ("The computer chose:...", True, (255,69,0))

    user_place_width = user_text.get_rect().width
    user_place_length = user_text.get_rect().height
    comuter_place_width =  computer_text.get_rect().width
    computer_place_length = computer_text.get_rect().height

    user_place_x = screen_place.get_rect().width / 20
    user_place_y = screen_place.get_rect().height / 4
    user_place_y -= user_place_length    
    

    computer_place_y = (screen_place.get_rect().height / 4) * 3

    screen_place.blit (user_text, (user_place_x, user_place_y))
    screen_place.blit (computer_text, (user_place_x, computer_place_y))

    user_option_place_width = living_option.get_rect().width
    user_option_place_length = living_option.get_rect().height
    computer_option_place_width = ai_option.get_rect().width
    computer_option_place_length = ai_option.get_rect().height

    user_option_place_x = screen_place.get_rect().width / 2
    user_option_place_x -= user_option_place_width / 2
    computer_option_place_x = screen_place.get_rect().width / 2
    computer_option_place_x -= computer_option_place_width / 2
    computer_option_place_y = screen_place.get_rect().height 
    computer_option_place_y -= ai_option.get_rect().height

    reset_image_x = screen_place.get_rect().width / 20
    
    screen_place.blit (living_option, (user_option_place_x,0))
    screen_place.blit (ai_option, (computer_option_place_x,computer_option_place_y))
    return screen_place.blit (reset_image, (0,0))

    print (user_option_place_width)

    
score = 0
ai = 0

#setup the display
pygame.init()
screen_width=800
screen_length=600
screen = pygame.display.set_mode((screen_width, screen_length))

#choosing font
font = pygame.font.SysFont("Arial",75)
font_states = pygame.font.SysFont("Arial", 30)
font_big = pygame.font.SysFont("Arial", 85)
font_small = pygame.font.SysFont("Arial", 30)

#tick tok
clock=pygame.time.Clock()

#load all images
image_rock = pygame.image.load(r'images/rock.jpg') #import rock image
image_paper = pygame.image.load(r'images/paper.jpg') #import paper image
image_scissors = pygame.image.load (r'images/scissors.jpg') #import scissors image
image_reset = pygame.image.load (r'images/reset.png') #imports reset button

sound_rock = pygame.mixer.Sound(r"recordings/final/rock.wav")
sound_paper = pygame.mixer.Sound(r"recordings/final/paper.wav")
sound_scissors = pygame.mixer.Sound(r"recordings/final/scissors.wav")


list_images = {
    Player_Option.ROCK: image_rock, 
    Player_Option.PAPER: image_paper , 
    Player_Option.SCISSORS: image_scissors
    }


#finding yposition
ypos_rock = calc_ypos(image_rock.get_rect().height,screen_length)
ypos_paper = calc_ypos(image_paper.get_rect().height, screen_length)
ypos_scissors = calc_ypos(image_scissors.get_rect().height, screen_length)


#finding xpos?
gap = screen_width
gap -= image_rock.get_rect().width
gap -= image_paper.get_rect().width
gap -= image_scissors.get_rect().width
gap /= 4

xpos_rock = gap
xpos_paper = gap + image_rock.get_rect().width + gap
xpos_scissors = xpos_paper + image_paper.get_rect().width + gap


state = Game_States.BEGINNING

#start the main game loop
while True:
    clock.tick(30)

    #Drawing the images
    #display all of the images

    if state == Game_States.BEGINNING:
        screen.fill ((0,0,0))
        welcome_text = font_big.render("Welcome to the game!", True, (0,0,255))
        welcome_text_x = screen_width / 2
        welcome_text_x -= welcome_text.get_rect().width / 2
        welcome_text_y = screen_length / 2
        welcome_text_y -= welcome_text.get_rect().height / 2
        screen.blit (welcome_text, (welcome_text_x,welcome_text_y))
        
        start_text = font_big.render("Start.", True, (0,0,255))
        start_text_x = screen_width / 2
        start_text_x -= start_text.get_rect().width / 2
        start_text_y = screen_length / 4
        start_text_y -= start_text.get_rect().height / 4
        start_image = screen.blit (start_text, (start_text_x, start_text_y))

        points_text = font_big.render("Credits", True, (0,0,255))
        points_text_x = screen_width / 2
        points_text_x -= points_text.get_rect().width / 2
        points_text_y = (screen.get_rect().height / 4) * 3
        credits_image = screen.blit (points_text, (points_text_x, points_text_y))


    

    if state == Game_States.CHOOSING:
        screen.fill((18.2,160.5,245.9))
        rock_blit = screen.blit(image_rock, (xpos_rock, ypos_rock))
        paper_blit = screen.blit(image_paper, (xpos_paper, ypos_paper))
        scissors_blit = screen.blit(image_scissors, (xpos_scissors, ypos_scissors))
    
    if state == Game_States.ANSWERING:
        screen.fill((255,0,0))
        text_image = font.render("The computer is choosing.", True, (255,255,255))

        drawing_centre(text_image, screen)
        pygame.display.update()
        pygame.time.delay(3000)
        
        computer_Option = random.choice(list(Player_Option))
        ending = decision(human_option, computer_Option)



        if ending == Ending_Option.DRAW:
            state = Game_States.DRAW
            ai = ai + 0.5
            score = score + 1
        if ending == Ending_Option.LOSE:
            state = Game_States.LOSE
            ai = ai + 1
        if ending == Ending_Option.WIN:
            state = Game_States.WIN
            score = score + 1
        
    if state == Game_States.WIN:
        screen.fill((124,252,0))
        win_image = font.render("You won! Well done!", True, (255,255,255), (135,206,250))
        drawing_centre(win_image, screen)
        reset_button = end_displaying(screen, list_images[human_option], list_images[computer_Option], image_reset)
                        
    if state == Game_States.LOSE:
        screen.fill((250,128,114))
        lose_image = font.render("You lost! Shame.", True, (255,255,255), (255,215,0))
        drawing_centre(lose_image, screen)
        reset_button = end_displaying(screen, list_images[human_option], list_images[computer_Option], image_reset)
                        
    if state == Game_States.DRAW:
        screen.fill((255,255,153))
        draw_image = font.render("It's a draw!", True, (255,69,0), (240,255,240))
        drawing_centre(draw_image, screen)
        reset_button = end_displaying(screen, list_images[human_option], list_images[computer_Option], image_reset)
            

    if state != Game_States.ANSWERING and state != Game_States.BEGINNING:
        score_blit = font.render (str(score), True, (255,69,0), (240,255,240))
        score_x = screen.get_rect().width
        score_x -= score_blit.get_rect().width
        screen.blit (score_blit, (score_x,0))  

        ai_blit = font.render (str(ai), True, (255,69,0), (240,255,240))
        ai_x = screen.get_rect().width
        ai_x -= score_blit.get_rect().width
        #ai_y = screen_length / 2
        #ai_y -= (screen_length.get_rect().height / 4) * 3
        
        screen.blit(ai_blit, (ai_x,513))

    if state == Game_States.SUBTITLE:
        screen.fill ((0,0,0))
        credits_one = font_small.render("This is a credits list.", True, ((255,255,255)))
        credits_two = font_small.render("Thank you to Dom for helping me write this program.", True, ((255,255,255)))
        credits_three = font_small.render("Thank you to Chris for the moral support!", True, ((255,255,255)))
        credits_four = font_small.render("Shoutout to gogs, ci and wiki.", True, ((255,255,255)))
        screen.blit (credits_one,(100,100))
        screen.blit (credits_two,(100,200))
        screen.blit (credits_three,(100,300))
        screen.blit (credits_four,(100,400))

    

    #Updating the display
    pygame.display.update()              

    # Handling events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit
        

        if event.type == MOUSEBUTTONUP:
            if event.button == 1:
                if state == Game_States.CHOOSING:


                
                    #adds events
                    if rock_blit.collidepoint(event.pos):
                        state = Game_States.ANSWERING
                        human_option = Player_Option.ROCK
                        sound_rock.play()
                    if paper_blit.collidepoint(event.pos):
                        state = Game_States.ANSWERING
                        human_option = Player_Option.PAPER
                        sound_paper.play()
                    if scissors_blit.collidepoint(event.pos):
                        state = Game_States.ANSWERING
                        human_option = Player_Option.SCISSORS
                        sound_scissors.play()
               

    
                if state == Game_States.DRAW or state == Game_States.LOSE or state == Game_States.WIN:
                    if reset_button.collidepoint(event.pos):
                        state = Game_States.CHOOSING
                if state == Game_States.BEGINNING:
                    if start_image.collidepoint(event.pos):
                        state = Game_States.CHOOSING
                    if credits_image.collidepoint(event.pos):
                        state = Game_States.SUBTITLE
