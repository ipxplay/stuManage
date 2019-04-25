#coding:utf-8
class MsgPrint(object):
    '''
    classdocs
    '''


    def __init__(self, **krgs):
        '''
        Constructor
        '''
        self._krgs = krgs
    
    def mainMenu(self):
        print("*************欢迎使用学生成绩管理系统*************\n\
              1、学生管理\n\
              2、学生查找\n\
              3、成绩管理\n\
                            请输入编号进入相应菜单")
        
        
    def studentManageMenu(self):
        print("*************欢迎使用学生管理功能模块*************\n\
                            1、添加\n\
                            2、删除\n\
                            3、查找\n\
                                ")
    def studentAddMenu(self):
        print("*************欢迎使用学生管理功能模块*************\n\
                                请输入学生信息：姓名，学号，专业，年级，成绩")
        
    def studentDelMenu(self):
        print("*************欢迎使用学生管理功能模块*************\n\
                                请输入学生信息：学号") 
           
    def studentFindMenu(self):
        print("*************欢迎使用学生管理功能模块*************\n\
                                请输入学生信息：姓名，学号，专业，年级，成绩")
    
    def studentManageInfo(self):
        if isinstance(self._krgs, dict):
            nametitle = "{0: ^15}".format("姓名")
            notitle = "{0: ^21}".format("学号")
            majortitle = "{0: ^16}".format("专业")
            gradetitle = "{0: ^16}".format("年级")
            scoretitle = "{0: ^21}".format("成绩")
            title = nametitle+"|"+notitle+"|"+majortitle+"|"+gradetitle+"|"+scoretitle+"|"
            print(title)
            for stu in self._krgs["key"]:
                name = "{0: ^15}".format(stu["name"])
                no = "{0: ^15}".format(stu["no"])
                major = "{0: ^15}".format(stu["major"])
                grade = "{0: ^15}".format(stu["grade"])
                score = "{0: ^15}".format(stu["score"])
                stu_info = "{0}|{1}|{2}|{3}|{4}|"
                stu_info=stu_info.format(name,no,major,grade,score)
                print(stu_info)
        else:
            print("the input must be dict!")
        

                
            
        
        