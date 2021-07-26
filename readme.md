#Project Structure
front-end:
    导航栏公用组建：front-end/src/components/Navbar.vue



##知识点：
ORM：把model中的模型和数据库中的一条数据相互转换
CRUD(Create Read Update Delete, 增查改删)
####python中几个类的区别

    def __init__(self, n):
        self.name = n
    # 下面这两个的功能都是用于显示，如果是两个重写了，则优先调__str__
    def __str__(self): # __str__是面向用户的
        return str(self.name)   #这里的返回值必须为字符串

    def __repr__(self): # __repr__是面向程序的，给程序员调用使用的
        return "zzzzz"		#返回值也必须为字符串
