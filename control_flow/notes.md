CONTROL FLOW IN PYTHON

Conditional Statements
These are for decision making. Python normally runs on a top-down flow but with conditional statements, you can make it run specific blocks of code when a condition is satisfied. 
Conditional statements include if,elif and else. More recent addition to the conditional statements list is the Match-Case which behaves like the Switch-case in some other languages.
The if statements executes a block of code (one indented into it) when the condition specified is TRUE. the elif is used to check if a different version of the same condition is true. the else statement executes when none of the previous ifs and elifs are found to be true. When a condition is true, the program ignores the other statements of if, elifs and else as the case may be within the particular if bubble.

LOOPS 
There are two loop statements in python, while and for loop.
The while loop executes a block of code as long as a condition remains true. Excecution only stops on the while loop when the condition that started it no longer holds or a "Break" within the block of code.
The for loop in python executes based on a specified array. The for loop iterates over the elements in the array and executes a block of code on each iteration.

EXCEPTION HANDLING (TRY, EXCEPT, FINALLY)
The try is used to attempt a block of potentially exception causing code, if the code does not run into any exception, the code is run smoothly and the EXCEPT block is ignored, however if an exception is encountered, the EXCEPT block is added to catch the suspecting exception so that the program does not crash. The finally runs irrespective of what happens with the try and except. 

BREAK, CONTINUE, PASS
The break is used to exit the inner-most loop where it is placed even if the loop has not completed it's iterations or the conditions that initiated it has not been changed. the continue is used to ignore the current loop iteration from where it is placed.
The pass is used to usually where a statement is required syntactically but not required in the context of what the programmer wants yet.