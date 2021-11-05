# 원티드x위코드 백엔드 프리온보딩 과제 :: 프레시코드

## [TEAM] WithCODE

### Members

|이름|github|
|---|--------|
|김민호|https://github.com/maxkmh712|
|김주형|https://github.com/BnDC|
|박치훈|https://github.com/chihunmanse|
|박현우|https://github.com/Pagnim|
|이기용|https://github.com/leeky940926|
|이정아|https://github.com/wjddk97|

------

##  📝 아래 요구사항에 맞춰 상품 관리 Restfull API를 개발합니다.

### **[필수 포함 사항]**

- Swagger나 Postman을 이용하여 API 테스트 가능하도록 구현
    - Swagger 대신 Postman 이용시 API 목록을 Export하여 함께 제출해 주세요
- READ.ME 작성
    - 프로젝트 빌드, 자세한 실행 방법 명시
    - 구현 방법과 이유에 대한 간략한 설명
    - 완료된 시스템이 배포된 서버의 주소
    - Swagger를 통한 API 테스트할때 필요한 상세 방법
    - 해당 과제를 진행하면서 회고 내용 블로그 포스팅

### 1. 개발 요구사항

- Database 는 RDBMS를 이용합니다.
- 로그인 기능
    - JWT 인증 방식을 구현합니다.

### 2. 평가 요소

- 주어진 요구사항에 대한 설계/구현 능력
- 코드로 동료를 배려할 수 있는 구성 능력 (코드, 주석, README 등)
- 유닛 테스트 구현 능력

### 3. 기능 개발

- **로그인 기능**
    - 사용자 인증을 통해 상품 관리를 할 수 있어야 합니다.
        - 구현
            - JWT 인증 방식을 이용합니다.
            - 서비스 실행시 데이터베이스 또는 In Memory 상에 유저를 미리 등록해주세요.
            - Request시 Header에 Authorization 키를 체크합니다.
            - Authorization 키의 값이 없거나 인증 실패시 적절한 Error Handling을 해주세요.
            - 상품 추가/수정/삭제는 admin 권한을 가진 사용자만 이용할 수 있습니다.

- **상품 관리 기능**
    - 아래 상품 JSON 구조를 이용하여 데이터베이스 및 API를 개발해주세요.
        - 구현
            - 서비스 실행시 데이터베이스 또는 In Memory 상에 상품 최소한 5개를 미리 생성해주세요.
            - 상품 조회는 하나 또는 전체목록을 조회할 수 있으며, 전체목록은 페이징 기능이 있습니다.
                - 한 페이지 당 아이템 수는 5개 입니다.
            - 사용자는 상품 조회만 가능합니다.
            - 관리자는 상품 추가/수정/삭제를 할 수 있습니다.
            - 상품 관리 API 개발시 적절한 Error Handling을 해주세요.

-------

## Skill & Tools
> **Skill :** <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=Django&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=MySQL&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/JWT-232F3E?style=for-the-badge&logo=JWT&logoColor=white"/>&nbsp;<br>
> **Depoly :** <img src="https://img.shields.io/badge/AWS EC2-232F3E?style=for-the-badge&logo=Amazon AWS&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/AWS RDS-232F3E?style=for-the-badge&logo=Amazon AWS&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=Docker&logoColor=white"/> <br>
> **ETC :**  <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=Git&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Github-181717?style=for-the-badge&logo=Github&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=Postman&logoColor=white"/>

-------

## 모델링

![image](https://user-images.githubusercontent.com/88086271/140482742-d494ecff-ec1c-4821-b101-0741f280647b.png)


## Postman API 명세서

https://documenter.getpostman.com/view/17716434/UVC2H91e#intro

## 구현사항 상세 설명

### 로그인

POST /users/login
body key list : email, password

* 로그인 시, jwt 토큰이 발행됩니다.

* Unit Test

### 메뉴 등록

POST /menus <br>
body key list : category_id, tag_id, badge_id, name, description

* 신규 상품을 등록하는 메뉴이며, 상품이 속하는 카테고리와 상품에 추가할 태그와 신상품을 표시해주기 위한 뱃지를 변수로 받습니다.

* 상품명과 상품에 대한 설명을 입력합니다.

* 해당 기능은 관리자계정만 다룰 수 있도록 설정되었으며, 일반유저가 접근 시 403에러가 발생합니다.

* Unit Test

### 메뉴 리스트 조회

GET /menus?page={page}&category_id={category_id}

* 리스트는 페이지네이션 기법을 사용하여 조회할 수 있도록 설정하였습니다.

* page는 특정 페이지 버튼을 누를 때 이동할 페이지입니다.

* 전체상품 조회 시, category_id를 입력하지 않으며, 특정 카테고리를 선택 시에만 변수를 받습니다.

* Soft Delete기법을 사용하여 deleted_at이 null인 데이터만 조회됩니다.

* Unit Test

### 메뉴 상세 조회

GET /menus/{menu_id}

* 특정 상품을 클릭 시 정보를 보여줍니다.

* 일반유저는 조회만 가능하고, 그 외 작업은 관리자만 할 수 있기 때문에 Role을 식별해주기 위한 login_decorator를 선언했습니다.

* Soft Delete기법을 사용하여 deleted_at이 null인 데이터만 조회됩니다.

* Unit Test

### 메뉴 수정

PATCH /menus/{menu_id} <br>
body key list : name, description

* 상품을 수정을 할 수 있으며, 관리자만 수정할 수 있기 때문에 식별하기 위한 login_decorator를 선언했습니다.

* HTTP Method를 PATCH를 사용함으로써, 유동적인 변경을 할 수 있게 설정하였습니다.

* Unit Test

### 메뉴 삭제

DELETE /menus/{menu_id}

* 상품을 삭제할 수 있으며, 관리자만 삭제할 수 있기 때문에 식별하기 위한 login_decorator를 선언했습니다.

* Soft Delete기법을 사용하였으며, 삭제 시 삭제일자에 현재 날짜가 들어가도록 했습니다.

* Unit Test

### 상품 상세정보 추가

POST /menus/items <br>
body key list : menu_id, size_id, price

* 관리자만 추가할 수 있기 때문에 식별하기 위한 login_decorator를 선언했습니다.

* 대표메뉴의 상세정보를 추가하기 위한 메뉴입니다.

* 특정 메뉴의 상세 아이템이기 때문에 menu_id를 받고, 메뉴마다 사이즈가 다르기 때문에 size_id를 받습니다.

* 사이즈별 가격이 다르기 때문에 가격도 함께 입력 받습니다.

* Unit Test

### 상품 상세정보 수정

PATCH /menus/items/{item_id} <br>
body key list : size_id, price, is_sold

* 관리자만 수정할 수 있기 때문에 식별하기 위한 login_decorator를 선언했습니다.

* 수량관리를 통해 품절여부(is_sold)가 자동으로 바뀌어야 하지만,
현 프로젝트에서는 수량에 대한 고려를 하지 않아, 수동으로 수정할 수 있게 설정하였습니다.

* Unit Test

### 상품 상세정보 삭제

DELETE /menus/items/{item_id} 

* 관리자만 삭제할 수 있기 때문에 식별하기 위한 login_decorator를 선언했습니다.

* Soft Delete기법을 사용하였으며, 삭제 시 삭제일자에 현재 날짜가 들어가도록 했습니다.

* Unit Test 



## API TEST 방법

### 1.  [해당 링크](https://grey-comet-304334.postman.co/workspace/freshcode~d93e7197-5ffb-40af-8ca6-1958ba5aef72/collection/17716434-cf3ad77a-f5a7-43c5-8605-635e6468d8c0?ctx=documentation)에 접속합니다

### 2. 우측 상단의 아이콘을 클릭하여, SERVER_URL의 주소를 확인합니다.

![image](https://user-images.githubusercontent.com/88086271/140480799-9be62dbf-8a95-4b9b-a642-60d1858dd850.png)

경우에 따라 변수들을 바꿔가면서 테스트할 수 있습니다.

배포된 서버의 주소(http://18.223.102.56:8000) 로 세팅을 했습니다.

### 3. 정의된 예시에 따라 로그인을 진행하여 토큰을 발급받습니다.

일반유저 : user@freshcode.me/user <br>
관리계정 : admin@freshcode.me/admin

### 4. admin 계정으로 접속하여, 헤더에 발급받은 토큰을 입력해서 테스트를 진행하시면 됩니다.

![image](https://user-images.githubusercontent.com/88086271/140481465-357df303-069b-493b-a303-69bb707dbe74.png)

### 5. send버튼이 활성화 되지 않거나, 문제가 발생할 경우 fork를 받아서 진행 부탁 드립니다.

![image](https://user-images.githubusercontent.com/88086271/140481893-0798b177-e179-476d-bdee-d1f73939d53e.png)
