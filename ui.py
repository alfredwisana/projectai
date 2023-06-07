import pygame
import math
# import generate_parent
# import genetic_algotithm


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

def inputWattMaintenanceScreen(screen):
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
        # for i in range (i<n):
        # inputFrame = ButtonImage((30, 30), (150, 150), 'projectai/assets/inputFrame1.png', 'projectai/assets/inputFrame2.png')
        # inputFrame = ButtonImage((770, 30), (150, 150), 'projectai/assets/inputFrame1.png', 'projectai/assets/inputFrame2.png')
        # inputFrame = ButtonImage((585, 30), (150, 150), 'projectai/assets/inputFrame1.png', 'projectai/assets/inputFrame2.png')
        # inputFrame = ButtonImage((400, 30), (150, 150), 'projectai/assets/inputFrame1.png', 'projectai/assets/inputFrame2.png')
        # inputFrame = ButtonImage((215, 30), (150, 150), 'projectai/assets/inputFrame1.png', 'projectai/assets/inputFrame2.png')
        inputFrame = ButtonImage((100, 80), (750, 400), 'projectai/assets/inputFrame1.png', 'projectai/assets/inputFrame2.png')


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if inputFrame.is_clicked(event):
                    inputNMesinScreen(screen)

        pos = pygame.mouse.get_pos()

        if pos[0] >= 50 and pos[0] <= 250 and pos[1] >= 150 and pos[1] <= 210:
            inputFrame.hover(screen)
        else:
            inputFrame.draw(screen)

        pygame.display.update()


def hasilScreen(screen):
    SCREEN_WIDTH, SCREEN_HEIGHT = 960, 540
    TABLE_WIDTH, TABLE_HEIGHT = 890, 450
    CELL_WIDTH, CELL_HEIGHT = 200, 50
    rows_per_page = 5
    scroll_speed = 30
    pygame.display.set_caption('PROJECT KECERDASAN BUATAN')
    # Load image
    bg = pygame.image.load('projectai/assets/bg.png')
    bg = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
    bg_width = bg.get_width()
    bg_rect = bg.get_rect()
    table_x = (SCREEN_WIDTH - TABLE_WIDTH) // 2
    table_y = (SCREEN_HEIGHT -TABLE_HEIGHT) //2    
    table_data = [
    ["Name", "Age", "Score"],
    ["John", "25", "80"],
    ["Alice", "30", "95"],
    ["Bob", "28", "70"],
    # Add more rows as needed
]

# Define table style
    header_color = (100, 100, 100)
    cell_color1 = (200, 200, 200)
    cell_color2 = (220, 220, 220)
    font = pygame.font.Font(None, 30)

# Define scroll position and boundaries
    scroll_y = 0
    max_scroll_y = max(0, (len(table_data) - rows_per_page) * CELL_HEIGHT)
    pygame.display.update()
    pygame.init()

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
                if event.button == 4:  # Scroll up
                    scroll_y = max(0, scroll_y - scroll_speed)
                elif event.button == 5:  # Scroll down
                    scroll_y = min(max_scroll_y, scroll_y + scroll_speed)

        
    start_row = scroll_y // CELL_HEIGHT
    end_row = min(start_row + rows_per_page + 1, len(table_data))
    for row in range(start_row, end_row):
        for col in range(len(table_data[row])):
            cell_x = table_x + col * CELL_WIDTH
            cell_y = table_y + (row - start_row) * CELL_HEIGHT
            cell_rect = pygame.Rect(cell_x, cell_y, CELL_WIDTH, CELL_HEIGHT)

            # Draw cell background
            if row == 0:
                color = header_color
            else:
                color = cell_color1 if row % 2 == 0 else cell_color2
            pygame.draw.rect(screen, color, cell_rect)

            # Draw cell text
            text_surface = font.render(table_data[row][col], True, (0, 0, 0))
            text_rect = text_surface.get_rect(center=cell_rect.center)
            screen.blit(text_surface, text_rect)

        pygame.display.update()

hasilScreen(screen)
pygame.quit()
