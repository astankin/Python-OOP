from unittest import TestCase, main

from project.movie import Movie


class TestMovie(TestCase):
    def test_init(self):
        movie = Movie("Test", 1983, 5.6)
        self.assertEqual("Test", movie.name)
        self.assertEqual(1983, movie.year)
        self.assertEqual(5.6, movie.rating)
        self.assertEqual([], movie.actors)

    def test_name_an_empty_string_raise(self):
        with self.assertRaises(ValueError) as err:
            movie = Movie("", 1983, 5.6)
        self.assertEqual("Name cannot be an empty string!", str(err.exception))

    def test_year_an_les_the_1887_raise(self):
        with self.assertRaises(ValueError) as err:
            movie = Movie("Test", 1000, 5.6)
        self.assertEqual("Year is not valid!", str(err.exception))

    def test_add_actor_if_name_of_actor_not_in_collection(self):
        movie = Movie("Test", 1983, 5.6)
        movie.add_actor("Test_actor")
        self.assertEqual(["Test_actor"], movie.actors)
        movie.add_actor("Test_actor2")
        self.assertEqual(["Test_actor", "Test_actor2"], movie.actors)

    def test_add_actor_name_not_in_collection(self):
        movie = Movie("Test", 1983, 5.6)
        movie.add_actor("Test_actor")
        result = movie.add_actor("Test_actor")
        self.assertEqual(f"Test_actor is already added in the list of actors!", result)

    def test_gt_movie_rating_greater_then_other_rating(self):
        movie1 = Movie("Test1", 1983, 5.6)
        movie2 = Movie("Test2", 1983, 2)
        result = movie1 > movie2
        self.assertEqual(f'"Test1" is better than "Test2"', result)

    def test_gt_movie_rating_not_greater_then_other_rating(self):
        movie1 = Movie("Test1", 1983, 5)
        movie2 = Movie("Test2", 1983, 5.1)
        result = movie1 > movie2
        self.assertEqual(f'"Test2" is better than "Test1"', result)

    def test_repr(self):
        movie = Movie("Test1", 1983, 5.6)
        movie.add_actor("actor1")
        movie.add_actor("actor2")
        movie.add_actor("actor3")
        expected = f"Name: Test1\n" \
                   f"Year of Release: 1983\n" \
                   f"Rating: 5.60\n" \
                   f"Cast: actor1, actor2, actor3"
        self.assertEqual(expected, repr(movie))


if __name__ == "__main__":
    main()
