def Connect(): 
    from pymongo import MongoClient 
    mongoClient = MongoClient("mongodb://localhost:27017")
    database = mongoClient["local"]
    return database 

database = Connect() # Connect를 호출하여 MongoDB 내 Database까지 연결을 하고 이를 database라는 변수로 선언한다.
Quiz_insert = database["Quiz_insert"] # Mongo DB 내 'local 데이터베이스'에서 "todos_list" 이라는 collection에 연결
Quiz_answer = database["Quiz_answer"]# Mongo DB 내 'local 데이터베이스'에서 "participants" 이라는 collection에 연결


num_answers= int(input("출제하실 문제 유형을 입력하세요. : "))
num_questions = int(input("문항의 수를 입력하세요"))

for i in range(len(num_questions)+1):
    questions_title = input(str(i+1) + "번 문제를 입력하세요. : ")
    questions = Quiz_insert.insert_one({"questions" : questions_title})
    questions_id = questions.inserted_id
    for j in range(len(num_answers)+1):
        question_answers[j] = input(str(j+1) + "번 보기를 입력하세요. : ")
        answers = Quiz_answer.update_one( {'_id': questions_id },
                                         { "$set" : { (str(j+1)+"번") : question_answers[j] } } ,upsert=True)
    points = str(input("배점을 입력하세요. : "))
    Quiz_answer.update_one({'_id': questions_id }, { "$set" : { ("점수") : points } } ,upsert=True )
    correct_answer = str(input("정답의 번호를 입력하세요. : "))
    Quiz_answer.update_one({'_id': questions_id }, { "$set" : { ("점수") : points } } ,upsert=True )
