# Resolute
GUI for Resolution Problem Solving

### Instructions
#### Windows:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Run ```resolute.exe```\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Note: If the executable doesn't run correctly, run ```python resolute.py``` in command prompt

#### Linux:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Run the shell script in ```compile.sh```

#### Mac:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Download the Mac app and run\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Note: If this doesn't work, run ```python resolute.py``` in the terminal

Use the "Add Sentence" button to add the required number of sentences, and "Remove Sentence" to remove a sentence.\
Enter the sentences. The following symbols can be used:\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```v``` - disjunction (logical or)\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```^``` - conjunction (logical and)\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```->``` - conditional (implies)\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```<->``` - biconditional (if and only if)\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```~``` - negation\
Make sure to enter the negation of the conclusion in the "Therefore" sentence (at the bottom, with the therefore symbol).

When finished entering the sentences, press the ```Solve``` button, and your resolution graph will appear.

The ```File``` menu has ```Save``` and ```Open``` options, where the current file can be saved as a ```.reso``` file and reopened.

Example:\
![Example](https://github.com/matthewyoungbar/Resolute/blob/main/img/Example.png?raw=true)
