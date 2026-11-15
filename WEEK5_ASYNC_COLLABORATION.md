# [5주차] 비동기 협업 체계 구축 (Discussions / Wiki / ADR)

## 1. 과제 개요

본 과제에서는 GitHub Wiki, Discussions, ADR 및 GitHub Actions를 활용하여 비동기 협업 체계를 구축하였다.

프로젝트 관련 문서를 체계적으로 관리하고, 기술적 의사결정 과정과 협업 활동을 기록하여 실시간 의사소통에 의존하지 않는 개발 환경을 구성하는 것을 목표로 하였다.

**프로젝트 저장소:** [OSS_SW_Programming](https://github.com/lmlalalala/OSS_SW_Programming)

## 2. 과제 수행 목표

### 필수과제

- GitHub Wiki 문서 3개 작성
- Getting Started, Development Guide, Troubleshooting 문서 구성
- Wiki 문서 간 상호 링크 연결

### 선택과제 1. Discussions 기반 기술 토론

- GitHub Discussions 활성화
- 토론 목적별 카테고리 설계
- RFC 형식 기술 토론 1건 이상 운영

### 선택과제 2. ADR 및 협업 자동화

- ADR 템플릿 작성
- `docs/adr/` 문서 관리 구조 생성
- 기술적 의사결정 기록 작성
- 자동 응답, SLA 추적, 주간 요약 워크플로우 구성

## 3. GitHub Wiki 구축

### 3.1 Wiki 활성화

GitHub 저장소 Settings에서 Wiki 기능을 활성화하고, 문서 탐색을 위한 Home 페이지를 작성하였다.

### 3.2 Wiki 문서 구성

| 문서 | 주요 내용 |
|---|---|
| Getting Started | 프로젝트 소개, 환경 설정, 저장소 복제, 주차별 실습 내용 |
| Development Guide | GitHub Flow, 브랜치 전략, 커밋 규칙, PR 및 코드 리뷰 |
| Troubleshooting | Git Push 오류, 브랜치 오류, SSH 인증, GitHub Actions 오류 해결 |

### 3.3 문서 상호 링크

각 문서 하단에 Home 및 다른 Wiki 문서로 이동할 수 있는 링크를 추가하였다.

이를 통해 문서 간 이동 편의성을 높이고, 새로운 기여자가 필요한 정보를 쉽게 확인할 수 있도록 구성하였다.

**구현 결과:** Wiki 문서 3개 작성 및 상호 링크 동작 검증 완료

[GitHub Wiki 바로가기](https://github.com/lmlalalala/OSS_SW_Programming/wiki)

## 4. GitHub Discussions 구축

### 4.1 Discussions 활성화

GitHub Discussions를 활성화하고 협업 목적 및 운영 원칙을 안내하는 환영 게시글을 작성하였다.

### 4.2 카테고리 설계

| 카테고리 | 역할 |
|---|---|
| Announcements | 프로젝트 공지 및 주요 업데이트 |
| Q&A | 기술적 질문 및 답변 |
| Ideas | 기능 개선 및 아이디어 제안 |
| RFC | 기술적 제안 및 의견 수렴 |

기본 제공 카테고리를 활용하고 RFC 카테고리를 추가하여 기술 토론을 구분하였다.

### 4.3 RFC-001 기술 토론

**토론 주제:** GitHub Actions 기반 DORA 주간 리포트 공유 방식 개선

2주차 과제에서 구현한 DORA 메트릭 자동화의 결과 공유 방식을 개선하기 위한 RFC를 작성하였다.

다음 두 가지 대안을 검토하였다.

- 대안 A: 기존 Artifact 저장 방식 유지
- 대안 B: Artifact 저장을 유지하면서 Discussions에 주간 요약 자동 게시

1차 검토 결과, 기존 원본 데이터 보존과 정보 접근성을 함께 고려하여 대안 B를 우선 권고하였다.

검토 의견을 댓글로 기록하고, 추가적인 의견 수렴을 위해 Discussion을 유지하였다.

**구현 결과:** RFC-001 게시 및 1차 검토 의견 작성 완료

[RFC-001 바로가기](https://github.com/lmlalalala/OSS_SW_Programming/discussions/21)

## 5. ADR 문서 관리 체계 구축

### 5.1 ADR 도입 목적

ADR(Architecture Decision Record)은 프로젝트의 기술적 의사결정에 대한 배경, 검토 대안 및 결정 이유를 기록하는 문서이다.

RFC가 의견 수렴을 위한 제안이라면, ADR은 기술적 판단과 결정 내용을 지속적으로 관리하는 데 목적이 있다.

### 5.2 디렉터리 구성

```text
docs/
└── adr/
    ├── ADR_TEMPLATE.md
    └── ADR-001-dora-weekly-report.md
```

### 5.3 ADR 템플릿

다음 항목을 포함하는 공통 템플릿을 작성하였다.

- 기본 정보 및 상태
- 의사결정 배경
- 검토한 대안
- 결정 사항
- 예상 영향
- 후속 작업
- 참고 자료

### 5.4 ADR-001 작성

RFC-001에서 검토한 DORA 주간 리포트 공유 방식 개선안을 ADR-001로 문서화하였다.

Artifact 유지와 Discussions 자동 게시의 장단점, 예상 효과 및 추가 구현 시 고려해야 할 사항을 기록하였다.

**작성 결과:** ADR 템플릿 및 기술적 의사결정 기록 1건 생성

## 6. GitHub Actions 협업 자동화

비동기 협업 과정에서 반복적으로 발생하는 작업을 자동화하기 위해 세 가지 워크플로우를 작성하였다.

### 6.1 자동 응답 워크플로우

**파일:** `.github/workflows/week5-auto-reply.yml`

GitHub Discussions의 Q&A 카테고리에 새로운 질문이 등록되면 GitHub Actions가 자동으로 실행되도록 구성하였다.

주요 기능은 다음과 같다.

- Discussion 생성 이벤트 감지
- Q&A 카테고리 여부 확인
- GitHub API를 통한 자동 안내 댓글 작성
- Getting Started, Development Guide, Troubleshooting 링크 제공

**검증 결과:** 테스트 Q&A 게시글 등록 시 워크플로우 실행 성공 및 자동 안내 댓글 생성 확인

### 6.2 SLA 추적 워크플로우

**파일:** `.github/workflows/week5-sla-tracking.yml`

Q&A 질문의 첫 응답까지 소요되는 시간을 측정하기 위한 워크플로우를 구성하였다.

실습용 SLA 목표를 24시간으로 설정하고 다음 네 가지 상태로 분류하도록 구현하였다.

| 상태 | 의미 |
|---|---|
| ON_TIME | 24시간 이내 응답 |
| LATE | 24시간 초과 후 응답 |
| WAITING | 아직 미응답이며 24시간 이내 |
| OVERDUE | 24시간 초과 및 미응답 |

수동 실행과 Schedule 기반 정기 실행을 지원하며, 분석 결과를 JSON 파일로 생성하여 Artifact로 저장한다.

**검증 결과**

- GitHub Actions 실행 성공
- 실행 시간: 11초
- Artifact: 1개 생성
- `track-sla` Job 정상 종료

단, 실제 다양한 응답 시간에 대한 SLA 판정 정확성은 추가 테스트가 필요하다.

### 6.3 주간 요약 워크플로우

**파일:** `.github/workflows/week5-weekly-summary.yml`

프로젝트의 GitHub 활동을 주간 단위로 집계하고 공유하기 위한 워크플로우를 구성하였다.

주요 집계 항목은 다음과 같다.

- 신규 Issue
- 종료된 Issue
- 병합된 Pull Request
- 신규 Discussion

매주 월요일 예약 실행을 지원하며, 수동 실행 시에는 기본적으로 미리보기 기능을 제공하도록 구현하였다.

**검증 결과**

- GitHub Actions 실행 성공
- 실행 시간: 8초
- 주간 요약 미리보기 정상 생성
- 집계 기간: 2026-11-02 ~ 2026-11-08
- 신규 Issue, 종료 Issue, 병합 PR, 신규 Discussion 모두 0건으로 표시

해당 실행은 미리보기 방식으로 수행하였으며, Discussions 자동 게시 기능의 실제 실행 검증은 별도로 필요하다.

또한 DORA 메트릭의 실제 수치는 현재 주간 요약 워크플로우에 연동하지 않았다.

## 7. GitHub Flow 적용 및 PR 관리

작업 브랜치 `docs/week5-adr`에서 ADR 문서와 GitHub Actions 워크플로우를 작성하였다.

각 변경 사항을 커밋한 후 Pull Request를 생성하여 `main` 브랜치에 병합하였다.

PR 검토 과정에서 자동 응답 워크플로우 파일의 디렉터리 경로가 잘못 지정된 문제를 발견하였다.

기존의 잘못된 경로를 수정하여 GitHub Actions가 인식하는 `.github/workflows/` 디렉터리로 이동하였다.

수정 사항을 추가 커밋하고 PR 변경 파일을 재확인한 후 병합을 완료하였다.

**PR:** [5주차 Pull Request #22](https://github.com/lmlalalala/OSS_SW_Programming/pull/22)

## 8. 최종 구현 및 검증 결과

| 항목 | 수행 결과 |
|---|---|
| Wiki 문서 3개 작성 | 완료 |
| Wiki 상호 링크 연결 | 완료 |
| Discussions 활성화 | 완료 |
| RFC 카테고리 설계 | 완료 |
| RFC 기술 토론 1건 운영 | 완료 |
| ADR 템플릿 및 ADR-001 | 완료 |
| 자동 응답 워크플로우 | 실행 및 댓글 생성 성공 |
| SLA 추적 워크플로우 | 실행 및 Artifact 생성 성공 |
| 주간 요약 워크플로우 | 미리보기 실행 성공 |
| GitHub Flow 기반 PR 병합 | 완료 |

## 9. 한계 및 향후 개선 사항

이번 과제를 통해 Wiki, Discussions, ADR을 활용하는 비동기 협업 체계를 구축하고 GitHub Actions 기반 자동화 기능을 실습하였다.

다만 다음과 같은 개선 사항이 남아 있다.

1. 기존 DORA 메트릭 JSON 결과를 주간 요약에 직접 연동
2. 주간 요약의 실제 Discussions 자동 게시 검증
3. SLA 추적 시 다양한 응답 시간 및 예외 상황 검증
4. RFC 의견 수렴 결과에 따른 ADR 상태 관리
5. 워크플로우 실행 실패 시 알림 및 대응 절차 보완

## 10. 결론 및 고찰

이번 과제를 진행하면서 비동기 협업에서는 단순히 메시지를 주고받는 것보다 필요한 정보를 누구나 확인할 수 있도록 기록하고 공유하는 것이 중요하다는 점을 이해하였다.

Wiki를 통해 개발 정보를 문서화하고, Discussions를 통해 기술적 의견을 수렴하며, ADR로 의사결정의 근거를 기록하는 구조를 구축하였다.

또한 GitHub Actions를 활용하여 질문에 대한 자동 안내, 응답 시간 추적, 주간 활동 요약 기능을 구현하였다. 특히 워크플로우 파일 경로 오류를 수정하고 실제 실행 결과를 확인하면서 GitHub Flow와 자동화 검증 과정의 중요성을 확인할 수 있었다.

이를 통해 이전 주차에 학습한 GitHub 협업 및 자동화 기능을 확장하여 기록 중심의 비동기 협업 환경을 구성할 수 있었다.