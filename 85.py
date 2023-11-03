with open('countries_raw.txt', 'r') as f:
    countries = f.readlines()
    countries = [country for country in countries if country!='\n' and country != 'Top of Page\n' and len(country)>3]

with open('countries_refined.txt', 'w') as f:
    f.writelines(countries)