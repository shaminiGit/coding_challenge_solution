# coding_challenge_solution
Insight Data Engineering Coding Challenge

##Approach and Thought-Process:

I tried solving it using basic python data structures as well as numoy and pandas. The later helped me to verify if the former answers right.
Given the time limit I couldn't make it look aesthetic in a csv so I tried printing the output in text file. 

I tried nesting three dictionaries with "year", "product" and "Company" as their keys respectively. Sicne the dictionaries keys where not linked as in a nested Hashmap in java , I went along with the following solution.

Step 1: I tried to read the csv and format it. I also selected the columns that are necessary to solve the problem </br>
Step 2: Then I created a tuple pair of 'year' and 'product" and created a set out of it which will act as a refernce(more like cache) in the future.
Step 3: I added the tuple pair as key(so that I can add the companies belonging to THAT key as values in a dictionary
Step 4: After adding the companies as values, I tried to create a counter using collections module so that I can add and find the neccessary values.

##Future Wrok:
The code can be further improvised in terms of space and time complexity.

