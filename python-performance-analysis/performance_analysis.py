import csv

students = []

with open("students.csv", "r") as file:

    reader = csv.DictReader(file)

    for row in reader:

        java = int(row["java"])
        python = int(row["python"])
        math = int(row["math"])

        total = java + python + math
        average = total / 3

        if average >= 90:
            grade = "A+"
        elif average >= 80:
            grade = "A"
        elif average >= 70:
            grade = "B"
        elif average >= 60:
            grade = "C"
        elif average >= 50:
            grade = "D"
        else:
            grade = "F"

        students.append({
            "id": row["id"],
            "name": row["name"],
            "total": total,
            "average": average,
            "grade": grade
        })


print("\n===== STUDENT PERFORMANCE ANALYSIS =====")

for student in students:

    print(
        "ID:", student["id"],
        "| Name:", student["name"],
        "| Total:", student["total"],
        "| Average:", round(student["average"], 2),
        "| Grade:", student["grade"]
    )