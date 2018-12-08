import unittest
import datetime
import numpy as np
import day4 as d4


class TestDay0(unittest.TestCase):
    def test_string_to_datetime(self):
        raw = """[1518-06-15 00:29] falls asleep
[1518-05-25 00:44] wakes up
[1518-11-21 00:00] Guard #3203 begins shift""".split('\n')

        result = d4.parse_entry(raw[0])
        expected = (
            datetime.datetime(year=1518, month=6, day=15, hour=0, minute=29),
            "falls asleep")
        self.assertEqual(result, expected, "Should return (datetime, record)")
        
        
        result = d4.parse_entry(raw[2])
        expected = (
            datetime.datetime(year=1518, month=11, day=21, hour=0, minute=0),
            "Guard #3203 begins shift")
        self.assertEqual(result, expected, "Should return (datetime, record)")
        
    
    def test_sort_by_date(self):
        entries = [
            (
                datetime.datetime(year=1518, month=11, day=21, hour=0, minute=2),
                "wakes up"
            ), 
            (
                datetime.datetime(year=1518, month=11, day=21, hour=0, minute=1),
                "falls asleep"
            ),
            (
                datetime.datetime(year=1518, month=11, day=21, hour=0, minute=0),
                "Guard #3203 begins shift"
            ),
        ]
        
        entries = d4.sort_dates_asc(entries)
        self.assertGreater(entries[2][0], entries[1][0])
        self.assertEqual(entries[0][1], "Guard #3203 begins shift")
        
    
    
    def test_parse_record(self):
        entries = [
            (
                datetime.datetime(year=1518, month=11, day=21, hour=0, minute=0),
                "Guard #3203 begins shift"
            ),
            (
                datetime.datetime(year=1518, month=11, day=21, hour=0, minute=1),
                "falls asleep"
            ),
            (
                datetime.datetime(year=1518, month=11, day=21, hour=0, minute=2),
                "wakes up"
            ),
            (
                datetime.datetime(year=1518, month=11, day=22, hour=0, minute=0),
                "Guard #100 begins shift"
            ),
            (
                datetime.datetime(year=1518, month=11, day=22, hour=0, minute=1),
                "falls asleep"
            ),
            (
                datetime.datetime(year=1518, month=11, day=22, hour=0, minute=2),
                "wakes up"
            ),
        ]
        
        expected = [
            (
                3203,
                datetime.datetime(year=1518, month=11, day=21, hour=0, minute=0),
                "begins shift"
            ),
            (
                3203,
                datetime.datetime(year=1518, month=11, day=21, hour=0, minute=1),
                "falls asleep"
            ),
            (
                3203,
                datetime.datetime(year=1518, month=11, day=21, hour=0, minute=2),
                "wakes up"
            ),
            (
                100,
                datetime.datetime(year=1518, month=11, day=22, hour=0, minute=0),
                "begins shift"
            ),
            (
                100,
                datetime.datetime(year=1518, month=11, day=22, hour=0, minute=1),
                "falls asleep"
            ),
            (
                100,
                datetime.datetime(year=1518, month=11, day=22, hour=0, minute=2),
                "wakes up"
            ),
            
        ]
        
        result = d4.mutate_with_id(entries)
        self.assertEqual(result, expected)
    
    def test_plot_sleep_minutes_with_id(self):
        entries = [
            (
                3203,
                datetime.datetime(year=1518, month=11, day=21, hour=0, minute=0),
                "begins shift"
            ),
            (
                3203,
                datetime.datetime(year=1518, month=11, day=21, hour=0, minute=1),
                "falls asleep"
            ),
            (
                3203,
                datetime.datetime(year=1518, month=11, day=21, hour=0, minute=2),
                "wakes up"
            ),
            (
                100,
                datetime.datetime(year=1518, month=11, day=22, hour=0, minute=0),
                "begins shift"
            ),
            (
                100,
                datetime.datetime(year=1518, month=11, day=22, hour=0, minute=1),
                "falls asleep"
            ),
            (
                100,
                datetime.datetime(year=1518, month=11, day=22, hour=0, minute=2),
                "wakes up"
            ),
        ]
        
        expected = """[[   0 3203    0    0    0    0    0    0    0    0    0    0    0    0
     0    0    0    0    0    0    0    0    0    0    0    0    0    0
     0    0    0    0    0    0    0    0    0    0    0    0    0    0
     0    0    0    0    0    0    0    0    0    0    0    0    0    0
     0    0    0    0]
 [   0  100    0    0    0    0    0    0    0    0    0    0    0    0
     0    0    0    0    0    0    0    0    0    0    0    0    0    0
     0    0    0    0    0    0    0    0    0    0    0    0    0    0
     0    0    0    0    0    0    0    0    0    0    0    0    0    0
     0    0    0    0]]"""
        
        result = d4.plot_sleep_chart(entries)
                
        self.assertEqual(str(result), expected)
                
    
                
        

if __name__ == "__main__":
    unittest.main()