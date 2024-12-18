# zyDE 11.3.1: Iterating over a dictionary example: Gradebook statistics.
# Print the name and grade percentage of the student with the highest total of points.
# Find the average score of each assignment.
# Find and apply a curve to each student's total score, such that the best student has 100% of the total points.
# student_grades contains scores (out of 100) for 5 assignments

def printGradeBook(gradesDict):
    print(f"{'Name':15s} {'Asgn1':5s} {'Asgn2':5s} {'Asgn3':5s} "
          f"{'Asgn4':5s} {'Asgn5':5s} {'Curve':5s}")






def applyCurve(gradesDict, curve):
    # Find and apply a curve to each student's total score, such that the best student has 100% of the total points.
    print('\n')




    print(f'\nThis is the updated dictionary: \n {gradesDict}')

def asgnAverage(gradesDict):
    # Find the average score of each assignment.
    totAsgn = [0, 0, 0, 0, 0]

    for scores in gradesDict.values():
        for i in range(len(scores)):
            totAsgn[i] += scores[i]

    for i in range(len(totAsgn)):
        print(f'Average for assignment #{i + 1:d}: {totAsgn[i] / len(gradesDict):.1f}')
    return

def highestPercent(gradesDict):
    # Locate student with highest percent average across all assignments. Also return curve.
    totPoints = 0
    percentage = 0.0
    topScoreName = ''

    for name, grades in gradesDict.items():
        if sum(grades) > totPoints:
            topScoreName = name
            percentage = sum(grades) / len(grades)

    print(f'\n{topScoreName} had the highest score with an average of: {percentage:.1f}%\n')
    curve = (100 - percentage) * 5  # The curve needs to be multiplied by 5 for total of 5 tests
    return round(curve,1)   # changed from video

def main():
    student_grades = {
        'Andrew': [56, 79, 90, 22, 50],
        'Nisreen': [88, 62, 68, 75, 78],
        'Alan': [95, 88, 92, 85, 85],
        'Chang': [76, 88, 85, 82, 90],
        'Tricia': [99, 92, 95, 89, 99]
    }
    print(f'\nThis is the dictionary: \n {student_grades}')
    asgnAverage(student_grades)  # changed order
    curve = highestPercent(student_grades)
    # applyCurve(student_grades, curve)
    # printGradeBook(student_grades)

main()