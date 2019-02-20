from data_loader import Data_Loader
from data_generator import Data_Generator

if __name__ == "__main__":
    loader = Data_Loader()
    generator = Data_Generator()

    filename = 'names1.csv'
    df = loader.read_csvfile(filename)
    
    for religion in loader.religion:
        for gender in loader.gender:
            firstnames, middlenames, lastnames = loader.get_names_by_religion_gender(religion, gender)
            
            for i in range(2):
                if i % 2 == 0:
                    if gender == 'unisex':
                        gender1 = 'male'
                        firstnames1, middlenames1 , lastnames1 = loader.get_names_by_religion_gender(religion, gender1)
                        first_names1 = firstnames + firstnames1
                        last_names1 = lastnames + lastnames1 
                        generator.generate_profile(first_names1, None, last_names1, gender1, religion)
                        
                        gender2 = 'female'
                        firstnames2, middlenames2 , lastnames2 = loader.get_names_by_religion_gender(religion, gender2)
                        first_names2 = firstnames + firstnames2
                        last_names2 = lastnames + lastnames2
                        generator.generate_profile(first_names2, None, last_names2, gender2, religion)
                else:
                    if gender == 'unisex':
                        gender3 = 'male'
                        firstnames3, middlenames3 , lastnames3 = loader.get_names_by_religion_gender(religion, gender3)
                        first_names3 = firstnames + firstnames3
                        middle_names3 = middlenames + middlenames3 
                        last_names3 = lastnames + lastnames3
                        generator.generate_profile(first_names3, middle_names3, last_names3, gender3, religion)
                        
                        gender4 = 'female'
                        firstnames4, middlenames4 , lastnames4 = loader.get_names_by_religion_gender(religion, gender4)
                        first_names4 = firstnames + firstnames4
                        middle_names4 = middlenames + middlenames4
                        last_names4 = lastnames + lastnames4
                        generator.generate_profile(first_names4, middle_names4, last_names4, gender4, religion)
                        
    data, collumns = generator.get_data()
    filename = 'new.csv'
    saved_data = loader.save_csvfile(filename, data, collumns)
    print(saved_data)