# Week 3 - GitHub Projects 계획·추적 체계 구축

## 1. GitHub Project 생성

기존 `OSS_SW_Programming` 저장소와 연계하여 GitHub Project를 생성하고,
칸반 방식으로 작업 상태를 관리할 수 있도록 구성하였다.

### 상태 컬럼

- Backlog
- To Do
- In Progress
- Review
- Done

각 이슈의 진행 상태에 따라 카드를 이동하여 작업 흐름을 관리하도록 구성하였다.

---

## 2. Issues 구성

프로젝트 진행에 필요한 작업을 세분화하여 10개 이상의 Issue를 생성하였다.

주요 Issue는 다음과 같다.

- 프로젝트 요구사항 정리
- DORA Deployment Frequency 수집
- DORA Lead Time 수집
- DORA Change Failure Rate 수집
- DORA MTTR 수집
- GitHub Actions 워크플로우 정리
- DORA 데이터 JSON 저장
- Dashboard UI 구성
- Dashboard 그래프 표시
- 주간 DORA 리포트 자동 생성
- README 사용법 작성
- 오류 처리 및 테스트

각 Issue는 Project Board의 상태에 따라 분류하여 관리하였다.

---

## 3. Issue Template 구성

Issue 작성 형식을 표준화하기 위해 다음 2개의 템플릿을 생성하였다.

- Bug report
- Feature request

템플릿 파일은 다음 경로에 구성하였다.

~~~text
.github/ISSUE_TEMPLATE/
├── bug_report.md
└── feature_request.md
~~~

---

## 4. Label 체계 구성

Issue의 유형과 우선순위를 쉽게 구분할 수 있도록 Label 체계를 구성하였다.

주요 Label은 다음과 같다.

- bug
- feature
- documentation
- github-actions
- dashboard
- dora
- priority-high
- priority-medium
- priority-low

각 Issue의 성격에 따라 적절한 Label을 적용하였다.

---

## 5. Milestone 구성

프로젝트 작업을 단계별로 관리하기 위해 2개의 Milestone을 생성하였다.

### Milestone 1
**DORA 데이터 수집 자동화**

DORA 4대 지표 수집과 GitHub Actions 기반 자동화 작업을 관리한다.

주요 작업:

- Deployment Frequency 수집
- Lead Time 수집
- Change Failure Rate 수집
- MTTR 수집
- GitHub Actions 워크플로우
- DORA 데이터 JSON 저장

### Milestone 2
**Dashboard 및 문서화**

수집된 데이터를 시각화하고 프로젝트 사용 방법을 정리하는 작업을 관리한다.

주요 작업:

- Dashboard UI 구성
- Dashboard 그래프 표시
- 주간 DORA 리포트 자동 생성
- README 사용법 작성
- 오류 처리 및 테스트

각 Issue에는 해당 작업에 맞는 Milestone을 지정하였다.

---

## 6. Kanban Board 운영

생성한 Issue를 Project Board에 등록하고,
현재 진행 상태에 따라 다음과 같이 관리하였다.

~~~text
Backlog → To Do → In Progress → Review → Done
~~~

이를 통해 앞으로 수행할 작업, 현재 진행 중인 작업,
검토가 필요한 작업, 완료된 작업을 한눈에 확인할 수 있도록 구성하였다.

---

## 7. Project URL

- Repository  
  https://github.com/lmlalalala/OSS_SW_Programming

- GitHub Project  
 https://github.com/users/lmlalalala/projects/1
---

## 8. Project Board Screenshot

아래 이미지는 GitHub Project의 칸반 보드 구성 화면이다.

![GitHub Project Board](images/week3-project-board.png)