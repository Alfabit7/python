import controller
# base= [ {Familiya:  [ {Biologiya:[5,4,5,4]}, { geografiya:[5,4,5,4] }, {himiya: [5,4,5,4]} ] }    ]
# base=  List [ dict {fio: list [{predmet: ocenka}] }   ]
# shoolBase = [{'Иванов': {'География': [4, 5, 4, 5, 5]}, {'Биология': [4, 5, 4, 5, 5]}, {'Химия': [4, 5, 4, 5, 5]}, {'Рисование': [4, 5, 4, 5, 5]}   }]
# lessonName = 'География'
# nameUser = 'Иванов Сергей'
# usersList = [nameUser, nameUser, nameUser, nameUser]
# gradeUser = 5
# gradeLessonDict = {lessonName: [gradeUser, gradeUser, gradeUser]}
# itemsLessonList = [gradeLessonDict, gradeLessonDict,
#                    gradeLessonDict, gradeLessonDict]
# userDict = {nameUser: itemsLessonList}
# generalList = [userDict, userDict, userDict, userDict]
controller.start()

# [ {fio: { {predmet:[grade]}, {predmet:[grades]} }  fio}]
