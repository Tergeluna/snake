import random
import turtle
import time

s = turtle.Screen()
s.title("Snake Game by Tergel aka Luna")
s.bgcolor("grey")
s.setup(width=600, height=600)
s.tracer(0)
delay = 0.2

sn = turtle.Turtle()
sn.speed(0)
sn.shape("square")
sn.color("black")
sn.penup()
sn.goto(0, 0)
sn.direction = "stop"

score = 0
high_score = 0

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score : 0 High Score: 0", align="center", font=("Monoid", 26, "normal"))


def move():
    if sn.direction == "up":
        y = sn.ycor()
        sn.sety(y + 20)

    if sn.direction == "down":
        y = sn.ycor()
        sn.sety(y - 20)

    if sn.direction == "left":
        x = sn.xcor()
        sn.setx(x - 20)

    if sn.direction == "right":
        x = sn.xcor()
        sn.setx(x + 20)


def go_up():
    if sn.direction != "down":
        sn.direction = "up"


def go_down():
    if sn.direction != "up":
        sn.direction = "down"


def go_left():
    if sn.direction != "right":
        sn.direction = "left"


def go_right():
    if sn.direction != "left":
        sn.direction = "right"


s.listen()
s.onkey(go_up, "Up")
s.onkey(go_down, "Down")
s.onkey(go_left, "Left")
s.onkey(go_right, "Right")

f = turtle.Turtle()
f.speed(0)
f.shape("circle")
f.color("red")
f.penup()
f.goto(0, 100)

segments = []

while True:
    s.update()
    if sn.xcor() > 290 or sn.xcor() < -290 or sn.ycor() > 290 or sn.ycor() < -290:
        time.sleep(1)
        sn.goto(0, 0)
        sn.direction = "stop"

        for segment in segments:
            segment.goto(1000, 1000)

        segments.clear()
        score = 0
        delay = 0.2

        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Monoid", 26, "normal"))

    if sn.distance(f) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        f.goto(x, y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("green")
        new_segment.penup()
        segments.append(new_segment)

        score += 10
        delay -= 0.002

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Monoid", 26, "normal"))

    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        x = sn.xcor()
        y = sn.ycor()
        segments[0].goto(x, y)

    move()

    for segment in segments:
        if segment.distance(sn) < 20:
            time.sleep(1)
            sn.goto(0, 0)
            sn.direction = "stop"

            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()

    time.sleep(delay)

sn.mainloop()
