course_data = [ {'id':'HW1',
                 'title': 'Intro to Database Design',
                 'description': 'basics',
                 'due_date': '2026-01-20',
                 'score': 10,
                 },
                 {'id':'HW2',
                 'title': 'Homework 2: Normalization',
                 'description': 'learn normalization',
                 'due_date': '2026-01-26',
                 'score':100,}
                 
                 ]

course_data.append({'id':'HW3',
                    'title':'Homework 3 case study',
                    'description':'build a ERD',
                    'due_date':'2026-02-10',
                    'score': 100,
                    })
for assignment in course_data:
    print(f'title: {assignment["title"]}')

for assignment in course_data:
    if 'title' in assignment and assignment['title'] == 'Homework 3 case study':
        print(assignment)

counter = 0
for assignment in course_data:
    if 'title' in assignment and assignment['title'] == 'Homework 3 case study':
        print('Assignment index: ', counter)
        break
        counter += 1

for index, assignment in enumerate(course_data):
    if 'title' in assignment and assignment['title'] == 'Homework 3 case study':
        print('index using enum: ', index)