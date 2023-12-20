import parts.quiz_input_dj
import parts.Name_myungjun
from parts.teampj_result_yohan import Quest_result

parts.quiz_input_dj.input_questions() #퀴즈 내용 인풋
parts.Name_myungjun.quiz_program()  #이용자 퀴즈 풀기
runProgram=Quest_result('mongodb://192.168.0.92:27017',"local",'Quiz_insert','Quiz_answer','Name_input','Answer_input')
runProgram.cal_data()   #시험 결과 출력

