# [4주차] GitHub Flow 및 코드리뷰 협업 실습

## 1. 실습 개요

GitHub Flow 브랜치 전략을 적용하여 독립적인 작업 브랜치에서 변경 사항을 관리하고, Pull Request(PR)를 통한 코드 리뷰 및 병합 과정을 실습하였다.

개인 GitHub 저장소 환경에서 총 3건의 PR을 생성하고, 각 PR에 자체 리뷰(Self-review) 피드백을 작성하였다. `[MUST]`, `[SHOULD]` 태그를 활용하여 개선 사항을 제안하고, 이를 실제 수정 커밋에 반영한 후 main 브랜치로 병합하였다.

또한 선택과제로 PR 템플릿과 프로젝트 기여 가이드를 작성하여 협업 규칙을 문서화하였다.

## 2. 실습 환경

| 항목 | 내용 |
|---|---|
| 저장소 | [OSS_SW_Programming](https://github.com/lmlalalala/OSS_SW_Programming) |
| GitHub 계정 | lmlalalala |
| 개발 도구 | Git Bash, VS Code, GitHub |
| 기본 브랜치 | main |
| 브랜치 전략 | GitHub Flow |
| 커밋 방식 | Conventional Commits |
| 리뷰 방식 | 개인 프로젝트 자체 리뷰(Self-review) |

## 3. GitHub Flow 적용

기존 main 브랜치에서 작업별 Feature 브랜치를 생성하고, 변경 사항을 별도의 브랜치에서 작성하였다.

**작업 절차**

1. main 브랜치의 최신 내용 가져오기
2. 작업별 Feature 브랜치 생성
3. 파일 작성 및 변경 사항 커밋
4. 원격 저장소에 Push
5. Pull Request 생성
6. 리뷰 피드백 작성 및 수정 사항 반영
7. 변경 사항 검토 후 main 브랜치로 Merge

모든 작업을 main 브랜치에서 직접 수행하지 않고 PR을 통해 병합하는 방식으로 진행하였다.

## 4. Pull Request 수행 결과

### 4.1 PR #16 — GitHub Flow 실습 문서

- 작업 브랜치: `feature/week4-review`
- 작성 파일: `WEEK4_GITHUB_FLOW.md`
- 커밋 유형: `docs`
- 진행 상태: Merged

GitHub Flow의 개념과 기본 작업 절차를 Markdown 문서로 정리하였다.

**리뷰 및 피드백**

- `[SHOULD]` GitHub Flow의 각 단계에 대한 Git 명령어 예시 추가 제안
- `[MUST]` main 브랜치 병합 전 리뷰 및 검사 결과 확인 절차 보완 요청

피드백을 반영하여 Git 명령어 예시와 병합 전 검증 절차를 추가하였다. 이후 수정 내용을 커밋하고 PR을 병합하였다.

**PR 링크:** https://github.com/lmlalalala/OSS_SW_Programming/pull/16

### 4.2 PR #17 — Pull Request 템플릿 작성

- 작업 브랜치: `feature/week4-pr-template`
- 작성 파일: `.github/pull_request_template.md`
- 커밋 유형: `docs`
- 진행 상태: Merged

PR 작성 시 변경 목적, 변경 유형, 관련 이슈, 테스트 결과 및 리뷰 요청 사항을 일정한 형식으로 기록할 수 있도록 템플릿을 구성하였다.

**리뷰 및 피드백**

- `[SHOULD]` 코드 리뷰 피드백의 우선순위를 구분할 수 있도록 리뷰 태그 사용 기준 추가 제안

피드백을 반영하여 `[MUST]`, `[SHOULD]`, `[NITS]`, `[PRAISE]` 태그의 의미를 템플릿에 추가하였다.

이후 PR #18 생성 화면에서 템플릿 내용이 자동으로 표시되는 것을 확인하여 실제 적용 여부를 검증하였다.

**PR 링크:** https://github.com/lmlalalala/OSS_SW_Programming/pull/17

### 4.3 PR #18 — 협업 가이드 작성

- 작업 브랜치: `feature/week4-contributing`
- 작성 파일: `CONTRIBUTING.md`
- 커밋 유형: `docs`
- 진행 상태: Merged

프로젝트에 참여하는 기여자가 동일한 규칙을 따를 수 있도록 브랜치 네이밍, 커밋 메시지, PR 작성 및 코드 리뷰 규칙을 문서화하였다.

**리뷰 및 피드백**

- `[SHOULD]` 리뷰 태그별 실제 사용 예시를 추가하여 가이드의 이해도 향상 제안

피드백을 반영하여 `[MUST]`, `[SHOULD]`, `[NITS]`, `[QUESTION]`, `[PRAISE]` 태그의 실제 사용 예시를 추가하였다.

수정 내용을 Push한 후 최종적으로 main 브랜치에 병합하였다.

**PR 링크:** https://github.com/lmlalalala/OSS_SW_Programming/pull/18

## 5. 코드 리뷰 실습 결과

개인 저장소 기반 실습 환경을 고려하여 3건의 PR에 자체 리뷰 피드백을 작성하였다.

| PR | 리뷰 내용 | 반영 결과 |
|---|---|---|
| #16 | 명령어 예시 및 병합 전 검증 절차 보완 | 문서 수정 |
| #17 | 코드 리뷰 태그 사용 기준 추가 | 템플릿 수정 |
| #18 | 리뷰 태그별 사용 예시 추가 | 가이드 수정 |

단순히 댓글을 작성하는 데 그치지 않고, 리뷰에서 발견한 개선 사항을 실제 파일 수정과 추가 커밋으로 연결하였다.

단, 개인 프로젝트의 자체 리뷰 댓글은 다른 기여자가 수행하는 공식 승인 리뷰와 구분된다.

## 6. 선택과제 구현 결과

### 6.1 PR 템플릿 구성

`.github/pull_request_template.md` 파일을 작성하였다.

템플릿에는 변경 사항 요약, 변경 유형, 관련 이슈, 테스트 및 검증, 리뷰 요청 사항, 최종 체크리스트를 포함하였다.

이를 통해 PR 작성 형식을 표준화하고 필요한 정보가 누락되지 않도록 하였다.

### 6.2 CONTRIBUTING.md 작성

프로젝트 참여 및 협업 규칙을 문서화하였다.

주요 내용은 다음과 같다.

- GitHub Flow 브랜치 전략
- 브랜치 네이밍 규칙
- Conventional Commits 유형과 작성 예시
- Pull Request 작성 및 병합 절차
- 코드 리뷰 태그와 사용 예시

본 실습에서는 PR 템플릿과 협업 문서화 선택과제를 수행하였으며, CODEOWNERS 및 브랜치 보호 규칙 설정은 진행하지 않았다.

## 7. 실습 중 확인한 사항

GitHub Flow를 활용하면 main 브랜치를 직접 수정하지 않고 작업별로 변경 사항을 분리하여 관리할 수 있음을 확인하였다.

또한 PR을 생성한 후에도 동일한 작업 브랜치에서 추가 커밋을 Push하면 기존 PR에 변경 내용이 반영된다는 점을 실습하였다.

리뷰 태그를 활용하면 수정 필요성과 우선순위를 명확하게 전달할 수 있었으며, 피드백을 문서에 반영하는 과정을 통해 코드 리뷰가 단순한 오류 지적이 아닌 품질 개선 활동임을 이해하였다.

개인 프로젝트에서는 다른 기여자의 공식 리뷰를 경험하기 어렵다는 한계가 있었지만, 자체 리뷰 방식으로 피드백 작성과 수정 과정을 실습하였다.

## 8. 최종 구현 및 제출 결과

| 항목 | 수행 결과 |
|---|---|
| Feature 브랜치 전략 | 완료 |
| Conventional Commits 활용 | 완료 |
| PR 3건 생성 및 병합 | 완료 |
| PR별 자체 리뷰 피드백 | 완료 |
| [MUST] / [SHOULD] 태그 사용 | 완료 |
| 리뷰 피드백 수정 반영 | 완료 |
| PR 템플릿 작성 | 완료 (선택) |
| CONTRIBUTING.md 작성 | 완료 (선택) |
| CODEOWNERS 설정 | 미진행 (선택) |
| 브랜치 보호 규칙 | 미진행 (선택) |

**최종 PR 증빙**

- [PR #16 — GitHub Flow 문서](https://github.com/lmlalalala/OSS_SW_Programming/pull/16)
- [PR #17 — Pull Request 템플릿](https://github.com/lmlalalala/OSS_SW_Programming/pull/17)
- [PR #18 — CONTRIBUTING.md](https://github.com/lmlalalala/OSS_SW_Programming/pull/18)

## 9. 결론

이번 실습에서는 GitHub Flow를 적용하여 총 3건의 Pull Request를 생성하고 병합하는 과정을 수행하였다.

특히 자체 리뷰에서 작성한 피드백을 실제 파일 수정과 추가 커밋으로 반영하여 PR 기반 개발 과정을 경험할 수 있었다.

또한 PR 템플릿과 CONTRIBUTING.md를 작성하여 향후 프로젝트에서도 활용할 수 있는 기본적인 협업 규칙을 마련하였다.

이를 통해 GitHub의 브랜치 관리, 변경 이력 추적, 코드 리뷰 및 문서 중심 협업 방식의 중요성을 이해할 수 있었다.