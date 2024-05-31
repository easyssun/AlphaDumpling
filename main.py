import pygame
import time
import random
import sys

sys.path.append('')

from Algorithm.Synergy import *
from Algorithm.algorithm import *

# Functions that adjust image size
# image_file_name: file name
# ratio: scaling size
def image_rescale(image_file_name, ratio = 0.27):
    image = pygame.image.load("image/" + image_file_name + ".png")
    image_size = image.get_rect().size
    image_width = image_size[0]
    image_height = image_size[1]

    image = pygame.transform.scale(image, (image_width * ratio, image_height * ratio))

    return image
    
# general button class
class Button():
    
    # Value received as a factor:
    # Button x, y coordinates | Button length, width | Text x, y coordinates | Text | Functions to run when clicked | Button image
    def __init__(self, x, y, width, height, text_x, text_y, buttonText = 'Button', onclickFunction = None, onePress = False, buttonImage = None):
        
        # Button x, y coordinates
        self.x = x
        self.y = y

        # Button length, width
        self.width = width
        self.height = height

        # Text x, y coordinates
        self.text_x = text_x
        self.text_y = text_y

        # Functions to run when clicked
        self.onclickFunction = onclickFunction

        # location of cursor
        mouse = pygame.mouse.get_pos()
        self.mouse = pygame.mouse.get_pos()

        # clicked or not
        click = pygame.mouse.get_pressed()

        # button
        self.buttonSurface = pygame.Surface((self.width, self.height))

        # rectangle bound
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        # button surface
        self.buttonSurf = font.render(buttonText, True, (20, 20, 20))

        # button color(normal / hover / pressed)
        self.fillColors = {
            'normal': '#ffffff',
            'hover': '#666666',
            'pressed': '#333333',
        }

        # button image
        self.buttonImage = buttonImage
        

        # (1) If the mouse is in the button
        if x + width > mouse[0] > x and y + height > mouse[1] > y:
            # change button color
            self.buttonSurface.fill(self.fillColors['hover'])
            screen.blit(self.buttonSurface, (x, y))

            if self.buttonImage is None:
                screen.blit(self.buttonSurf, (self.text_x, self.text_y))
            else:
                screen.blit(self.buttonImage, (self.x, self.y))
                
            # (2) If the mouse is clicked inside the button
            if click[0] and onclickFunction is not None:
                # button color change
                self.buttonSurface.fill(self.fillColors['pressed'])
                time.sleep(0.2)
                
                # execute function
                onclickFunction()

                
        # (3) If the mouse is not in the button
        else:
            # change button color
            self.buttonSurface.fill(self.fillColors['normal'])
            screen.blit(self.buttonSurface, (x, y))
            if self.buttonImage is None:
                screen.blit(self.buttonSurf, (self.text_x, self.text_y))
            else:
                screen.blit(self.buttonImage, (self.x, self.y))


# Ingredient selection button class
class ingredient_button():

    # argument: 
    # Button x, y coordinates | Button length, width | Material number
    def __init__(self, x, y, width, height, buttonIndex = 0, ImageName = None, onePress = False):
        
        # Button x, y coordinates
        self.x = x
        self.y = y

        # Button length, width
        self.width = 100
        self.height = 90

        # Ingredient number
        self.buttonIndex = buttonIndex

        # location of cursor
        self.mouse = pygame.mouse.get_pos()
        mouse = pygame.mouse.get_pos()
        
        # clicked or not
        click = pygame.mouse.get_pressed()
            
        # button surface
        self.buttonSurface = pygame.Surface((self.width, self.height))

        # rectangle bound
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        # button image
        self.ImageName = ImageName
        self.buttonImage = None
        
        # Ingredients to be 0.185x
        rate_185 = ["mintchoco", "Gochujang", "soju", "garlic", "onion"]
        
        # Ingredients to be 0.205x
        rate_205 = ["chamoil", "mayo", "Cheese", "juice", "water"]

        if self.ImageName in rate_185:
            self.buttonImage = image_rescale(self.ImageName + "-removebg-preview", 0.185)
        elif self.ImageName in rate_205:
            self.buttonImage = image_rescale(self.ImageName + "-removebg-preview", 0.205)
        
        # x mark on the ingredient that already selected
        self.x_user = image_rescale("x_user", 0.3)
        self.x_robot = image_rescale("x_robot", 0.3)

        # button color(normal / hover / pressed)
        self.fillColors = {
            'normal': '#B475D0',
            'hover': '#666666',
            'pressed': '#333333',
        }
        
        # the variable used to create the DP table
        index = 0
        
        global userSelectCount

        if self.buttonImage == None:
            print("buttonImage is none")



        # If it's the ingredient that user chose,
        if (self.buttonIndex in ingredient_user):
            screen.blit(self.buttonSurface, (self.x, self.y))
            screen.blit(self.buttonImage, (self.x, self.y))
            # show red x mark on
            screen.blit(self.x_user, (self.x, self.y))
            
        # Else if it's the ingredient that robot chose,
        elif (self.buttonIndex in ingredient_robot):
            screen.blit(self.buttonSurface, (self.x, self.y))
            screen.blit(self.buttonImage, (self.x, self.y))
            # show blue x mark on
            screen.blit(self.x_robot, (self.x, self.y))
             
        # Else no one chose it,
        else:

            # (1) If the mouse is in the button
            if x + width > mouse[0] > x and y + height > mouse[1] > y:

                # button color change
                self.buttonSurface.fill(self.fillColors['hover'])
                screen.blit(self.buttonSurface, (x, y))  
                screen.blit(self.buttonImage, (self.x, self.y))
                
                # (2) If the mouse is clicked inside the button
                if click[0]:
                
                    # button color change
                    screen.blit(self.buttonSurface, (x, y)) 
                    screen.blit(self.buttonImage, (self.x, self.y))
                    self.buttonSurface.fill(self.fillColors['pressed'])
                     
                    # append ingredients that user chose to ingredient_user list
                    ingredient_user.append(buttonIndex)
                    total_ingredient.append(buttonIndex)
                    
                    # if user select ingredient, increase user count
                    userSelectCount += 1
                    
                    # show remaining select count
                    pygame.draw.rect(screen, (180, 117, 208), (550, 10, 100, 100))   
                    text_remaining_choice = font.render("Remain: " + (str)(maxSelectCount - userSelectCount), True, [0, 0, 0])
                    screen.blit(text_remaining_choice, [435, 10])

                    # load ingredient button
                    ingredient_button_load()

                    # load ingredient image
                    ingredient_put_load()

                    pygame.display.update()
                            

                    # When the user makes the first choice on that stage,
                    # Create Synergy DP
                    if (len(ingredient_user) == 1):
                        firstSynergyList = Synergy.getSynergyList()
                        firstSynergyList.remove(buttonIndex)
                        botRandomChoice = random.choice(firstSynergyList)
                        initSynergy(botRandomChoice, ingredient_robot)
                        weightDP[buttonIndex].append(-1)
                        total_ingredient.append(botRandomChoice)
                        print("BOT Random Choice ", botRandomChoice)
                        time.sleep(1)

                    # When it's not the first choice on that stage,
                    # -> Robot selects materials in a greener way.
                    # -> Add materials to the list
                    # -> Update the robot's DP table
                    # -> Robot guess synergy table update (learning)
                    else:
                        print("-------------------")
                        
                        weightDP[buttonIndex].append(-1)
                        time.sleep(1)
                        botSelect = Greedy()
                        print("BOT Choice ", botSelect)
                        ingredient_robot.append(botSelect)
                        total_ingredient.append(botSelect)
                        learning(ingredient_robot, botSelect)
                        updateDP(index, botSelect, ingredient_robot)
                        
                        
                    time.sleep(0.2)
                        
            # (3) If the mouse is not in the button   
            else:

                # button color change
                self.buttonSurface.fill(self.fillColors['normal'])
                screen.blit(self.buttonSurface, (x, y))
                screen.blit(self.buttonImage, (x, y)) 


#------------------------------
# Initialize before game starts
#------------------------------

# initialize the pygame library
pygame.init()

# set screen size
screen_width = 1000
screen_height = 562

# screen setting
screen = pygame.display.set_mode((screen_width, screen_height))

# title setting
title = "Alpha Dumpling"
pygame.display.set_caption(title)

# loading background image
background = image_rescale("Main_background")        

# font setting
font = pygame.font.SysFont('Arial', 40)

# initialize ingredient choice list
global ingredient_user
ingredient_user = []

global ingredient_robot
ingredient_robot = []

global total_ingredient 
total_ingredient = []

global maxSelectCount 
maxSelectCount = 4

# user's selection count
global userSelectCount
userSelectCount = 0

#------------------------------------
# load ingredient buttons and images
#------------------------------------

# global running_menu
# global running_info
# global running_game
    
# load ingredient image
def ingredient_button_load():
     # setting y-coordinate of ingredient button
    ingredient_line1_y_pos = 370
    ingredient_line2_y_pos = 470
    
    # load ingredient button (num 1~5)
    ingredient_button(83, ingredient_line1_y_pos, 100, 70, "MINT_CHOCOLATE", "mintchoco")
    ingredient_button(266, ingredient_line1_y_pos, 100, 70, "SESAME_OIL", "chamoil")
    ingredient_button(449, ingredient_line1_y_pos, 100, 70, "KOCHUJANG", "Gochujang")
    ingredient_button(632, ingredient_line1_y_pos, 100, 70, "MAYONNAISE", "mayo")
    ingredient_button(815, ingredient_line1_y_pos, 100, 70, "SOJU", "soju")

    # load ingredient button (num 6~10)
    ingredient_button(83, ingredient_line2_y_pos, 100, 70, "CHEESE", "Cheese")
    ingredient_button(266, ingredient_line2_y_pos, 100, 70, "GALIC", "garlic")
    ingredient_button(449, ingredient_line2_y_pos, 100, 70, "ONION", "onion")
    ingredient_button(632, ingredient_line2_y_pos, 100, 70, "JUICE", "juice")
    ingredient_button(815, ingredient_line2_y_pos, 100, 70, "WATER", "water")

    ingredient_put_load()


# load ingredient images
# on a mixing bowl
def ingredient_put_load():
    ingredient_image = ["mintchoco", "chamoil", "Gochujang", "mayo", "soju", "Cheese", "garlic", "onion", "juice", "water"]
    
    ingredient_to_num = {"MINT_CHOCOLATE": 1, "SESAME_OIL": 2, "KOCHUJANG": 3, "MAYONNAISE": 4, "SOJU": 5, \
        "CHEESE": 6, "GALIC": 7, "ONION": 8, "JUICE": 9, "WATER": 10}
    
    # location of image
    location_put_user = [(600, 120), (700, 160), (650, 220), (550, 220)]
    
    location_put_robot = [(230, 120), (330, 160), (280, 220), (180, 220)]
    
    # Ingredients to be 0.185x
    rate_185 = ["mintchoco", "Gochujang", "soju", "garlic", "onion"]
    
    # Ingredients to be 0.205x
    rate_205 = ["chamoil", "mayo", "Cheese", "juice", "water"]


    location_num = 0
    
    # load ingredient that user chose
    for user_ingredient in ingredient_user:
        
        ingredient = ingredient_image[ingredient_to_num[user_ingredient] - 1]
        
        if ingredient in rate_185:
            image = image_rescale(ingredient + "-removebg-preview", 0.185)
        elif ingredient in rate_205:
            image = image_rescale(ingredient + "-removebg-preview", 0.205)
            
        screen.blit(image, location_put_user[location_num])
        location_num += 1

    location_num = 0

    # load ingredient that robot chose
    for robot_ingredient in ingredient_robot:
        ingredient = ingredient_image[ingredient_to_num[robot_ingredient] - 1]
        
        if ingredient in rate_185:
            image = image_rescale(ingredient + "-removebg-preview", 0.185)
        elif ingredient in rate_205:
            image = image_rescale(ingredient + "-removebg-preview", 0.205)
        
        screen.blit(image, location_put_robot[location_num])
        location_num += 1
    
#------------------
# load intro screen
#------------------

# intro image list
intro_images = ["intro1", "intro2", "intro3", "intro4", "intro5", "intro6", "intro7", "intro8"]

def intro():
    for intro_image in intro_images:
        intro_image = image_rescale(intro_image)
       
        screen.blit(intro_image, (0, 0))
        pygame.display.flip()
        time.sleep(2)
    menu()

#------------------
# load main screen
#------------------

def menu():
    initialize()
    initialize_algorithm()
    random_estimation()

    # setting font
    font_title = pygame.font.SysFont('Arial', 80)
    text = font_title.render("Alpha Dumpling", True, (0,0,0))

    global running_menu
    running_menu = True
    while running_menu:
        for event in pygame.event.get():

            # When an event occurred to close the window
            if event.type == pygame.QUIT:
                running_menu = False # exit

        # setting screen
        screen.fill((0, 0, 0)) # fill color on the screen
        screen.blit(background, (0, 0)) # load background image
        Button(300, 250, 400, 100, 410, 280, 'Game Start', onclickFunction = loading) # load start button
        Button(300, 400, 400, 100, 365, 430, 'Game Information', onclickFunction = info) # load game information button

        # update screen
        pygame.display.flip()
        
#-----------------
# loading information screen
#-----------------

def info():

    # setting home button
    home_button = pygame.image.load("image/home.png")
    
    global running_info
    running_info = True
    while running_info:
        for event in pygame.event.get():

            # When an event occurred to close the window
            if event.type == pygame.QUIT:
                running_info = False # exit

        # screen setting 
        info_image = image_rescale("info")

        screen.blit(info_image, (0, 0))
        Button(0, 0, 50, 50, 0, 0, onclickFunction = menu, buttonImage = home_button)
        
        # screen update
        pygame.display.flip()

#----------------------------------
# Loading main game loading screen
#----------------------------------

# loading images
loading_images = ["loading1", "loading2", "loading3"]

def loading():
    for loading_image in loading_images:
        screen.fill((0,0,0))
        loading_image = image_rescale(loading_image)

        screen.blit(loading_image, (0, 0))
        pygame.display.flip()
        time.sleep(1.5)
    game()
        
#-----------------
# loading game screen
#-----------------

global stage
stage = 1

def game():
    initialize()
    initialize_algorithm()
    global userSelectCount
    global stage
    userSelectCount = 0
    
    botScore = 0
    userScore = 0

    # setting background
    game_background = image_rescale("game_background")
        
    # setting home button
    home_button = pygame.image.load("image/home.png")
    
    running_game = True
    while running_game:

        # setting text
        text_robot_score = font.render((str)(botScore), True, [0, 0, 0])

        text_ajussi_score = font.render((str)(userScore), True, [0, 0, 0])
        
        text_remaining_choice = font.render("Remain: " + (str)(maxSelectCount - userSelectCount), True, [0, 0, 0])
        
        text_stage = font.render("Stage " + (str)(stage), True, [0, 0, 0])


        for event in pygame.event.get():

            # When an event occurred to close the window
            if event.type == pygame.QUIT:
                running_game = False # eixt

        # update score
        userScore = sumSynergy(ingredient_user)

        botScore = sumSynergy(ingredient_robot)

        
        # if user has made all the choices,
        if userSelectCount == maxSelectCount:
            # update score
            userScore = sumSynergy(ingredient_user)

            botScore = sumSynergy(ingredient_robot)
            
            print("User score: ", userScore)
            print("Alpha score: ", botScore)

            # If user won on the stage,
            if (userScore > botScore):
                # If it was fourth stage,
                # win
                if(stage == 4): 
                    win()

                # Or,
                # go to next stage
                stage += 1
                print("Next Stage: " + (str)(stage))
                time.sleep(1)
                game()

            # Else robot won on the stage,
            else:
                stage = 1
                lose()
                print("You lose.....")
                return

        # setting screen
        screen.fill((0,0,0)) 
        screen.blit(game_background, (0,0)) 
        Button(0, 0, 50, 50, 0, 0, onclickFunction=menu, buttonImage = home_button) # load home button

        screen.blit(text_robot_score, [290, 70])
        screen.blit(text_ajussi_score, [725, 70])
        screen.blit(text_remaining_choice, [435, 10])
        screen.blit(text_stage, [850, 10])
        
        # load ingredient button
        ingredient_button_load()

        # screen update
        pygame.display.flip()

#------------------
# loading win screen
#------------------

# win images
win_images = ["victory1", "victory2"]

def win():
    for win_image in win_images:
        win_image = image_rescale(win_image)
        
        screen.blit(win_image, (0,0))
        pygame.display.flip()
        time.sleep(1.5)
    time.sleep(0.5)
    
    global running_win
    running_win = True

    continue_button = image_rescale("continue", 0.08)

    while(running_win) :
        for event in pygame.event.get():

            # When an event occurred to close the window
            if event.type == pygame.QUIT:
                running_win = False # eixt
            
        screen.blit(image_rescale("victory3"), (0,0))
        Button(710, 490, 280, 75, 0, 0, buttonText = ' ', onclickFunction = menu, buttonImage = continue_button)
        pygame.display.flip()
        

#------------------
# loading lose screen
#------------------

# lose images
lose_images = ["lose1","lose2","lose3"]

def lose():
    for lose_image in lose_images:
        lose_image = image_rescale(lose_image)

        screen.blit(lose_image, (0,0))
        pygame.display.flip()
        time.sleep(1.5)

    global running_lose
    running_lose = True

    retry_button = image_rescale("retry", 0.08)


    while(running_lose) :
        for event in pygame.event.get():

            # When an event occurred to close the window
            if event.type == pygame.QUIT:
                running_lose = False # eixt
    
        screen.blit(image_rescale("lose4"), (0,0))
        Button(70, 420, 250, 100, 0, 0, buttonText = ' ', onclickFunction = menu, buttonImage = retry_button)
        pygame.display.flip()

#-------------
# Initialize
# ------------
def initialize():

    # Initialize ingredient selection list
    global ingredient_user
    ingredient_user = []
    
    global ingredient_robot
    ingredient_robot = []
    
    global total_ingredient
    total_ingredient = []
    
    # Maximum selections in the stage
    global maxSelectCount
    maxSelectCount = 4

    # Number that user chose
    global userSelectCount
    userSelectCount = 0
    
    global running_lose
    running_lose = False

    global running_win
    running_win = False

    global running_info
    running_info = False

    global running_menu
    running_menu = False

    global running_game
    running_game = False
    
# game start at the intro screen
intro()

# exit pygame
pygame.quit()