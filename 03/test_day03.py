import unittest
import numpy as np
import day03 as d3


class TestDay3(unittest.TestCase):
    def test_parse_claim(self):
        raw_claim = "#1 @ 287,428: 2x2"
        self.assertEqual(d3.parse_claim(raw_claim), (1, (287, 428), (2, 2)))
        
    
    def test_get_end_point(self):
        start_point = (0, 0)
        size = (3, 4)
        self.assertEqual(d3.get_end_point(start_point, size), (2, 3))
    
    # @unittest.skip
    def test_can_add_claim(self):
        sheet = np.zeros((10,10), dtype=int)
        claim = (1, (1, 3), (4, 6))
        
        claim_id, start_point, (w, h) = claim
        end_point = d3.get_end_point(start_point, (w, h))
        
        x1, y1 = start_point
        x2, y2 = end_point
        
        
        kernel = np.ones((h, w), dtype=int)*4
        sheet[y1:y2+1, x1:x2+1] += kernel
        
        print(sheet)
        
        kernel = np.ones((2, 2), dtype=int)
        sheet[3:5, 1:3] += kernel
        
        # get sum
        sheet[sheet < 2] = 0
        sheet[sheet > 0] = 1
        
        print(np.sum(sheet))
    
    
        


if __name__ == "__main__":
    unittest.main()