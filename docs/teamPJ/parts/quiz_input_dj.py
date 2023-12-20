def Connect(): 
    from pymongo import MongoClient 
    mongoClient = MongoClient("mongodb://192.168.0.92:27017")
    database = mongoClient["local"]
    return database 

database = Connect() # Connect를 호출하여 MongoDB 내 Database까지 연결을 하고 이를 database라는 변수로 선언한다.
Quiz_insert = database["Quiz_insert"] # Mongo DB 내 'local 데이터베이스'에서 "Quiz_insert" 이라는 collection에 연결
Quiz_answer = database["Quiz_answer"]# Mongo DB 내 'local 데이터베이스'에서 "Quiz_answer" 이라는 collection에 연결

def input_questions():    
    num_answers= int(input("출제하실 문제 유형을 입력하세요. : ")) # 보기가 몇개인지를 입력받는 변수를 num_answers라고 지정
    num_questions = int(input("문항의 수를 입력하세요. : "))      # 질문이 몇개인지를 입력받는 변수를 num_questions라고 지정

    for i in range(num_questions):               # 질문의 개수만큼 반복 실행할 for 구문을 생성
        questions_title = input(str(i+1) + "번 문제를 입력하세요. : ")         # 입력받은 질문을 questions_title이라고 선언
        questions = Quiz_insert.insert_one({"questions" : questions_title})  # 입력받은 질문을 Quiz_insert라는 collection에 저장하고 이를 questions라는 변수로 선언
        questions_id = questions.inserted_id                                 # 저장한 질문의 _id를 가져와서 questions_id라고 변수 지정  
        for j in range(num_answers):                                  # 보기를 입력받는 것을 반복하는 반복문 생성
            question_answers = input(str(j+1) + "번 보기를 입력하세요. : ")    # 보기의 순서에 해당되는 보기를 입력받는 것을 question_answers라고 변수 지정
            answers = Quiz_answer.update_many( {'_id': questions_id },        # questions_id와 동일한 선상에 있는 답안을 Quiz_answer collection에 해당 번호의 key값에 위치한 value값으로 보기를 저장
                                                { "$set" : { (str(j+1)+"번") : question_answers } } ,upsert=True)
        points = int(input("배점을 입력하세요. : "))                          # 해당 문제의 배점을 입력받고 points 라는 변수로 선언
        Quiz_answer.update_one({'_id': questions_id }, { "$set" : { "점수" : points } } ,upsert=True ) # 입력받은 points를 Quiz_answers collection에 동일한 위치 선상에 저장하도록 한다.
        correct_answer = int(input("정답의 번호를 입력하세요. : "))            # 출제한 문제의 정답을 입력받고 correct_answer라는 변수로 선언한다.
        Quiz_answer.update_one({'_id': questions_id }, { "$set" : { "정답" : correct_answer } } ,upsert=True ) # 입력받은 correct_answer를 Quiz_answers collection에 동일한 위치 선상에 저장하도록 한다.
    return


