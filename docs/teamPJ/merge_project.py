import parts.quiz_input_dj
import parts.Name_myungjun
from  parts.quiz_input_dj import Connect

database = Connect()
Quiz_insert = database["Quiz_insert"]
Quiz_answer = database["Quiz_answer"]
Name_input = database["Name_input"]         
Answer_input = database["Answer_input"]

parts.quiz_input_dj.input_questions() #퀴즈 내용 인풋
parts.Name_myungjun.quiz_program()  #이용자 퀴즈 풀기
from parts.teampj_result_yohan import Quest_result # 응시자 별 점수를 파악한 뒤 평균값을 구하기


