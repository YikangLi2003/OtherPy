#-*- coding:utf-8 -*-

lst = [5,19,22,26,35,3,4,7,27,31,11,14,29,31,
	32,7,8,15,19,28,18,21,22,23,35,17,18,25,
	27,28,8,9,13,29,30,8,13,19,20,29,4,25,28,
	29,35,11,18,21,22,33,14,17,18,28,34,1,2,
	9,16,30,5,10,21,25,31,2,15,19,29,30,14,15,
	26,27,29,8,23,26,27,33,10,17,22,25,35,17,
	19,21,27,31,1,11,12,34,35,1,2,15,17,26,14,
	17,18,23,27,2,16,17,18,34,2,3,14,27,28,6,
	8,16,34,35,4,21,28,29,33,8,9,17,26,28,2,6,
	14,19,28,4,7,17,29,31,8,12,19,27,33,2,7,13,14,19]
result = {}

setted_lst = set(lst)
for x in setted_lst:
    result[x] = 0

for key in result.keys():
    for i in lst:
        if i == key:
            result[key] += 1

times = []
for key, value in result.items():
    print(key, " - ", value, "次")
    times.append(value)

for key in result.keys():
    if result[key] == max(times):
        print(key,"最多，", result[key], "次")