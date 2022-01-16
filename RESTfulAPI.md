## REST Api

### REST? (Representational State Transfer)
- 단어 그 자체로는 별 뜻 없는 단어임.
- 표준안이 존재하지 않고, 프로토콜을 가리키는 단어도 아님.

### What is REST ??
- Uniform (형식에 맞춘) -> 의미를 파악하기 쉬운 엔드포인트
- Stateless (어떠한 상태를 담지 않는) -> HTTP 주요한 특징 중 하나
- Cacheable (캐싱 가능한) -> 쿠키,세션 등을 통해 상태를 관리

### Implements
- Method 로 실제 행위를 구별(GET,POST,PATCH,PUT,DELETE...)
- Item(Entity), id 만을 URL 에 담음 (create, delete 같은 동사는 포함 X)
- "-"(대쉬, 하이픈) 사용. "_"(언더스코어) 사용X. (식별하기 힘들어짐)
- 파일 확장자는 uri 에 포함하지 않음 (좀 더 의미에 집중한 URL 권장)
- 대소문자를 구분해 사용하지 않고 소문자로만 사용함.

#### example
- GET + ITEMs 가져온다(복수)
- GET + ITEMs + id 가져온다(단수)
- POST + ITEMs 작성(생성)한다.
- PUT + ITEMs + id 수정한다.
- PATCH + ITEMs + id 일부 수정한다.
- DELETE + ITEMs + id 삭제한다.