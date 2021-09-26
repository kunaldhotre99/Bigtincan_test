
# Bigtincan technical assessment

The code takes in the user id and returns the  details of all subordinates of the given user. The function getSubOrdinates() takes in single argument i.e. userID and processes data (users and roles) to return subordinates of the
 in the hierarchy userID entered. test_SubordinateModule.py performs unit testing on the getSubOrdinates(userID) function. 
 


## Tech Stack

**programming language:** Python 3.9

**Editor:** Sublime text 4

  
## Running file and unit tests

To run SubordinateModule.py, run the following command in command prompt. 
First uncomment the print(getSubOrdinates(userID)) at the bottom of the file and save the file to print the output on the terminal.

```bash
  python SubordinateModule.py
```

To run test_SubordinateModule.py, run the following command in command prompt

```bash
  python test_SubordinateModule.py
```

The tests can also be run using text editors like Sublime text 4. Edit the **python.exe file path** in the code below to your own python path on your own PC and save
the file with a .sublime-build extension. Select this build to run test_SubordinateModule.py and SubordinateModule.py in sublime text 4 editor.
```bash
{
	//"shell_cmd": "make"
	"cmd": ["python.exe file path", "-u", "$file"],
    "file_regex": "^[ ]*File \"(...*?)\", line ([0-9]*)",
    "selector": "source.python"
}
```
