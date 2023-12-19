# Util Lib
# set_title
Set the title of the command window.
# clr
Clears all of the output of the command window.
# get_args
Get all of the args. Example:
```
// command window
> example.py 1 2 3

// example.py
Util = Utilclass()
print(Util.get_args())

// output
> ["1","2","3"]
```
# get_raw_args
Get alls of the args (raw). Not recommended.
Example:
```
// command window
> example.py 1 2 3

// example.py
Util = Utilclass()
print(Util.get_raw_args())

// output
> ["example.py", "1","2","3"]
```
# wait
Waits for a certain amount of time
# run_command
Runs a command in the command window.
# run_powershell
Runs a powershell command. Returns output (stdout not stderr, and doesnt detect for stdstatus).
# create_file
Just creates a file. If theres already a file at that path it will overwrite it to nothing.
# read_file
Returns the contents of a file.
# write_file
Writes something to a file. Doesnt append, just overwrites.
# append_file
Appends text to a file. No space at the beggining. Just raw appends.
# raw_append_file
Uses an alternitive method to appending. More raw.
