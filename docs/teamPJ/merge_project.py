import parts.quiz_input_dj
parts.quiz_input_dj.input_questions()

import parts.Name_myungjun
parts.Name_myungjun.quiz_program()

from parts.teampj_result_yohan import Quest_result

runProgram=Quest_result('mongodb://192.168.0.92:27017',"local",'Quiz_insert','Quiz_answer','Name_input','Answer_input')
runProgram.cal_data()

