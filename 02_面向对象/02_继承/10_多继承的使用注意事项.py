class A:
    def test(self):
        print("A --- test 方法")

    def demo(self):
        print("A --- demo 方法")


class B:
    def demo(self):
        print("B --- demo 方法")

    def test(self):
        print("B --- test 方法")


class C(A, B):
    """多继承可以让子类对象，同时具有多个父类的属性和方法"""
    pass


c = C()
print(C.__mro__)
# (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>) object是所有类的基类
c.test()
c.demo()
