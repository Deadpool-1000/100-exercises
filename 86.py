with open('countries_clean.txt', 'r') as f:
    countries = f.readlines()
    countries = [country.strip('\n') for country in countries]

checklist = ["Portugal", "Germany", "Munster", "Spain"]

# One of the items is not a country. Please use Python and the file containing the list of countries (attached) 
# as the data source to filter out the checklist  
# of non-country items. Once you have filtered out checklist , then print it out.
print([country for country in checklist if country in countries])
