import unittest
import os

from chronal_calibration import Helpers, ChronalCalibrator


class TestChronalCalibration(unittest.TestCase):

    def setUp(self):
        self.calibrator = ChronalCalibrator()
    
    def test_file_to_list(self):
        calibrations = [1, 2, 3]
        
        # write to file
        test_file = "input_test.txt"
        f = open(test_file, "w")
        for calib in calibrations:
            f.write(f"{calib}\n")
        f.close()
        
        self.assertEqual(Helpers.file_to_list(test_file), [1, 2, 3], "Should convert file to list.")
        
        if os.path.exists(test_file):
            os.remove(test_file)

    def test_frequency_set_to_0(self):
        self.assertEqual(self.calibrator.frequency, 0, "Should be set initially to 0.")
    
    
    def test_frequency_adjusted_single_calibration(self):
        self.calibrator.adjust(3)
        self.assertEqual(self.calibrator.frequency, 3, "Should adjust with single arg.")
    
    
    def test_frequency_adjusted_list(self):
        self.calibrator.adjust(*[1, 2, 3])
        self.assertEqual(self.calibrator.frequency, 6, "Should adjust with splatted list as argument.")
    

    def test_frequency_adjustments_added_to_adjustments_list(self):
        self.calibrator.adjust(1, 2, -2, -3, 4)
        self.assertEqual(self.calibrator.adjustments, [1, 2, -2, -3, 4], "Should add each adjustment to list.")

    
    def test_frequency_log(self):
        # results                1  2   1  2  3
        self.calibrator.adjust(*[1, 1, -1, 1, 1])
        self.assertEqual(self.calibrator.log[1], 2, "Should update log when adjustment is made.")
    
    
    def test_get_first_repeated_once_through2(self):
        # result   1  2  3  4   2  3
        changes = [1, 1, 1, 1, -2, 1]
        self.calibrator.adjust(*changes)
        self.assertEqual(self.calibrator.get_first_repeated(), 2, "Should get first repeated once through (2).")
        
    
    def test_get_first_repeated__twice_through(self):
        # result   2  6   4
        #          6
        changes = [2, 4, -2]
        self.calibrator.adjust(*changes)
        self.assertEqual(self.calibrator.get_first_repeated(), 6, "Should loop through change list.")

if __name__ == "__main__":
    unittest.main()
