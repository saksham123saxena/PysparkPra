student_detail = [
    {
        "name": "hello",
        "roll": 6,
        "age": 21,
        "course": "python"
    },
    {
        "name": "hello1",
        "roll": 16,
        "age": 24,
        "course": "java"
    }
]


def add_new_student(name, roll, age, course):
    new_student = {"name": name, "roll": roll, "age": age, "course": course}
    student_detail.append(new_student)
    print(student_detail)


add_new_student("testing", 12, 21, "cpp")
print(student_detail)
