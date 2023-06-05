import pygame
from grid import LineGrid
from car import Car 
from player import Player
from time import time, sleep
from random import choice

win = pygame.display.set_mode((1000, 720))

frog = pygame.image.load("assets/frogger frog.png")
frog = pygame.transform.scale(frog, (frog.get_width() * 7, frog.get_height() * 7))
frog_attracting = pygame.image.load("assets/frogger frog attracting.png")
frog_attracting = pygame.transform.scale(frog_attracting, (100, 100))

road = pygame.image.load("assets/road.png")
road = pygame.transform.scale(road, (road.get_width() * 0.225, road.get_height() * 0.225))
road_list = list()
for i in range(5):
    road_line = LineGrid(road, road.get_height(), win.get_height() - road.get_height() * (i + 2))
    road_line.fill_line()
    road_list.append(road_line)

scale = 0.8
blue_car = pygame.image.load("assets/blue_car.png")
blue_car = pygame.transform.scale(blue_car, (blue_car.get_width() * scale, blue_car.get_height() * scale))
red_car = pygame.image.load("assets/red_car.png")
red_car = pygame.transform.scale(red_car, (red_car.get_width() * scale, red_car.get_height() * scale))
yellow_car = pygame.image.load("assets/yellow_car.png")
yellow_car = pygame.transform.scale(yellow_car, (yellow_car.get_width() * scale, yellow_car.get_height() * scale))
no_roof_car = pygame.image.load("assets/no_roof_car.png")
no_roof_car = pygame.transform.scale(no_roof_car, (no_roof_car.get_width() * scale, no_roof_car.get_height() * scale))
cars = []

player = Player(frog, [win.get_width() / 2 - frog.get_width() / 2, win.get_height() - frog.get_width()], "up")

def main():
    run = True
    last_time = time()
    clock = pygame.time.Clock()
    while run:
        win.fill("#00539C")

        delta_time = clock.tick(100) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        if time() - last_time > 0.1:
            if player.direction == "up":
                player.texture = frog
            if player.direction == "down":
                player.texture = pygame.transform.rotate(frog, 180)
            if player.direction == "right":
                player.texture = pygame.transform.rotate(frog, -90)
            if player.direction == "left":
                player.texture = pygame.transform.rotate(frog, 90)

        keys = pygame.key.get_pressed()
        last_time = movement(keys, last_time, delta_time)
        player.update()

        for i in range(len(road_list)):
            if time() - road_list[i].last_time > road_list[i].timing:
                if i % 2 == 1: direction = "right"
                else: direction = "left"
                if direction == "right": car = Car(choice([blue_car, red_car, yellow_car, no_roof_car]), [0, road_list[i].y], road_list[i].line_speed, direction)
                if direction == "left": car = Car(choice([blue_car, red_car, yellow_car, no_roof_car]), [win.get_width(), road_list[i].y], road_list[i].line_speed, direction)
                cars.append(car)
                road_list[i].last_time = time()
        
        for car in cars:        
            if car.pos[0] < 0 - car.texture.get_width() or car.pos[0] > win.get_width():
                cars.remove(car)
            else:
                car.pos[0] -= car.speed * 120 * delta_time
                car.update()
                if car.hitbox.colliderect(player.hitbox):
                    game_over()
        
        for road_line in road_list:
            for line in road_line.line:
                win.blit(road_line.texture, (line, road_line.y))

        for car in cars:
                win.blit(car.texture, (car.pos[0], car.pos[1]))

        win.blit(player.texture, (player.pos[0], player.pos[1])) 
        pygame.display.update()

def movement(keys, last_time, delta_time):
    if (keys[pygame.K_w] or keys[pygame.K_UP]) and time() - last_time > 0.2 and player.pos[1] > road.get_height():
        player.pos[1] -= road.get_height()
        player.texture = frog_attracting
        player.direction = "up"
        last_time = time()
    if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and time() - last_time > 0.2 and player.pos[1] < road.get_height() * 6:
        player.pos[1] += road.get_height()
        player.texture = pygame.transform.flip(frog_attracting, False, True)
        player.direction = "down"
        last_time = time()
    if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and player.pos[0] < win.get_width() - player.texture.get_width():
        player.pos[0] += 300 * delta_time
        player.direction = "right"
    if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and player.pos[0] > 0:
        player.pos[0] -= 300 * delta_time
        player.direction = "left"

    return last_time

def game_over():
    player.pos = [win.get_width() / 2 - frog.get_width() / 2, win.get_height() - frog.get_width()]
    player.direction = "up"

if __name__ == "__main__":
    main()