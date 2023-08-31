# WorkEarly_Real_World_Asignment

## The initial problem:
--The HR department asked for an easy way to organize employee data. The idea is to store each person's data in a separate 
file named after them so they can be easily found and retrieved. 

### Task 1
--Please create a python routine that generates a '.txt' file for each employee named after him.

--Sample input
employee_list = ["Jasen_Kerluke", "Lazlo_Daniel", "Amparo_Schuster", "Tia_Kunde",  "Alana_Lueilwitz", "Tia_Mraz", "Lazlo_Metz", "Caroline_Pollich", "Aiyana_Weber", "Lazlo_Rolfson"]
 
--Sample output: Jasen_Kerluke.txt, Lazlo_Daniel.txt, Amparo_Schuster.txt (files should be created in the filesystem)


## Additional request made by HR
--Out of curiosity, HR would like to discover which are the 5 most frequent first names on this list.

### Task 2
--Please print out top 5 frequent first names and the respective frequency.

--Sample input (emplyee_list) - already provided above
--Sample output: Jasen: 7, Lazlo: 4, Amparo: 3, Tia: 1, Lazlo: 1



## Further requirement
--They would also like to organize these files in a intuitive way, and group them in folders according to the first letter of each person's firstname.

### Task 3
--Please create a folder for each letter and move the previously created files in the respective folder according to the person's firstname. For example, "Jasen_Kerluke" should be moved to folder "J".

--Sample input (employee_list) - already provided above
--Sample output: J/Jasen_Kerluke.txt (folders should be created in the filesystem and .txt files should be moved / copied inside the respective folder)
##NOTE: folders usually do not appear in the filesystem when they do not contain any files / objects
