# 创建一个名为 guests 的列表，有三个元素分别是三个人名
guests = ['Billy Gates', 'Zark Hamburger', 'Tim Cookie']

#用 print() 函数在命令行输出一句话：邀请人如下
print("The following persons have been invited:")

# 利用 for 语句遍历刚才声明的 guests 列表, for 语句下 guest 为被遍历的人名
for guest in guests:
	# print() 函数输出遍历到的人名
	print(guest)

# 输出临时违约人以及替补人
print("\nBilly Gates said that he cannot attend the dinner, and he was replaced by L.B.Jefferies")
# 列表名后加方括号[]并在内填入索引，加等号为其赋新的值，修改为新的人名
guests[0] = 'L.B.Jefferies'

#再次用for循环输出列表内容
for guest in guests:
	# print() 函数输出遍历到的人名
	print(guest)

print("\nA larger table for the dinner was just founded, which can let six people have dinner together.")
# 列表对象有方法insert用来在指定位置插入一个元素，列表名后加.insert()来调用
# ()括号内接受两个参数，第一个为数字：表示插入元素在列表内的位置，如1的意思是 在原列表中以0和1为索引的元素之间插入
# 第二个参数为插入的元素的值，见下方
guests.insert(1, "Lars Thorwald")
guests.insert(2, "Lisa Fremont")

# 另一个对与列表的方法为append，列表名后加.append()调用，用于给列表末尾添加一个元素
# 括号内只接受一个参数，即为元素的值
guests.append("Tom Doyle")
#再次用for循环输出列表内容
for guest in guests:
	# print() 函数输出遍历到的人名
	print(guest)

#大桌子无法使用 需要移走其他人 剩下两个人
print("\nThe larger table cannot arrive on time, so there will not be enough space for the following persons:")

# while为另一个循环语句，当while后追加的条件成立时 会反复循环while下的代码 直到条件不成立 才会跳出循环 继续向下执行
# 下方的while后追加的条件意思是 guests列表长度大于2时 反复执行while下缩进的代码
# 列表长度不足为2时会停止循环 继续向下执行新的代码
# len()是另一个函数，括号内接受一个参数：可以是一个列表，这样len()代表列表长度的数值
while len(guests) > 2:
	# pop()方法用于修改列表，若括号内没有参数，则默认将列表最后一个元素弹出 并返回这个元素的值
	# 列表被弹出的值会被赋给 popped_person
	popped_person = guests.pop()
	print(popped_person)

print("\nThe following persons are still in the guest list:")
#再次用for循环输出列表内容 此时列表仅剩两人
for guest in guests:
	# print() 函数输出遍历到的人名
	print(guest)

print("\nThe remaining two persons are going to be deleted.")
# del语句用于删除已经存在的值 可以是变量 也可以是列表的元素
# del 后加上要删除的值 下方用del删除guests列表中的索引为1和0的元素
del guests[1]
del guests[0]

# 列表可直接提供给print()函数 再命令行里输出 此时guests已经被以上代码清空
print(guests)