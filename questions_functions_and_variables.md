# Questions for Functions and Variables
These are questions on functions and variables.

## Indoor Voice
WRITING IN ALL CAPS IS LIKE YELLING.

Best to use your “indoor voice” sometimes, writing entirely in lowercase.

In a file called indoor.py, implement a program in Python that 

prompts the user for input and then outputs that same input in lowercase.

Punctuation and whitespace should be outputted unchanged. 

You’re welcome, but not required, to prompt the user explicitly, 

as by passing a str of your own as an argument to input.

### Concept learned
str.lower() Return a copy of the string with all the cased characters converted 

to lowercase.

## Playback Speed
Some people have a habit of lecturing speaking rather quickly, 

and it’d be nice to slow them down, a la YouTube’s 0.75 playback speed,

or even by having them pause between words.

In a file called playback.py, implement a program in Python that prompts the user 

for input 

and then outputs that same input, replacing each space with ... (i.e., three periods).

### Concept Learned
str.replace(old, new, /, count=-1) Return a copy of the string with all occurrences of 

substring old replaced by new. 

If count is given, only the first count occurrences are replaced. 

If count is not specified or -1, then all occurrences are replaced.

## Making Faces
Before there were emoji, there were emoticons, whereby text like :) was a happy face 

and text like :( was a sad face. Nowadays, programs tend to convert emoticons to 

emoji automatically!

In a file called faces.py, implement a function called convert that accepts a str as 

input and returns that same input with any :) converted to 🙂 

(otherwise known as a slightly smiling face) and any :( converted to 🙁

(otherwise known as a slightly frowning face). All other text should be returned 

unchanged.

Then, in that same file, implement a function called main that prompts the user 

for input, calls convert on that input, and prints the result. 

You’re welcome, but not required, to prompt the user explicitly, 

as by passing a str of your own as an argument to input. 

Be sure to call main at the bottom of your file.


### Concept Learned
str.replace(old, new, /, count=-1) Return a copy of the string with all occurrences of 

substring old replaced by new. 

If count is given, only the first count occurrences are replaced. 

If count is not specified or -1, then all occurrences are replaced.


## Einstein
Even if you haven’t studied physics (recently or ever!), 

you might have heard that 𝐸 =𝑚𝑐2, 

wherein 𝐸 represents energy (measured in Joules), 

𝑚 represents mass (measured in kilograms), 

and 𝑐 represents the speed of light (measured approximately as 300000000 meters 

per second), per Albert Einstein et al. 

Essentially, the formula means that mass and energy are equivalent.

In a file called einstein.py, implement a program in Python that prompts 

the user for mass as an integer (in kilograms) and then outputs the 

equivalent number of Joules as an integer. 

Assume that the user will input an integer.
