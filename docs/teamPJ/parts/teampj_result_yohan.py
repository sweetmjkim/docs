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
        self.QI_collection = db_local[self.collection1] # db에 저장되어 있는 각각의 collection 접속
        self.QA_collection = db_local[self.collection2]
        self.NI_collection = db_local[self.collection3]
        self.AI_collection = db_local[self.collection4]
        return

    def get_answer(self):
        get_correct_list=list(self.QA_collection.find({},{})) #점수랑 정답 문제id 가져오기
        for i in range(len(get_correct_list)):
            self.struct_correct_list.append(get_correct_list[i]['정답']) #정답만 들어있는 리스트 저장
            self.struct_score_list.append(get_correct_list[i]['점수'])  #점수만 들어있는 리스트 저장
            self.struct_question_list.append(get_correct_list[i]['_id']) # 문제의 id만 들어있는 리스트 저장
        print("각 문항 정답 : ", end="")
        for i in range(len(self.struct_correct_list)):
            if i == len(self.struct_correct_list)-1:
                print("{}".format(self.struct_correct_list[i])) # 저장되어 있는 정답 문항 리스트 출력
                pass
            else:
                print("{},".format(self.struct_correct_list[i]), end="")
        pass
        return
                
    def struct_data(self):
        self.name_list=list(self.NI_collection.find({},{})) #이름과 이름 id 가져오기
        self.get_answer_list=list(self.AI_collection.find({},{})) #이름id, 문제id, 입력값 가져오기
        for i in range(len(self.name_list)):
            self.struct_name_list.append(self.name_list[i]['Names']) # 가져온 이름만 들어있는 리스트 저장
            self.struct_id_list.append(self.name_list[i]['_id']) # 가져온 유저의 id만 들어있는 리스트 저장
            pass
        return

    def cal_data(self):
        self.connect_mongo() # 몽고접속 실행
        self.get_answer()   # 문항 정답 펑션 실행
        self.struct_data() # 각 db항목에 대한 리스트 정제
        quest_id_list=[] # 문제 id를 호출하여 대조할 리스트 초기화
        answer_list=[]    # 문제 id에 대응하는 유저의 답변 리스트 초기화
        numcount=0  # 총 인원수 카운팅
        result_score=0  # 총 점수 카운팅
        print("응시자별 채점 결과")
        for i in range(len(self.name_list)):
            score = 0   # 하나의 유저에 대한 점수 합계를 위해 초기화
            answer_list=[] # 호출한 답변 리스트 사람에 맞게 저장하기 위해 초기화
            Name = self.name_list[i]['Names'] # 유저 이름 저장
            idset = self.struct_id_list[i]  # 유저 id 저장
            for j in range(len(self.get_answer_list)):
                if idset == self.get_answer_list[j]['User_id']:
                    quest_id_list.append(self.get_answer_list[j]['Questions_id']) #문제 id 저장
                    answer_list.append(self.get_answer_list[j]['Answers'])  # 답변 저장
                    pass
                pass
            for j in range(len(self.struct_correct_list)):
                if answer_list[j] == self.struct_correct_list[j]:  #유저의 답변과 호출하여 저장한 문제의 답이 맞다면
                    score += self.struct_score_list[j]  # 스코어에 문제의 점수를 저장해라
                    pass
                pass
            print("{} : {}".format(Name,score))
            numcount += 1   # 한번 돌때마다 사람수 카운트
            result_score += score   # 총 점수는 한번 돌때마다 스코어의 합산
            pass
        if numcount==0:
            numcount = 1
            print("과목 평균 점수 : {}".format(result_score/numcount))
            pass
        else:
            print("과목 평균 점수 : {}".format(result_score/numcount))
            pass
        return
    

if __name__ == "__main__":
    runProgram=Quest_result('mongodb://localhost:27017',"local",'Quiz_insert','Quiz_answer','Name_input','Answer_input')
    runProgram.cal_data()

runProgram=Quest_result('mongodb://192.168.10.236:27017',"local",'Quiz_insert','Quiz_answer','Name_input','Answer_input')
runProgram.cal_data()   #시험 결과 출력
