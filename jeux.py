import pygame
import random
import sys

# Initialisation de Pygame
pygame.init()

# Définition de la taille de l'écran
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Jeu Pygame")

# Couleurs
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Définition de la classe pour le joueur
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        # Limites de l'écran
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

# Définition de la classe pour les obstacles
class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randrange(SCREEN_HEIGHT - self.rect.height)
        self.speed = random.randint(1, 3)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.y = 0
            self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)

# Groupe de sprites
all_sprites = pygame.sprite.Group()
obstacles = pygame.sprite.Group()

# Création du joueur
player = Player()
all_sprites.add(player)

# Création des obstacles
for i in range(8):
    obstacle = Obstacle()
    all_sprites.add(obstacle)
    obstacles.add(obstacle)

# Boucle principale du jeu
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Mise à jour des sprites
    all_sprites.update()

    # Gestion des collisions
    hits = pygame.sprite.spritecollide(player, obstacles, False)
    if hits:
        print("Vous avez perdu !")
        pygame.quit()
        sys.exit()

    # Affichage
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    pygame.display.flip()

    # Limite de 60 FPS
    clock.tick(60)

# Quitter Pygame
pygame.quit()
