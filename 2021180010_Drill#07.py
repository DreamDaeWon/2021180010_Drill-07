import random
from pico2d import *



# Game object class here

class Grass:
    #생성자 함수 : 객체의 초기 상태를 설정
    def __init__(self):
        # 모양없는 납작한 붕어빵의 초기모습 결정
        self.image = load_image('grass.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(400,30)

    def late_update(self):
        pass

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
        self.image.clip_draw(self.frame*100,0,100,100,self.x,self.y)

    def late_update(self):
        pass


class Ball:
    def __init__(self):
        self.x, self.y = random.randint(100,700), 599
        self.image1 = load_image('ball21x21.png')
        self.image2 = load_image('ball41x41.png')
        self.selectimage = random.randint(0,1)
        self.move = True
        self.movespeed = random.randint(5,15)

    def update(self):
        if self.move:
            self.y -= self.movespeed

    def draw(self):

        if self.selectimage == 0:
            self.image1.draw(self.x, self.y)
        else:
            self.image2.draw(self.x, self.y)

    def late_update(self):
        if self.selectimage == 0 and self.y <= 55:
            self.y = 55
            self.move = False
        if self.selectimage == 1 and self.y <= 65:
            self.y = 65
            self.move = False
        pass


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def reset_world():
    global running
    global grass
    global boy
    global team
    global allball
    global world

    running = True
    world = [] # 전체

    grass = Grass() # 잔디를 찍어낸다.(생성한다.)
    world.append(grass)

    team = [Boy() for i in range(11)]
    allball = [Ball() for j in range(20)]

    world += team
    world += allball

running = True


def update_world():
    global grass
    for o in world:  # 객체의 상태를 업데이트
        o.update()

    for o in world:  # 객체의 상태를 업데이트
        o.late_update()
    pass

def render_world():
    #global grass
    clear_canvas()
    for o in world:  # 객체의 상태를 그리기
        o.draw()

    update_canvas()


    pass


open_canvas()



# initialization code
reset_world()

# game main loop code

while running:
    # game logic
    handle_events()
    update_world()
    render_world()
    delay(0.05)

# finalization code

close_canvas()
