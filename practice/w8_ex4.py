class Patient:
    
    def __init__(self, name: str):
        self.__name = name
        

    @property
    def name(self) -> str:
        return self.__name
    

class Doctor:
    
    def __init__(self, name, speciality):
        self.__name = name
        self.__speciality = speciality
        
    @property
    def name(self) -> str:
        return self.__name

    @property
    def speciality(self) -> str:
        return self.__speciality
    
    def __str__(self):
        return f"Dr. {self.name}({self.speciality})"   

class Appointment:
    
    def __init__(self, date: str, doctor: Doctor, patient: Patient):
        self.__date = date
        self.__doctor = doctor
        self.__patient = patient
    
    @property
    def date(self) -> str:
        return self.__date

    @property
    def doctor(self) -> Doctor:
        return self.__doctor

    @property
    def patient(self) -> Patient:
        return self.__patient

    def __str__(self):
        return f"Patient: {self.patient.name} has an appointment with {self.doctor} on {self.date}"

    
    
patient1 = Patient("John")
patient2 = Patient("Sara")
patient3 = Patient("Isack")
patient4 = Patient("Jacob")


doc1 = Doctor("Luc", "Family")
doc2 = Doctor("Caleb", "Neurologist")
doc3 = Doctor("Kisa", "Dermatologist")


appointments = [Appointment("12-05-2025", doc1, patient1),
                 Appointment("12-05-2025", doc1, patient2),
                 Appointment("12-05-2025", doc2, patient1),
                 Appointment("12-05-2025", doc2, patient2),
                 Appointment("12-05-2025", doc2, patient3),
                 Appointment("12-05-2025", doc3, patient4),]



def print_appointments_for_doctor(name: str):
    print(f"Appointments for Dr.{name}:")
    print("-----------------------------")
    has_appointment = False
    for appointment in appointments:
        if appointment.doctor.name == name:
            has_appointment = True
            print(appointment)
    
    if not has_appointment:
        print("Doesn't have appointemnts")


def print_appointments_for_patient(name: str):
    print(f"Appointments for Mr/Mis {name}:")
    print("-----------------------------")
    has_appointment = False
    for appointment in appointments:
        if appointment.patient.name == name:
            has_appointment = True
            print(appointment)
    
    if not has_appointment:
        print("Doesn't have appointemnts")
        
        
        
print_appointments_for_doctor("Luc")
print_appointments_for_doctor("John")

print_appointments_for_patient("John")
print_appointments_for_patient("Luc")




