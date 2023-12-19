from pymongo import MongoClient


class Quest_result:

    def __init__(self,address,db,collection1,collection2,collection3,collection4) -> None:
        self.address=address
        self.db=db
        self.collection1=collection1
        self.collection2=collection2
        self.collection3=collection3
        self.collection4=collection4

        self.struct_correct_list=[]
        self.struct_score_list=[]
        self.name_list=[]
        self.get_answer_list=[]
        self.struct_question_list=[]
        self.struct_name_list=[]
        self.struct_id_list=[]
        pass

    def connect_mongo(self):
        mongoclient = MongoClient(self.address)
        db_local = mongoclient[self.db]
        self.QI_collection = db_local[self.collection1]
        self.QA_collection = db_local[self.collection2]
        self.NI_collection = db_local[self.collection3]
        self.AI_collection = db_local[self.collection4]
        return

    def get_answer(self):
        get_correct_list=list(self.QA_collection.find({},{})) #점수랑 정답 문제id 가져오기
        for i in range(len(get_correct_list)):
            self.struct_correct_list.append(get_correct_list[i]['정답']) #정답만 들어있는 리스트 저장
            self.struct_score_list.append(get_correct_list[i]['점수'])  #점수만 들어있는 리스트 저장
            self.struct_question_list.append(get_correct_list[i]['_id'])
        print("각 문항 정답 : ", end="")
        for i in range(len(self.struct_correct_list)):
            if i == len(self.struct_correct_list)-1:
                print("{}".format(self.struct_correct_list[i]))
                pass
            else:
                print("{},".format(self.struct_correct_list[i]), end="")
        pass
        return
                
    def struct_data(self):
        self.name_list=list(self.NI_collection.find({},{})) #이름과 이름 id 가져오기
        self.get_answer_list=list(self.AI_collection.find({},{})) #이름id, 문제id, 입력값 가져오기
        for i in range(len(self.name_list)):
            self.struct_name_list.append(self.name_list[i]['Names'])
            self.struct_id_list.append(self.name_list[i]['_id'])
            pass
        return

    def cal_data(self):
        self.connect_mongo()
        self.get_answer()
        self.struct_data()
        quest_id_list=[]
        answer_list=[]    
        numcount=0
        result_score=0
        print("응시자별 채점 결과")
        for i in range(len(self.name_list)):
            score = 0
            answer_list=[]
            Name = self.name_list[i]['Names']
            idset = self.struct_id_list[i]
            for j in range(len(self.get_answer_list)):
                if idset == self.get_answer_list[j]['User_id']:
                    quest_id_list.append(self.get_answer_list[j]['Questions_id']) #여기 최종 db랑 맞춰야됨
                    answer_list.append(self.get_answer_list[j]['Answers'])
                    pass
                pass
            for j in range(len(self.struct_correct_list)):
                if answer_list[j] == self.struct_correct_list[j]:
                    score += self.struct_score_list[j]
                    pass
                pass
            print("{} : {}".format(Name,score))
            numcount += 1
            result_score += score
            pass
        print("과목 평균 점수 : {}".format(result_score/numcount))
        return


# mongodb://192.168.0.92:27017 최종 주소
runProgram=Quest_result('mongodb://192.168.0.92:27017',"local",'Quiz_insert','Quiz_answer','Name_input','Answer_input')
runProgram.cal_data()