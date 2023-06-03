import pygame
import math

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 960, 540
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

class ButtonImage(object):
    def __init__(self, position, size, path, path2):
        self.pos = position
        self.path2 = path2
        self.img = pygame.transform.scale(pygame.image.load(path), size)
        self.rect = pygame.Rect(position, size)
        screen.blit(self.img, position)
        self.size = size
    def draw(self, screen):
        screen.blit(self.img, self.pos)
    def is_hover(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                return self.rect.collidepoint(event.pos)
    def hover(self, screen):
        img2 = pygame.transform.scale(pygame.image.load(self.path2), self.size)
        screen.blit(img2, self.pos)
    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                return self.rect.collidepoint(event.pos)


def startScreen(screen):
    SCREEN_WIDTH, SCREEN_HEIGHT = 960, 540
    pygame.display.set_caption('PROJECT KECERDASAN BUATAN')
    # Load image
    bg = pygame.image.load('projectai/assets/bg.png')
    bg = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
    bg_width = bg.get_width()
    bg_rect = bg.get_rect()
    # Scrolling background
    scroll = 0
    tiles = math.ceil(SCREEN_WIDTH / bg_width) + 1
    run = True
    while run:
        for i in range(0, tiles):
            screen.blit(bg, (i * bg_width + scroll, 0))
            bg_rect.x = i * bg_width + scroll
            pygame.draw.rect(screen, (255, 0, 0), bg_rect, 1)
            scroll -= 1
            if abs(scroll) > bg_width:
                scroll = 0
        start = ButtonImage((400, 200), (200, 200), 'projectai/assets/start1.png', 'projectai/assets/start2.png')
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start.is_clicked(event):
                    inputNMesinScreen(screen)

        pos = pygame.mouse.get_pos()

        if pos[0] >= 50 and pos[0] <= 250 and pos[1] >= 150 and pos[1] <= 210:
            start.hover(screen)
        else:
            start.draw(screen)

        pygame.display.update()


def inputNMesinScreen(screen):
    SCREEN_WIDTH, SCREEN_HEIGHT = 960, 540
    pygame.display.set_caption('PROJECT KECERDASAN BUATAN')
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    # Load image
    bg = pygame.image.load('projectai/assets/bg.png')
    bg = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
    bg_width = bg.get_width()
    bg_rect = bg.get_rect()
    inputNMesin = pygame.transform.scale(pygame.image.load('projectai/assets/inputNMesin.png'), (600,100))
    #Input box properties
    input_box = pygame.Rect(200, 200, 300, 40)
    input_text = ""
    font = pygame.font.Font(None, 32)
    active = False
    # Scrolling background
    scroll = 0
    tiles = math.ceil(SCREEN_WIDTH / bg_width) + 1
    run = True
    while run:
        for i in range(0, tiles):
            screen.blit(bg, (i * bg_width + scroll, 0))
            bg_rect.x = i * bg_width + scroll
            pygame.draw.rect(screen, (255, 0, 0), bg_rect, 1)
            scroll -= 1
            if abs(scroll) > bg_width:
                scroll = 0
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
            elif event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        print(input_text)
                        input_text = ""
                    elif event.key == pygame.K_BACKSPACE:
                        input_text = input_text[:-1]
                    else:
                        input_text += event.unicode
        # Draw the input box
        pygame.draw.rect(screen, WHITE, input_box, 2)
        # Render the input text
        text_surface = font.render(input_text, True, WHITE)
        screen.blit(text_surface, (input_box.x + 5, input_box.y + 10))
        
        screen.blit(inputNMesin, (20,20))
        pygame.display.update()

def inputWattmesin(screen):
    SCREEN_WIDTH, SCREEN_HEIGHT = 960, 540
    pygame.display.set_caption('PROJECT KECERDASAN BUATAN')
    # Load image
    bg = pygame.image.load('projectai/assets/bg.png')
    bg = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
    bg_width = bg.get_width()
    bg_rect = bg.get_rect()
    # Scrolling background
    scroll = 0
    tiles = math.ceil(SCREEN_WIDTH / bg_width) + 1
    run = True
    while run:
        for i in range(0, tiles):
            screen.blit(bg, (i * bg_width + scroll, 0))
            bg_rect.x = i * bg_width + scroll
            pygame.draw.rect(screen, (255, 0, 0), bg_rect, 1)
            scroll -= 1
            if abs(scroll) > bg_width:
                scroll = 0
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        pos = pygame.mouse.get_pos()

        pygame.display.update()

pygame.display.update()
pygame.init()
inputNMesinScreen(screen)
pygame.quit()
