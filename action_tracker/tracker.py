import simplejson as json
import threading

class ActionTracker(object):

    def __init__(self):
        '''
        Lock to later ensure 'self' data is multithreading-safe
        Dictionary for actions, format given below in addAction
        '''
        self.lock = threading.Lock()
        self.actions = {}
  
    def addAction(self, json_string):
        '''
        Validate JSON format via json.loads
        Store the parsed_object on success, or return error
        Format of input json_string is {"action":"jump", "time":100}
        Acquire lock when accessing 'self' data
        Increment existing action times by the new time
        Add any new action, format: { action_key : { total_time: #,  count: # } }
        Release lock when done accessing 'self' data
        Return the error from the failed json.loads() attempt
        '''
        try:
            parsed_object = json.loads(json_string)
            if (isinstance(parsed_object['action'],str) and isinstance(parsed_object['time'],int)):   
                action_key = parsed_object['action']        
                self.lock.acquire()
                if action_key in self.actions:
                    self.actions[action_key]['total_time'] += parsed_object['time']
                    self.actions[action_key]['count'] += 1
                else:
                    self.actions[action_key] = { "total_time": parsed_object['time'], "count":1 }
                self.lock.release()
            else:
                return("Error: Invalid Data")
        except ValueError as e:
            return(e)

    def getStats(self):
        '''
        Format of output needs to be JSON serialized list of actions and average times.
        Example: [ {"action": "action1", "avg": 10}, {"action": "action2", "avg": 20 } ]
        Acquire lock when accessing 'self' data
        Build dictionary pairs for each action
        Assumption: Average needs to only be in whole numbers, so use round() 
        Release lock when done accessing 'self' data
        Return JSON serialized results with json.dumps
        '''
        action_stats = []
        self.lock.acquire()
        for action_key in self.actions:       
            action_stats.append({"action": action_key, "avg" : (round(self.actions[action_key]['total_time'] / self.actions[action_key]['count'])) })
        self.lock.release()
        return (json.dumps(action_stats))
