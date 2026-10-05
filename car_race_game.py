# -*- coding: utf-8 -*-
"""
Created on Wed May  8 11:08:57 2024

@author: José Alberto Rocha Munguía
"""

# Simple pygame car race: three cars move right until one crosses the finish.
# Needs pygame. Install once if missing:
#   python3 -m pip install pygame
# Run:
#   python3 car_race_game.py
#
# A white window opens. Rectangles race left -> right.
# First car past x > 800 wins; the name prints in the terminal and the window closes.
# Close the window anytime with the window X button.
#
# Speeds (pixels per frame @ 60 FPS): Lightning 2, Francesco 3, Tow Mater 2.5
# Francesco should normally win. Change max_speed in the Car(...) list to try others.

import pygame
import sys

class Car:
    def __init__(self, name, max_speed, color, y_position):
        self.name = name
        self.max_speed = max_speed
        self.color = color
        self.x_position = 0
        self.y_position = y_position

    def move_forward(self):
        self.x_position += self.max_speed

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Car Race")
    font = pygame.font.Font(None, 24)

    clock = pygame.time.Clock()

    cars = [
        Car("Lightning McQueen", 2, (255, 0, 0), 100),
        Car("Francesco", 3, (128, 255, 255), 200),      # fastest — usually wins
        Car("Tow Mater", 2.5, (187, 51, 255), 300),
    ]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))

        for car in cars:
            car.move_forward()
            pygame.draw.rect(screen, car.color, pygame.Rect(car.x_position, car.y_position, 60, 30))
            label = font.render(f"{car.name} - {car.max_speed * 60} km/h", True, (0, 0, 0))
            screen.blit(label, (car.x_position, car.y_position - 20))

        pygame.display.flip()

        for car in cars:
            if car.x_position > 800:
                print(f"{car.name} has won the race!")
                running = False
                break

        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
