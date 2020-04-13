# coding_challenge_solution
Insight Data Engineering Coding Challenge

#Approach and Thought-Process:

I tried solving it using basic python data structures.  </br>

I tried nesting three dictionaries with "year", "product" and "Company" as their keys respectively. Since the dictionaries keys where not linked as in a nested Hashmap in java , I went along with the following solution. </br>

Step 1: I tried to read the csv and format it. I also selected the columns that are necessary to solve the problem. I sorted the list first by product and then by year</br>
Step 2: Then I created a tuple pair of 'year' and 'product" and created a set out of it which will act as a refernce(more like cache) in the future. </br>
Step 3: I added the tuple pair as key(so that I can add the companies belonging to THAT key as values in a dictionary</br>
Step 4: After adding the companies as values, I tried to create a counter using collections module so that I can add and find the neccessary values.</br>
Step 5: I wrote each output list as I created into a CSV.

