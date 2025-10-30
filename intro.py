gradebook = {
    "Alice":  {"Math": 90, "English": 88},
    "Bob":    {"Math": 76, "English": 92},
    "Charlie":{"Math": 85, "English": 78}
}
def average_grade(gradebook, subject):
    total = 0
    count = 0
    for subjects in gradebook.values():
        if subject in subjects:
            total += subjects[subject]
            count += 1
    return total / count if count > 0 else 0
for name, subjects in gradebook.items():
    print(f"{name} - Math: {subjects['Math']}, English: {subjects['English']}")
print(f"Average Math Grade: {average_grade(gradebook, 'Math'):.2f}")
print(f"Average English Grade: {average_grade(gradebook, 'English'):.2f}")