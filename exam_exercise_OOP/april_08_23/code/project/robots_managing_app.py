from typing import List

from project.robots.base_robot import BaseRobot
from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.base_service import BaseService
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    SERVICES_TYPE = {"MainService": MainService, "SecondaryService": SecondaryService}
    ROBOTS_TYPE = {"MaleRobot": MaleRobot, "FemaleRobot": FemaleRobot}
    VALID_MATCH = {"MaleRobot": "MainService", "FemaleRobot": "SecondaryService"}

    def __init__(self):
        self.robots: List[BaseRobot] = []
        self.services: List[BaseService] = []

    def add_service(self, service_type: str, name: str):

        if service_type not in self.SERVICES_TYPE.keys():
            raise Exception("Invalid service type!")

        self.services.append(self.SERVICES_TYPE[service_type](name))
        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):

        if robot_type not in self.ROBOTS_TYPE.keys():
            raise Exception("Invalid robot type!")

        self.robots.append(self.ROBOTS_TYPE[robot_type](name, kind, price))
        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):

        robot = [r for r in self.robots if r.name == robot_name][0]
        service = [s for s in self.services if s.name == service_name][0]

        if self.VALID_MATCH[robot.ROBOT_TYPE] != service.SERVICE_TYPE:
            return "Unsuitable service."

        if service.capacity == len(service.robots):
            raise Exception("Not enough capacity for this robot!")

        self.robots.remove(robot)
        service.robots.append(robot)
        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):

        service = [s for s in self.services if s.name == service_name][0]

        try:
            robot = next(filter(lambda r: r.name == robot_name, service.robots))
            service.robots.remove(robot)
            self.robots.append(robot)
            return f"Successfully removed {robot_name} from {service_name}."

        except StopIteration:
            raise Exception("No such robot in this service!")

    def feed_all_robots_from_service(self, service_name: str):

        service = [s for s in self.services if s.name == service_name][0]
        [r.eating() for r in service.robots]

        return f"Robots fed: {len(service.robots)}."

    def service_price(self, service_name: str):

        service = [s for s in self.services if s.name == service_name][0]
        total_price = sum(r.price for r in service.robots)

        return f"The value of service {service_name} is {total_price:.2f}."

    def __str__(self):

        return "\n".join([s.details for s in self.services])
