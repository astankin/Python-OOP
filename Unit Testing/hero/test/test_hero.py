from unittest import TestCase, main

from project.hero import Hero


class HeroTest(TestCase):
    def setUp(self) -> None:
        self.hero = Hero("Warier", 10, 100, 50)
        self.enemy = Hero("Defender", 10, 100, 50)

    def test_hero_initialization(self):
        hero = Hero("Warier", 10, 100, 50)
        self.assertEqual("Warier", hero.username)
        self.assertEqual(10, hero.level)
        self.assertEqual(100, hero.health)
        self.assertEqual(50, hero.damage)

    def test_battle_if_enemy_hero_same_raises(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_hero_health_zero_or_negative_value_raises(self):
        for health in [0, -50]:
            self.hero.health = health
            with self.assertRaises(ValueError) as ex:
                self.hero.battle(self.enemy)
            self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_enemy_health_zero_or_negative_value_raises(self):
        for health in [0, -50]:
            self.enemy.health = health
            with self.assertRaises(ValueError) as ex:
                self.hero.battle(self.enemy)
            self.assertEqual(f"You cannot fight {self.enemy.username}. He needs to rest", str(ex.exception))

    def test_battle_draw(self):
        result = self.hero.battle(self.enemy)
        self.assertEqual("Draw", result)
        self.assertEqual(-400, self.hero.health)
        self.assertEqual(-400, self.enemy.health)

    def test_battle_hero_winn(self):
        enemy = Hero("Defender", 1, 100, 50)
        result = self.hero.battle(enemy)
        self.assertEqual("You win", result)
        self.assertEqual(11, self.hero.level)
        self.assertEqual(55, self.hero.health)
        self.assertEqual(55, self.hero.damage)
        self.assertEqual(-400, enemy.health)

    def test_battle_enemy_winn(self):
        hero = Hero("Warier", 1, 100, 50)
        enemy = Hero("Defender", 1, 100, 50)
        result = hero.battle(enemy)
        self.assertEqual("You lose", result)
        self.assertEqual(2, enemy.level)
        self.assertEqual(55, enemy.health)
        self.assertEqual(55, enemy.damage)
        self.assertEqual(50, hero.health)

    def test_str_print(self):
        expected = "Hero Warier: 10 lvl\n" \
               "Health: 100\n" \
               "Damage: 50\n"
        actual = str(self.hero)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    main()