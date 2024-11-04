import random

WIDTH = 1200
HEIGHT = 800

hit = False

score = 0

alien_count = 1

frame_count = 0

speed = 2

alien = Actor('alien')
alien.y = random.randint(100, HEIGHT - 100)

def draw():
    #screen.clear()
    screen.blit('background_stars12', (0,0))
    alien.draw()
    screen.draw.text(f'Score: {score}/{alien_count}', centerx = WIDTH // 2, centery = 40)



def update():
    global hit
    global speed
    global frame_count
    global alien_count


    frame_count += 1

    if frame_count % 300 == 0:
        speed += 1

    alien.x += speed


    if alien.left > WIDTH or alien.bottom < 0:
        alien.right = 0
        alien.y = random.randint(100, HEIGHT - 100)
        hit = False
        alien.angle = 0

        alien_count += 1

    if hit:
        alien.angle += 4
        alien.y -= 4


def on_mouse_down(pos):
    global hit
    global score

    if alien.collidepoint(pos):
        #alien.image = 'alien_hurt'
        hit = True
        score += 1

        sounds.eep.play()
