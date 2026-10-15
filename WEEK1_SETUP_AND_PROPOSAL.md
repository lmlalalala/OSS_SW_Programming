# Week 1 - 개발 환경 설정 및 프로젝트 제안

## 1. 과제 개요

1주차에는 OSS 기반 소프트웨어 프로그래밍 과제를 진행하기 위한 Git / GitHub 개발 환경을 설정하고,  
`OSS_SW_Programming` Repository를 생성하여 로컬 개발 환경과 GitHub 저장소를 연결했습니다.

또한 Git을 이용한 최초 커밋 및 Push 과정을 실습하고,  
향후 진행할 프로젝트의 주제와 개발 계획을 정리한 `PROJECT_PROPOSAL.md`를 작성했습니다.

---

## 2. Git / GitHub 개발 환경 설정

Git Bash를 이용하여 로컬 프로젝트 폴더를 Git Repository로 초기화하고 GitHub와 연결했습니다.

로컬 작업 경로:

    C:/OSS_SW_Programming

Git Repository 초기화:

    git init

초기 파일을 Git에 등록한 뒤 커밋을 생성했습니다.

    git add .
    git commit -m "first commit"

기본 브랜치는 `main`으로 설정했습니다.

    git branch -M main

GitHub의 `OSS_SW_Programming` Repository를 원격 저장소로 등록하고 Push를 진행했습니다.

    git remote add origin https://github.com/lmlalalala/OSS_SW_Programming.git
    git push -u origin main

GitHub와 로컬 Repository를 연결하는 과정에서 SSH 기반 GitHub 연동 및 Git/GitHub 사용 환경도 함께 확인했습니다.

---

## 3. Repository 생성 및 첫 커밋

1주차 과제를 진행하기 위한 GitHub Repository로 다음 저장소를 사용했습니다.

Repository 이름:

    OSS_SW_Programming

초기 Repository에는 README 파일을 생성하여 Git 관리 대상에 추가하고,  
최초 커밋 및 Push를 수행하여 로컬 Repository의 변경 사항이 GitHub에 정상적으로 반영되는 것을 확인했습니다.

초기 작업 과정은 다음과 같습니다.

    로컬 프로젝트 폴더 생성
            ↓
    git init
            ↓
    README.md 생성
            ↓
    git add
            ↓
    git commit
            ↓
    GitHub 원격 Repository 연결
            ↓
    git push
            ↓
    GitHub에서 업로드 결과 확인

이후 동일한 `OSS_SW_Programming` Repository에서 각 주차별 과제를 계속 관리하고 있습니다.

---

## 4. 프로젝트 제안서 작성

향후 수업에서 진행할 프로젝트의 주제와 개발 계획을 정리하기 위해  
별도의 프로젝트 제안서 파일을 작성했습니다.

제안서 파일:

    PROJECT_PROPOSAL.md

프로젝트명:

    InfraLog - 서버 및 서비스 상태 모니터링 웹 서비스

프로젝트는 여러 서버의 상태와 장애 발생 기록을 한 곳에서 확인할 수 있는  
서버 및 서비스 모니터링 웹 서비스를 목표로 합니다.

주요 기능은 다음과 같이 구성했습니다.

- 서버 상태 모니터링
- 장애 및 이벤트 기록 관리
- 대시보드 및 통계 확인

기술 스택으로는 Spring Boot, Thymeleaf, HTML/CSS/JavaScript, MySQL, Linux, Git/GitHub, GitHub Actions 등을 고려했습니다.

또한 프로젝트 제안서에는 요구사항 분석, 개발 환경 구성, UI 및 시스템 설계,  
서버 관리 기능 구현, 상태 수집, 장애 감지, 대시보드 구현, 테스트 및 문서화 등의 내용을 포함한  
16주 개발 계획을 작성했습니다.

프로젝트 제안서의 전체 내용은 아래 파일에서 별도로 확인할 수 있습니다.

[`PROJECT_PROPOSAL.md`](PROJECT_PROPOSAL.md)

---

## 5. 주요 결과물

1주차 과제를 통해 작성하거나 설정한 주요 결과물은 다음과 같습니다.

| 구분 | 내용 |
|---|---|
| Repository | `OSS_SW_Programming` |
| Git 초기화 | 로컬 프로젝트에 Git Repository 생성 |
| GitHub 연결 | 로컬 Repository와 GitHub 원격 저장소 연결 |
| Branch | `main` |
| 최초 커밋 | README 등 초기 파일 Commit 및 Push |
| 프로젝트 제안서 | `PROJECT_PROPOSAL.md` |
| 프로젝트 주제 | InfraLog - 서버 및 서비스 상태 모니터링 웹 서비스 |

---

## 6. Repository URL

GitHub Repository:

https://github.com/lmlalalala/OSS_SW_Programming

프로젝트 제안서:

https://github.com/lmlalalala/OSS_SW_Programming/blob/main/PROJECT_PROPOSAL.md