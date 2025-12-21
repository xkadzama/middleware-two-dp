
date = ['10', '05', '2025']
validate = [num.isdigit() for num in date]

if False in validate:
	print('Ошибка')
else:
	print('Все правильно!')