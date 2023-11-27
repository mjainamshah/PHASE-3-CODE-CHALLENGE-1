# PHASE-3-CODE-CHALLENGE-1

#### TOY PROBLEMS | (27/11/2023)

#### **CREATED BY JAINAM SHAH**

## Learning Goals
    - Build a React single page application from scratch
    - Apply your knowledge of components, props and state management
    - Design and architect features across a frontend
    - Communicate and collaborate in a technical environment
    - IntegrateJSON/API
    - Incorporate client-side routing 
    - Learn how to integrate Bootstrap
    - Debug any issues

## Project Description
    A product catalogue!

## Requirements
    - You must make a single page application (only one index.html file) using create-react-app
    - Your app should use at least 5 components/6 pages in a way that keeps your code well organized
    - There should be at least 3 client-side routes using react-routerLinks to an external site.
  

## Setup/Installation Requirements
    - Download zip in the code section of github to your desired folder on your device
    - Extract the files
    - Open the folder with vs code.
    - In the terminal run pipenv install & pipenv shell to get the neccesary depencies & python files installed.
    - Your application is running! Ready to go!
    
## Features
    - CHALLENGE 1: Converting 12-hour time to 24-hour time
    - CHALLENGE 2: Two numbers are positive.
    - CHALLENGE 3: Consonant values

## Challenge 1: Converting 12-hour time to 24-hour time
    - Converting a 12-hour time like "8:30 am" or "8:30 pm" to 24-hour time (like "0830" or "2030") sounds easy enough, right? Well, let's see if you can do it!
    - You will have to define a function, which will be given an hour (always in the range of 1 to 12, inclusive), a minute (always in the range of 0 to 59, inclusive), and a period (either "am" or "pm") as input.
    - Your task is to return a four-digit string that encodes that time in 24-hour time.
    **NOTES:**
    - By convention, noon is 12:00 pm, and midnight is 12:00 am.
    - On 12-hours clock, there is no 0 hour, and time just after midnight is denoted as, for example, 12:15 am. On 24-hour clock, this translates to 0015. 

 ## Challenge 2: Two numbers are positive
    - Your job is to write a function, which takes three integers a, b, and c as arguments, and returns True if exactly two of of the three integers are positive numbers (greater than zero), and False - otherwise.
    **EXAMPLES:**
    - (2, 4, -3) == True
    - (-4, 6, 8) == True
    - (4, -6, 9) == True
    - (-4, 6, 0) == False
    - (4, 6, 10) == False
    - (-14, -3, -4) == False

 ## Challenge 3: Consonant value
    - Given a lowercase string that has alphabetic characters only and no spaces, return the highest value of consonant substrings. Consonants are any letters of the alphabet except "aeiou".We shall assign the following values: a = 1, b = 2, c = 3, .... z = 26.
    **EXAMPLES:**
    - For the word "zodiacs", solve("zodiacs") = 26
    - For example, for the word "zodiacs", let's cross out the vowels. We get: "z d cs"
    - The consonant substrings are: "z", "d" and "cs" and the values are z = 26, d = 4 and cs = 3 + 19 = 22. The highest is 26.
    - For the word "strength", solve("strength") = 57.
    - The consonant substrings are: "str" and "ngth" with values "str" = 19 + 20 + 18 = 57 and "ngth" = 14 + 7 + 20 + 8 = 49. The highest is 57.
    
## Known Bugs
    All challenges working in order, no issues.

## Technologies used
    - PYTHON
    
## Support and contact details
    - email :: mjainamshah@gmail.com
    - phone :: +254721282868

### License
    *Licenced under the MIT Licence
    Copyright (c) 2023 **JAINAM SHAH**
