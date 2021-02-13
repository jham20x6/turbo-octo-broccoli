import simplejson as json

class ActionTracker(object):

    def __init__(self):
        self.actions = {}
        #Action dictionary format { action : [ total_time, count ] }
        #             for example { "jog"  : [ 300, 5 ] }
        self.parsedObj = {}
        #Format of JSON serialized string {"action":"jump", "time":100}
        #TODO: add a check for this format as well as proper json syntax
        self.parsingError = ""
 
    #validate JSON format via json.loads
    #store either the parsed Object or the error to be returned later
    def is_valid_json(self, jsonString):
        try:
            self.parsedObj = json.loads(jsonString)
            return True
        except ValueError as e:
            self.parsingError = e
            return False
        
    def addAction(self, jsonString):
        #Check if string is valid JSON.  self.parsedObj is populated if successful)
        if self.is_valid_json(jsonString):
            
            #Average will later be calculated by the total time field divided by the count field.
            actionKey = self.parsedObj['action']
            if actionKey in self.actions:
                #Increment existing action times by the new time field
                #self.actions[actionKey][0] = self.actions.get(actionKey)[0] + self.parsedObj['time']
                #self.actions[actionKey][1] = self.actions.get(actionKey)[1] + 1
                self.actions[actionKey][0] += self.parsedObj['time']
                self.actions[actionKey][1] += 1
            else:
                #Add new actions to the ActivityAverages list
                self.actions[actionKey] = [self.parsedObj['time'],1]

        else:
            #return the error from the failed json.loads() attempt
            return(self.parsingError)

    def getStats(self):
        activityStats = []
        for actionKey in self.actions:
            #build dictionary pairs for the output
            #Assumption: Average needs to only be in whole numbers, type cast as int
            activityStats.append({"action": actionKey, "avg" : (int(self.actions[actionKey][0] / self.actions[actionKey][1])) })
        return json.dumps(activityStats)
