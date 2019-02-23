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
            7: "Athlete",
            8: "Postman",
            9: "Peon",
            10: "Government Officer",
            11: "Army Officer",
            12: "Artist",
            13: "Doctor",
            14: "Politician",
            15: "Chef",
            16: "Judge",
            17: "Journalist",
            18: "Social Worker",
            19: "Free lancer",
            20: "Media Worker",
            21: "Student"
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

        self.divisions = {
           1: "Barisal",
           2: "Chittagong",
           3: "Dhaka",
           4: "Khulna",
           5: "Rajshahi",
           6: "Mymensingh",
           7: "Rangpur",
           8: "Sylhet",  
        }
        
        self.districts = {
            1: ['Barisal', 'Barguna', 'Bhola', 'Jhalokati', 'Patuakhali', 'Pirojpur'],
            2: ['Brahmanbaria', 'Comilla', 'Chandpur', 'Lakshmipur', 'Noakhali', 'Feni'],
            3: ['Dhaka', 'Gazipur', 'Kishoreganj', 'Manikganj', 'Narayanganj', 'Gopalganj'],    
            4: ['Bagerhat', 'Chuadanga', 'Jessore', 'Jhenaidah', 'Khulna', 'Kushtia'],
            5: ['Bogura', 'Chapainawabganj', 'Joypurhat', 'Naogaon', 'Natore', 'Rajshahi'],
            6: ['Jamalpur', 'Mymensingh', 'Netrokona', 'Sherpur'],
            7: ['Thakurgaon', 'Rangpur', 'Panchagarh', 'Nilphamari', 'Lalmonirhat', 'Kurigram'],
            8: ['Habiganj', 'Moulvibazar', 'Sunamganj', 'Sylhet'],
        }
        
        self.thanas = {
            'Dhaka' : ['Motijheel', 'Mirpur', 'Badda', 'Kotwali', 'Tejgaon'],
            'Chittagong' : ['Rouzan', 'Patiya', 'Mirsharai', 'Barura', 'Fatikchhari'],
            'Barisal' : ['Amtali', 'Betagi', 'Patharghata', 'Agailzhara', 'Babuganj'],
            'Khulna' : ['Chitalmari', 'Fakirhat', 'Kachua', 'Mollahat', 'Rampal'],
            'Rajshahi' : ['Dhunat', 'Gabtoli', 'kalai', 'Ahsanganj', 'Nitpur'],
            'Mymensingh' : ['Bhaluka', 'Shorishabari', 'Gaforgaon', 'Haluaghat', 'Muktagachha'],
            'Rangpur': ['Kaunia', 'Gangachara', 'Mithapukur', 'Saidpur', 'Jaldhaka'],
            'Sylhet' : ['Kalauk', 'Bahubal', 'Madhabpur', 'Nabiganj', 'Kulaura'],
        }
        
        self.villages = {
            'Dhaka' : ['Bagra', 'Dingamanik', 'Haridaspur', 'Goalgram', 'Fardabad'],
            'Chittagong' : ['Baria', 'Aitpara', 'Dhumdumia', 'Ramnagar', 'Harbang '],
            'Barisal' : ['Durga Sagar', 'Gabkhan', 'Ratnopur', 'Goila', 'Kathira'],
            'Khulna' : ['Payari', 'Rajapur', 'Sarankhola', 'Dumuria', 'Rupsa'],
            'Rajshahi' : ['Nagar', 'Bhatahar', 'Paikpara', 'Dhopapara', 'Haribhanga'],
            'Mymensingh' : ['Ujalhati', 'Trishal', 'Phulpur', 'Bahadurpur', 'Nandail'],
            'Rangpur': ['Badarganj ', 'Palash Kandi', 'Panchanan Barma', 'Mistry Para', 'Dahala'],
            'Sylhet' : ['Jahidpur', 'Sujaul', 'Balaganj', 'Jotyintapur', 'Sagarnal '],
        }
        
        self.default_female_names = ['Afsana Ara Hoque', 'Khadija begum', 'Maimuna Haque', \
                                     'Nafisa Kabir', 'Rehnuma Haque']
        self.default_male_names = ['Ahmed Kamal', 'Kamal Ahmed', 'Kamal Haque', 'Jamal Ahmed', 'Jamal Haque']
        
        self.new_generated_names = []
        self.new_generated_sex = []
        self.new_generated_religion = []
        self.new_generated_marital_status = []
        self.new_generated_profession = []
        self.new_generated_DOB = []
        self.new_generated_emails = []
        self.new_generated_mobile_no = []
        self.new_generated_permanent_address = []
        self.new_generated_present_address = []
        self.new_generated_fathers_name = []
        self.new_generated_mothers_name = []
        self.new_generated_place_of_birth = []
        self.new_generated_NID = []
        
        for i in range(5):
            self.new_generated_names.append("Ahmed Reza Haque")
            self.new_generated_NID.append(self.generate_NID())
            self.new_generated_sex.append("male")
            self.new_generated_religion.append("muslim")
            self.new_generated_marital_status.append("Single")
            self.new_generated_profession.append("Student")
            self.new_generated_DOB.append("01/01/1990")
            self.new_generated_emails.append("reza.ahmed@gmail.com")
            self.new_generated_mobile_no.append(self.generate_phone_no())
            self.new_generated_permanent_address.append(self.generate_permanent_address())
            self.new_generated_present_address.append(self.generate_present_address())
            self.new_generated_fathers_name.append(self.default_male_names[i])
            self.new_generated_mothers_name.append(self.default_female_names[i])
            self.new_generated_place_of_birth.append(random.choice(self.districts[random.randint(1, 4)]))


    def get_data(self):
        Data = {'Name': self.new_generated_names,
                'NID': self.new_generated_NID,
                'Fathers Name': self.new_generated_fathers_name,
                'Mothers Name': self.new_generated_mothers_name,
                'Sex': self.new_generated_sex,
                'Religion': self.new_generated_religion,
                'Marital Status': self.new_generated_marital_status,
                'Profession': self.new_generated_profession,
                'Date of Birth': self.new_generated_DOB,
                'Email Address': self.new_generated_emails,
                'Mobile No. (+880)': self.new_generated_mobile_no,
                'Permanent Address': self.new_generated_permanent_address,
                'Present Address': self.new_generated_present_address,
                'Place of Birth': self.new_generated_place_of_birth,
                }
        columns = ['Name', 'NID', 'Fathers Name', 'Mothers Name', 'Sex', 'Religion', 'Marital Status', 'Profession', 'Date of Birth', \
                   'Email Address', 'Mobile No. (+880)', 'Permanent Address', 'Present Address', 'Place of Birth']

        return Data, columns

    def generate_profile(self, first_names, middle_names, last_names, gender, religion):
        num = random.randint(5, 15)
        for firstname in first_names:
            for lastname in last_names:
                if middle_names != None:
                    for middlename in middle_names:
                        for i in range(num):
                            self.generate_single_profile(first_names, last_names, firstname, middlename, lastname, gender, religion)
#                        
                else:
                    for i in range(num):
                        self.generate_single_profile(first_names, last_names, firstname, None, lastname, gender, religion)
             
    def generate_single_profile(self, first_names, last_names, firstname, middlename, lastname, gender, religion):
        if middlename is None:
            self.new_generated_names.append(firstname + " " + lastname)
        else:
            self.new_generated_names.append(firstname + " " + middlename + " " + lastname)
                 
        self.new_generated_NID.append(self.generate_NID())
        self.new_generated_sex.append(gender)
        self.new_generated_religion.append(religion)
        self.new_generated_marital_status.append(self.marital_status[random.randint(1, 4)])
        self.new_generated_profession.append(self.profession[random.randint(1, 21)])
        self.new_generated_DOB.append(self.generate_DOB())
        self.new_generated_emails.append(firstname.lower() + "." + lastname.lower() + self.email[random.randint(1, 3)])
        self.new_generated_mobile_no.append(self.generate_phone_no())
        self.new_generated_permanent_address.append(self.generate_permanent_address())
        self.new_generated_present_address.append(self.generate_present_address())
        self.new_generated_fathers_name.append(self.get_fathers_name(first_names, "", lastname, gender))
        self.new_generated_mothers_name.append(self.get_mothers_name(first_names, last_names, gender))
        self.new_generated_place_of_birth.append(random.choice(self.districts[random.randint(1, 4)]))
        
    
    def get_fathers_name(self, firstnames, middlename, lastname, gender):
        fathers_name = None
        if gender is 'male':
            fathers_name = random.choice(firstnames) + " " + middlename + " " + lastname
        else:
            fathers_name = random.choice(self.new_generated_fathers_name)
        
        return fathers_name
        
    def get_mothers_name(self, firstnames, lastnames, gender):
        mothers_name = None
        if gender is 'female':
            mothers_name = random.choice(firstnames) + " " + random.choice(lastnames)
        else:
            if len(self.new_generated_mothers_name) > 0 :
                mothers_name = random.choice(self.new_generated_mothers_name)
            
        return mothers_name
        
    def generate_present_address(self):
        house_no = random.randint(1, 70)
        road_no = random.randint(1, 20)
        ward_no = random.randint(1, 45)
        div = random.randint(1, 7)
        city = random.choice(self.districts[div])
        thana = random.choice(self.thanas[self.divisions[div]])
        dist = city
        division = self.divisions[div]
        
        return "House no. " + str(house_no) +  ", Road no. " + str(road_no) + ", Ward no. " + str(ward_no) + \
                ", Thana: " + thana + ", City: " + city +", District: " + dist + ", Division: " + division + "."
    
    def generate_permanent_address(self):
        ward_no = random.randint(1, 45)
        div = random.randint(1, 7)
        village = random.choice(self.villages[self.divisions[div]])
        thana = random.choice(self.thanas[self.divisions[div]])
        dist = random.choice(self.districts[div])
        division = self.divisions[div]
        
        return "Ward no. " + str(ward_no) +  ", Village name: " + village + \
                ", Thana: " + thana + ", District: " + dist + ", Division: " + division + "."
                
    def generate_DOB(self):
        return str(random.randint(1, 28)) + "/" + str(random.randint(1, 12)) + "/" + str(random.randint(1950, 1999))

    def generate_phone_no(self):
        str1 = str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + \
               str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + \
               str(random.randint(0, 9)) + str(random.randint(0, 9))
               
        return self.mobile_no[random.randint(1, 5)] + str1
    
    def generate_NID(self):
        str1 = str(random.randint(1, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + \
               str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + \
               str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9))

        return str1
