#coding:utf-8

class Student(object):
    '''
            学生类
    '''
    '''全局变量，存放学生信息'''
    _students = []
#     [{stu1},{stu2}]
#     [stu2,stu3]
# {no1:{stu1},no2:{stu2}}

    def __init__(self):
        '''学生实例初始方法
                                 输入：属性（姓名、学号、专业、年级、成绩）
                                   输出：无                      
        '''
        pass
    
    def add(self,name,no,major,grade,score):
        '''学生信息添加方法
                                 输入：姓名、学号、专业、年级、成绩
                                输出：true/false                      
        '''
        self.name = name
        self.no = no
        self.major = major
        self.grade = grade
        self.score = score
        studict = {}
        studict["name"]=self.name
        studict["no"]=self.no
        studict["major"]=self.major
        studict["grade"]=self.grade
        studict["score"]=self.score
        self._students.append(studict)
        
    
    def delete(self,no):
        '''学生信息删除方法
                                 输入：学号
                                输出：true/false                      
        '''
        flag = False
        self._students.remove(self.select(no=no))
    
    def alert(self):
        '''学生信息修改方法
                                 输入：姓名、学号、专业、年级
                                输出：true/false                      
        '''
        pass
    
    def select(self,no=None,major=None,grade=None):
        '''学生信息查找方法
                                 输入：学号、专业、年级
                                输出：学生信息                      
        '''
        result = self._students
        if no!=None and self._students!=None:
            for student in self._students:
                for k,v in student.items():
                    if v==no:
                        result = student
                        break
        return result

    def alertScore(self):
        '''学生成绩添加方法
                                 输入：学号、成绩
                                输出：true/false                      
        '''
    def rankScore(self):
        '''学生成绩添加方法
                                 输入：专业
                                输出：学生信息                      
        '''
             