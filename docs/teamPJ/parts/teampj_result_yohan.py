from pymongo import MongoClient


class Quest_result:

    def __init__(self,address,db,collection1,collection2,collection3,collection4) -> None:
        self.address=address
        self.db=db
        self.collection1=collection1
        self.collection2=collection2
        self.collection3=collection3
        self.collection4=collection4

        # self.struct_answer_list=[]
        self.struct_correct_list=[]
        self.struct_score_list=[]
        self.name_list=[]
        self.get_answer_list=[]
        self.result=0
        self.struct_question_list=[]
        # self.struct_name_list=[]
        # self.struct_id_list=[]
        # self.struct_answerID_list=[]
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

    def get_name(self):
        self.name_list=list(self.NI_collection.find({},{})) #이름과 이름 id 가져오기
        # for i in range(len(name_list)):
        #     self.struct_name_list.append(name_list[i][명준님 id 필드이름, 명준님 이름 필드이름])
        #     # self.struct_id_list.append(name_list[i][명준님 id 필드이름])
        #     pass
        return

    def cal_result(self):
        self.get_answer_list=list(self.AI_collection.find({},{})) #이름id, 문제id, 입력값 가져오기
        # for i in range(len(get_answer_list)):
        #     self.struct_answer_list.append(get_answer_list[i][명준님 이름id 필드이름,명준님 정답 필드이름]) #입력만 들어있는 리스트 저장
        #     # self.struct_answerID_list.append(get_answer_list[i][명준님 이름id 필드이름])
        #     pass
        count_index=[]
        for i in range(len(self.get_answer_list)):
            for j in range(len(self.name_list)):
                if self.get_answer_list[j]['명준님 AI 이름id'] in self.name_list[i]['명준님 NI 이름ID']:
                    count_index.append(self.name_list[j]['명준님 AI 문제id'])
                    pass
                pass
            pass
        # for i in range():

                
    # AI에서 가져온 이름id와 NI에서 가져온 이름 id 비교
            # 비교한 내용에서 AI의 문제id와 QA에서의 문제id 비교
            # 비교한 내용에서 AI의 입력값과 QA에서의 정답값 비교
            # 비교한 내용에서 정답이면 QA의 점수값 출력 후 덧셈

    def run_result(self):
        print("응시자별 채점 결과")
        for i in range(len(self.name_list)):
            print("{} : {}".format(self.name_list[i],self.result))








runProgram=Quest_result('mongodb://192.168.0.92:27017',"local",'Quiz_insert','Quiz_answer','Name_input','Answer_input')
runProgram.connect_mongo()
runProgram.get_answer()
runProgram.get_name()
runProgram.cal_result()