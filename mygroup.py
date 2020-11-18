groupmates = [
 {
 "name": "Константин",
 "surname": "Краснов",
 "exams": ["Информатика", "ЭЭиС", "Web"],
 "marks": [5, 4, 5]
 },
 {
 "name": "Сергей",
 "surname": "Левин",
 "exams": ["История", "АиГ", "КТП"],
 "marks": [4, 5, 4]
 },
 {
 "name": "Андрей",
 "surname": "Воропаев",
 "exams": ["Философия", "ИС", "КТП"],
 "marks": [5, 5, 5]
 },
 {
  "name": "Владислав",
  "surname": "Макеев",
  "exams": ["Философия", "ИС", "КТП"],
  "marks": [3, 3, 4]
 },
 {
  "name": "Андрей",
  "surname": "Воробьев",
  "exams": ["Философия", "ИС", "КТП"],
  "marks": [4, 4, 4]
 }
]




def count_mark(students, mark):
 print(u"name".ljust(15), u"surname".ljust(10),  u"exams".ljust(30), u"marks".ljust(20))
 for student in students:
  marks_list = student['marks']
  result = (sum(marks_list) / len(marks_list))
  if result > mark:
   print(student["name"].ljust(15),
         student["surname"].ljust(10), str(student["exams"]).ljust(30),
         str(student["marks"]).ljust(20))


need = float(input('Input :'))

count_mark(groupmates, need)