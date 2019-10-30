class patient() :
    
    def __init__(self, num, name, age, state, status) :
        self.num = num
        self.name = name
        self.age = age
        self.state = state
        self.status = status
            
    def __repr__(self) :
        return f"{self.num}, {self.name}, {self.age}, {self.state}, {self.status}"
    
    def add(self, key, value) :
        self[key] = value
    
        

class doctor() :
    def __init__(self, name, age, grade) :
        self.name = name
        self.age = age
        self.grade = grade