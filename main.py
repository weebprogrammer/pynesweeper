from random import randint
# Используется стандартная библиотека random для расставления бомб на поле
# игровое поле
gamefield = [[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
]

# Поле, которое видит игрок
userfield = [[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
]

# Вывод поля на экран
def printfield():
	for strings in userfield:
		print(*strings, sep=" ")

# Размещает бомбы на игровом поле
def bombplanter():
	for i in range(10):
		x = randint(0,7)
		y = randint(0,7)
		if gamefield[x][y] != "X":
			gamefield[x][y] = "X"

# Расставляет числа вокруг бомб
def bombcounter():
	for strings in gamefield:
		# Итерация по строкам поля
		for columns in range(8):
			# Итерация по значениям каждой строки и проверка условия для расставления чисел
			if strings[columns] == "X" and columns+1 < 8 and strings[columns+1] != "X":
				strings[columns+1] += 1
			if strings[columns] == "X" and columns-1 > -1 and strings[columns-1] != "X":
				strings[columns-1] += 1
			if strings[columns] == "X" and gamefield[gamefield.index(strings)-1][columns] != "X":
				gamefield[gamefield.index(strings)-1][columns] += 1
			if strings[columns] == "X" and gamefield.index(strings)+1 < 8 and gamefield[gamefield.index(strings)+1][columns] != "X":
				gamefield[gamefield.index(strings)+1][columns] += 1 
			if strings[columns] == "X" and gamefield.index(strings)+1 < 8 and columns+1 < 8 and gamefield[gamefield.index(strings)+1][columns+1] != "X":
				gamefield[gamefield.index(strings)+1][columns+1] += 1 
			if strings[columns] == "X" and gamefield.index(strings)+1 < 8 and columns-1 > -1 and gamefield[gamefield.index(strings)+1][columns-1] != "X":
				gamefield[gamefield.index(strings)+1][columns-1] += 1 
			if strings[columns] == "X" and columns+1 < 8 and gamefield[gamefield.index(strings)-1][columns+1] != "X":
				gamefield[gamefield.index(strings)-1][columns+1] += 1 
			if strings[columns] == "X" and columns-1 > -1 and gamefield[gamefield.index(strings)-1][columns-1] != "X":
				gamefield[gamefield.index(strings)-1][columns-1] += 1 

# Проверяет клетки, выбранные игроком 
def userchecker(x, y):
	if gamefield[x][y] == "X":
		print("YOU LOSE")
	if gamefield[x][y] == 0:
		
	if gamefield[x][y] != "X" and != 0:
		userfield[x][y] = gamefield[x][y]

bombplanter()
bombcounter()
userchecker(x, y)
printfield()
