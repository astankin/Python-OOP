from unittest import TestCase, main

from project.team import Team


class TestTeam(TestCase):
    def test_init(self):
        team = Team("Test")
        self.assertEqual("Test", team.name)
        self.assertEqual({}, team.members)

    def test_name_not_alpha_raise(self):
        with self.assertRaises(ValueError) as err:
            team = Team("123as")
        self.assertEqual("Team Name can contain only letters!", str(err.exception))

    def test_add_member(self):
        team = Team("Test")
        members = {"member1": 12, "member2": 20, "member3": 40}
        result = team.add_member(**members)
        self.assertEqual(f"Successfully added: member1, member2, member3", result)
        self.assertEqual({"member1": 12, "member2": 20, "member3": 40}, team.members)
        members1 = {"member1": 12}
        result1 = team.add_member(**members1)
        self.assertEqual(f"Successfully added: ", result1)
        self.assertEqual({"member1": 12, "member2": 20, "member3": 40}, team.members)

    def test_remove_member_if_member_in_collection(self):
        team = Team("Test")
        team.members = {"member1": 12}
        result = team.remove_member("member1")
        self.assertEqual(f"Member member1 removed", result)
        self.assertEqual({}, team.members)
        self.assertEqual(0, len(team))

    def test_remove_member_if_member_not_in_collection(self):
        team = Team("Test")
        team.members = {"member1": 12}
        result = team.remove_member("member2")
        self.assertEqual(f"Member with name member2 does not exist", result)
        self.assertEqual({"member1": 12}, team.members)

    def test_gt_return_true(self):
        team1 = Team("first")
        team2 = Team("second")
        team1.members = {"member1": 12, "member2": 20, "member3": 40}
        team2.members = {"member1": 12, "member2": 20}
        result = team1 > team2
        self.assertEqual(True, result)
        self.assertTrue(team1 > team2)

    def test_gt_return_falce(self):
        team1 = Team("first")
        team2 = Team("second")
        team2.members = {"member1": 12, "member2": 20, "member3": 40}
        team1.members = {"member1": 12, "member2": 20}
        result = team1 > team2
        self.assertEqual(False, result)
        self.assertFalse(team1 > team2)

    def test_len(self):
        team = Team("first")
        team.members = {"member1": 12, "member2": 20, "member3": 40}
        self.assertEqual(3, len(team))
        team.members = {}
        self.assertEqual(0, len(team))

    def test_add(self):
        team1 = Team("first")
        team2 = Team("second")
        team2.members = {"member1": 12, "member2": 20, "member3": 40}
        team1.members = {"member4": 12, "member5": 20}
        result = team1 + team2
        self.assertEqual("firstsecond", result.name)
        self.assertEqual({"member1": 12, "member2": 20, "member3": 40, "member4": 12, "member5": 20}, result.members)
        self.assertEqual(5, len(result))

    def test_str_sorted_by_values_in_descending(self):
        team = Team("Test")
        team.members = {"member3": 40, "member2": 20, "member1": 12}
        expected = f"Team name: Test\n" \
                   f"Member: member3 - 40-years old\n" \
                   f"Member: member2 - 20-years old\n" \
                   f"Member: member1 - 12-years old"
        self.assertEqual(expected, str(team))

    def test_str_sorted_by_values_and_then_by_names(self):
        team = Team("Test")
        team.members = {"amember3": 40, "member2": 40, "member1": 12}
        expected = f"Team name: Test\n" \
                   f"Member: amember3 - 40-years old\n" \
                   f"Member: member2 - 40-years old\n" \
                   f"Member: member1 - 12-years old"
        self.assertEqual(expected, str(team))


if __name__ == "__main__":
    main()
