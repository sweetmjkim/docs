<!-- - refer : screen definition
- 문제 제출자 작성 하기 : 4지 선다형, 5문항, 문항마다 다른 점수, 정답 입력
- 응시자 문제 풀기 : 응시자 이름 입력 -> 문제 풀기 -> 다음 응시자 여부(계속:c, 종료:x)
- 통계 : 각 응시자 채점, 과목 평균 표시
- Naming Rule(Sample) : Prefix(num_, str_, list_, dict_, mixed_)
- Dabase 설계 규칙 : 한 shell에는 묶음 datatype 안 넣기
- 산출물 : README.md(구성원별 역할 기록), 동작 Youtube 작성 -->

|역할| 담당자 |
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

<details>

  <summary>예제 탬플릿</summary>

  |예  제    탬  플  릿|보   기|정     답|
  |--|--|--|
  |데이터를 검색하고자 할 때 사용하는 언어는 무엇인가요?|	1)SQL  	2)HTML	3)Java	4)Python	|1|
  |중복된 데이터를 제거하고자 할 때 사용하는 용어는 무엇인가요?|	1)Delete	2)Update	3)Distinct	4)Select	|3|
  |여러 테이블을 연결하여 데이터를 가져올 때 사용하는 개념은 무엇인가요?|	1)Join	2)Union	3)Merge	4)Intersect	|1|
  |특정 조건을 만족하는 데이터를 선택하기 위해 사용하는 구문은 무엇인가요?|	1)Where	2)From	3)Group By	4)Order By	|1|
  |테이블의 구조를 정의하고 데이터를 저장하는 데 사용되는 객체는 무엇인가요?|	1)Index	2)View	3)Trigger	4)Table	|4|
  |데이터를 추가하거나 수정, 삭제하기 위해 사용하는 언어는 무엇인가요?|	1)SQL	2)JSON	3)XML	4)YAML	|1|
  |테이블 간의 관계를 정의하고 참조 무결성을 유지하기 위해 사용하는 개념은 무엇인가요?|	1)Index	2)Constraint	3)Procedure	4)Function	|2|
  |특정 컬럼을 기준으로 데이터를 정렬하기 위해 사용하는 구문은 무엇인가요?|	1)Order By	2)Group By	3)Having	4)Where	|1|
  |특정 컬럼을 기준으로 데이터를 그룹화하기 위해 사용하는 구문은 무엇인가요?|	1)Group By	2)Order By	3)Having	4)Where	|1|
  |특정 작업이 수행되기 전 또는 후에 자동으로 실행되는 코드 블록을 무엇이라고 하나요?|	1)Index	2)View	3)Trigger	4)Procedure	|3|

</details>
