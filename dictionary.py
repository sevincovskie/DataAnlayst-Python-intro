# dictionary-açar–dəyər (key–value)
# Dictionary istifadə edilir, əgər:
# bir məlumatı başqa bir məlumatla əlaqələndirmək lazımdırsa
# axtarış sürətli olmalıdırsa
# məlumat ad–qiymət, id–obyekt, status–dəyər formasındadırsa
# Misallar:
# istifadəçi məlumatları
# konfiqurasiya faylları
# JSON strukturları
# sayğaclar (frequency count)

# Əgər key yoxdursa → KeyError



# student = {
#     "name": "Sevinc",
#     "age":25,
#     "courses": ["Math", "Science"],
#     "city": "Baku"
# }
# print(student)

# print(student["name"])
# print(student["age"])               
# print(student["courses"])
# print(student.get("name"))
# student.get("email") # → None

# for k in student:
#     print(k)

# for v in student.values():
#     print(v)
# for k, v in student.items():
#     print(k, v)

# dictionary methods-> update, keys, values, items




# zip-> birlesdirmek
# name= ["Sevinc", "Sona", "Matt"]
# surname=["Yusifova", "Alakbarova", "Smith"]
# fullname= dict(zip(name, surname))
# print(fullname)

companies = {
    "Google": "Larry Page",
    "Apple": "Tim Cook",
    "Meta": "Mark Zuckerberg"
}
for company, ceo in companies.items():
    print(f"{company} has CEO {ceo}")
    
# enumerate-> index, value gosterir
    
for index, company in enumerate(companies):
    print(f"{index}. {company}")
    
    
    # split-> stringi listə çevirir
    