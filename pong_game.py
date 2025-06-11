from tkinter import *
import random

# Global variables
WIDTH = 300
HEIGHT = 300
BALL_RADIUS = 15
INITIAL_SPEED = 20
PLAYER1_SCORE = 0
PLAYER2_SCORE = 0

# Ball speed variables
BALL_X_SPEED = INITIAL_SPEED
BALL_Y_SPEED = INITIAL_SPEED

def update_score(player):
    global PLAYER1_SCORE, PLAYER2_SCORE
    if player == "right":
        PLAYER2_SCORE += 1
        p2_text.config(text=PLAYER2_SCORE)
    else:
        PLAYER1_SCORE += 1
        p1_text.config(text=PLAYER1_SCORE)

def spawn_ball():
    global BALL_X_SPEED, BALL_Y_SPEED
    BALL_X_SPEED = random.randrange(-10, 10)
    BALL_Y_SPEED = INITIAL_SPEED

# Setting up the window
root = Tk()
root.title("Pong")

# Canvas area
c = Canvas(root, width=WIDTH, height=HEIGHT, background="#003300")
c.pack()

# Game elements
c.create_line(0, 0, 0, HEIGHT, fill="white")  # Left line
c.create_line(WIDTH - 1, 0, WIDTH - 1, HEIGHT, fill="white")  # Right line
c.create_line(WIDTH / 2, 0, WIDTH / 2, HEIGHT, fill="white")  # Center line

# Initialize ball
ball = c.create_oval(WIDTH / 2 - BALL_RADIUS, HEIGHT / 2 - BALL_RADIUS,
                      WIDTH / 2 + BALL_RADIUS, HEIGHT / 2 + BALL_RADIUS, fill="white")

# Create paddles
left_paddle = c.create_line(20, HEIGHT / 2 - 30, 20, HEIGHT / 2 + 30, fill="yellow")
right_paddle = c.create_line(WIDTH - 20, HEIGHT / 2 - 30, WIDTH - 20, HEIGHT / 2 + 30, fill="yellow")

# Score display
p1_text = c.create_text(WIDTH / 4, 20, text=PLAYER1_SCORE, font="Arial 20", fill="white")
p2_text = c.create_text(3 * WIDTH / 4, 20, text=PLAYER2_SCORE, font="Arial 20", fill="white")

# Start the ball
spawn_ball()

# Start the Tkinter main loop
root.mainloop()