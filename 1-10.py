###
# Prints test results
#

test_results = [
   False, True, False, True, True,
   True, True, False, True, True,
   False, True, True, True, False
]

question_number = len(test_results)     # Number of questions

correct_answers = 0     # Number of correct answers
for answer in test_results:
   if answer:
      correct_answers += 1

incorrect_answers = question_number - correct_answers   # Number of incorrect answers

percentage_correct = (correct_answers / question_number) * 100  # Percentage of correct answers

print('TEST STATISTICS')
print('===============')
print(f'Number of questions: {question_number}')
print(f'Number of correct answers: {correct_answers}')
print(f'Number of incorrect answers: {incorrect_answers}')
print(f'Percentage of correct answers: {percentage_correct:.2f}%')
