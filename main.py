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
                        gender = 'male'
                    generator.generate_profile(firstnames, None, lastnames, gender, religion)
                else:
                    if gender == 'unisex':
                        gender = 'female'
                    generator.generate_profile(firstnames, middlenames, lastnames, gender, religion)
            
    data, collumns = generator.get_data()
    filename = 'new.csv'
    saved_data = loader.save_csvfile(filename, data, collumns)
    print(saved_data)