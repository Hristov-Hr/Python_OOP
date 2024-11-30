from project.horse_specification.horse import Horse


class Appaloosa(Horse):

    MAX_SPEED = 120

    def train(self):
        self.speed += 2