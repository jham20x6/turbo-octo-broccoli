'''
Created on Feb 13, 2021

@author: jeff
This test runs through the default input and output provided from the assignment prompt.
3 JSON serialized strings as input:
{"action":"jump", "time":100}
{"action":"run", "time":75}
{"action":"jump", "time":200}

One JSON serialized string as output:
[
    {"action":"jump", "avg":150},
    {"action":"run", "avg":75}
]
'''
import unittest
from action_tracker.Tracker import ActionTracker

class TestActionTracker(unittest.TestCase):
    
    action_tracker = ActionTracker()
    
    def testAddAction(self):
        
        result = self.action_tracker.addAction(json_string='{"action":"jump", "time":100}')
        self.assertEqual(result, None, "Add Action Failed")
        result = self.action_tracker.addAction(json_string='{"action":"run", "time":75}')
        self.assertEqual(result, None, "Add Action Failed")
        result = self.action_tracker.addAction(json_string='{"action":"jump", "time":200}')
        self.assertEqual(result, None,"Add Action Failed")
                
    def testGetStats(self):
        result = self.action_tracker.getStats()
        self.assertEqual(result,'[{"action": "jump", "avg": 150}, {"action": "run", "avg": 75}]',"GetStats() Failed")
        