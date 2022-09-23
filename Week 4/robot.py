class Robot:
    """Represents a robot, with a name."""

    # A class variable, counting the number of robots
    all_robots = []

    def __init__(self, name):
        """Initializes the data."""
        self.name = name
        print("(Initializing {})".format(self.name))

        # When this person is created, the robot
        # adds to the population
        Robot.all_robots.append(self)

    def die(self):
        """I am dying."""
        print("{} is being destroyed!".format(self.name))

        Robot.all_robots.remove(self)

        if Robot.num_robots() == 0:
            print(f"{self.name} was the last one.")
        else:
            print(f"There are still {Robot.num_robots()} robots working.")

    def say_hi(self):
        """Greeting by the robot.
        Yeah, they can do that."""
        print(f"Greetings, people call me {self.name}.")

    @classmethod
    def num_robots(cls):
        """Total Number of robots"""
        return len(cls.all_robots)

    @classmethod
    def create_robots(cls, robot_names):
        """Create a bunch of robots

        :param robot_names: list of robot names
        :return: list of robots
        """
        return [cls(name) for name in robot_names]

    def __str__(self):
        return f'Robot: {self.name}'

    def __repr__(self):
        return f'<Robot {self.name}>'



if __name__ == "__main__":
    droid1 = Robot("R2-D2")
    droid1.say_hi()
    print(f'Total Robots = {Robot.num_robots()}')

    droid2 = Robot("C-3PO")
    droid2.say_hi()
    print(f'Total Robots = {Robot.num_robots()}')

    print("\nRobots can do some work here.\n")

    print("Robots have finished their work. So let's destroy them.")
    droid1.die()
    droid2.die()

    print(f'Total Robots = {Robot.num_robots()}')

    names = ['HAL 9000', 'Roomba', 'Spirit', 'Opportunity']
    bots = Robot.create_robots(names)
    for bot in bots:
        bot.say_hi()
