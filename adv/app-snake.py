from tkinter import *
import random

GAME_W = 700
GAME_H = 700
SPEED = 200
SPACE_SIZE = 50 # 
BODY_PARTS = 3 # starting parts
SNAKE_COLOR = "green"
FOOD_COLOR = "red"
BG_COLOR = "black"

class Snake:
    def __init__(self) -> None:
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
            self.squares.append(square)

class Food:
    def __init__(self):
        x = random.randint(0, (GAME_W / SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (GAME_H / SPACE_SIZE) - 1) * SPACE_SIZE
        self.coordinates = [x, y]
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tags="food")

def next_turn(snake, food):
    x, y = snake.coordinates[0] # snake's head
    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0, (x, y)) # snake's head new location
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1
        label.config(text=f"Score: {score}")
        canvas.delete("food")
        food = Food()
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if check_collision(snake):
        game_over()
    else:
        window.after(SPEED, next_turn, snake, food)

def change_direction(new_direction):
    global direction
    print(direction)
    if new_direction == "left":
        if direction != "right":
            direction = new_direction
    elif new_direction == "right":
        if direction != "left":
            direction = new_direction
    elif new_direction == "up":
        if direction != "down":
            direction = new_direction
    elif new_direction == "down":
        if direction != "up":
            direction = new_direction

def check_collision(snake):
    x, y = snake.coordinates[0] # head
    if x < 0 or x >= GAME_W or y < 0 or y >= GAME_H:
        return True
    for body_part in snake.coordinates[1:]: # anything after head
        if x == body_part[0] and y == body_part[1]:
            return True
    return False

def game_over():
    canvas.delete("all")
    canvas.create_text(
        canvas.winfo_width() / 2,
        canvas.winfo_height() / 2,
        text="GAME OVER", font=("Arial", 40), fill="red")

window = Tk()
window.title("Snake Game")
window.resizable(False, False)

score = 0
direction = 'down'

label = Label(window, text=f"Score: {score}", font=("Arial", 20))
label.pack()

canvas = Canvas(window, width=GAME_W, height=GAME_H, bg=BG_COLOR)
canvas.pack()

window.update() # important which refresh the window and show canvas's object

# center the window in the middle of the screen
window_w = window.winfo_width()
window_h = window.winfo_height()
screen_w = window.winfo_screenwidth()
screen_h = window.winfo_screenheight()
x = (int((screen_w/2) - (window_w/2)))
y = (int((screen_h/2) - (window_h/2)))
window.geometry(f"{window_w}x{window_h}+{x}+{y}")

window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

snake = Snake()
food = Food()

next_turn(snake, food)

window.mainloop()