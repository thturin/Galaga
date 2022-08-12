"""
Project: Galaga Remake

"""
import pgzrun, random

WIDTH = 1200
HEIGHT = 800
CENTER_X = WIDTH/2
CENTER_Y = HEIGHT/2
SHIP_SPEED =  5
BULLET_SPEED = 10
ENEMY_SPEED = 10

ship = Actor('galaga', pos=(CENTER_X,HEIGHT-50))
bullets = []
enemies = []
enemies.append(Actor('bug', pos=(random.randint(40,WIDTH),random.randint(40,HEIGHT-100))))
score = 0
game_over = False

def draw():
    if not game_over:
        screen.clear()
        screen.fill('BLUE')
        ship.draw()
        screen.draw.text('Score: ' + str(score),  topright=(WIDTH - 100, 50),fontsize=40,color="white", gcolor="#66AA00", owidth=1.5, ocolor="black", alpha=0.8)
        for b in bullets:
            b.draw()

        for e in enemies:
            e.draw()
    else:
        screen.clear()
        screen.fill('red')
        screen.draw.text('You lose! Final Score: ' + str(score), topright=(CENTER_X+150,CENTER_Y), fontsize=40, color="white", gcolor="#66AA00",
                         owidth=1.5, ocolor="black", alpha=0.8)

def update():
    global bullets
    if not game_over:
        if keyboard.left and ship.x>30:
            ship.x -= SHIP_SPEED
        if keyboard.right and ship.x<WIDTH-30:
            ship.x += SHIP_SPEED

        for b in bullets:
            if b.y < -20:
                bullets.remove(b)
            else:
                b.y -= BULLET_SPEED

        for e in enemies:
            if e.y>HEIGHT+20:
                # e.x = random.randint(20,WIDTH-50)
                # e.y= -50
                enemies.remove(e)
            else:
                e.y += ENEMY_SPEED

        check_Collision()





def check_Collision():
    global score, game_over
    for bullet in bullets: #if there are no bullets in here, this will not execute so don't have the if enemy.colliderect(ship) in there
        for enemy in enemies:
            if bullet.colliderect(enemy):
                #update score, delete enemy and bullet
                bullets.remove(bullet)
                enemies.remove(enemy)
                score+=15

    for enemy in enemies:
        if enemy.colliderect(ship):
            game_over=True



def spawn_Enemies():
    enemies.append(Actor('bug', pos=(random.randint(40, WIDTH), -40)))


def on_key_down(key): #use this because it will only shoot one bullet when holding down the space bar
    if key == keys.SPACE:
        bullets.append(Actor('bullet_small', pos=(ship.x, ship.y-30)))




clock.schedule_interval(spawn_Enemies,0.5)
pgzrun.go()