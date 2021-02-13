'''
Created on Feb 13, 2021

@author: jeff
'''
import unittest
from action_tracker.Tracker import ActionTracker

class TestActionTracker(unittest.TestCase):
    
    action_tracker = ActionTracker()
    
    def testAddAction(self):
        
        result = self.action_tracker.addAction(jsonString='{"action":"jump", "time":100}')
        self.assertEqual(result, None, "Add Action Failed")
        result = self.action_tracker.addAction(jsonString='{"action":"run", "time":75}')
        self.assertEqual(result, None, "Add Action Failed")
        result = self.action_tracker.addAction(jsonString='{"action":"jump", "time":200}')
        self.assertEqual(result, None,"Add Action Failed")
        
    def testAddActionValueError(self):
        
        with self.assertRaises(ValueError): 
            self.action_tracker.addAction(jsonString='{"action":"jump", "time"-200}')
                
        