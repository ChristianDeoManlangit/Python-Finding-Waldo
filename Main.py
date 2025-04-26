import pygame
import sys
import random

pygame.init()

screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Where's Waldo?")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

try:
    main_image = pygame.image.load("Assets/main.jpg")
    splash_image = pygame.image.load("Assets/background.png")
    start_image = pygame.image.load("Assets/start.png")
    game_mechanics = pygame.image.load("Assets/game_mechanics.png")
    instructions = pygame.image.load("Assets/instructions.png")
    countdown_3 = pygame.image.load("Assets/countdown_3.png")
    countdown_2 = pygame.image.load("Assets/countdown_2.png")
    countdown_1 = pygame.image.load("Assets/countdown_1.png")
    countdown_images = [countdown_3, countdown_2, countdown_1]
    hint_image = pygame.image.load("Assets/hint.png")
    heart_images = []
    for i in range(6):
        heart_image = pygame.image.load(f"Assets/hearts_{5-i}.png")
        heart_images.append(heart_image)
except pygame.error as e:
    print(f"Error loading image: {e}")
    pygame.quit()
    sys.exit()

main_image = pygame.transform.scale(main_image, (screen_width, screen_height))
hint_image = pygame.transform.scale(hint_image, (120, 60))
for i in range(len(heart_images)):
    heart_images[i] = pygame.transform.scale(heart_images[i], (300, 60))

lives = 5
hints_left = 3
is_game_over = False
waldo_x = 508
waldo_y = 265
waldo_radius = 30

def draw_screen():
    screen.fill(WHITE)
    screen.blit(main_image, (0, 0))
    screen.blit(hint_image, (10, screen_height - 70))
    if 0 <= lives <= 5:
        screen.blit(heart_images[5 - lives], (10, 10))

def is_hint_button_clicked(mouse_x, mouse_y):
    return 10 <= mouse_x <= 130 and screen_height - 70 <= mouse_y <= screen_height - 10

def give_hint():
    global hints_left
    hints = [
        "Look for a man with a red and white striped shirt! 🎩👕",
        "Waldo might be near a crowded area! 🚂👀",
        "Check the center of the image! 🔍✨"
    ]
    if hints_left > 0:
        print(f"Hint: {random.choice(hints)}")
        hints_left -= 1
    else:
        print("No more hints available!")

def is_waldo_clicked(mouse_x, mouse_y):
    global lives, is_game_over
    distance = ((mouse_x - waldo_x) ** 2 + (mouse_y - waldo_y) ** 2) ** 0.5
    if distance <= waldo_radius:
        print("Congratulations! You found Waldo!")
        is_game_over = True
        show_end_screen("You Win!")
        return True
    else:
        lives -= 1
        print(f"Incorrect! Lives left: {lives}")
        if lives == 0:
            print("Game Over! You've lost all lives.")
            is_game_over = True
            show_end_screen("Game Over")
        return False

def show_splash_screen():
    start_time = pygame.time.get_ticks()
    while pygame.time.get_ticks() - start_time < 2000:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.blit(splash_image, (0, 0))
        pygame.display.flip()
        pygame.time.delay(100)

def show_start_screen():
    start_time = pygame.time.get_ticks()
    while pygame.time.get_ticks() - start_time < 3000:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.blit(start_image, (0, 0))
        pygame.display.flip()
        pygame.time.delay(100)

def show_mechanics_screen():
    start_time = pygame.time.get_ticks()
    while pygame.time.get_ticks() - start_time < 3000:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.blit(game_mechanics, (0, 0))
        pygame.display.flip()
        pygame.time.delay(100)

def show_instructions_screen():
    start_time = pygame.time.get_ticks()
    while pygame.time.get_ticks() - start_time < 3000:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.blit(instructions, (0, 0))
        pygame.display.flip()
        pygame.time.delay(100)

def show_countdown_screen():
    countdown_images = [countdown_3, countdown_2, countdown_1]
    for image in countdown_images:
        start_time = pygame.time.get_ticks()
        while pygame.time.get_ticks() - start_time < 1000:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            screen.blit(image, (0, 0))
            pygame.display.flip()
            pygame.time.delay(100)

def show_end_screen(message):
    overlay = pygame.Surface((screen_width, screen_height))
    overlay.set_alpha(128)
    overlay.fill(BLACK)
    screen.blit(overlay, (0, 0))
    font = pygame.font.Font(None, 74)
    text = font.render(message, True, GREEN if message == "You Win!" else RED)
    text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
    screen.blit(text, text_rect)
    pygame.display.flip()
    pygame.time.wait(3000)

def game_loop():
    global is_game_over
    while not is_game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if is_hint_button_clicked(mouse_x, mouse_y):
                        give_hint()
                    else:
                        is_waldo_clicked(mouse_x, mouse_y)
        draw_screen()
        pygame.display.flip()

show_splash_screen()
show_start_screen()
show_mechanics_screen()
show_instructions_screen()
show_countdown_screen()
game_loop()
pygame.quit()
sys.exit()