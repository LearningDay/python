
# coding: utf-8

# # class
# * 最基本的作用--**封装**
# ## 命名规则
# * 首字母大写
#     * StudentHomework
# * 别用【_】连接多个单词
# ## 类的内部
# * 定义若干变量
# * 定义函数




class Student():
    name = '类demo' #name 全局变量、类变量
    age = 0 # 类变量，全局变量，

    # 构造函数    
    def __init__(self,name,age):
        # 初始化对象的属性
        self.name = name# self.name是实例变量，第二个name 是参数列表中的name
        self.age = age #第二个age是参数，self.age是实例变量

    
    # 行为
    def do_homework(self):
        print('homework')

