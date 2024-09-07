from abc import ABC, abstractmethod


class Robot(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def sensors_amount(self):
        pass


class BasicRobot(Robot):
    def sensors_amount(self):
        return 1


class MedicalRobot(Robot):
    def sensors_amount(self):
        return 6


class ChefRobot(Robot):
    def sensors_amount(self):
        return 4


class WarRobot(Robot):
    def sensors_amount(self):
        return 12


def number_of_robot_sensors(robot):
    return robot.sensors_amount()


robots = [BasicRobot('Robo'), MedicalRobot('Da Vinci'), ChefRobot('Moley'), WarRobot('Griffin')]

for r in robots:
    print(number_of_robot_sensors(r))