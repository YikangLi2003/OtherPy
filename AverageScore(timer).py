import random
import uuid
import time

time_start = time.time()

subjects = ["CFL", "MM2", "EAL", "PEP", "BAL", "MM1", "MM3", "PHY", "CHM", "ART", "ACC", "BM", "JSL"]
#persons = ["Peter", "Jack", "Oliver", "Eason", "Ethan", "Eric", "Jasper", "Jason", "White", "Bill"]
persons = []
scores = []
subject_average = []
person_average = []

# 生成随机字符串填充人名
for i in range(500000):
    persons.append(str(uuid.uuid4())[1:5])

# 使用0为默认值暂时填充结果
for i in range(2):
    subject_average.append([])
    for j in range(len(subjects)):
        subject_average[i].append(0)
for i in range(len(persons)):
    person_average.append([0, 0])

# 随机数填充成绩单
for p in range(len(persons)):
    scores.append([])
    for s in range(len(subjects)):
        scores[p].append(random.randint(0, 101))

# 随机设定六门非必修课为未选修状态（分数设为-1）
for p in range(len(scores)):
    unslected = random.sample(range(4, 13), 6)
    for s in unslected:
        scores[p][s] = -1

# 统计数据并储存
for p in range(len(persons)):
    for s in range(len(subjects)):
        if scores[p][s] != -1:
            person_average[p][0] += scores[p][s]
            person_average[p][1] += 1
            subject_average[0][s] += scores[p][s]
            subject_average[1][s] += 1

# 输出原始数据
'''
print("\t\t\t\t\t成绩单")
for s in subjects:
    print(s + "\t", end = "")
print("\n", end = "")
for p in range(len(persons)):
    for s in range(len(subjects)):
        print(str(scores[p][s]) + "\t", end = "")
    print(persons[p] + "\n", end = "")
'''

# 输出统计结果
#print("\n科目平均分")
for i in range(len(subjects)):
    #print(subjects[i] + ":", subject_average[0][i] / subject_average[1][i])
    value = subject_average[0][i] / subject_average[1][i]

#print("\n个人平均分")
for i in range(len(persons)):
    #print(persons[i] + ":", person_average[i][0] / person_average[i][1])
    value = person_average[i][0] / person_average[i][1]

time_end = time.time()
print("Finish in", (time_end - time_start), "seconds.")