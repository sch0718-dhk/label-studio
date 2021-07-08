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
export LABEL_STUDIO_USERNAME=<username>
export LABEL_STUDIO_PASSWORD=<password>
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

## 실행

### Local 실행

```sh
# Start the server in development mode at http://localhost:8080
python label_studio/manage.py runserver
```

### Skaffold로 K8S에서 개발

```sh
./skaffold.sh
```

```sh
skaffold dev --filename=./deploy/skaffold/skaffold.yaml
```
