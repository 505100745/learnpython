class Student(object):
    def __init__(self,name,gender):
        self.name = name 
        self.__gender = gender

    def get_gender():
        return self.__gender

    def set_gender():
        if gender == "male" or gender == "female":
            self._gender = gender
        else:
            raise ValueError('error')

s = Student("zhangsan","tmale")
print(s.name)




