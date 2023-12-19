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