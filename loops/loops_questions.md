<!-- markdownlint-disable -->
# questions on loops

## Camel Case

In some languages, it’s common to use camel case (otherwise known as “mixed case”) for variables’ names when those names comprise multiple words, whereby the first letter of the first word is lowercase but the first letter of each subsequent word is uppercase. For instance, whereas a variable for a user’s name might be called name, a variable for a user’s first name might be called firstName, and a variable for a user’s preferred first name (e.g., nickname) might be called preferredFirstName.

Python, by contrast, recommends snake case, whereby words are instead separated by underscores (_), with all letters in lowercase. For instance, those same variables would be called name, first_name, and preferred_first_name, respectively, in Python.

In a file called camel.py, implement a program that prompts the user for the name of a variable in camel case and outputs the corresponding name in snake case. Assume that the user’s input will indeed be in camel case.

Tests:
Input and Output
(o)camelCase: (i)name
(o)snake_case: (o)name

(o)camelCase: (i)firstName
(o)snake_case: (i)first_name

(o)camelCase: (i)preferredFirstName
(o)snake_case: (i)preferred_first_name

### Concepts Learned
    str.isupper()
Return True if all cased characters in the string are uppercase and there is at least one cased character, False otherwise.

    'BANANA'.isupper()

    'banana'.isupper()

    'baNana'.isupper()

    ' '.isupper()
Much like a list, a str is “iterable,” which means you can iterate over each of its characters in a loop. For instance, if s is a str, you could print each of its characters, one at a time, with code like:
    for c in s:
        print(c, end="")


## Coke Machine
Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.

In a file called coke.py, implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due. Once the user has inputted at least 50 cents, output how many cents in change the user is owed. Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.

Tests:
Input and Output
(o)Amount Due: (o)50
(o)Insert Coin: (i)25
(o)Amount Due: (o)25
(o)Insert Coin: (i)25
(o)Change Owed: (0)0



### Concepts Learned
while loop


## Just Setting up My Twttr
When texting or tweeting, it’s not uncommon to shorten words to save time or space, as by omitting vowels, much like Twitter was originally called twttr. In a file called twttr.py, implement a program that prompts the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.

Tests:
Input and Output
(o)Input: (i)Twiter
(o)Output: (o)Twttr

(o)Input: (i)What's your name?
(o)Output: (o)Wht's yr nm?

(o)Input: (i)CS50
(o)Output: (o)CS50
### Concepts Learned:
str.replace()


## Vanity Plates
In Massachusetts, home to Harvard University, it’s possible to request a vanity license plate for your car, with your choice of letters and numbers instead of random ones. Among the requirements, though, are:

+ “All vanity plates must start with at least two letters.”
+ “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
+ “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
+ “No periods, spaces, or punctuation marks are allowed.”

In plates.py, implement a program that prompts the user for a vanity plate and then output Valid if meets all of the requirements or Invalid if it does not. Assume that any letters in the user’s input will be uppercase. Structure your program per the below, wherein is_valid returns True if s meets all requirements and False if it does not. Assume that s will be a str. You’re welcome to implement additional functions for is_valid to call (e.g., one function per requirement).

    def main():
        plate = input("Plate: ")
        if is_valid(plate):
            print("Valid")
        else:
            print("Invalid")


    def is_valid(s):
        ...


    main()
Tests:
Input and Output:
(o) Plate: (i) HELLO
(o) Valid

(o) Plate: (i) GOODBYE 
(o) invalid

(o) Plate: (i) CS50
(o) Valid


### Concepts Learned:


## Nutrition Facts
The U.S. Food & Drug Adminstration (FDA) offers downloadable/printable posters that “show nutrition information for the 20 most frequently consumed raw fruits … in the United States. Retail stores are welcome to download the posters, print, display and/or distribute them to consumers in close proximity to the relevant foods in the stores.”

In a file called nutrition.py, implement a program that prompts consumers users to input a fruit (case-insensitively) and then outputs the number of calories in one portion of that fruit, per the FDA’s poster for fruits, which is also available as text. Capitalization aside, assume that users will input fruits exactly as written in the poster (e.g., strawberries, not strawberry). Ignore any input that isn’t a fruit.

Tests:
Input and Output:
(o) Item: (i) apple
(o) Calories: (o) 130

(o) Item: (i) banana 
(o) Calories: (o) 110

(o) Item: (i) chocolate 
(o) Calories: (o)




### Concepts Learned:


