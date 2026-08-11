exams = ['E1', 'E2', 'E3', 'E4', 'E5', 'E6']
slots = ['T1', 'T2', 'T3', 'T4']

constraints = {
    'E1': ['E2', 'E3'],
    'E2': ['E1', 'E4', 'E5'],
    'E3': ['E1', 'E5'],
    'E4': ['E2', 'E6'],
    'E5': ['E2', 'E3'],
    'E6': ['E4']
}

assignment = {}

def safe(exam, slot):
    for neighbor in constraints[exam]:
        if neighbor in assignment and assignment[neighbor] == slot:
            return False
    return True

def solve(index):
    if index == len(exams):
        return True

    exam = exams[index]

    for slot in slots:
        if safe(exam, slot):
            assignment[exam] = slot

            if solve(index + 1):
                return True

            del assignment[exam]

    return False

solve(0)

print("Exam Timetable")
for exam in exams:
    print(exam, "->", assignment[exam])
