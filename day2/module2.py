# from day2 import module1
# from day2.module1 import a as module1_a,name,test



# a = "模块二中的a变量"
#
# def name():
#     print("模块二中的name方法")
# class test():
#     name = "模块二中的test类"

# print(module1_a)
# name()
# print(test.name)
# a  =123
# b = "贡绪豪"
# t =(1,2,3,4)
# f = [3,4,5,6]
# l = {4,5,67,7}
# print(a + int(b))
# print(list(t))
# print(tuple(f))
# print(tuple(l))
# print(set(f))
# print(list(b))



# f = open("贡绪豪.txt","w")
# f.write("123")
# f.close


# f = open("贡绪豪.txt","w")
# f.writelines(["hbfjg\n","jifsg\n","bfsjgfug\n","oiuoiuo\n","pokicgiuwjh\n"])
# f.close

# f = open("贡绪豪.txt","r")
# # print(f.read())
# # print(f.read(10))
# # print(f.readline())
# print(f.readlines())
# a = "0123456789"
# # print(a[9])
# print(a[-1])
# print(a[1:-1])
# print(a[0:-1:1])
# print(a[::-1])
# print(a[2:])
# print(a[:2])


# for i in range(1,10):
#     for j in range(1,i+1):
#         print("%d * %d = %d"%(j,i,i*j),end="\t")
#     print()

# for i in range(1,10):
#     for j in range(1,i+1):
#         print("{} * {} = {}".format(j,i,i*j),end="\t")
#     print()
# l = [1,2,34,24,5,7,0,5]
# l[1:5] = 14,3
# print(l)
# l = [2,3,4]
# l.append("王尼玛")
# l.append('王尼玛')
# l.extend({"123",123})
# print(l)

# l = [1,2,34,24,5,7,0,5]

# l.remove(1)

# l.pop(l.pop(4))
# print(l)
# l = [True,3,5,12,5,4]
# l.remove(1)
# print(l)
# l.clear()
# print(l)


# d = {"name":"小明","age":18,"sex":"男"}
# print(d)
# d["adder"] = "江苏苏州"
# d["age"] = 20
# print(d)
# d.update({"adder":"江苏南京","学历":"胎教"})
# print(d)


def div(a,b):
    try:
        return a / b
    except ZeroDivisionError as e:
        print(e)
    else:
        print("除法执行成功")
    finally:
        print("操作成功")

print(div(20,0))

# try:
#     f = open("123.txt","r")
#     print(f.read())
#     f.close()
# except:
#     print("文件错误")
#
# print("操作完成")


class Cust



