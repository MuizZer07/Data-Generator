import random


class Data_Generator():

    def __init__(self):
        self.marital_status = {
            1: 'Single',
            2: 'Married',
            3: 'Widowed',
            4: 'Devorced'
        }

        self.profession = {
            1: "Service Holder",
            2: "Businessman",
            3: "Teacher",
            4: "Salesman",
            5: "Farmer",
            6: "Minister",
            7: "Rickshaw Puller",
            8: "Postman",
            9: "Peon",
            10: "Government Officer",
            11: "Army Officer",
            12: "Artist"
        }

        self.email = {
            1: '@gmail.com',
            2: '@yahoo.com',
            3: '@outlook.com'
        }

        self.mobile_no = {
            1: '019',
            2: '017',
            3: '018',
            4: '015',
            5: '016'
        }

        self.new_generated_names = []
        self.new_generated_sex = []
        self.new_generated_religion = []
        self.new_generated_marital_status = []
        self.new_generated_profession = []
        self.new_generated_DOB = []
        self.new_generated_emails = []
        self.new_generated_mobile_no = []

    def get_data(self):
        Data = {'Name': self.new_generated_names,
                'Sex': self.new_generated_sex,
                'Religion': self.new_generated_religion,
                'Marital Status': self.new_generated_marital_status,
                'Profession': self.new_generated_profession,
                'Date of Birth': self.new_generated_DOB,
                'Email Address': self.new_generated_emails,
                'Mobile No. (+880)': self.new_generated_mobile_no,
                }
        columns = ['Name', 'Sex', 'Religion', 'Marital Status', 'Profession', 'Date of Birth', \
                   'Email Address', 'Mobile No. (+880)']

        return Data, columns

    def generate_profile(self, first_names, middle_names, last_names, gender, religion):
        for firstname in first_names:
            for lastname in last_names:
                
                if middle_names != None:
                    for middlename in middle_names:
                        self.new_generated_names.append(firstname + " " + middlename + " " + lastname)
                        self.new_generated_sex.append(gender)
                        self.new_generated_religion.append(religion)
                        self.new_generated_marital_status.append(self.marital_status[random.randint(1, 4)])
                        self.new_generated_profession.append(self.profession[random.randint(1, 12)])
                        self.new_generated_DOB.append(self.generate_DOB())
                        self.new_generated_emails.append(firstname.lower() + "." + lastname.lower() + self.email[random.randint(1, 3)])
                        self.new_generated_mobile_no.append(self.generate_phone_no())
                else:
                    self.new_generated_names.append(firstname + " " + lastname)
                    self.new_generated_sex.append(gender)
                    self.new_generated_religion.append(religion)
                    self.new_generated_marital_status.append(self.marital_status[random.randint(1, 4)])
                    self.new_generated_profession.append(self.profession[random.randint(1, 12)])
                    self.new_generated_DOB.append(self.generate_DOB())
                    self.new_generated_emails.append(firstname.lower() + "." + lastname.lower() + self.email[random.randint(1, 3)])
                    self.new_generated_mobile_no.append(self.generate_phone_no())
                

    def generate_DOB(self):
        return str(random.randint(1, 28)) + "/" + str(random.randint(1, 12)) + "/" + str(random.randint(1950, 1999))

    def generate_phone_no(self):
        str1 = str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + \
               str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + \
               str(random.randint(0, 9)) + str(random.randint(0, 9))

        return self.mobile_no[random.randint(1, 3)] + str1
