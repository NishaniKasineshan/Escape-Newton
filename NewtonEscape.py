import pygame
import random

screen_size=(360,600)
screen=pygame.display.set_mode(screen_size)
pygame.font.init()
pygame.mixer.init()

background=pygame.image.load('background.jpg')
newton=pygame.image.load('newton.png')
apple=pygame.image.load('apple.png')

winner_font=pygame.font.SysFont('comicsans',50)
bullet_hit_sound=pygame.mixer.Sound('Assets_Grenade+1.mp3')

def display_score(score):
    font=pygame.font.SysFont('Comic Sans MS',30)
    score_text="Score: "+str(score)
    text_img=font.render(score_text,True,(240,240,240))
    screen.blit(text_img,(20,40))

def random_offset():
    return -1*random.randint(100,2500)

apple_y=[random_offset(),random_offset(),random_offset()]
newton_x=150
newton_y=520
score=10

def draw_winner(text):
    draw_text=winner_font.render(text,1,(255,255,255))
    screen.blit(draw_text,(360/2-draw_text.get_width()/2,600/2-draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)

def crashed(idx):
    global score
    global keep_alive
    score=score-5
    #print('Oh god!Crashed with apple',idx,score)
    apple_y[idx]=random_offset()
    if score<0:
          keep_alive=False
          
        
def update_apple_position(idx):
    global score
    if apple_y[idx]>600:
        apple_y[idx]=random_offset()
        score=score+10
        #print("Score",score)
    else:
        apple_y[idx]=apple_y[idx]+5
    

keep_alive=True
clock=pygame.time.Clock()
while keep_alive:
    pygame.event.get()
    keys=pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and newton_x<280:
        newton_x=newton_x+10
    elif keys[pygame.K_LEFT] and newton_x>0:
        newton_x=newton_x-10
        
    update_apple_position(0)
    update_apple_position(1)
    update_apple_position(2)
    
    screen.blit(background,(0,0))
    screen.blit(newton,(newton_x,520))
    screen.blit(apple,(0,apple_y[0]))
    screen.blit(apple,(150,apple_y[1]))
    screen.blit(apple,(280,apple_y[2]))

    if apple_y[0]>500 and newton_x<50:
        crashed(0)
        bullet_hit_sound.play()

    if apple_y[1]>500 and newton_x>80 and newton_x<150:
        crashed(1)
        bullet_hit_sound.play()

    if apple_y[2]>500 and newton_x>180 and newton_x<300 :
        crashed(2)
        bullet_hit_sound.play()

    display_score(score)

    winner_text=""
    if score<=0:
        winner_text="Oh my God!"
    if score==1000:
        winner_text="Newton Saves Us!"
    if winner_text!="":
            draw_winner(winner_text)
            break
        
    pygame.display.update()
    clock.tick(60)
