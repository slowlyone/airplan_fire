# class Medine(object):
#     a=None
#     b=0
#     init_flag=False
#     def __init__(self):
#         if Medine.init_flag==False:
#             print("初始化播放器")
#             Medine.b +=1
#         Medine.init_flag=True
#         # if Medine.b==1:
#         #     return
#
#         # pass
#
#     def __new__(cls, *args, **kwargs):
#         # print("overwrite")
#         if cls.a is  None:
#             cls.a=super().__new__(cls)
#             # Medine.a=1
#             # cls.c=Medine.a
#         return  cls.a
#         # else:
#         #     return cls.c
#         #
#         # instance=super().__new__(cls)
#         # return instance
#
# comid=Medine()
# print(comid)
# comid2=Medine()
# print(comid2)
# comid3=Medine()
# print(comid3)
# print(Medine.b)
import  hm_pack
def password_len():
    password=input("请输入一个长度为8位的密码:\n")
    if len(password)  < 8:
        # 1 创建异常对象
        ex=Exception("密码长度不够")
    #     抛出异常对象
        raise ex
    else:
        print(password)
try:
    password_len()
except Exception  as result:
    print(result)

hm_pack.send_message.send_message("hello")
print(hm_pack.receive_message.receive())