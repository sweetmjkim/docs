from pymongo import MongoClient


class Quest_result:

    def __init__(self) -> None:
        self.struct_answer_list=[]
        self.struct_correct_list=[]
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
        get_correct_list=list(self.QA_collection.find({})) #점수랑 정답 가져오기
        for i in range(len(get_correct_list)):
            self.struct_correct_list.append(get_correct_list[i][덕재님 입력값 필드이름]) #정답만 들어있는 리스트 저장
        print("각 문항 정답 : {}".format(self.struct_correct_list[덕재님 입력값 필드이름]))
        pass

    def cal_result(self):
        get_answer_list=self.AI_collection.find({}) #이름id, 문제id, 입력값 가져오기
        for i in range(len(get_answer_list)):
            self.struct_answer_list.append(get_answer_list[i][명준님 정답 필드이름]) #입력만 들어있는 리스트 저장
            pass


    def run_result(self):
        print("응시자별 채점 결과")
        name_list=list(self.NI_collection.find({}))
        struct_name_list=[]
        for i in range(len(name_list)):
            struct_name_list.append(name_list[i][명준님 이름 필드이름])
            pass








runProgram=Quest_result('mongodb://192.168.0.92:27017',"local",'Quiz_insert','Quiz_answer','Name_input','Answer_input')