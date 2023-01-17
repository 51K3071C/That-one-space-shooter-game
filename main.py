import pygame, sys

class Ship(pygame.sprite.Sprite):
    def __init__(self, groups):
        #init parent class
        super().__init__(groups) 
        #surface -> image
        self.image = pygame.image.load("./graphics/ship.png").convert_alpha()

        #get rect
        self.rect = self.image.get_rect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT /2))

        self.can_shoot = True
        self.shoot_time = None

    def laser_timer(self):
        if not self.can_shoot:
            current_time = pygame.time.get_ticks()
            if current_time - self.shoot_time > 500:
                self.can_shoot = True
                

    def input_position(self):
        pos = pygame.mouse.get_pos()
        self.rect.center = pos
    
    def laser_shoot(self):
        if pygame.mouse.get_pressed()[0] and self.can_shoot:
            print('shoot laser')
            self.can_shoot = False
            self.shoot_time = pygame.time.get_ticks()
    def update(self):
        self.input_position()
        self.laser_shoot()
        self.laser_timer()
#laser stuff-
class Laser(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load("./graphics/laser.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom = pos)

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space Shooter")
clock = pygame.time.Clock()

#ground's back
background_surf = pygame.image.load('./graphics/background.png').convert()

#sprite groups
spaceship_group = pygame.sprite.Group()

laser_group = pygame.sprite.Group()

#sprite create
ship = Ship(spaceship_group)
laser = Laser((100, 300), laser_group)

#main game loop
while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #delta time
    dt = clock.tick() / 1000
    
    #ground's back
    display_surface.blit(background_surf,(0,0))
    #update
    spaceship_group.update();
    #draw sprites
    spaceship_group.draw(display_surface)
    laser_group.draw(display_surface)
    pygame.display.update()
