import random
import time

# ===== Base Classes =====
class Animal:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")


# ===== Animal Subclasses =====
class Dog(Animal):
    def move(self):
        return "Running 🐕"

class Bird(Animal):
    def move(self):
        return "Flying 🐦"

class Fish(Animal):
    def move(self):
        return "Swimming 🐠"

class Snake(Animal):
    def move(self):
        return "Slithering 🐍"


# ===== Vehicle Subclasses =====
class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

class Boat(Vehicle):
    def move(self):
        return "Sailing 🚤"

class Bicycle(Vehicle):
    def move(self):
        return "Pedaling 🚴"


# ===== Race Simulator =====
def race(participants):
    print("🏁 The race is starting! 🏁\n")
    time.sleep(1)

    results = {}

    for p in participants:
        # Each participant gets a random "speed" between 10 and 100
        speed = random.randint(10, 100)
        results[p.__class__.__name__] = speed
        print(f"{p.__class__.__name__} is {p.move()} at speed {speed}!")

    print("\n⏱️ Race Finished!\n")

    # Sort results by speed
    sorted_results = sorted(results.items(), key=lambda x: x[1], reverse=True)

    # Display standings
    for i, (name, speed) in enumerate(sorted_results, start=1):
        print(f"{i}. {name} ({speed} speed)")

    # Winner
    winner = sorted_results[0][0]
    print(f"\n🥇 Winner: {winner}! 🎉")


# ===== Main Program =====
def main():
    movers = [Dog(), Car(), Bird(), Plane(), Fish(), Boat(), Snake(), Bicycle()]
    race(movers)


if __name__ == "__main__":
    main()
