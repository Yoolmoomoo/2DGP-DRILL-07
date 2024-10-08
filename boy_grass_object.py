from pico2d import *
import random

# Game object class here
class Grass:
    def __init__(self):
       self.image = load_image('grass.png') # Ctor function : Set objects' attributes (allocate memory)
    def draw(self):
        self.image.draw(400, 30)
    def update(self):
        pass

class Ball:
  def __init__(self):
    self.small_ball = load_image('ball21x21.png')
    self.big_ball = load_image('ball41x41.png')
    self.s_x, self.s_y = random.randint(100,700), 599
    self.b_x, self.b_y = random.randint(100, 700), 599
    self.speed = random.randint(5, 10)
    self.dy = 1
  def draw(self):
    self.small_ball.draw(self.s_x, self.s_y)
    self.big_ball.draw(self.b_x, self.b_y)
    pass
  def update(self):
    self.s_y -= self.dy * self.speed
    self.b_y -= self.dy * self.speed
    if (self.s_y <= 30): self.s_y = 30
    if (self.b_y <= 30): self.b_y = 30
    pass

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100,700), 90
        self.frame = random.randint(0,7)
        self.image = load_image('run_animation.png')
    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5
    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def reset_world():
    global running, grass, team, world#, boy
    running = True
    grass = Grass() # 'Grass' object instancing
    # boy = Boy() # 'Boy' object instancing
    team = [Boy() for i in range(11)]
    balls = [Ball() for i in range(10)]
    world.append(grass)
    world += team # to add each element apart in list
    world += balls

def update_world():
    # grass.update() # object's attribute is updated
    # for boy in team:
    #     boy.update()
    for o in world:
        o.update()

def render_world():
    clear_canvas()
    # grass.draw()
    # for boy in team:
    #     boy.draw()
    for o in world:
        o.draw()
    update_canvas()

running = True
world = []  # for improving maintenance
open_canvas()

# initialization code
reset_world()

# game main loop code
while running:
    # game logic
    handle_events()
    update_world() # simulate interaction
    render_world() # render simulated results from update_world()
    delay(0.05)

# finalization code

close_canvas()
