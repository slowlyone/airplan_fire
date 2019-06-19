class A:
    def test(self):
        print("testA")


class B:
    def test(self):
        print("demo")

class C(B,A):
    pass

class O(object):
    pass
c=C()
# c.test()
# c.demo()
# print(C.__mro__)
o=O()
dir(o)