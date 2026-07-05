grades = {"Michael":96,"David":89,"Ana":94,"Rick":79,"Kel":95}

current = 0
total_score = 0
total_members = 5

for i in range(5):
    if current == 0:
        score = 96
    elif current == 1:
        score = 89
    elif current == 2:
        score = 94
    elif current == 3:
        score = 79 
    elif current == 4:
        score = 95
    else:
        break
    current += 1
    total_score = 96+89+94+79+95

average = total_score/5
print("Average is: ",average)
    
bottom_scorer = min(grades)
top_scorer = max(grades)
bottom_scorer = "Rick"
top_scorer = "Michael"
print("Bottom scorer:",bottom_scorer,",top scorer:",top_scorer)

student = input("Enter student's name: ")

answer = grades.get(student)

print(answer)