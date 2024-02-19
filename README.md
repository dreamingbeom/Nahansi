
# 🍀 나행시 - 나만의 은행, 행운의 시작. 웹앱기반 금융상품 추천 서비스

</br>
</br>

## 🍀 나행시 - 개요
나행시 프로젝트는 스마트폰 이용자들을 위한 웹앱 기반의 서비스입니다.

가장 높은 이자율의 예적금 금융 상품을 빠르게 찾고 싶을 때, 간단하게 환율을 계산하고 싶을 때, 스마트폰으로 내 주변의 가까운 은행을 알고싶을 때, 복잡한 절차 없이 스마트폰과 나행시를 활용하여 빠르게 이용 할 수 있습니다.

</br>


## 💚 프로젝트 진행 기간
2023.11.16 ~ 2023.11.23 (8일간 진행)  

</br>

|   | 11/16(목) | 11/17(금) | 11/18(토) | 11/19(일) |
| --- | --- | --- | --- | --- |
| 김경범 | 프로젝트 기획 및 화면 구성, 카카오 map API 연결 테스트, ERD 작성 |  회원가입 화면 구성, 로그인, 로그아웃 기능 구현 |회원 정보 수정 화면 구현, 회원정보 및 비밀번호 변경 화면 구현  | 회원 정보 수정 화면 구성 추가 |
| 이현직 | 카카오 오븐을 이용해 로그인, 회원가입, 환율 계산기, 지도 페이지 디자인 | 커뮤니티 생성, 삭제 기능 구현 | 커뮤니티 상세 정보 기능 구현 | 커뮤니티 수정 기능 구현 |
| 조수현 | ERD 작성, 장고 모델링, CRUD 구현 | 환율 계산기 만들기, 예적금 데이터 저장하기 | ERD 수정, 좋아요 기능 추가, 회원가입, 로그인 구현 | 커스텀 유저 모델 생성 밒 유저 모델 수정 기능 |

</br>

|   | 11/20(월)  | 11/21(화) | 11/22(수) | 11/23(목) |
| --- | --- | --- | --- | --- |
| 김경범 |  회원정보 마이페이지 화면 수정 및 알고리즘 수정 | 회원 정보 수정 화면 구성 추가 | 예적금리스트 조회 화면 구현 및 조회 최고금리순, 기본금리순 알고리즘 구현   | 예적금리스트 저축기간별 최고금리순, 기본금리순 알고리즘, 은행선택별 최고금리순, 기본금리순 알고리즘 구현, 화면 상세페이지 구현,  |  예적금리스트과 관심상품기능 충돌 해결, , 상세 및 조회 페이지 디자인 수정, 주변은행찾기, 게시글 조회, 게시글 상세페이지, 댓글 등 사이트 전반적인 화면디자인 개선, 메인페이지 애니메이션 추가 및 구성 |
| 이현직 | 댓글 생성, 삭제 기능 구현 | 댓글 수정 기능 구현, 게시글 좋아요 기능 구현 | 상품 가입하기 기능 구현, 게시판 CSS 작업 | 앱 로고 디자인 생성, 기능 작동 확인, 메인 페이지 디자인 |
| 조수현 | 유저 수정하기, 카카오맵(근처 은행 찾기) 기능 | 필요한 에셋들 다운로드, 기본 디자인 구상 | 지도, 계산기 디자인, 날짜 라이브러리 적용, 본인이 작성한 글, 댓글만 삭제하도록 구현 | 장바구니 기능, 상품 추천하기 기능 구현, CSS 다듬기  |

</br>



## 💚 주요 기능
---
- ### 예적금 상품 비교
    - 제1금융권을 기준으로 다양한 은행의 예적금 상품을 확인 할 수 있습니다.
    - 스마트폰의 작은 화면과 UX를 고려하여 가장 중요한 금리를 최우선적으로 확인 할 수 있도록 하였습니다.
    - 최고금리순, 기본금리순으로 정렬 할 수 있으며, 기간별, 은행별로 필터링하여 원하는 상품만을 확인 할 수 있습니다.
    - 상품의 유형에 따라 가입제한, 방문제한을 손쉽게 확인할 수 있습니다.
    - 상품 찜하기 버튼을 통해 즐겨찾기에 상품을 등록할 수 있습니다.
    - 금융상품의 상세페이지에서 해당 상품의 모든 기간별 금리를 확인 할 수 있습니다.
    
    <br/>
- ### 주변 은행 검색
    - kakao map API를 기반으로 주변 은행 검색 기능을 구현하였습니다.
    - 시, 도, 구를 선택하여 원하는 위치의 주변 은행을 검색 할 수 있습니다.
    - 검색 결과로 나오는 은행의 위치를 파란색 핀으로 빠르게 확인 할 수 있습니다.
    - 핀을 클릭 시, 해당 은행의 이름을 확인 할 수 있습니다.
    <br/>
- ### 환율 계산기
    - 스마트폰 이용을 고려햐여 간편하고 빠른 환율 계산기 기능을 구현하였습니다.
    - 원하는 나라와 매매 기준을 선택하고 금액을 입력하여 환율을 확인 할 수 있습니다.
    <br/>
- ### 예적금 정보 공유 게시판
    - 이용자들의 다양한 정보공유를 돕기위해 게시판 기능을 구현하였습니다.
    - 스마트폰 이용을 고려하여 글쓰기 버튼은 하단에 고정하여 언제든지 글을 작성할 수 있습니다.
    - 댓글을 통해 언제든지 다른 이용자와 소통 할 수 있습니다.
    <br/>
    
</br>

## ✔ 주요 기술
---

**Backend**
- Ptyhon 3.9.12
- Django 4.2.4
- dj-rest-auth 5.0.2
- django-allauth 0.58.2
- SQLite

**Frontend**
- node 20.10.0
- vue 3.3.4
- pinia 2.1.7
- vuetify 3.4.3
- vue-router 4.2.5
- vite 4.4.11

## ✔ 협업 툴
---
- Git
- Notion
- MatterMost

## ☘ 나행시 서비스 화면
---

### 메인화면
- 캐러셀을 이용하여 나행시 서비스의 최신 정보를 보여줍니다.
- 스크롤 애니메이션으로 이용자에게 흥미와 재미를 이끌면서 서비스에 대한 소개를 진행합니다.
- 스마트폰 이용자의 인터페이스를 고려하여 최상단, 최하단에 네비게이션바를 배치하였습니다.

![main](https://github.com/dreamingbeom/Nahansi/assets/128280944/8d6feb7d-a331-4223-8e97-3d66468aa694)

<br>

### 회원가입
- 아이디를 필수적으로 입력하지 않으면 회원가입을 진행할 수 없도록 안내하고있습니다.
- 스마트폰 이용자를 고려하여 'X' 아이콘을 클릭시 모든 내용이 사라지도록 구현하였습니다.
- 이용자 데이터 기반 상품 추천 기능을 위하여 선택 사항으로 이용자의 다양한 정보를 수집합니다.

![signup](https://github.com/dreamingbeom/Nahansi/assets/128280944/30938927-d218-442e-b74a-ad086a08437f)

<br>

### 예적금 상품 비교 서비스
- 제1금융권을 기준으로 다양한 은행의 예적금 상품을 확인 할 수 있습니다.
- 스마트폰의 작은 화면과 UX를 고려하여 가장 중요한 금리를 최우선적으로 확인 할 수 있도록 하였습니다.
- 최고금리순, 기본금리순으로 정렬 할 수 있으며, 기간별, 은행별로 필터링하여 원하는 상품만을 확인 할 수 있습니다.
- 상품의 유형에 따라 가입제한, 방문제한을 손쉽게 확인할 수 있습니다.
- 상품 찜하기 버튼을 통해 즐겨찾기에 상품을 등록할 수 있습니다.
- 금융상품의 상세페이지에서 해당 상품의 모든 기간별 금리를 확인 할 수 있습니다.

![product](https://github.com/dreamingbeom/Nahansi/assets/128280944/ed817d1c-d263-4a90-ac28-b5c9d7ec108f)

<br>

### 주변 은행 검색
- kakao map API를 기반으로 주변 은행 검색 기능을 구현하였습니다.
- 시, 도, 구를 선택하여 원하는 위치의 주변 은행을 검색 할 수 있습니다.
- 검색 결과로 나오는 은행의 위치를 파란색 핀으로 빠르게 확인 할 수 있습니다.
- 핀을 클릭 시, 해당 은행의 이름을 확인 할 수 있습니다.

![map](https://github.com/dreamingbeom/Nahansi/assets/128280944/db2f24ea-fb94-4786-9411-afb7693d5750)

<br>

### 환율 계산기
- 스마트폰 이용을 고려햐여 간편하고 빠른 환율 계산기 기능을 구현하였습니다.
- 원하는 나라와 매매 기준을 선택하고 금액을 입력하여 환율을 확인 할 수 있습니다.

![change](https://github.com/dreamingbeom/Nahansi/assets/128280944/fae5416e-7d7d-44b2-b91c-f1176924bb95)

<br>

### 예적금 정보 공유 게시판
- 이용자들의 다양한 정보공유를 돕기위해 게시판 기능을 구현하였습니다.
- 스마트폰 이용을 고려하여 글쓰기 버튼은 하단에 고정하여 언제든지 글을 작성할 수 있습니다.
- 댓글을 통해 언제든지 다른 이용자와 소통 할 수 있습니다.

![article](https://github.com/dreamingbeom/Nahansi/assets/128280944/1fdfbda3-cc10-43a0-ba8b-f6e1c9de9b90)

<br>

### 마이페이지
- 상세프로필을 통해 자신의 프로필을 확인 할 수 있습니다
- 정보 수정을 통하여 자신의 정보를 수정 할 수 있습니다.
- 비밀번호를 변경하거나 회원 탈퇴를 진행 할 수 있습니다.
- 환율 계산기, 주변 은행 찾기 탭을 이용하여 해당 기능을 이용 할 수 있습니다

![mypage](https://github.com/dreamingbeom/Nahansi/assets/128280944/74e30fe1-385a-4eb0-8093-0deae76ab660)

<br>

## ERD 설계

<br>

<img src="https://github.com/dreamingbeom/Nahansi/assets/128280944/ba28c2c3-fd64-46ab-bf79-df9c624d1aa6" />

</br>

## API 입력 위치
```
Frontend
카카오맵 : final-pjt-front\front\index.html
src="//dapi.kakao.com/v2/maps/sdk.js?appkey={api키입력}=services"
api 레퍼런스 주소 : https://apis.map.kakao.com/web/guide/ JavaScript  키

Backend
금융감독원 : final-pjt-back\deposits\views.py
변수명 api_key에 할당
api 레퍼런스 주소
- 예금 : https://finlife.fss.or.kr/finlife/api/fdrmDpstApi/list.do?menuNo=700052
- 적금 : https://finlife.fss.or.kr/finlife/api/fdrmDpstApi/list.do?menuNo=700052
```

