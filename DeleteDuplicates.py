student_data = {
    "id1":{"name":"Sara","class":"V","subject integirations":"math,science,python"},
    "id2":{"name":"David","class":"V","subject integirations":"math,science,python"},
    "id3":{"name":"Sara","class":"V","subject integirations":"math,science,python"},
    "id4":{"name":"Michael","class":"V","subject integirations":"math,science,python"}
}

result = {}
seen_key = []

for studentid, details in student_data.items():
    uniqueid = (details["name"],details["class"],details["subject integirations"])
    if uniqueid not in seen_key:
        seen_key.append(uniqueid)
        result[studentid] = details

for k,v in result.items():
    print(k,":",v)
