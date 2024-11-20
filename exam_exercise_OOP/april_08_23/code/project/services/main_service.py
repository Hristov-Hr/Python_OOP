from project.services.base_service import BaseService


class MainService(BaseService):

    SERVICE_TYPE = "MainService"

    def __init__(self, name: str):
        super().__init__(name, capacity=30)

    def details(self):
        return f"{self.name} Main Service:\nRobots: {' '.join(r.name for r in self.robots) if self.robots else 'none'} "