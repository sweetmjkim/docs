from pymongo import MongoClient

def Connect_Mongo():
    mongoClient = MongoClient("mongodb://192.168.0.92:27017")
    database = mongoClient["local"]
    return database



database = Connect_Mongo()
Quiz_insert = database["Quiz_insert"]
Quiz_answer = database["Quiz_answer"]
Name_input = database["Name_input"]
Answer_input = database["Answer_input"]


while True : 
    user_name = input("응시자 : ")
    insert_name = Name_input.insert_one({"Names" : user_name })
    names_id = insert_name.inserted_id
    answers = list(Quiz_answer.find())
    question = list(Quiz_insert.find())

    for i in range(len(question)):
        questions = question[i]
        print(str(i+1) + "." + questions["questions"])
        for j in range(4):
            print(str(j+1) + "." + answers[i]["{}번".format(j+1)])
        answer = int(input(" 답 : "))
        Answer_input.insert_one( {'User_id' : names_id , 'Questions_id' : questions['_id'] ,  'Answers' : answer})    
    
    print("")
    keepgoing = input("다음 응시자가 있나요? (계속: c, 종료: x):")
    print("")
    if keepgoing == "c" :
        continue
    elif keepgoing =='x' : 
        print("----------" * 5)
        print("프로그램이 종료되었습니다.")
        break






    # while True:  
    #     todo_list = list(todos_list.find()) #위의 내용과 동일하다.
    #     inserted_participants = get_name()  #get_name()을 호출한 뒤 inserted_participants라고 변수로 지정한다.
    #     user_answer = survey(todo_list) #설문을 시작하는 survey를 설문의 내용과 같이 호출한 뒤 입력받을 내용을 user_answer라고 변수를 선언한다.
    #     status = stutus_input() # 사용자의 업무가 진행중 또는 완료 여부를 묻는 status_input function을 호출한 뒤 status라는 변수로 선언한다.
    #     update_database(user_answer,status,inserted_participants) #update_database function을 호출하면서, 위의 변수들을 같이 불러 값을 반영한다.
    #     exit = ' '
    #     while exit != "x" and exit != "X": 
    #         exit = input("설문을 계속 진행하시려면 'C', 프로그램을 종료하시려면 'X'를 입력해 주세요. :")
    #         if exit in ['c','C']:
    #             todo_list = list(todos_list.find()) 
    #             user_answer = survey(todo_list)
    #             status = stutus_input()
    #             Answers(answers, question)
    #         else:
    #             print("잘못 입력하셨습니다. 다시 입력해 주세요.")
    #     if exit in ["x","X"]:
    #         break