### turbo-octo-broccoli 
*Randomly generated repo name.  Eat your vegetables.*
___
#### Description:
This small class library is for recording activities and times, and retrieving their averages.
Written in python (version 3.8)
___
#### To install the library:
1. Verify python 3.8 or higher is installed by trying `python` at the command prompt
- If needed, [install python3.8 or higher](https://www.python.org/downloads/)
	- This install should include **pip**, a Python package installer
2. Verify pip is installed (version 21.0.1 for me): 
	- **windows:**`py -m pip --version` or **unix/mac:**`pip --version`
- If needed, [install pip](https://pip.pypa.io/en/stable/installing/)
3. [Install git if needed](https://git-scm.com/downloads) 
4. Install the library:
`pip install git+https://github.com/jham20x6/turbo-octo-broccoli.git@main`
___
#### Usage Example:
*for windows use 'py' instead of 'python3'*
```
python3
>>>import action_tracker as at
>>> my_at = at.ActionTracker()
>>> my_at.addAction('{"action":"jump", "time":200}')
>>> my_at.addAction('{"action":"jump", "time":100}')
>>> my_at.getStats()
'[{"action": "jump", "avg": 150}]'
>>> 
```
#### To uninstall the library:
`pip uninstall jc_ActionsJH`
___
#### Extras:
['test'](https://github.com/jham20x6/turbo-octo-broccoli/tree/main/action_tracker/test) directory in repository has artifacts from testing.
