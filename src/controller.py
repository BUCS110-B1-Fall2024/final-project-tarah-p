import pygame
import json
from src.player import Player
from src.city import City
from src.task import Task
from src.view import View

class Controller:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("EcoQuest")
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = "MENU"
        self.player = Player()
        self.city = City()
        self.tasks = self.load_tasks_from_file()
        self.view = View(self.screen)

    def load_tasks_from_file(self):
        try:
            with open("etc/tasks.json", "r") as file:
                data = json.load(file)
                return [Task(task["description"], task["points"]) for task in data]
        except FileNotFoundError:
            print("Error: tasks.json file not found. Ensure it is in the 'etc' folder.")
            return []

    def mainloop(self):
        self.view.start_background_music()
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if self.state == "MENU" and event.key == pygame.K_SPACE:
                    self.state = "GAME"
                elif self.state == "GAME" and event.key == pygame.K_RETURN:
                    self.complete_task()
                elif event.key == pygame.K_ESCAPE:
                    self.running = False

    def complete_task(self):
        for task in self.tasks:
            if not task.completed:
                self.player.add_points(task.complete())
                self.view.task_complete_sound.play()  # Play task completion sound
                if self.player.eco_points >= 30:
                    self.city.upgrade()
                break

    def update(self):
        if self.state == "GAME" and all(task.completed for task in self.tasks):
            self.state = "GAME_OVER"

    def draw(self):
        if self.state == "MENU":
            self.view.draw_main_menu()
        elif self.state == "GAME":
            self.view.draw_gameplay(self.player, self.city, self.tasks)
        elif self.state == "GAME_OVER":
            self.view.draw_game_over()
        pygame.display.flip()
