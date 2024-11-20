from project.tennis_player import TennisPlayer

from unittest import TestCase, main


class TestTennisPlayer(TestCase):

    def setUp(self) -> None:
        self.player = TennisPlayer("Nadal", 36, 1200.0)

    def test_init(self):
        self.assertEqual(1200.0, self.player.points)
        self.assertEqual([], self.player.wins)

    def test_name(self):
        self.assertEqual("Nadal", self.player.name)
        with self.assertRaises(ValueError) as p:
            self.player.name = "az"
        self.assertEqual("Name should be more than 2 symbols!", str(p.exception))
        self.player.name = "Iam"
        self.assertEqual("Iam", self.player.name)

    def test_age(self):
        self.player.age = 18
        self.assertEqual(18, self.player.age)
        with self.assertRaises(ValueError) as p:
            self.player.age -= 1
        self.assertEqual("Players must be at least 18 years of age!", str(p.exception))

    def test_add_new_win(self):
        self.assertEqual([], self.player.wins)
        self.player.add_new_win("U.S.Open")
        self.assertEqual(["U.S.Open"], self.player.wins)
        self.assertEqual("U.S.Open has been already added to the list of wins!", self.player.add_new_win("U.S.Open"))
        self.assertEqual(["U.S.Open"], self.player.wins)
        self.player.add_new_win("Sofia Open")
        self.assertEqual(["U.S.Open", "Sofia Open"], self.player.wins)

    def test_lt_(self):
        other = TennisPlayer("test", 32, 1199.0)
        self.assertEqual('Nadal is a better player than test', self.player.__lt__(other))
        other.points += 2
        self.assertEqual("test is a top seeded player and he/she is better than Nadal", self.player.__lt__(other))

    def test_str_(self):
        self.assertEqual(f"Tennis Player: Nadal\nAge: 36\nPoints: 1200.0\nTournaments won: ", self.player.__str__())
        self.player.add_new_win("U.S.Open")
        self.player.add_new_win("Sofia Open")
        self.assertEqual(f"Tennis Player: Nadal\nAge: 36\nPoints: 1200.0\nTournaments won: U.S.Open, Sofia Open", self.player.__str__())


if __name__ == "__main__":
    main()