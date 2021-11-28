from random import randint
# 通过from和import语句导入python内置库 用于生成随机整数

lst = [] # 提前创建空列表 用于存原始数据
# for 循环100000次 每次获取一个0-100之内的随机整数 并存入lst中
for _ in range(100000):
	lst.append(randint(0, 100))

# 生名一个空字典用于存储计算后的数据
# 键值对为 数字：数字的出现次数
# 例如5:121 意思为lst中5出现121次
result = {}

# set(lst)返回一个列表 是剔除掉重复内容的lst
# 若lst = [1,1,1,2,3,3,5,5,5,5] 则 setted_lst = set(lst) = [1,2,3,5]
setted_lst = set(lst)

# 将原始数据lst中的每种数字存入字典的键中，每个键的初始值为0
for x in setted_lst:
    result[x] = 0

for key in result.keys(): # 用for循环遍历字典的键，key为lst中包含的一类数字
    for i in lst: # 在for循环中嵌套的循环 i为lst中的逐个数字
        if i == key: # 如果此次循环到的lst中的数字i等于字典中的一个键
            result[key] += 1 # 则给这个键的值加1 代表这个数出现了一次
            # 对于出现多次的数字 每匹配到相等就给出现次数加1 

times = [] # 用于存储每个数字出现的次数 仅用于最后确定哪个数字出现做多
for key, value in result.items(): # 循环字典键值对 输出结果
    print(key, "出现", value, "次")
    times.append(value) # 向times中添加每个数字出现的次数

for key in result.keys(): # 循环字典的键 键的含义是lst中的一类数字
    if result[key] == max(times): # 如果这个键的值（这类数字的出现次数）等于times中的一个最大值（出现次数最多的数字的出现次数）
        print(key,"出现次数最多，为", result[key], "次") # 输出最频繁出现的数字 以及其出现次数