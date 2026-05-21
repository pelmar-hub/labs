from lab_9 import build_transition_table, fsm_search
import unittest

class TestFsmSearch(unittest.TestCase):

    def test_fsm_search(self):
        haystack = "ababcababc"
        needle = "ababc"
        expected_indices = [0, 5]
        

        self.assertEqual(fsm_search(haystack, needle), expected_indices)

if __name__ == "__main__":
    unittest.main()
