import unittest
import inventory_management as ims


class TestNumber2(unittest.TestCase):
    def test_get_count_abcdef_counts_0_0(self):
        id = "abcdef"
        self.assertEqual(ims.get_count(id), (0, 0), "Should not find any doubles or triples.")
    
    def test_get_count_abbcde_counts_1_0(self):
        id = "abbcde"
        self.assertEqual(ims.get_count(id), (1, 0), "Should find one double")
    
    
    def test_get_count_bababc_counts_1_1(self):
        id = "bababc"
        self.assertEqual(ims.get_count(id), (1, 1), "Should count for both")
        
    
    def test_get_count_aabcdd_counts_only_once(self):
        id = "aabcdd"
        self.assertEqual(ims.get_count(id), (1, 0), "Should count double only once")
    
    
    def test_get_diffs_no_diff(self):
        id1 = "abcdef"
        id2 = "abcdef"
        self.assertEqual(ims.get_diffs(id1, id2), [0, 0, 0, 0, 0, 0], "Should give no diffs.")
    
    
    def test_get_diffs_all_diff(self):
        id1 = "abcdef"
        id2 = "ghijkl"
        self.assertEqual(ims.get_diffs(id1, id2), [1, 1, 1, 1, 1, 1], "Should give all diffs.")


if __name__ == "__main__":
    unittest.main()