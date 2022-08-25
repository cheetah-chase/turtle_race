from turtle import Screen
from turtle_class import TurtleCl

try:

    print("Welcome to the Turtle Game")
    print("Instruction are: \n "
          "1. To control the red turtle click 'r' on your computer \n "
          "2. To control the orange turtle click 'o' on your computer \n "
          "3. To control the yellow turtle click 'y' on your computer \n "
          "4. To control the green turtle click 'g' on your computer \n "
          "5. To control the blue turtle click 'b' on your computer \n "
          "6. To control the red turtle click 'p' on your computer")
    is_on = True
    no_of_player = int(input("How many people want to play: "))
    all_turtle = []

    screen = Screen()
    screen.setup(width=1100, height=500)
    screen.title("Turtle Race")

    # Red Turtle
    red_turtle = TurtleCl((-500, -100), "red")
    red_turtle.hideturtle()
    all_turtle.append(red_turtle)
    # Orange Turtle
    orange_turtle = TurtleCl((-500, -50), "orange")
    orange_turtle.hideturtle()
    all_turtle.append(orange_turtle)
    # Yellow Turtle
    yellow_turtle = TurtleCl((-500, 0), "yellow")
    yellow_turtle.hideturtle()
    all_turtle.append(yellow_turtle)
    # Green Turtle
    green_turtle = TurtleCl((-500, 50), "green")
    green_turtle.hideturtle()
    all_turtle.append(green_turtle)
    # Blue Turtle
    blue_turtle = TurtleCl((-500, 100), "blue")
    blue_turtle.hideturtle()
    all_turtle.append(blue_turtle)
    # Purple Turtle
    purple_turtle = TurtleCl((-500, 150), "purple")
    purple_turtle.hideturtle()
    all_turtle.append(purple_turtle)

    if no_of_player == 1:
        print("Not enough player")
    elif no_of_player == 2:
        red_turtle.showturtle()
        orange_turtle.showturtle()
    elif no_of_player == 3:
        red_turtle.showturtle()
        orange_turtle.showturtle()
        yellow_turtle.showturtle()
    elif no_of_player == 4:
        red_turtle.showturtle()
        orange_turtle.showturtle()
        yellow_turtle.showturtle()
        green_turtle.showturtle()
    elif no_of_player == 5:
        red_turtle.showturtle()
        orange_turtle.showturtle()
        yellow_turtle.showturtle()
        green_turtle.showturtle()
        blue_turtle.showturtle()
    elif no_of_player == 6:
        red_turtle.showturtle()
        orange_turtle.showturtle()
        yellow_turtle.showturtle()
        green_turtle.showturtle()
        blue_turtle.showturtle()
        purple_turtle.showturtle()
    else:
        print("More/Less than the color please reduce/increase the number of player in it")

    while is_on:
        if red_turtle.xcor() > 540:
            is_on = False
            print(f"The winner is red")
        elif orange_turtle.xcor() > 540:
            is_on = False
            print(f"The winner is orange")
        elif yellow_turtle.xcor() > 540:
            is_on = False
            print(f"The winner is yellow")
        elif green_turtle.xcor() > 540:
            is_on = False
            print(f"The winner is green")
        elif blue_turtle.xcor() > 540:
            is_on = False
            print(f"The winner is blue")
        elif purple_turtle.xcor() > 540:
            is_on = False
            print(f"The winner is purple")

    screen.listen()

    screen.onkey(red_turtle.go_forward, "r")
    screen.onkey(orange_turtle.go_forward, "o")
    screen.onkey(yellow_turtle.go_forward, "y")
    screen.onkey(green_turtle.go_forward, "g")
    screen.onkey(blue_turtle.go_forward, "b")
    screen.onkey(purple_turtle.go_forward, "p")

    screen.exitonclick()
except IndexError:
    print("The number of turtle is more than the length of the height")
