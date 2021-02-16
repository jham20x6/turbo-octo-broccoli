'''
Created on Feb 14, 2021

@author: jeff
This test generates addAction threads for each line in the input file.
The averages are matched to the output file.
'''
import simplejson as json
import unittest
import concurrent.futures
from action_tracker.Tracker import ActionTracker


class TestActionTracker3(unittest.TestCase):
    action_tracker = ActionTracker()
    
    def testAddActionWithThreads(self):
        '''
        Open the test input file for reading
        Create a thread pool executor for handling threads and their output
        Starting threads for each input line in the input file
        Verify that each addAction() was successful using future.result()
        '''
        with open("test3input.txt") as f:    
            with concurrent.futures.ThreadPoolExecutor() as executor:
                future_add_actions = {executor.submit(self.action_tracker.addAction,line): line for line in f}
                for future in concurrent.futures.as_completed(future_add_actions):
                    self.assertEqual(future.result(), None, "addAction() Failed")
        
    def testGetStatsWithThreads(self):
        '''
        Open the test input file for reading
        Only one thread is needed, however ThreadPoolExecutor allows for returned value in .result()
        Starting threads for each input line in the input file
        Verify that the getStats() call was successful
        '''
        with open("test3output.txt") as f:
            with concurrent.futures.ThreadPoolExecutor() as executor:    
                future_add_actions = {executor.submit(self.action_tracker.getStats)}
                for future in concurrent.futures.as_completed(future_add_actions):
                    formatted_line = json.dumps(json.loads(f.readline()))
                    self.assertEqual(future.result(), formatted_line, "getStats() Failed")
                
                
    