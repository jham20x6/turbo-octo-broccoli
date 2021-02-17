### turbo-octo-broccoli 
*Randomly generated repo name.  Eat your vegetables.*

This small class library is for recording activities and times, and retreiving their averages.
Written in python (version 3.8)
##### To install the library:
`pip install git+https://github.com/jham20x6/turbo-octo-broccoli.git@main`

##### Usage:

```
python
>>>import action_tracker as at
>>> my_at = at.ActionTracker()
>>> my_at.addAction('{"action":"jump", "time":200}')
>>> my_at.addAction('{"action":"jump", "time":100}')
>>> my_at.getStats()
'[{"action": "jump", "avg": 150}]'
>>> 
```

##### Extras:
'test' directory in repository has artifacts from testing.
