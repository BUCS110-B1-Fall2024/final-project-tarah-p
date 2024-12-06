import pygame

class View:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)
        self.background = pygame.image.load("assets/sprites/background.jpg")
        self.task_icon = pygame.image.load("assets/sprites/task_icon.png")
        self.task_complete_sound = pygame.mixer.Sound("assets/sounds/completion.wav")
        pygame.mixer.music.load("assets/sounds/background_music.mp3")

    def start_background_music(self):
        pygame.mixer.music.play(-1)  # Loop indefinitely

    def draw_main_menu(self):
        self.screen.fill((0, 100, 0))
        text = self.font.render("EcoQuest - Press SPACE to Start", True, (255, 255, 255))
        self.screen.blit(text, (100, 100))

    def draw_gameplay(self, player, city, tasks):
        self.screen.blit(self.background, (0, 0))  # Draw background
        # Player stats
        stats = self.font.render(f"Player: {player.name} | Eco Points: {player.eco_points}", True, (0, 0, 0))
        self.screen.blit(stats, (10, 10))
        # City status
        city_status = self.font.render(city.get_status(), True, (0, 0, 0))
        self.screen.blit(city_status, (10, 50))
        # Tasks
        for i, task in enumerate(tasks):
            task_text = self.font.render(f"Task {i+1}: {task.description}", True, (0, 0, 0))
            self.screen.blit(task_text, (10, 100 + i * 30))
            self.screen.blit(self.task_icon, (700, 100 + i * 30))

    def draw_game_over(self):
        self.screen.fill((0, 0, 0))
        text = self.font.render("Game Over - Press ESC to Quit", True, (255, 0, 0))
        self.screen.blit(text, (100, 100))
