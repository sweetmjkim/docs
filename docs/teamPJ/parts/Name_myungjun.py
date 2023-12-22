from pymongo import MongoClient     # 

def Connect_Mongo():
    mongoClient = MongoClient("mongodb://192.168.10.236:27017")       # mongodb 연결
    database = mongoClient["local"]                                 # mongodb의 'local' 데이터베이스
    return database


database = Connect_Mongo()
Quiz_insert = database["Quiz_insert"]       # mongodb에서 'Quiz_insert' collection에 연결
Quiz_answer = database["Quiz_answer"]       # mongodb에서 'Quiz_answer' collection에 연결
Name_input = database["Name_input"]         # mongodb에서 'Name_input' collection에 연결
Answer_input = database["Answer_input"]     # mongodb에서 'Answer_input' collection에 연결

def quiz_program():
    while True :
        user_name = input("응시자 : ")                                   # 응시자 : 입력 받으면 user_name으로 담는다.
        insert_name = Name_input.insert_one({"Names" : user_name })     # mongodb에서 'Name_input' collection에 연결해서 user_name을 insert_name으로 담는다.
        names_id = insert_name.inserted_id                              # mongodb에서 'insert_name','inserted_id'를 names_id로 담는다.
        answers = list(Quiz_answer.find())                              # Quiz_answer에 있는 자료를 리스트화 시켜서 answers으로 지정한다.
        question = list(Quiz_insert.find())                             # Quiz_insert 있는 자료를 리스트화 시켜서 question으로 지정한다.

        for i in range(len(question)):                                  # question에 있는 갯수만큼 반복하도록 for문 작성한다.
            questions = question[i]                                     # question의 인덱스 값을 questions라는 변수로 지정한다.
            print(str(i+1) + "." + questions["questions"])              # 리스트에 저장된 값은 0부터 이므로 +1을 더해준 뒤 해당 문제를 출력해 준다.
            for j in range(4):                                          # 문제 보기를 출제하기 위하여 반복문을 사용
                print(str(j+1) + "." + answers[i]["{}번".format(j+1)])
            answer = int(input(" 답 : "))                               # 답의 입력값은 answer라는 변수로 지정한다.
            Answer_input.insert_one( {'User_id' : names_id , 'Questions_id' : questions['_id'] ,  'Answers' : answer})    
        
        print("")
        keepgoing = input("다음 응시자가 있나요? (계속: c, 종료: x):")      # "다음 응시자가 있나요?" (계속: c, 종료: x)
        print("")
        if keepgoing == "c" :
            continue
        elif keepgoing =='x' : 
            print("----------" * 5)
            print("프로그램이 종료되었습니다.")
            break
