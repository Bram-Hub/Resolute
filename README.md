# Resolute
GUI for Resolution Problem Solving

### Instructions
#### Windows:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Download and run ```resolute.exe```\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Note: If exe doesn't run correctly, download the respository and run in command prompt by navigating to the correct directory, and running ```python resolute.py```

#### Linux:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Run the shell script in ```compile.sh```

#### Mac:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Run the executable

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
