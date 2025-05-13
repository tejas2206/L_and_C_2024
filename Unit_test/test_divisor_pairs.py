import unittest
from divisor_pairs import count_same_divisor_pairs


class TestDivisorPairs(unittest.TestCase):

    def test_sample_inputs(self):
        self.assertEqual(count_same_divisor_pairs(3), 1)
        self.assertEqual(count_same_divisor_pairs(15), 2)
        self.assertEqual(count_same_divisor_pairs(100), 15)

    def test_small_ranges(self):
        self.assertEqual(count_same_divisor_pairs(6), 2)
        self.assertEqual(count_same_divisor_pairs(10), 4)

    def test_invalid_lower_limit(self):
        with self.assertRaises(ValueError):
            count_same_divisor_pairs(2)

    def test_large_valid_input(self):
        result = count_same_divisor_pairs(10**6)
        self.assertIsInstance(result, int)
        self.assertGreaterEqual(result, 0)


if __name__ == "__main__":
    unittest.main()
