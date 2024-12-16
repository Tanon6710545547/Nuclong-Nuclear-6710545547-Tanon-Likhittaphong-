import turtle
import math
import random
import time

# Set up the game screen
screen = turtle.Screen()
screen.title("Enhanced Nuclear Fission Simulation")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)  # Turn off animation for smoother updates


# Define the Neutron class
class Neutron:
    def __init__(self, x, y, speed, color="white"):
        self.neutron = turtle.Turtle()
        self.neutron.shape("circle")
        self.neutron.color(color)
        self.neutron.shapesize(
            stretch_wid=0.3 if color in ["white", "green"] else 0.5,
            stretch_len=0.3 if color in ["white", "green"] else 0.5,
        )  # Slightly larger neutrons
        self.neutron.penup()
        self.neutron.speed(0)
        self.neutron.goto(x, y)  # Start from the fission point
        self.x_speed = random.uniform(-1, 1) * speed  # Random horizontal speed
        self.y_speed = random.uniform(-1, 1) * speed  # Random vertical speed

    def move(self):
        x = (self.neutron.xcor()
             + self.x_speed)
        y = (self.neutron.ycor()
             + self.y_speed)
        if x > 390 or x < -390:
            self.x_speed *= -1
        if y > 290 or y < -290:
            self.y_speed *= -1
        self.neutron.goto(x, y)

    def collision_with_uranium(self, uranium):
        # Check if the neutron collides with a uranium atom
        return self.neutron.distance(uranium.atom) < 20

    def collision_with_neutron(self, other_neutron):
        # Check if this neutron collides with another neutron
        return self.neutron.distance(other_neutron.neutron) < 15

    def bounce_off(self, other_neutron):
        # Exchange velocities upon collision
        self.x_speed, other_neutron.x_speed = other_neutron.x_speed, self.x_speed
        self.y_speed, other_neutron.y_speed = other_neutron.y_speed, self.y_speed

        # Apply small random adjustments to separate the neutrons
        self.x_speed += random.uniform(-0.1, 0.1)
        self.y_speed += random.uniform(-0.1, 0.1)
        other_neutron.x_speed += random.uniform(-0.1, 0.1)
        other_neutron.y_speed += random.uniform(-0.1, 0.1)

    def bounce_off_uranium(self):
        # Apply a physics-based bounce effect
        speed = (self.x_speed ** 2 + self.y_speed ** 2) ** 0.5  # Calculate the magnitude of velocity
        angle = random.uniform(0, 360)  # Generate a random bounce angle in degrees
        angle_rad = math.radians(angle)  # Convert to radians

        # Update x_speed and y_speed based on bounce angle
        self.x_speed = speed * math.cos(angle_rad)
        self.y_speed = speed * math.sin(angle_rad)


class Uranium:
    def __init__(self, x, y):
        self.atom = turtle.Turtle()
        self.atom.shape("circle")
        self.atom.color("green")
        self.atom.shapesize(stretch_wid=1.2, stretch_len=1.2)  # Larger uranium atom
        self.atom.penup()
        self.atom.goto(x, y)
        self.split = False  # Flag to indicate if the atom has already split

    def fission(self, new_neutrons, element_count, white_neutrons_count):
        # Simulate the fission process

        self.atom.color("red")  # Change color to indicate
        self.atom.hideturtle()
        self.split = True

        # Add exactly 2 new white neutrons with random offsets
        for _ in range(2):
            dx = random.uniform(-30, 30)  # Random horizontal offset
            dy = random.uniform(-30, 30)  # Random vertical offset
            new_neutron = Neutron(self.atom.xcor() + dx, self.atom.ycor() + dy, speed=0.75, color="white")
            new_neutrons.append(new_neutron)
            white_neutrons_count[0] += 1  # Increment white neutrons count

        # Add one randomly chosen color pair
        color_pairs = [
            ("Krypton", "Barium"),
            ("Xenon", "Strontium"),
            ("Cesium", "Rubidium"),
        ]
        selected_pair = random.choice(color_pairs)
        offsets = [(-20, -20), (20, 20)]

        # Create two neutrons for the chosen color pair
        for element, (dx, dy) in zip(selected_pair, offsets):
            neutron_color = (
                "red" if element == "Cesium" else
                "orange" if element == "Xenon" else
                "blue" if element == "Krypton" else
                "lime" if element == "Rubidium" else
                "pink" if element == "Strontium" else
                "yellow"
            )
            new_neutron = Neutron(self.atom.xcor() + dx, self.atom.ycor() + dy, speed=0.75, color=neutron_color)
            new_neutrons.append(new_neutron)
            element_count[element] += 1


def play_simulation():
    fission_count = 0
    neutron_count = int(screen.numinput("Setup", "Enter number of neutrons:", default=6, minval=1, maxval=50))
    white_neutrons_count = [neutron_count]  # To track white neutron count explicitly

    uranium_positions = []
    num_uranium = int(screen.numinput("Setup", "Enter number of uranium atoms:", default=10, minval=1, maxval=50))
    for _ in range(num_uranium):
        x = random.randint(-300, 300)
        y = random.randint(-200, 200)
        uranium_positions.append((x, y))

    uranium_atoms = [Uranium(x, y) for x, y in uranium_positions]
    neutrons = [Neutron(random.randint(-300, 300), random.randint(-200, 200), speed=0.25) for _ in range(neutron_count)]

    element_count = {"Krypton": 0, "Barium": 0, "Xenon": 0, "Strontium": 0, "Rubidium": 0, "Cesium": 0}

    score_writer = turtle.Turtle()
    score_writer.hideturtle()
    score_writer.penup()
    score_writer.color("white")
    score_writer.goto(-350, 250)

    element_writer = turtle.Turtle()
    element_writer.hideturtle()
    element_writer.penup()
    element_writer.color("white")
    element_writer.goto(200, 250)  # Position

    def update_score():
        score_writer.clear()
        score_writer.write(f"Fissions: {fission_count}  "
                           f"Neutrons: {white_neutrons_count[0]}", align="left", font=("Arial", 16, "normal"))

    def update_elements():
        element_writer.clear()
        element_writer.write(
            f"Krypton: {element_count['Krypton']}  Barium: {element_count['Barium']}\n"
            f"Xenon: {element_count['Xenon']}  Strontium: {element_count['Strontium']}\n"
            f"Rubidium: {element_count['Rubidium']}  Cesium: {element_count['Cesium']}",
            align="left",
            font=("Arial", 12, "normal"),
        )

    update_score()
    update_elements()

    while True:
        screen.update()

        new_neutrons = []

        for neutron in neutrons:
            neutron.move()

            # Check for collisions between neutrons
            for other_neutron in neutrons:
                if neutron is not other_neutron and neutron.collision_with_neutron(other_neutron):
                    neutron.bounce_off(other_neutron)

            # Check for collisions with uranium atoms
            for uranium in uranium_atoms:
                if not uranium.split:
                    if neutron.collision_with_uranium(uranium):
                        if neutron.neutron.color()[0] == "white":
                            uranium.fission(new_neutrons, element_count, white_neutrons_count)
                            fission_count += 1
                            update_score()
                            update_elements()
                        else:
                            neutron.bounce_off_uranium()

        neutrons.extend(new_neutrons)

        # Check if all uranium atoms have split
        if all(uranium.split for uranium in uranium_atoms):
            complete_message = turtle.Turtle()
            complete_message.hideturtle()
            complete_message.penup()
            complete_message.color("white")
            complete_message.goto(0, 0)
            complete_message.write("Chain Reaction Complete!", align="center", font=("Arial", 24, "bold"))
            screen.update()
            time.sleep(10)  # Pause for 10 seconds before showing restart button
            return


play_simulation()
