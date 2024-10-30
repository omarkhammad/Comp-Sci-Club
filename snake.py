# Omar Hammad
# Snake Game
# Comp-Sci Club Demo

import random
import turtle

WIDTH = 800
HEIGHT = 800
FOOD_SIZE = 20


def go_up():
    global snake_direction
    if snake_direction != "down":
        snake_direction = "up"


def go_down():
    global snake_direction
    if snake_direction != "up":
        snake_direction = "down"


def go_right():
    global snake_direction
    if snake_direction != "left":
        snake_direction = "right"


def go_left():
    global snake_direction
    if snake_direction != "right":
        snake_direction = "left"


def random_food_position():
    x = random.randint(- WIDTH / 2 + FOOD_SIZE, WIDTH / 2 - FOOD_SIZE)
    y = random.randint(- HEIGHT / 2 + FOOD_SIZE, HEIGHT / 2 - FOOD_SIZE)
    return [x, y]


def touching_food():
    x = new_head[0]
    y = new_head[1]
    return food.distance(x, y) < 20


def move_snake():
    global food_pos, snake, new_head

    # Next position for head of snake
    new_head = snake[-1].copy()

    if snake_direction == "up":
        new_head[1] += 20
    elif snake_direction == "down":
        new_head[1] -= 20
    elif snake_direction == "left":
        new_head[0] -= 20
    else:
        new_head[0] += 20

    # Check self-collision
    if new_head in snake:
        start()
    else:
        snake.append(new_head)

        if touching_food():
            food_pos = random_food_position()
            food.goto(food_pos)
        else:
            snake.pop(0)

        pen.clearstamps()

        for segment in snake:
            pen.goto(segment[0], segment[1])
            pen.stamp()

        window.update()

        turtle.ontimer(move_snake, 100)


def start():
    global snake, food_pos, snake_direction
    snake_direction = "up"
    snake = [[0, 0], [0, 20], [0, 40], [0, 60], [0, 80]]
    food_pos = random_food_position()
    food.goto(food_pos)
    move_snake()


# Window
window = turtle.Screen()
window.setup(WIDTH, HEIGHT)
window.title("Fun Snake Game")
window.bgcolor("green")
window.tracer(0)

# Pen draws our snake
pen = turtle.Turtle("square")
pen.penup()

# Food
food = turtle.Turtle("circle")
food.color("red")
food.penup()

# Event handler
window.listen()
window.onkey(go_up, "w")
window.onkey(go_down, "s")
window.onkey(go_left, "a")
window.onkey(go_right, "d")


start()
turtle.done()
