from pymongo import MongoClient


class Quest_result:

    def __init__(self) -> None:
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

    def connect_mongo(self,address,DB,collection1,collection2,collection3,collection4):
        mongoclient = MongoClient(address)
        db_local = mongoclient[DB]
        self.QI_collection = db_local[collection1]
        self.QA_collection = db_local[collection2]
        self.NI_collection = db_local[collection3]
        self.AI_collection = db_local[collection4]
        return

    def get_answer(self):
        get_correct_list=list(self.QA_collection.find({},{})) #점수랑 정답 문제id 가져오기
        for i in range(len(get_correct_list)):
            self.struct_correct_list.append(get_correct_list[i][덕재님 정답 필드이름]) #정답만 들어있는 리스트 저장
            self.struct_score_list.append(get_correct_list[i][덕재님 점수값 필드이름])  #점수만 들어있는 리스트 저장
            self.struct_question_list.append(get_correct_list[i][덕재님 문제id 필드이름])
        print("각 문항 정답 : {}".format(self.struct_correct_list[덕재님 정답 필드이름]))
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
        self.get_answer_list=self.AI_collection.find({},{}) #이름id, 문제id, 입력값 가져오기
        # for i in range(len(get_answer_list)):
        #     self.struct_answer_list.append(get_answer_list[i][명준님 이름id 필드이름,명준님 정답 필드이름]) #입력만 들어있는 리스트 저장
        #     # self.struct_answerID_list.append(get_answer_list[i][명준님 이름id 필드이름])
        #     pass
        for i in range(len(self.get_answer_list)):
            if 
                
# AI에서 가져온 이름id와 NI에서 가져온 이름 id 비교
            # 비교한 내용에서 AI의 문제id와 QA에서의 문제id 비교
            # 비교한 내용에서 AI의 입력값과 QA에서의 정답값 비교
            # 비교한 내용에서 정답이면 QA의 점수값 출력 후 덧셈

    def run_result(self):
        print("응시자별 채점 결과")
        for i in range(len(self.name_list)):
            print("{} : {}".format(self.name_list[i],self.result))








runProgram=Quest_result('mongodb://192.168.0.92:27017',"local",'Quiz_insert','Quiz_answer','Name_input','Answer_input')