# Data-Generator
This code is to generate random dataset of **Bangladeshi people's profile**. A few attributes were considered like a person's NID, 
name (first-name, middle name, last name), father's name (first-name, middle name, last name), mother's name (first-name, middle name, 
last name), present address (house number, street, ward number, area, thana (Police Station), city, district, division) for people 
living in cities, present address ( ward number, village, thana (Police Station), district, division) for people living in villages, 
permanent address (house number, street, ward number, area, thana, city, district, division) for people living in cities, permanent 
address ( ward number, village, thana (Police Station), district, division) for people living in villages, date of birth, profession,
mobile, email if any, marital status, gender, place of birth, Passport number if any, TIN number if any, height, weight, emergency contact 
person (name as above, address as above, mobile and email), income, asset, tax, educational qualification (SSC, HSC, graduation,
post graduation, PhD).

## Procedure
First, a list of Bangladeshi people's names (in names1.csv file) were collected from the internet. All the names were fragmented to 
single names. Then different tags were assigned to each of them based on whether the name is a male or female name (gender), whether it 
is a Muslim, or other religion's name and whether it is a first, middle or last name (Positioning). Tags were used to generate more 
realistic names randomly. Total number of 350,000 random unique names (2 and 3 word length) were generated from roughly 800 single 
names. Their gender, religion were also generated based on their names. Similarly, three other names, mother's name, father's name,
emergency contact person's name were generated for each person. Attributes like NID number, Passport number, phone number, Tax 
Identification Number (TIN) were randomly generated as sequence of characters or numbers. Profession was generated based on a
person's age from a specified list in the program with corresponding income range. Random number between the income ranges 
assigned as their income per month and income tax was generated based on 30\% of their income. Permanent addresses and present 
addresses have many fields such as house number, street number, ward number, thana, district, division. A sample list for each 
of the fields were given and then randomly picked from them. For educational qualification S.S.C result, school (where a person 
passed S.S.C from), H.S.C result, college (where a person passed H.S.C from), under graduation result, university, post graduation 
result, university were generated. Other personal information like marital status, height, weight also generated randomly.

### Package installation
The scripts requires some libraries to be installed before executing. By running the following code all the required modules can be installed.
```sh
$ pip install -r requirements.txt
```

### Run
```sh
$ python main.py
```

It will take one input asking for how many rows to generate. e.g. 500000000 person's profile to generate.

**Thank You**

