# 10. Testing
print('Testing:')

def get_formatted_name(first, last, middle=''):
	"""Строит отформатированное полное имя."""
	if middle:
		full_name = first + ' ' + middle + ' ' + last
	else:
		full_name = first + ' ' + last
	return full_name.title()

# def get_formatted_name(first, last):
	# """Строит отформатированное полное имя."""
	# full_name = first + ' ' + last
	# return full_name.title()

# def get_formatted_name(first, middle, last):
	# """Строит отформатированное полное имя."""
	# full_name = first + ' ' + middle + ' ' + last
	# return full_name.title()


from survey import AnonymousSurvey

# Определение вопроса с созданием экземпляра AnonymousSurvey.
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

# Вывод вопроса и сохранение ответов.
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
	response = input("Language: ")
	if response == 'q':
		break
	my_survey.store_response(response)

# Вывод результатов опроса.
print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()
