# 의약품 정보 관리 시스템 (Medicine Information Management System)

Django와 MySQL을 사용한 의약품 정보 관리 웹 애플리케이션입니다.

## 프로젝트 소개

의약품의 안전한 사용을 위해 정확한 의약품 정보를 제공하는 전문 웹 시스템입니다.
성분별, 회사별, 효능별로 의약품을 검색할 수 있으며, 커뮤니티 게시판 기능을 제공합니다.

## 주요 기능

- **의약품 정보 검색**
  - 성분별 검색
  - 회사별 검색
  - 효능별 검색
  - 의약품 상세 정보 조회

- **회원 관리**
  - 회원가입 및 로그인
  - 회원정보 수정
  - 비밀번호 변경

- **게시판**
  - 게시글 작성, 수정, 삭제
  - 게시글 목록 및 상세보기
  - 조회수 카운팅
  - 페이지네이션

- **기타**
  - 반응형 UI (Bootstrap 5)
  - 한국어 인터페이스
  - 보안 기능 (CSRF, XSS 방지)

## 기술 스택

- **Backend**: Django 4.2+
- **Database**: MySQL
- **Frontend**: Bootstrap 5
- **Language**: Python 3.12+

## 설치 방법

### 1. 저장소 클론

```bash
git clone https://github.com/ywhcho/med_eun2b.git
cd med_eun2b
```

### 2. 가상환경 생성 및 활성화

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 3. 의존성 패키지 설치

```bash
pip install -r requirements.txt
```

### 4. 환경 변수 설정

`.env.example` 파일을 복사하여 `.env` 파일을 생성하고 설정을 수정합니다:

```bash
cp .env.example .env
```

`.env` 파일 내용:
```
SECRET_KEY=your-secret-key-here
DEBUG=True
DB_NAME=med_eun2b
DB_USER=root
DB_PASSWORD=your-database-password
DB_HOST=localhost
DB_PORT=3306
```

### 5. 데이터베이스 설정

MySQL에서 데이터베이스를 생성합니다:

```sql
CREATE DATABASE med_eun2b CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

### 6. 마이그레이션 실행

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. 샘플 데이터 로드

```bash
python manage.py loaddata medicine/fixtures/sample_medicines.json
```

### 8. 관리자 계정 생성

```bash
python manage.py createsuperuser
```

## 실행 방법

개발 서버를 실행합니다:

```bash
python manage.py runserver
```

브라우저에서 `http://localhost:8000`으로 접속합니다.

## URL 구조

- `/` - 의약정보 검색 메인
- `/accounts/signup/` - 회원가입
- `/accounts/login/` - 로그인
- `/accounts/logout/` - 로그아웃
- `/accounts/profile/` - 회원정보 수정
- `/board/` - 게시판 목록
- `/board/create/` - 게시글 작성
- `/board/<pk>/` - 게시글 상세
- `/medicine/ingredient/` - 성분별 검색
- `/medicine/company/` - 회사별 검색
- `/medicine/efficacy/` - 효능별 검색
- `/medicine/<pk>/` - 의약품 상세정보
- `/about/` - About Us

## 프로젝트 구조

```
med_eun2b/
├── config/                 # Django 프로젝트 설정
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── accounts/              # 회원 관리 앱
├── board/                 # 게시판 앱
├── medicine/              # 의약정보 앱
├── pages/                 # 정적 페이지 앱
├── static/                # 정적 파일
│   └── css/
├── templates/             # 템플릿
│   ├── base.html
│   ├── accounts/
│   ├── board/
│   ├── medicine/
│   └── pages/
├── requirements.txt
├── .env.example
├── .gitignore
└── manage.py
```

## 관리자 페이지

관리자 페이지는 `http://localhost:8000/admin/`에서 접속할 수 있습니다.
생성한 관리자 계정으로 로그인하여 의약품 정보와 게시글을 관리할 수 있습니다.

## 보안 고려사항

개발 환경과 프로덕션 환경에서 다음 사항을 고려하세요:

### 개발 환경
- DEBUG=True로 설정
- SQLite 사용 가능 (USE_SQLITE=True)
- ALLOWED_HOSTS는 빈 리스트 가능

### 프로덕션 환경
프로덕션 배포 시 다음 설정을 변경해야 합니다:

```python
# settings.py에 추가
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']

# HTTPS 설정 (선택사항, 권장)
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
```

### 보안 기능
이 프로젝트는 다음 보안 기능을 포함합니다:
- CSRF 보호 활성화
- XSS 방지 (Django 템플릿 자동 이스케이핑)
- SQL Injection 방지 (Django ORM 사용)
- 비밀번호 해싱 (PBKDF2)
- 폼 유효성 검사
- 로그인 필요 페이지 접근 제어

## 라이선스

이 프로젝트는 교육 목적으로 제작되었습니다.

## 문의

문의사항이 있으시면 이슈를 등록해주세요.
