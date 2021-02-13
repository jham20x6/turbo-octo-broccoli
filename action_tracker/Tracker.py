import simplejson as json

class ActionTracker(object):

    def __init__(self):
        self.actions = {}
        #Format of input JSON string {"action":"jump", "time":100}
        #TODO: add a check for this format
  
    def addAction(self, jsonString):
        #Check if string is valid JSON.  parsedObj is populated if successful)
        try:
            #validate JSON format via json.loads
            #store object on success or return error
            parsedObj = json.loads(jsonString)
            #TODO: Verify that format here. We at least need action and time as first two items            
            actionKey = parsedObj['action']
            
            if actionKey in self.actions:
                #Increment existing action times by the new time field
                self.actions[actionKey]['total_time'] += parsedObj['time']
                self.actions[actionKey]['count'] += 1
            else:
                #Add any new action
                #Action dictionary format { action : { total_time: t,  count: c } }
                self.actions[actionKey] = { "total_time":parsedObj['time'],"count":1 }

        except ValueError as e:
            #return the error from the failed json.loads() attempt
            return(e)

    def getStats(self):
        #Format of output needs to be list of actions and average times.
        #example: [ {"action": "action1", "avg": 10}, {"action": "action2", "avg": 20 } ]
        activityStats = []
        for actionKey in self.actions:
            #build dictionary pairs for the output
            #Assumption: Average needs to only be in whole numbers, type cast as int
            activityStats.append({"action": actionKey, "avg" : (int(self.actions[actionKey]['total_time'] / self.actions[actionKey]['count'])) })
        return json.dumps(activityStats)
