grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = sorted(list(students))
lst_of_stud_average_grades = {k: sum(v)/len(v) for k, v in zip(students, grades)}
print(lst_of_stud_average_grades)