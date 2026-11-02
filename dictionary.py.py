#dictionary of students
student_data = {"id1":{"name": "Tuka" ,"class":"IX","subject":"coding, math, science" },
                "id2":{"name": "Tosan", "class":"V","subject":"coding, math, science" },
                "id3":{"name": "Dominic", "class":"VI","subject":"coding, math, science" }
                }
result = {}
seen_keys = []

for student_id, details in student_data.items():
    unique_key = (details["name"], details["class"], details["subject"])
    if unique_key not in seen_keys:
        seen_keys.append(unique_key)
        result[student_id] = details
for k, v in result.items():
    print(k, ":", v)
