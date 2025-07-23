import unittest
from bowling_score import bowling_score

class TestBowlingScore(unittest.TestCase):

    def test_all_gutter(self):
        rolls = [0] * 20
        score, _, _ = bowling_score(rolls)
        self.assertEqual(score, 0)

    def test_all_ones(self):
        rolls = [1] * 20
        score, _, _ = bowling_score(rolls)
        self.assertEqual(score, 20)

    def test_perfect_game(self):
        rolls = [10] * 12
        score, _, _ = bowling_score(rolls)
        self.assertEqual(score, 300)

    def test_all_spares(self):
        rolls = [9,1] * 10 + [9]  # 10 Spares + Bonuswurf 9
        score, _, _ = bowling_score(rolls)
        self.assertEqual(score, 190)

    def test_strike_in_last_frame(self):
        rolls = [0]*18 + [10, 5, 3]
        score, _, _ = bowling_score(rolls)
        self.assertEqual(score, 18)
    
    def test_strike_in_last_frame(self):
        rolls = [10] * 9 + [10, 5, 3]
        score, _, _ = bowling_score(rolls)
        self.assertEqual(score, 273)

    def test_mixed_game(self):
        rolls = [10, 5, 5, 3, 9, 1, 10, 10, 2, 8, 6]
        score, _, _ = bowling_score(rolls)
        self.assertEqual(score, 194)                

    def test_spare_in_last_frame(self):
        rolls = [0]*18 + [9, 1, 5]
        score, _, _ = bowling_score(rolls)
        self.assertEqual(score, 15)

    def test_random_game(self):
        rolls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        score, _, _ = bowling_score(rolls)
        self.assertEqual(score, 70)

    def test_invalid_rolls(self):
        rolls = [10, 5, 3]
        with self.assertRaises(ValueError):
            bowling_score(rolls)    

    def test_too_many_rolls(self):
        rolls = [1] * 21    
        with self.assertRaises(ValueError):
            bowling_score(rolls)                

if __name__ == '__main__':
    unittest.main()
