import pygame
from math import pi, sin, cos
from random import randint

pygame.mixer.pre_init()
pygame.init()

SIZE = WIDTH, HEIGHT = 600, 400
window = pygame.display.set_mode(SIZE, pygame.RESIZABLE | pygame.SCALED)
pygame.display.set_caption('Воздух хоккей')
pygame.display.set_icon(pygame.image.load('sprites/Гавной.png'))

# Mouse invisibility
pygame.mouse.set_visible(False)

FPS = 60
clock = pygame.time.Clock()

# Creating sound effects
collision_sound = pygame.mixer.Sound('sound effects/collision.ogg')
goal_sound = pygame.mixer.Sound('sound effects/goal.ogg')
win_sound = pygame.mixer.Sound('sound effects/win.ogg')


class Player:
    def __init__(self, name: str, path: str, key_list: tuple, x: int):
        objects.append(self)
        self.type = name
        # Creating surface and coordinates of player, uploading its image
        self.image = pygame.image.load(path).convert_alpha()
        self.image.set_colorkey('white')
        self.image = pygame.transform.scale(self.image, (25, 70))
        self.coordinate = self.image.get_rect(center=(x, HEIGHT // 2))
        # Creating player movement controls
        self.k_up = key_list[0]
        self.k_left = key_list[1]
        self.k_down = key_list[2]
        self.k_right = key_list[3]
        # Creating player speed and movements in x and y
        self.speed = 4
        self.move_x, self.move_y = 0, 0

    def update(self):
        # Pressing two keys
        if keys[self.k_up] and keys[self.k_right]:
            if self.type == 'player1':
                if self.coordinate.top >= 0 and self.coordinate.right <= 100:
                    self.move_y -= self.speed * sin(pi / 4)
                    self.move_x += self.speed * cos(pi / 4)
                elif not (self.coordinate.top >= 0) and self.coordinate.right <= 100:
                    self.move_x += self.speed
                elif self.coordinate.top >= 0 and not (self.coordinate.right <= 100):
                    self.move_y -= self.speed
            if self.type == 'player2':
                if self.coordinate.top >= 0 and self.coordinate.right <= WIDTH:
                    self.move_y -= self.speed * sin(pi / 4)
                    self.move_x += self.speed * cos(pi / 4)
                elif not (self.coordinate.top >= 0) and self.coordinate.right <= WIDTH:
                    self.move_x += self.speed
                elif self.coordinate.top >= 0 and not (self.coordinate.right <= WIDTH):
                    self.move_y -= self.speed
        elif keys[self.k_up] and keys[self.k_left]:
            if self.type == 'player1':
                if self.coordinate.top >= 0 and self.coordinate.left >= 2:
                    self.move_y -= self.speed * sin(pi / 4)
                    self.move_x -= self.speed * cos(pi / 4)
                elif not (self.coordinate.top >= 0) and self.coordinate.left >= 2:
                    self.move_x -= self.speed
                elif self.coordinate.top >= 0 and not (self.coordinate.left >= 2):
                    self.move_y -= self.speed
            if self.type == 'player2':
                if self.coordinate.top >= 0 and self.coordinate.left >= WIDTH - 100:
                    self.move_y -= self.speed * sin(pi / 4)
                    self.move_x -= self.speed * cos(pi / 4)
                elif not (self.coordinate.top >= 0) and self.coordinate.left >= WIDTH - 100:
                    self.move_x -= self.speed
                elif self.coordinate.top >= 0 and not (self.coordinate.left >= WIDTH - 100):
                    self.move_y -= self.speed
        elif keys[self.k_down] and keys[self.k_right]:
            if self.type == 'player1':
                if self.coordinate.bottom <= HEIGHT and self.coordinate.right <= 100:
                    self.move_y += self.speed * sin(pi / 4)
                    self.move_x += self.speed * cos(pi / 4)
                elif not (self.coordinate.bottom <= HEIGHT) and self.coordinate.right <= 100:
                    self.move_x += self.speed
                elif self.coordinate.bottom <= HEIGHT and not (self.coordinate.right <= 100):
                    self.move_y += self.speed
            if self.type == 'player2':
                if self.coordinate.bottom <= HEIGHT and self.coordinate.right <= WIDTH:
                    self.move_y += self.speed * sin(pi / 4)
                    self.move_x += self.speed * cos(pi / 4)
                elif not (self.coordinate.bottom <= HEIGHT) and self.coordinate.right <= WIDTH:
                    self.move_x += self.speed
                elif self.coordinate.bottom <= HEIGHT and not (self.coordinate.right <= WIDTH):
                    self.move_y += self.speed
        elif keys[self.k_down] and keys[self.k_left]:
            if self.type == 'player1':
                if self.coordinate.bottom <= HEIGHT and self.coordinate.left >= 2:
                    self.move_y += self.speed * sin(pi / 4)
                    self.move_x -= self.speed * cos(pi / 4)
                elif not (self.coordinate.bottom <= HEIGHT) and self.coordinate.left >= 2:
                    self.move_x -= self.speed
                elif self.coordinate.bottom <= HEIGHT and not (self.coordinate.left >= 2):
                    self.move_y += self.speed
            if self.type == 'player2':
                if self.coordinate.bottom <= HEIGHT and self.coordinate.left >= WIDTH - 100:
                    self.move_y += self.speed * sin(pi / 4)
                    self.move_x -= self.speed * cos(pi / 4)
                elif not (self.coordinate.bottom <= HEIGHT) and self.coordinate.left >= WIDTH - 100:
                    self.move_x -= self.speed
                elif self.coordinate.bottom <= HEIGHT and not (self.coordinate.left >= WIDTH - 100):
                    self.move_y += self.speed
        # Pressing one key
        elif keys[self.k_up]:
            if self.coordinate.top >= 0:
                self.move_y -= self.speed
        elif keys[self.k_left]:
            if self.type == 'player1':
                if self.coordinate.left >= 0:
                    self.move_x -= self.speed
            if self.type == 'player2':
                if self.coordinate.left >= WIDTH - 100:
                    self.move_x -= self.speed
        elif keys[self.k_down]:
            if self.coordinate.bottom <= HEIGHT:
                self.move_y += self.speed
        elif keys[self.k_right]:
            if self.type == 'player1':
                if self.coordinate.right <= 100:
                    self.move_x += self.speed
            if self.type == 'player2':
                if self.coordinate.right <= WIDTH - 1:
                    self.move_x += self.speed

        # Updating player coordinates
        if self.type == 'player1':
            self.coordinate = self.image.get_rect(center=(11 + self.move_x, HEIGHT // 2 + self.move_y))
        if self.type == 'player2':
            self.coordinate = self.image.get_rect(center=(WIDTH - 13 + self.move_x, HEIGHT // 2 + self.move_y))

    def draw(self):
        window.blit(self.image, self.coordinate)


class Puck:
    def __init__(self, path: str, x: int, y: int):
        objects.append(self)
        # Creating surface and coordinates of player, uploading his image
        self.image = pygame.transform.scale(pygame.image.load(path).convert_alpha(), (20, 20))
        self.coordinate = self.image.get_rect(center=(x // 2, y // 2))
        # Creating main puck speed and puck speed in x and y and puck movements in x and y
        self.speed = 6
        self.speed_x, self.speed_y = [-self.speed, 0], [-self.speed, 0]
        self.move_x, self.move_y = 0, 0
        # Creating bool start the game and goal var
        self.start_game = False

    def update(self):
        # Checking collision with boards
        def board_collision():
            if self.coordinate.top <= 0:
                collision_sound.play()
                self.speed_y[0], self.speed_y[1] = 0, self.speed
                self.move_y += self.speed_y[0] + self.speed_y[1]
            if self.coordinate.left < 0:
                goal_sound.play()
                score2.score += 0.5
                self.speed_x[0], self.speed_x[1] = 0, self.speed
                self.move_x += self.speed_x[0] + self.speed_x[1]
            if self.coordinate.bottom >= HEIGHT:
                collision_sound.play()
                self.speed_y[0], self.speed_y[1] = -self.speed, 0
                self.move_y += self.speed_y[0] + self.speed_y[1]
            if self.coordinate.right > WIDTH:
                goal_sound.play()
                score1.score += 0.5
                self.speed_x[0], self.speed_x[1] = -self.speed, 0
                self.move_x += self.speed_x[0] + self.speed_x[1]

        # Creating collisions between the puck and the players
        collision1 = pygame.rect.Rect.colliderect(self.coordinate, player1.coordinate)
        collision2 = pygame.rect.Rect.colliderect(self.coordinate, player2.coordinate)

        def collision_with_players():
            if not (collision1 and collision2):
                self.move_x += self.speed_x[0] + self.speed_x[1]
                self.move_y += self.speed_y[0] + self.speed_y[1]
            if collision1:
                collision_sound.play()
                # Player1 and puck accelerations
                player1.speed += 0.01
                self.speed += 0.03
                # Updating puck coordinates
                self.speed_x[0], self.speed_x[1] = 0, self.speed / cos(pi / randint(4, 6))
                if self.speed_y[0] < 0:
                    self.speed_y[0], self.speed_y[1] = 0, self.speed * sin(pi / randint(4, 6))
                elif self.speed_y[0] >= 0:
                    self.speed_y[0], self.speed_y[1] = -self.speed * sin(pi / randint(4, 6)), 0
                self.move_x += self.speed_x[0] + self.speed_x[1]
                self.move_y += self.speed_y[0] + self.speed_y[1]
            if collision2:
                collision_sound.play()
                # Player2 and puck accelerations
                player2.speed += 0.01
                self.speed += 0.03
                # Updating puck coordinates
                self.speed_x[0], self.speed_x[1] = -self.speed / cos(pi / randint(4, 6)), 0
                if self.speed_y[0] < 0:
                    self.speed_y[0], self.speed_y[1] = 0, self.speed * sin(pi / randint(4, 6))
                elif self.speed_y[0] >= 0:
                    self.speed_y[0], self.speed_y[1] = -self.speed * sin(pi / randint(4, 6)), 0
                self.move_x += self.speed_x[0] + self.speed_x[1]
                self.move_y += self.speed_y[0] + self.speed_y[1]

        if self.start_game:
            start_text.filling = 0
            collision_with_players()
            board_collision()
            # Updating puck coordinates
            self.coordinate = self.image.get_rect(center=(WIDTH // 2 + self.move_x, HEIGHT // 2 + self.move_y))

    def draw(self):
        window.blit(self.image, self.coordinate)


class Score:
    def __init__(self, x: int, count: int = 0):
        objects.append(self)
        # Creating a counter
        self.score = count
        # Creating scoreboard and its coordinates
        self.font = pygame.font.SysFont('georgia', 24)
        self.text = self.font.render(f'Score: {int(self.score)}', True, 'black')
        self.text.set_alpha(150)
        self.coordinate = self.text.get_rect(center=(x, 40))

    def update(self):
        # Counter update
        self.text = self.font.render(f'Score: {int(self.score)}', True, 'black')

    def draw(self):
        window.blit(self.text, self.coordinate)


class Text:
    def __init__(self, message: str, filling: int):
        objects.append(self)
        # Creating text, its filling and its coordinates
        self.font = pygame.font.SysFont('georgia', 24)
        self.message = message
        self.text = self.font.render(self.message, True, 'black')
        self.filling = filling
        self.coordinate = self.text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 75))

    def update(self):
        # Show and hide starting text and ending text
        if puck.start_game:
            self.text.set_alpha(0)
        else:
            self.text.set_alpha(self.filling)

    def draw(self):
        window.blit(self.text, self.coordinate)


# Creating list of all items
objects = []

# Creating two players, puck, score and start text
player1 = Player('player1', 'sprites/Onetwoз.png', (pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d), 0)
player2 = Player('player2', 'sprites/Onetwoз.png', (pygame.K_UP, pygame.K_LEFT, pygame.K_DOWN, pygame.K_RIGHT), WIDTH)
puck = Puck('sprites/Гавной.png', WIDTH, HEIGHT)
score1 = Score(WIDTH // 4)
score2 = Score(WIDTH * 3 // 4)
start_text = Text('Press SPACE to drop the puck', 255)
win_player1_text = Text('Left is winner!! Press SPACE to drop the puck', 0)
win_player2_text = Text('Right is winner!! Press SPACE to drop the puck', 0)


# Restart the game if score is ten. Reset scores and speeds
def restart_game():
    if score1.score == 10:
        win_sound.play()
        puck.start_game = False
        win_player1_text.filling, win_player2_text.filling = 255, 0
        score1.score, score2.score = 0, 0
        player1.speed, player2.speed = 4, 4
        puck.speed = 6
    elif score2.score == 10:
        win_sound.play()
        puck.start_game = False
        win_player1_text.filling, win_player2_text.filling = 0, 255
        score1.score, score2.score = 0, 0
        player1.speed, player2.speed = 4, 4
        puck.speed = 6


def update_window():
    # Updating all items
    for element in objects:
        element.update()
    # Updating window
    window.fill('white')
    # Draw all items
    for element in objects:
        element.draw()

    pygame.display.update()
    clock.tick(FPS)


game_over = False

while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                puck.start_game = True

    # Scanning all pressed keys
    keys = pygame.key.get_pressed()

    restart_game()

    update_window()
