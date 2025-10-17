# My Practice

'''
class Student:
    def __init__(self, name, level, course):
        """This function creates the bio of the student"""
        print("Creating a new student...")
        self.name = name
        self.level = level
        self.course = course
        print(f"Student {name} has been created.")


# when you create a student, __init__ runs automatically
kemi = Student("Michael Damilola", 800, "Computational Linguistics")
print(kemi.name)



class NigerianStudent:
    def __init__(self,name,state,course):
        self.name = name
        self.state = state
        self.course = course
        self.student_id = self.generate_id()
        print(f"Step6: {self.name} from {self.state} is ready")


    def generate_id(self):
        import random
        return f"UI{random.randint(1000,9999)}"
    

# when you create an object. here is what happens:
ayo = NigerianStudent("Ayomide", "Lagos", "Computer Science")

print(ayo.name)
print(ayo.student_id)


# Creating Multiple Users
class PhoneUser:
    def __init__(self, name, network, airtime):
        print("Creating user details...")
        self.name = name
        self.network = network
        self.airtime = 0
        print(f"{self.name} joined {self.network} network")

    def buy_airtime(self, amount):
        self.airtime += amount
        return f"{self.name} now has #{self.airtime} airtime."
    
    def send_airtime(self, amount):
        self.airtime -= amount
        return f"{self.name} just transfered {amount} has #{self.airtime} left."

onisemo = PhoneUser("Onisemo Williams", "Airtel", 200)

print(onisemo.buy_airtime(200))
print(onisemo.buy_airtime(200))
print(onisemo.send_airtime(150))
'''

class Student:
    university = "University of Ibadan"
    def __init__(self, name, course):
        self.name = name
        self.course = course
    
student1 = Student("Michael", "Computational Linguistics")
student2 = Student("Damilola", "Linguistics")
print(Student.university)
print(student1.university)
print(student2.university)

@classmethod
def get_university(cls):
    return cls.university



# Static Method - Dont need object or class data

@staticmethod
def academic_calendar():
    return " Academic sessison runs from September to July"

