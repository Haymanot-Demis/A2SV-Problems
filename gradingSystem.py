def gradingStudents(grades):
    # Write your code here
    for i in range(1, grades[0] + 1):
        print(i)
        if(grades[i] < 38):
            continue
        elif grades[i] % 5 >= 3:
            grades[i] = grades[i] - grades[i] % 5 + 5
    
    return grades


grades = [4, 73, 67, 38, 58];   

print(gradingStudents(grades))
