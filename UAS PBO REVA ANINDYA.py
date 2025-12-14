import pygame

#Warna 
TILE_SIZE = 32 
BLACK = (0, 0, 0)
BROWN = (139, 69, 19)
GREEN = (124, 252, 0) 
SILVER = (192, 192, 192)
GOLD = (255, 215, 0)
RED = (255, 0, 0) 

class GameObject:
    def __init__(self, x, y, color, size=TILE_SIZE):
        self.x = x * size
        self.y = y * size
        self.size = size
        self.rect = pygame.Rect(self.x, self.y, size, size)
        self.color = color

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

class Player(GameObject):
    def __init__(self, x, y, size=TILE_SIZE):
        super().__init__(x, y, BLACK, size)
        self.speed = TILE_SIZE 
        self.__score = 0  

    def get_score(self):
        return self.__score
  
    def add_score(self, amount):
        if amount > 0:
            self.__score += amount
 
    def move(self, dx, dy, walls):
        new_rect = self.rect.move(dx * self.speed, dy * self.speed)
        
        
        can_move = True
        for wall in walls:
            if new_rect.colliderect(wall.rect):
                can_move = False
                wall.on_collision(self) 
                break

        if can_move:
            self.rect = new_rect
            self.x = self.rect.x
            self.y = self.rect.y
            return True 
        return False 

class Wall(GameObject):
    def __init__(self, x, y, size=TILE_SIZE):
        super().__init__(x, y, GREEN, size)

    def on_collision(self, player):
        pass 

class SilverCoin(GameObject):
    def __init__(self, x, y, size=TILE_SIZE):
        super().__init__(x, y, SILVER, size)
        self.value = 10

    def on_collision(self, player):
        player.add_score(self.value)
        self.rect.width = 0 
        self.rect.height = 0
        return True 

class GoldCoin(GameObject):
    def __init__(self, x, y, size=TILE_SIZE):
        super().__init__(x, y, GOLD, size) 
        self.value = 30 

    def on_collision(self, player):
        player.add_score(self.value)
        self.rect.width = 0 
        self.rect.height = 0
        return True

class Exit(GameObject):
    def __init__(self, x, y, size=TILE_SIZE):
        super().__init__(x, y, RED, size)
    
    def on_collision(self, player):
        return True 
    
# 'W': Wall, 'P': Player Start, 'C': Coin, 'E': Exit ' ': Empty
MAZE_MAP = [
    ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
    ['W', 'P', ' ', ' ', 'W', ' ', ' ', ' ', 'S', ' ', ' ', 'W', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'W', 'W', 'W', ' ', ' ', ' ', 'W'],
    ['W', 'W', 'W', ' ', 'W', ' ', 'W', ' ', 'W', 'W', ' ', ' ', ' ', 'W', 'W', 'W', 'W', 'W', 'S', ' ', ' ', 'W', ' ', 'W', ' ', 'W'],
    ['W', 'W', 'S', ' ', ' ', ' ', 'W', ' ', ' ', 'W', 'W', 'W', 'W', 'W', ' ', ' ', ' ', 'W', ' ', 'W', ' ', ' ', ' ', 'W', ' ', 'W'],
    ['W', 'W', 'W', 'W', 'W', ' ', 'W', 'W', ' ', 'W', 'W', 'W', ' ', ' ', ' ', 'W', ' ', ' ', ' ', 'W', 'W', 'W', 'W', 'W', ' ', 'W'],
    ['W', ' ', ' ', ' ', ' ', ' ', ' ', 'W', 'S', ' ', ' ', ' ', ' ', 'W', 'W', 'W', 'W', 'W', 'W', ' ', ' ', ' ', 'W', 'W', 'G', 'W'],
    ['W', ' ', 'W', 'W', 'W', 'W', 'W', 'W', ' ', 'W', 'W', 'W', 'W', ' ', 'S', 'W', ' ', ' ', ' ', ' ', 'W', ' ', ' ', 'S', 'W', 'W'],
    ['W', 'S', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'W', 'W', ' ', ' ', 'W', ' ', ' ', 'W', ' ', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
    ['W', 'W', 'W', ' ', 'W', 'W', 'W', 'W', 'W', ' ', ' ', 'W', ' ', 'W', 'W', ' ', 'W', 'W', ' ', ' ', ' ', ' ', 'W', ' ', 'W', 'W'],
    ['W', ' ', ' ', ' ', 'W', 'S', ' ', ' ', 'W', 'W', ' ', ' ', ' ', 'W', 'W', ' ', 'W', 'W', 'W', 'W', 'W', ' ', 'W', ' ', 'W', 'W'],
    ['W', 'W', ' ', ' ', ' ', ' ', 'W', ' ', ' ', 'W', 'W', 'W', ' ', ' ', 'W', ' ', ' ', 'W', ' ', 'G', 'W', ' ', ' ', ' ', ' ', 'W'],
    ['W', 'W', ' ', 'W', 'W', ' ', 'W', 'W', ' ', 'W', 'S', 'W', 'W', ' ', ' ', 'W', ' ', 'W', ' ', 'W', 'W', 'W', 'W', 'W', 'G', 'W'],
    ['W', ' ', ' ', 'W', ' ', ' ', ' ', 'W', 'S', ' ', ' ', ' ', ' ', 'W', 'S', ' ', ' ', 'W', ' ', ' ', 'W', 'C', ' ', ' ', 'W', 'W'],
    ['W', ' ', 'W', 'W', 'S', 'W', 'W', 'W', ' ', 'W', 'W', 'W', ' ', 'W', 'W', 'W', 'W', 'W', 'W', ' ', ' ', ' ', 'W', ' ', 'W', 'W'],
    ['W', 'S', ' ', 'W', 'W', 'W', ' ', ' ', ' ', 'W', 'G', 'W', ' ', ' ', 'W', ' ', ' ', ' ', 'W', 'W', 'W', 'W', 'W', ' ', ' ', 'W'],
    ['W', 'W', ' ', ' ', ' ', ' ', ' ', 'W', 'W', ' ', ' ', 'W', 'W', ' ', ' ', ' ', 'W', ' ', ' ', ' ', ' ', ' ', ' ', 'W', ' ', 'W'],
    ['W', ' ', ' ', 'W', ' ', 'W', 'W', ' ', ' ', ' ', 'W', 'S', 'W', 'W', 'W', ' ', ' ', 'W', 'S', ' ', 'W', 'W', ' ', ' ', ' ', 'W'],
    ['W', ' ', 'W', ' ', ' ', 'W', ' ', ' ', 'W', ' ', 'W', ' ', ' ', ' ', ' ', 'W', ' ', 'W', 'W', ' ', ' ', ' ', 'W', 'S', 'W', 'W'],
    ['W', ' ', 'W', ' ', 'W', 'G', ' ', 'W', ' ', ' ', ' ', 'W', ' ', 'W', ' ', ' ', ' ', ' ', 'W', 'W', 'W', ' ', 'W', 'W', 'E', 'W'],
    ['W', ' ', ' ', ' ', 'S', 'W', 'W', 'W', ' ', 'W', ' ', 'W', ' ', 'W', 'W', 'S', 'W', 'W', 'W', 'W', ' ', ' ', 'W', ' ', ' ', 'W'],
    ['W', 'W', ' ', ' ', 'W', 'W', ' ', ' ', ' ', 'W', ' ', 'W', ' ', 'W', 'W', ' ', ' ', ' ', ' ', ' ', ' ', 'W', ' ', ' ', 'W', 'W'],
    ['W', 'W', 'W', ' ', ' ', ' ', ' ', 'W', 'S', ' ', ' ', 'W', ' ', ' ', ' ', ' ', 'W', 'W', ' ', 'W', 'S', ' ', ' ', 'W', 'W', 'W'],    
    ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W']
]

MAP_WIDTH = len(MAZE_MAP[0])
MAP_HEIGHT = len(MAZE_MAP)

SCREEN_WIDTH = MAP_WIDTH * TILE_SIZE
SCREEN_HEIGHT = MAP_HEIGHT * TILE_SIZE
FPS = 60

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Maze Block")
clock = pygame.time.Clock()

player = None
walls = []
collectables = []
exit_point = None

def load_maze(maze_map):
    """Membuat objek dari blueprint MAZE_MAP."""
    global player, exit_point, walls, collectables
    
    walls = []
    collectables = []
    
    for r, row in enumerate(maze_map):
        for c, tile in enumerate(row):
            if tile == 'W':
                walls.append(Wall(c, r))
            elif tile == 'P':
                player = Player(c, r)
            elif tile == 'S':
                collectables.append(SilverCoin(c, r))
            elif tile == 'G':
                collectables.append(GoldCoin(c, r))
            elif tile == 'E':
                exit_point = Exit(c, r)

def game_loop():
    running = True
    load_maze(MAZE_MAP)
    
    while running:
        dx, dy = 0, 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_UP:
                    dy = -1
                elif event.key == pygame.K_DOWN:
                    dy = 1
                elif event.key == pygame.K_LEFT:
                    dx = -1
                elif event.key == pygame.K_RIGHT:
                    dx = 1
      
        
        if player and (dx != 0 or dy != 0):
            player.move(dx, dy, walls)
         
        items_to_remove = []
        for item in collectables:
            if player.rect.colliderect(item.rect):
                
                if item.on_collision(player):
                    items_to_remove.append(item)
         
        for item in items_to_remove:
            collectables.remove(item)

        if exit_point and player.rect.colliderect(exit_point.rect):
            if exit_point.on_collision(player):
                print(f"YEYY MAZE BLOCK SELESAI! Skor Anda: {player.get_score()}")
                running = False # Game selesai

        screen.fill(BROWN) 

        for wall in walls:
            wall.draw(screen)
        for item in collectables:
            item.draw(screen)
        if exit_point:
             exit_point.draw(screen)
        if player:
            player.draw(screen)

       
        font = pygame.font.Font(None, 24)
        score_text = font.render(f"Score: {player.get_score()}", True, (BLACK))
        screen.blit(score_text, (5, 5))

        pygame.display.flip() 
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    game_loop()