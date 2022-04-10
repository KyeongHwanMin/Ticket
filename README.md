# Ticket

<br>

### 개요


영화 소개 API

### 필요

- Python 3.9.x
- Django 4.0.x
- djangorestframework 3.13.x
- Pillow==9.0.x
- SQL lite3

  <br>

## 서버 구동 방법

### 로컬환경 서버 구동

1. Python 종속성 설치

```
pip install -r requirements.txt
```

​	2. DB 마이그레이션

> 설계된 모델에 대한 스키마를 데이터베이스에 반영

```bash
python manage.py migrate
```

4. 서버실행

```bash
python manage.py runserver
```

5. 서버 정상 구동 확인

웹 브라우저에서http://127.0.0.1:8000/api/v1/movies/ 로 접속하여 페이지가 나온다면 정상적으로 서버 구동된 것입니다.

<br>



## API Specifications

### 회원가입

[요청]

- URL: POST /account/signup/
- Body
```json
{
    "username" : "test",
    "email" : "test@test.com",
    "password" : "test",
}
```

[응답]

- Body

```json
{
    "username" : "test",
    "email" : "test@test.com",
    "password" : "test",
}
```

- Error

| 에러코드 | 설명                        |
| -------- | --------------------------- |
| 400      | 파라미터 입력이 잘못된 경우 |
| 409      | 중복된 값이 입력된 경우     |

로그인
[요청]

URL: POST /api/accounts/login/
Body
{
  "username": "test",
  "password": "1234"
} 
[응답]

응답에 대한 설명

성공 응답 시 상태코드 : 200
Error

에러코드	설명
400	등록된 user가 없는 경우
401	Username or Password 틀릴 경우
