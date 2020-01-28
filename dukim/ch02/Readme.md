# Chapter 2_파이썬스러운(pythonic) 코드
- idiom(관용구)
    - 특정 작업을 수행하기 위해 코드를 작성하는 특별한 방법
    - 디자인 패턴과는 다름
    - 디자인 패턴은 언어와는 무관한 고차원의 개념
        - https://en.wikipedia.org/wiki/Design_Patterns
    - 관용구를 따르는 코드를 파이썬스럽다(Pythonic)고 함
- 파이썬스러운 코드를 작성하는 이유
    - 더 나은 성능
    - 동일한 패턴과 구조에 익숙해 지면 실수를 줄이고 문제의 본질에 보다 집중할 수 있음
- 이 장의 목표
    - 인덱스와 슬라이스를 이해하고 인덱싱 가능한 객체를 올바른 방식으로 구현
    - 시퀀스와 이터러블 구현하기
    - 컨텍스트 관리자를 만드는 모범 사례 연구
    - 매지 메서드를 사용해 보다 관용적인 코드 구현
    - 파이썬에서 부작용을 유발하는 흔한 실수 피하기
    
### 인덱스와 슬라이스
- 일부 데이터 구조나 타입은 자신이 가지고 있는 요소에 인덱스를 통해 접근하는 것을 지원
- 음수 인덱스를 사용하여 끝에서부터 접근이 가능
    ``` 
    my_numbers = (4, 5, 3, 9)
    my_numbers[-1]
    my_numbers[-3]  
    ```
- slice를 사용하여 특정 구간의 요소를 구할 수 있음
    ``` 
    my_numbers = (1, 1, 2, 3, 5, 8, 13, 21)
    my_numbers[2:5]
    ```
- slice의 시작 인덱스는 포함, 끝 인데스는 제외하고 선택
- 시작, 끝, 간격 파라미터 중 하나를 제외할 수 있음
    ```
    my_numbers[:3]
    my_numbers[3:]
    my_numbers[::]  # 원래 튜플의 복사본 생성
    my_numbers[1:7:2]
    ```
- 시퀀스에 간격을 전달할 때 실제로는 슬라이스를 전달하는 것과 같음
    ``` 
    interval = slice(1, 7, 2)
    my_numbers[interval]
    interval = slice(None, 3)
    my_numbers[interval] == my_mumbers[:3]
    ```
- slice의 (시작, 중지, 간격) 중 하나를 지정하지 않은 경우 None으로 간주
- 튜플, 문자열, 리스트의 특정 요소를 가져올땐 for루프 대신 인덱스와 슬라이스를 이용한 방법이 좋음
- 번외) is vs ==
    ``` 
    a = 1
    a == 1
    a is 1
  
    a = 257
    a == 257
    a is 257
    ``` 
#### 자체 시퀀스 생성
- 인덱스와 슬라이스 기능은 ```__getitem__```이라는 매직 메소드 덕분에 동작함
- myobject[key]와 같은 형태를 사용할 때 ```__getitem__``` 메소드의 파라미터로 전달
- 시퀀스는 ```__getitem__```과 ```__len__```을 모두 구현하는 객체
- 시퀀스의 예 : 리스트, 튜플, 문자열
- 사용자정의 클래스에 ```__getitem__```을 구현하는 방식
    - 캡슐화 방식
        ``` 
        class Items:
            def __init__(self, *values):
                self._values = list(values)
            def __len__(self):
                return len(self._values)
            def __getitem__(self, item):
                return self._values.__getitem__(item)
        ```
    - 상속
        - collections.UserList 부모 클래스를 상속해야 함
    - 자신만의 시퀀스를 구현
        - 범위로 인덱싱하는 결과는 해당 클래스와 같은 타입의 인스턴스여야 함
            - 리스트의 일부를 가져오면 결과는 리스트
            - 튜플에서 특정 range를 요청하면 결과는 튜플
            - substring의 결과는 문자열
            ``` 
            range(1, 100)[25:50]
            ```
        - slice에 의해 제공된 범위는 마지막 요소는 제외해야 함
     
### 컨텐스트 관리자(context manager)
- 주요 동작의 전후에 작업을 실행하려고 할 때 유용
- 리소스 관리와 관련하야 컨텍스트 관리자를 자주 볼 수 있음
    ``` 
    fd = open(filename)
    try:
        process_file(fd)
    finally: fd.close()
    ```
  
    ``` 
    with open(filename) as fd:
        process_file(fd)
    ```
    - with 문(pep-343)은 컨텍스트 관리자로 진입
    - open 함수는 컨텍스트 관리자 프로토콜을 구현
- ```__enter__```와 ```__exit__``` 두개의 메서드로 구성
- 관심사를 분리하고 독립적으로 유지되어야하는 코드를 분리하는 좋은 방법
    ``` 
    def stop_database():
        run("systemctl stop postgresql.server")
    def start_database():
        run("systemctl start postgresql.server")
    
    class DBHandler:
        def __enter__(self):
            stop_database()
            return self
        def __exit__(self, exc_type, ex_value, ex_traceback):
            start_database()
    
    def db_backup():
        run("pg_dump database")
  
    def main():
        with DBHandler():
            db_backup()
    ```
    - ```__enter__```에서 무언가를 반환하는 것은 좋은 습관
    - ```__exit__```는 블록에서 발생한 예외를 파라미터로 받음
        - 블록에 예외가 없으면 모두 None
        - True를 반환하면 예외를 호출자에게 전파하지 않고 멈춤(True 반환하지 않도록 주의 필요)

#### 컨텍스트 관리자 구현
- contextlib 모듈은 컨텍스트 관리자를 구현하는데 도움이 되는 도우미 함수와 객체를 제공
- contextlib.contextmanager 데코레이터를 적용하면 해당 함수의 코드를 컨텍스트 관리자로 변환
    - 함수는 제너레이터라는 특수한 함수의 형태여야 함
    - yield 전후 문장을 ```__enter__```와 ```__exit__```로 구분
    - ```__enter__```에서 반환값 지정도 가능
    ``` 
    @contextlib.contextmanager
    def db_handler():
        stop_database()
        yield
        start_database()
  
    def main():
        with db_handler():
            db_backup()
    ```
- contextlib.ContextDecorator 클래스
    - 컨텍스트 관리자 안에서 실행될 함수에 데코레이터를 적용하기 위한 로직을 제공하는 믹스인 클래스
    ``` 
    class dbhandler_decorator(contextlib.ContextDecorator):
        def __enter__(self):
            stop_database()
        def __exit__(self, exc_type, ex_value, ex_traceback):
            start_database()

    @dbhandler_decorator()
    def offline_backup():
        print("pg_dump database")
    
    def main():
        offline_backup()
    ```
    - with문이 없음
    - 컨텍스트 관리자 내부에서 사용하고자 하는 객체를 얻을수 없음
        - with offline_backup() as bp:
        - ```__enter__``` 메서드가 반환한 객체를 사용해야 하는 경우는 이전의 접근방식을 선택
- contextlib.suppress는 제공한 예외 중 하나가 발생한 경우에는 실패하지 않도록 함
    ``` 
    import contextlib
    
    with contextlib.suppress(DataConversionException):
        parse_data(input_json_or_dict)
    ```
### 프로퍼티, 속성과 객체 메서드의 다른 타입들
- 파이썬 객체의 모든 프로퍼티와 함수는 public
- 밑줄로 시작하는 속성은 해당 객체에 대해 private을 의미
    - 외부에서 호출하지 않기를 기대하는 것(문법상 사용 가능)
#### 파이썬에서의 밑줄
``` 
class Connector:
    def __init__(self, source):
        self.source = source
        self._timeout = 60
conn = Connector("postgresql://localhost")
conn.source
conn._timeout
conn.__dict__
```
- ```_timeout```은 Connector 클래스 안에서만 사용되고 호출자는 이 속성에 접근하지 않아야 함
- 동일한 원칙이 메소드에도 적용
- 이중 밑줄
    - private이 아님
    - 여러 번 확장되는 클래스의 메서드를 이름 충돌 없이 오버라이드하기 위해 만들어졌음
    - name mangling이라 부름
        - ```_<class-name>__<attribute-name>``` 형태로 만들어짐
    - 의도한 것이 아니라면 사용 금지
#### 프로퍼티
- 다른 프로그래밍 언어에서는 접근 메서드를 만들지만 파이썬에서는 프로퍼티를 사용함
``` 
class User:
    def __init__(self, username):
        self.username = username
        self._email = None

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, new_email):
        if not is_valid_email(new_email):
            raise ValueError(f"유효한 이메일이 아니므로 {new_email} 값을 사용할 수 없음")
        self._email = new_email
```
- 대부분의 경우 일반 속성을 사용하는 것으로 충분
- 특별한 로직이 필요한 경우에만 프로퍼티 사용 권장함
- 프로퍼티는 명령-쿼리 분리 원칙(command and query separation)을 따르기 위한 좋은 방법
    - ```@property```는 응답을 위한 쿼리
    - ```@<property_name>.setter```는 무언가를 하기 위한 커맨드
### 이터러블 객체
- 이터러블은 ```__iter__``` 매직 메서드를 구현한 객체
- 이터레이터는 ```__next__``` 매직 메서드를 구현한 객체
- 파이썬 반복은 이터러블 프로토콜이라는 자체 프로토콜을 사용해 동작
    - ```for e in myobject:```
    - 객체가 ```__next__```나 ```__iter__``` 이터레이터 메서드 중 하나를 포함하는지 여부
    - 객체가 시퀀스이고 ```__len__```과 ```__getitem```을 모두 가졌는지 여부
#### 이터러블 객체 만들기
- 객체를 반복하려고 하면 iter() 함수를 호출
    - 해당 객체에 ```__iter__``` 메서드가 있는지 확인하고 실행
    ``` 
    class DateRangeIterable:
    """자체 이터레이터 메서드를 가지고 있는 이터러블"""

    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        self._present_day = start_date

    def __iter__(self):
        return self

    def __next__(self):
        if self._present_day >= self.end_date:
            raise StopIteration
        today = self._present_day
        self._present_day += timedelta(days=1)
        return today
    ```
    - next() 함수를 호출하면 ```__next__``` 메서드에게 위임
    - 끝에 도달한 이후에도 호출하면 StopIteration 예외 발생
- 컨테이너 이터러블(container iterable)
    ``` 
    class DateRangeContainerIterable:
        def __init__(self, start_date, end_date):
            self.start_date = start_date
            self.end_date = end_date
    
        def __iter__(self):
            current_day = self.start_date
            while current_day < self.end_date:
                yield current_day
                current_day += timedelta(days=1)
    ```
    - for 루프는 ```__iter__```를 호출하고 ```__iter__```는 제너레이터를 생성
#### 시퀀스 만들기
- iter() 함수
    - ```__iter__``` -> ```__getitem__```순으로 찾음
    - 없을시 TypeError를 발생
- 시퀀스는 ```__len__```과 ```__getitem__```을 구현
- 이터러블 객체는 메모리를 적게 사용하고 n번째 요소 검색에 O(n)의 시간 복잡도를 갖음
- 시퀀스는 많은 메모리를 사용하지만 인덱싱의 시간복잡도는 O(1)임
    ``` 
    class DateRangeSequence:
        def __init__(self, start_date, end_date):
            self.start_date = start_date
            self.end_date = end_date
            self._range = self._create_range()
    
        def _create_range(self):
            days = []
            current_day = self.start_date
            while current_day < self.end_date:
                days.append(current_day)
                current_day += timedelta(days=1)
            return days
    
        def __getitem__(self, day_no):
            return self._range[day_no]
        def __len__(self):
            return len(self._range)
    ```

### 컨테이너 객체
- ```__contains__``` 메서드를 구현한 객체로 Boolean 값을 반환
- in 키워드가 발견될 때 호출
    ``` 
    element in container
    ```
    ``` 
    container.__contains__(element)
    ```
- 코드 리팩토링
    ``` 
    def mark_coodinate(grid, coord):
        if 0 <= coord.x < grid.width and 0 <== coord.y < grid.height:
            grid[coord] = MARKED
    ```

    ``` 
    class Boundaries:
        def __init__(self, width, height):
            self.width = width
            self.height = height
            
        def __contains__(self, coord):
            x, y = coord
            return 0 <= x < self.width and 0 <= y < self.height
    
    class Grid:
        def __init__(self, width, height):
            self.width = width
            self.height = height
            self.limits = Boundaries(width, height)
        
        def __contains__(self, coord):
            reutrn coord in self.limits
            
    def mark_coodinate(grid, coord):
        if coord in grid:
            grid[coord] = MARKED            
    ``` 
### 객체의 동적인 속성
- ```__getattr__``` 매직 메서드를 사용해 객체에서 속성을 얻는 방법을 제어 가능
- ```<myobject>.<myattribute>```를 호출하면 객체의 사전에서 ```<myattribute>```를 찾음
    - ```__getattribute__```를 호출
    - 속성이 없는 경우 속성의 이름을 파라미터로 전달하여 ```__getattr__``` 메서드 호출
 
### 호출형(callable) 객체
- ```__call__```을 사용하면 객체를 일반 함수처럼 호출할 수 있음
- 함수 호출 사이에 정보를 저장할 수 있음
    ``` 
    class CallCount:
        def __init__(self):
            self._counts = defaultdict(int)
        def __call__(self, argument):
            self._counts[argument] += 1
            return self._counts[argument]
    cc = CallCount()
    print(cc(1))
    print(cc(1))
    print(cc(2))
    print(cc(2))
    print(cc(2))
    ```
- 데코레이터 생성시 ```__call__``` 메서드를 사용하면 편리함
### 매직 메서드 예약
![magic_method](../images/magic_method.png)
### 파이썬에서 유의할 점
#### 변경 가능한(mutable) 파라미터의 기본 값
- 변경 가능한 객체를 함수의 기본 인자로 사용하면 안됨
``` 
def wrong_user_display(user_metadata: dict = {"name": "John", "age": 30}):
    name = user_metadata.pop("name")
    age = user_metadata.pop("age")
    return f"{name} ({age})"

print(wrong_user_display())
print(wrong_user_display({"name": "Jane", "age": 25}))
print(wrong_user_display())
```
    - 변경 가능한 인자를 사용
    - 가변 객체를 수정하여 부작용 발생
#### 내장(built-in) 타입 확장
- 리스트, 문자열, 사전과 같은 내장 타입을 확장하는 방법은 collections 모듈 이용
    - dict 확장시 : collections.UserDict
    - 리스트 확장시 : collections.UserList
    - 문자열 확장시 : collections.UserString
### 요약