class Student:
    def __init__(self, id, name, gpa):
        self.id = id
        self.name = name
        self.gpa = gpa
        
    def getID(self):
        return self.id
    
    def getName(self):
        return self.name
    
    def getGPA(self):
        return self.gpa
    
    def printDetails(self):
        print('\n ID:', self.id,'\n Name:', self.name,'\n GPA: ',self.getGPA())

class ProbHash: 
    def __init__(self, cap): 
        self.hashtable = cap * [None]
        self.n = cap
    
    def hashFunction(self, key):
        index = key%(self.n)
        return index
    
    def rehashFunction(self, hashkey):
        return (hashkey + 1) % self.n
        
    def insertData(self, student_obj):
        index = self.hashFunction(student_obj.getID())
        while self.hashtable[index] != None:
            index = self.rehashFunction(index)
        self.hashtable[index] = student_obj
        print('Insert '+str(self.hashtable[index].getID())+' at index ' + str(index))
        
        
    def searchData(self, std_id):
        index = self.hashFunction(std_id)
        times = 0
        while self.hashtable[index] != None and std_id != self.hashtable[index].getID() and times != self.n:
            index = self.rehashFunction(index)
            times += 1
            # print('!', index)
            # print(times)
        if self.hashtable[index] == None or times == self.n:
            print(std_id, 'does not exist.')
        else:
            print('Found',std_id, 'at index', index)
            return self.hashtable[index]
        
            
s1 = Student(65070001, "Sandee Boonmak", 3.05)
s2 = Student(65070077, "Somsak Jaidee", 2.78)
s3 = Student(65070021, "Somsri Jaiyai", 3.44)
s4 = Student(65070042, "Sommai Meeboon", 2.89)

myHash = ProbHash(4)
myHash.insertData(s1)
myHash.insertData(s2)
myHash.insertData(s3)
myHash.insertData(s4)

std = myHash.searchData(65070077)
std.printDetails()
print("-------------------------")
std = myHash.searchData(65070021)
std.printDetails()
print("-------------------------")
std = myHash.searchData(65070042)
std.printDetails()
print("-------------------------")
std = myHash.searchData(65070032)