'''
Created on Feb 14, 2021

@author: jeff
This test runs through a slightly larger set of input, reading from file.
The main purpose here is handling more than just the 2 actions given in the default input.
'''
import simplejson as json
import unittest
from action_tracker.Tracker import ActionTracker


class TestActionTracker2(unittest.TestCase):
    action_tracker = ActionTracker()

    def testAddActionWithFileInput(self):  
        '''
        Open the test input file for reading
        Call addAction for each line
        Verify that each addAction() was successful
        '''    
        with open("test2input.txt") as f:
            for line in f:
                result = self.action_tracker.addAction(json_string=line)
                self.assertEqual(result,None,"addAction() Failed")
    
    def testGetStatsWithFileInput(self):
        '''
        Verify that the results from getStats() call matches line in the output file
        json.loads and json.dumps ensures the same format/whitespace
        '''
        with open("test2output.txt") as f:
                self.assertEqual(json.dumps(json.loads(f.readline())), self.action_tracker.getStats(), "getStats() Failed")
