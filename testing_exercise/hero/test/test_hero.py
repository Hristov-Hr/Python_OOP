from project.hero import Hero
from unittest import TestCase, main


class TestHero(TestCase):

    def setUp(self) -> None:
        self.hero = Hero("Adela", 24, 350.0, 22.0)

    def test_init(self):
        self.assertIsInstance(self.hero.username, str)
        self.assertIsInstance(self.hero.level, int)
        self.assertIsInstance(self.hero.health, float)
        self.assertIsInstance(self.hero.damage, float)
        self.assertNotEqual(self.hero.username, '')
        self.assertGreater(self.hero.level, 0)
        self.assertGreaterEqual(self.hero.damage, 0)
        self.assertGreaterEqual(self.hero.health, 0)

    def test_battle_against_yourself(self):

        with self.assertRaises(Exception) as h:
            self.hero.battle(enemy_hero=Hero("Adela", 20, 20.5, 25.0))
        self.assertEqual("You cannot fight yourself", str(h.exception))

    def test_battle_when_health_is_zero_or_negative(self):

        with self.assertRaises(Exception) as h:
            self.hero.health = 0
            self.hero.battle(enemy_hero=Hero("Craig", 10, 12.5, 33.5))
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(h.exception))

        with self.assertRaises(Exception) as h:
            self.hero.health = -1
            self.hero.battle(enemy_hero=Hero("Craig", 10, 12.5, 33.5))
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(h.exception))

    def test_battle_when_enemy_health_is_zero_or_negative(self):

        with self.assertRaises(ValueError) as h:
            self.hero.battle(enemy_hero=Hero("Craig", 2, 0, 20))
        self.assertEqual("You cannot fight Craig. He needs to rest", str(h.exception))

        with self.assertRaises(ValueError) as h:
            self.hero.battle(enemy_hero=Hero("Craig", 2, -1, 20))
        self.assertEqual("You cannot fight Craig. He needs to rest", str(h.exception))

    def test_battle_draw(self):
        self.assertEqual("Draw", self.hero.battle(enemy_hero=Hero("Craig", 20, 500.0, 20.0)))

    def test_battle_win(self):
        self.assertEqual("You win", self.hero.battle(enemy_hero=Hero("Craig", 1, 200.0, 5.5)))
        self.assertEqual(25, self.hero.level)
        self.assertEqual(349.5, self.hero.health)
        self.assertEqual(27.0, self.hero.damage)

    def test_battle_lost(self):
        enemy_hero = Hero("Craig", 20, 600.0, 20.0)
        self.assertEqual("You lose", self.hero.battle(enemy_hero))
        self.assertEqual(77.0, enemy_hero.health)
        self.assertEqual(21, enemy_hero.level)
        self.assertEqual(25.0, enemy_hero.damage)

    def test_str(self):
        self.assertEqual("Hero Adela: 24 lvl\nHealth: 350.0\nDamage: 22.0\n", str(self.hero))


if __name__ == "__main__":
    main()