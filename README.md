<!-- - refer : screen definition
- 문제 제출자 작성 하기 : 4지 선다형, 5문항, 문항마다 다른 점수, 정답 입력
- 응시자 문제 풀기 : 응시자 이름 입력 -> 문제 풀기 -> 다음 응시자 여부(계속:c, 종료:x)
- 통계 : 각 응시자 채점, 과목 평균 표시
- Naming Rule(Sample) : Prefix(num_, str_, list_, dict_, mixed_)
- Dabase 설계 규칙 : 한 shell에는 묶음 datatype 안 넣기
- 산출물 : README.md(구성원별 역할 기록), 동작 Youtube 작성 -->

|역할||
|--|--|
|문제 제출|김덕재(DB)|
|문제 풀이|김명준|
|통계|박요한|
|||

|||
|--|--|
|문제 collection|'Quiz_insert' (문제)|
|문제 답항 collection|'Quiz_answer' (보기,점수,정답)|
|입력자 collection|'Name_input' (이름)|
|입력자 답 collection|'Answer_input' (이름id,문제id,입력)|
|github|https://github.com/sweetmjkim/docs|
|DB|mongodb://192.168.0.92:27017|