# Local 개발환경 구성 가이드

## 설치

### 환경변수 설정

> https://labelstud.io/guide/start.html#Command-line-arguments-for-starting-Label-Studio 참조

```properties
# 외부 PostgreSQL을 사용하기 위한 환경변수
export DJANGO_DB="default"
export POSTGRE_NAME=<database_name>
export POSTGRE_USER=<account_name>
export POSTGRE_PASSWORD=<account_password>
export POSTGRE_PORT="5432"
export POSTGRE_HOST=<postgresql_host>
# GCS 접속을 위한 Access Credential Key 경로
export GOOGLE_APPLICATION_CREDENTIALS=<gcp_account_key_file_path>
# 사용자 가입 링크 비 활성화 여부
export LABEL_STUDIO_DISABLE_SIGNUP_WITHOUT_LINK="true"
# 구글 OAuth 관련 환경변수
export YODA_GOOGLE_OAUTH_ENABLE=true
```

### 초기 설정

> https://labelstud.io/guide/install.html#Install-from-source 참조

```sh
# Git clone repository
git clone git@github.com:sch0718-dhk/label-studio.git
cd label-studio
# Install all package dependencies
pip install -e .
# Run database migrations
python label_studio/manage.py migrate
```

### Django Super User 생성

Label Studio에서 사용하는 Django Framework에는 Admin 기능이 있습니다.
Admin을 사용하기 위해 Super User를 생성합니다.

```sh
python label_studio/manage.py createsuperuser
```

Admin은 http://127.0.0.1:8080/admin 로 접속 가능합니다.

## 실행

### Local 실행

#### Back-End

```sh
# Start the server in development mode at http://localhost:8080
python label_studio/manage.py runserver
```

#### Front-End

frontend 폴더로 이동 후 아래 명령어를 실행하면 Front-End의 소스 변경내용이 바로 반영됩니다.
브라우저에서 변경 내용이 반영되기 위해서는 캐시 때문에 강제 리로딩이 필요합니다.(MacOS + Chrome 기준 Command + Shift + R)

```sh
npx webpack --watch
```

### Skaffold로 K8S에서 개발

```sh
./skaffold.sh
```

## Build & Deploy

### Build

> 배포할 때는 먼저 Front-End 를 반드시 빌드 후 배포하여야 합니다.
> 그렇지 않으면 Front-End에 변경 내용이 있더라도 반영되지 않습니다.
>
> ```sh
> npm ci
> ```

```sh
docker build \
 -f Dockerfile \
 -t asia.gcr.io/dhk-data-yoda-dev/label-studio:latest \
 ./
```

### Deploy

TBD
