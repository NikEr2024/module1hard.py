grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

sorted(students)
x = sorted(students) # делаем в алфавитном порядке


print({x.pop(0): sum(grades[0]) / len(grades[0]),
       x.pop(0): sum(grades[1]) / len(grades[1]),
       x.pop(0): sum(grades[2]) / len(grades[2]),
       x.pop(0): sum(grades[3]) / len(grades[3]),
       x.pop(0): sum(grades[4]) / len(grades[4])})

