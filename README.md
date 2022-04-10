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


### 로그인
[요청]
- URL: POST /accounts/login/
- Body
```bash
{
  "username": "test",
  "password": "test"
} 
```
[응답]
- 응답에 대한 설명
  - 성공 응답 시 상태코드 : 200

- Error

|에러코드|설명|
|------|-----|
|400| 등록된 user가 없는 경우|
|401| Username or Password 틀릴 경우|

### 영화 조회
[요청]
- URL: GET /api/v1/movies/

[응답]
- Body
```bash
[
    {
        "id": 1,
        "name": "모비우스",
        "year": 2020,
        "original_title": "Mobius",
        "video_url1": "https://tv.naver.com/v/25898152",
        "video_url2": "https://tv.naver.com/v/25670458",
        "video_url3": "https://tv.naver.com/v/25628916",
        "video_url4": null,
        "cast": "자레드 레토, 아드리아 아르호나, 자레드 해리스, 알 마드리걸, 타이레스 깁슨, 맷 스미스, 찰리 쇼트",
        "synopsis": "희귀혈액병을 앓고 있는 생화학자 ‘모비우스’(자레드 레토)는 동료인 ‘마르틴’(아드리아 아르호나)과 함께 치료제 개발에 몰두한다. 흡혈 박쥐를 연구하던 중 마침내 치료제 개발에 성공한 ‘모비우스’는 새 생명과 강력한 힘을 얻게 되지만, 동시에 흡혈을 하지 않고는 생명을 유지할 수 없게 된다. 그러던 중 ‘모비우스’와 같은 병을 앓고 있던 그의 친구 ‘마일로’(맷 스미스)도 ‘모비우스’와 같은 힘을 얻게 되는데… 세상을 구할 능력, 파괴할 본능! 마블 최강의 안티 히어로가 탄생한다!",
        "image": "/media/%EB%AA%A8%EB%B9%84%EC%9A%B0%EC%8A%A4_fwd3OHA.png",
        "author": 1
    },
    {
        "id": 2,
        "name": "더 배트맨",
        "year": 2022,
        "original_title": "The Batman",
        "video_url1": "https://tv.naver.com/v/24663881",
        "video_url2": "https://tv.naver.com/v/24334475",
        "video_url3": "https://tv.naver.com/v/24334680",
        "video_url4": null,
        "cast": "로버트 패틴슨, 폴 다노, 조크라비츠, 앤디 서키스, 제프리 라이트, 콜린 파렐, 피터 사스가드, 존 터투",
        "synopsis": "지난 2년간 고담시의 어둠 속에서 범법자들을 응징하며 배트맨으로 살아온 브루스 웨인. 알프레드와 제임스 고든 경위의 도움 아래, 도시의 부패한 공직자들과 고위 관료들 사이에서 복수의 화신으로 활약한다. 고담의 시장 선거를 앞두고 고담의 엘리트 집단을 목표로 잔악한 연쇄살인을 저지르는 수수께끼 킬러 리들러가 나타나자, 최고의 탐정 브루스 웨인이 수사에 나서고 남겨진 단서를 풀어가며 캣우먼, 펭귄, 카마인 팔코네, 리들러를 차례대로 만난다. 사이코 범인의 미스터리를 수사하면서 그 모든 증거가 자신을 향한 의도적인 메시지였음을 깨닫고, 리들러에게 농락 당한 배트맨은 광기에 사로잡힌다. 범인의 무자비한 계획을 막고 오랫동안 고담시를 썩게 만든 권력 부패의 고리를 끊어야 하지만, 부모님의 죽음에 얽힌 진실이 밝혀지자 복수와 정의 사이에서 갈등한다. 선과 악, 빛과 어둠, 영웅과 악당, 정의와 복수.. 무엇을 선택할 것인가",
        "image": "/media/%EB%8D%94%EB%B0%B0%ED%8A%B8%EB%A7%A8_ebuL1RP.png",
        "author": 1
    }
]
```
- 응답에 대한 설명
  - 성공 응답 시 상태코드 : 200
  - 응답 Body 설명
    - 등록되어 있는 모든 영화의 정보들이 반환됩니다.

- Error

|에러코드|설명|
|------|-----|
|404| 영화 목록이 없는 경우|

