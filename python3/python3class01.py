
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

# In[1]:


class Student():
    name = '' #name-全局变量
    age = 0
    
    def print_file(self):
        print('name ' + self.name)
        print('age' + str(self.age)) # 注意str()
    


# ## 使用类
# * 实例化
# * 调用类，下面的方法
# ## 建议
# * 一个模块定义类
# * 另一个模块实例化

# In[2]:


student = Student()# 实例化
student.print_file()# 调用类下面的方法

