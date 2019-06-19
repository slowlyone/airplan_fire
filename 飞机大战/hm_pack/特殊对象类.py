class Tool(object):
    #使用赋值语句定义类属性
    count1 =0

    def __init__(self,name):
        self.name=name
        Tool.count1 +=1
    @classmethod
    def show_tool_count(cls):
        print("[%d]."%cls.count1)
#
# tool1=Tool("斧头")
tool2=Tool("刀")
# print(Tool.count1)
# tool1.count1=99
# print(tool1.count1
Tool.show_tool_count()
