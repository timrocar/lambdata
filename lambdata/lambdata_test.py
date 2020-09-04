""" Basic unit tests for Lambdata Package."""

import unittest
from random import randint
from example_module import increment, colors
from oop_examples import SocialMediaUser

class ExampleTests(unittest.TestCase):
    """Making sure examples work as expected."""
    def test_increment(self):
        """Testing that increment adds one to a number"""
        x0 = 0
        y0 = increment(x0)
        self.assertEqual(y0, 1)
        x1 = 123
        y1 = increment(x1)
        self.assertEqual(y1, 124)
        x2 = -57
        y2 = increment(x2)
        self.assertEqual(y2, -56)

    def test_increment_random(self):
        """Testing the increment function adds 1 to any number 1-1000)"""
        x0 = randint(1,1000)
        y0 = increment(x0)
        self.assertEqual(x0 +1, y0)

    def test_favorite_colors(self):
        """Testing presence/absence of members of collections."""
        self.assertIn('tan', colors)
        self.assertNotIn('auburn', colors)

    def test_number_colors(self):
        """Testing that we have the expected number of colors"""
        self.assertEqual(len(colors), 5)

    def test_the_same_or_not(self):
        """Testing if two variables are the same"""
        self.assertIs(1, (1/1))

class SocialMediaUserTests(unittest.TestCase):
    """Tests the usage of SocialMediaUser."""
    def setUp(self):
        """Common setup code run before all tests."""
        self.user1 = SocialMediaUser('Jane', 'Denmark')
        self.user2 = SocialMediaUser('Joe', 'Russia')
    
    def test_name(self):
        """Testing that naming is defined correctly"""
        self.assertEqual(self.user2.name, 'Joe')
        self.assertEqual(self.user1.name, 'Jane')

    def test_location(self):
        """Tests that the location is defined correctly"""
        self.assertEqual(self.user2.location, 'Russia')
        self.assertEqual(self.user1.location, 'Denmark')

    def test_default_upvotes(self):
        """Tests that the default upvote value is 0"""
        new_user = SocialMediaUser('Mary', 'Spain')
        self.assertEqual(new_user.upvotes, 0)

    def test_unpopular(self):
        """Test that a user with <= 100 upvotes is not popular."""
        new_user = SocialMediaUser('Tim', 'US')
        self.assertFalse(new_user.is_popular())
        for _ in range(randint(1, 100)):
            self.assertFalse(new_user.is_popular())

    def test_popular(self):
        """Test that a user with >100 upvotes is popular."""
        new_user = SocialMediaUser('Jack', 'US')
        for _ in range(randint(101, 10000)):
            new_user.receive_upvote()
        self.assertTrue(new_user.is_popular())




if __name__ == '__main__':
    unittest.main()