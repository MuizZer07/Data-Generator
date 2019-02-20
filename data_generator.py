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
        self.new_generated_permanent_address = []
        self.new_generated_present_address = []

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
        
    def get_data(self):
        Data = {'Name': self.new_generated_names,
                'Sex': self.new_generated_sex,
                'Religion': self.new_generated_religion,
                'Marital Status': self.new_generated_marital_status,
                'Profession': self.new_generated_profession,
                'Date of Birth': self.new_generated_DOB,
                'Email Address': self.new_generated_emails,
                'Mobile No. (+880)': self.new_generated_mobile_no,
                'Permanent Address': self.new_generated_permanent_address,
                'Present Address': self.new_generated_present_address,
                }
        columns = ['Name', 'Sex', 'Religion', 'Marital Status', 'Profession', 'Date of Birth', \
                   'Email Address', 'Mobile No. (+880)', 'Permanent Address', 'Present Address']

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
                        self.new_generated_permanent_address.append(self.generate_permanent_address())
                        self.new_generated_present_address.append(self.generate_present_address())
                else:
                    self.new_generated_names.append(firstname + " " + lastname)
                    self.new_generated_sex.append(gender)
                    self.new_generated_religion.append(religion)
                    self.new_generated_marital_status.append(self.marital_status[random.randint(1, 4)])
                    self.new_generated_profession.append(self.profession[random.randint(1, 12)])
                    self.new_generated_DOB.append(self.generate_DOB())
                    self.new_generated_emails.append(firstname.lower() + "." + lastname.lower() + self.email[random.randint(1, 3)])
                    self.new_generated_mobile_no.append(self.generate_phone_no())
                    self.new_generated_permanent_address.append(self.generate_permanent_address())
                    self.new_generated_present_address.append(self.generate_present_address())
                
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

        return self.mobile_no[random.randint(1, 3)] + str1
