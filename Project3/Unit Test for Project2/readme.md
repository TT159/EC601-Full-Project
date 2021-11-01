# Project 3 Unit Test Case
In each projcect, test process is really significant. This is the part of python unit test example for Project2. 
## My Test
In project 2, we try to develop an application in which user can search specific Twitter ID to get corresponding tweets. Then user can also evaluate the emotion of these tweets. In this case, we focus on the search tweets function which is the most important function of this application. If this function does not work, we can not continue any subprocess. I have create two unit test cases for two simple user cases and I believe that they must be a part of the application development process.</br>
For comparison, I also upload the result of the correct user operation. 

### First example
We try to test that what if the user enter two Twitter IDs together at one time with the test_two_TwitterIDs.py.</br>
We expect that the program to report an error because all searched tweets will be sorted in a JSON file, and we only allow one Twitter ID to be searched at a time for ease of differentiation.  

### Second example
In test_wrong_TwitterIDs.py, we try to test that what if the user enter the wrong Twitter ID which is not exist or the user input nothing.</br>
We ecpect that the program to report an error that it can not found the ID.



