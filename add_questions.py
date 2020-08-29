from google.cloud import firestore

import json

def get_questions_list():
    with open('questions.json', 'r') as questions_file:
        questions_dict = json.load(questions_file)
    questions_list = []
    for question in questions_dict.values():
        questions_list.append(question)
    return questions_list

# print(get_questions_list())

def add_from_dict():
    db = firestore.Client()
    questions_dict = get_questions_list()

    # city = City(name=u'Tokyo', state=None, country=u'Japan')
    # db.collection(u'questions').add(city.to_dict())

    # db.collection(u'questions').add(city.to_dict())
    for question in get_questions_list():
        question_dict = {"question_text": question}
        db.collection(u'questions').add(question_dict)
        print(f"printing: {question_dict}")

add_from_dict()


