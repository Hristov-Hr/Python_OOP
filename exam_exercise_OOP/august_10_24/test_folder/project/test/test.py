from project.soccer_player import SoccerPlayer
from unittest import TestCase, main


class TestSoccerPlayer(TestCase):

    def setUp(self) -> None:
        self.player = SoccerPlayer("Leo Messi", 30, 150, "Barcelona")

    def test_name(self):
        self.assertEqual("Leo Messi", self.player.name)
        with self.assertRaises(ValueError) as p:
            self.player.name = "Mesi"
        self.assertEqual("Name should be more than 5 symbols!", str(p.exception))

    def test_age(self):
        self.assertEqual(30, self.player.age)
        with self.assertRaises(ValueError) as p:
            self.player.age = 15
        self.assertEqual("Players must be at least 16 years of age!", str(p.exception))

    def test_goals(self):
        self.player.goals = -1
        self.assertEqual(0, self.player.goals)

    def test_team(self):
        self.assertEqual("Barcelona", self.player.team)
        with self.assertRaises(ValueError) as p:
            self.player.team = "CSKA"
        self.assertEqual(f"Team must be one of the following: {', '.join(SoccerPlayer._VALID_TEAMS)}!", str(p.exception))

    def test_change_team(self):
        self.assertEqual("Invalid team name!", self.player.change_team('CSKA'))
        self.assertEqual("Barcelona", self.player.team)
        self.assertEqual("Team successfully changed!", self.player.change_team("PSG"))
        self.assertEqual("PSG", self.player.team)

    def test_add_new_achievement(self):
        self.assertEqual("Cup has been successfully added to the achievements collection!", self.player.add_new_achievement("Cup"))
        self.assertEqual({"Cup": 1}, self.player.achievements)
        self.assertEqual("Cup has been successfully added to the achievements collection!", self.player.add_new_achievement("Cup"))
        self.assertEqual({"Cup": 2}, self.player.achievements)

    def test__lt__(self):

        player2 = SoccerPlayer("Ronaldo", 33, 151, "Real Madrid")
        self.assertEqual(f"Ronaldo is a top goal scorer! S/he scored more than Leo Messi.", self.player.__lt__(player2))
        self.player.goals += 2
        self.assertEqual("Leo Messi is a better goal scorer than Ronaldo.", self.player.__lt__(player2))


if __name__ == "__main__":
    main()