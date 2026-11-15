# [8주차] 워크플로우 실행 최적화

## 1. 기존 7주차 구현 재사용

main에 병합된 7주차 CI/CD를 기준으로 `feature/week8-workflow-optimization`에서 작업했다.
7주차 워크플로우와 테스트, 패키징 코드는 수정하지 않았다.
8주차 워크플로우에서 기존 Python 스크립트, 테스트 7개, 소스 ZIP 및 데모 ZIP 생성 기능을 호출한다.
실제 서버, Pages, Release 배포는 하지 않는다.

## 2. 최적화 전후 구성

| 항목 | 기존 7주차 | 8주차 |
|---|---|---|
| Matrix | OS 3종 × Python 3.11·3.12 (6개) | Python 3.13 추가 (9개) |
| 환경 준비 | 각 작업에서 setup-python 반복 | Composite Action 공유 |
| 테스트 정의 | 메인 워크플로우에 직접 정의 | workflow_call 기반 Reusable Workflow |
| 패키지 캐시 | 없음 | Build에서 고정 버전 Ruff의 pip 다운로드 캐시 |
| 변경 감지 | 워크플로우 전체 경로 필터 | changes 작업이 CI·배포 필요 여부를 출력 |
| 배포 조건 | PR 이외 이벤트 | 지정 브랜치 push + 관련 파일 변경 + 테스트 성공 |
| 배포 결과 | 데모 ZIP | 기존 데모 ZIP 재사용 |

Composite Action은 Python 설정과 선택적 검사 도구 설치·캐시를 여러 작업에서 공유한다.
Reusable Workflow는 9개 환경의 테스트 작업 전체를 재사용한다.
호출할 때 `artifact-name`을 전달해 Build가 만든 동일한 소스 ZIP을 검사한다.
`fail-fast: false`로 한 환경의 실패가 다른 환경의 결과 확인을 중단하지 않게 했다.

## 3. 캐시 측정

동일 커밋·Ubuntu·Python 3.12에서 캐시 없음, 최초 저장, 재사용을 순서대로 실행했다.
세 조건 모두 같은 Ruff 검사와 unittest 7개를 통과했다.

| 조건 | 환경 준비·설치 | 작업 전체 |
|---|---:|---:|
| 캐시 없음 | 2초 | 23초 |
| 최초 저장 | 4초 | 23초 |
| 재사용 | 2초 | 19초 |

개선률 = (적용 전 - 적용 후) / 적용 전 × 100.
환경 준비·설치 개선률은 **0.0%**, 전체 작업 관측 감소율은 **17.4%**이다.
checkout도 16초에서 12초로 달라졌으므로 전체 차이를 캐시 효과로 단정하지 않는다.
캐시 적중과 wheel 재사용은 실제 로그에서 확인했지만, Ruff 하나의 설치에서는 안정적인 시간 개선을 입증하지 못했다.
조건별 1회, 초 단위 측정이라는 한계가 있다.

- [상세 비교 및 로그 원자료](docs/week8/CACHE_COMPARISON.md)
- [비교 실험](https://github.com/lmlalalala/OSS_SW_Programming/actions/runs/43725114162)

## 4. 선택적 데모 배포

changes 작업은 checkout의 전체 이력과 git diff를 사용한다.
Push는 직전 SHA와 현재 SHA, PR은 대상 브랜치 SHA와 PR head SHA를 비교한다.
이전 SHA가 없는 최초 push나 수동 실행에서는 빈 트리를 기준으로 전체 파일을 검사한다.
토큰이나 PR 제목을 명령문에 삽입하지 않고 SHA를 환경변수로 전달한다.

| 변경·이벤트 | Build·Test | 데모 ZIP |
|---|---|---|
| 지정 브랜치 Push + scripts/dashboard/패키징 코드/8주차 CI 설정 | 실행 | 테스트 성공 후 생성 |
| 지정 브랜치 Push + week7 테스트·검사 설정만 변경 | 실행 | 생략 |
| 지정 브랜치 Push + 문서만 변경 | 생략 | 생략 |
| main 대상 PR + 관련 파일 변경 | 실행 | 생략 |
| 수동 실행 | 전체 코드 검사 | 생략 |
| 그 밖의 브랜치 Push | 워크플로우 미실행 | 미실행 |

지정 브랜치는 main과 feature/week8-workflow-optimization이다.
문서만 바뀌어도 changes 결과를 볼 수 있도록 메인 워크플로우의 paths 필터를 제거했다.
PR은 main과의 전체 차이를 검사하므로, 코드 변경이 포함된 PR에서 문서만 추가해도 CI는 실행된다.
캐시 비교 워크플로우는 별도 경로 조건으로 불필요한 재측정을 피한다.

기본 토큰 권한은 contents: read이며, 기존 실제 지표 수집을 수행하는 데모 작업만 actions: read를 추가한다.
배포 결과는 Artifact로만 보관하며 테스트나 변경 감지가 실패하면 데모 작업도 진행하지 않는다.

## 5. 실제 검증 링크

- [Matrix 확장 성공](https://github.com/lmlalalala/OSS_SW_Programming/actions/runs/43724437296)
- [재사용 구조 분리 성공](https://github.com/lmlalalala/OSS_SW_Programming/actions/runs/43724769337)
- [캐시 적용 후 CI 성공](https://github.com/lmlalalala/OSS_SW_Programming/actions/runs/43725114049)
- [선택적 배포 Push 실행](https://github.com/lmlalalala/OSS_SW_Programming/actions/runs/43725542489)
- [선택적 배포 PR 실행](https://github.com/lmlalalala/OSS_SW_Programming/actions/runs/43725553386)
- [검토용 초안 PR #27](https://github.com/lmlalalala/OSS_SW_Programming/pull/27)

선택적 배포의 최종 실행 상태와 문서만 변경한 Push의 검증 결과는 실행 종료 후 아래에 기록한다.

## 6. 제출 파일

- [메인 워크플로우](.github/workflows/week8-ci-cd.yml)
- [Reusable Workflow](.github/workflows/week8-reusable-test.yml)
- [Composite Action](.github/actions/setup-week8-python/action.yml)
- [캐시 비교 워크플로우](.github/workflows/week8-cache-benchmark.yml)
- [캐시 비교용 재사용 작업](.github/workflows/week8-cache-sample.yml)

## 7. 정리

설정을 재사용하면 공통 환경 준비와 테스트 정의를 한 곳에서 수정할 수 있다.
Matrix 확장은 호환성 확인 범위를 넓히지만 총 실행 자원은 늘린다.
캐시는 항상 속도 개선을 보장하지 않으므로 실제 측정으로 판단해야 한다.
문서만 변경한 Push에서 검사와 데모 생성을 생략하는 조건은 불필요한 작업을 줄인다.
과제 확인을 위한 브랜치와 초안 PR만 만들었으며 main 병합은 하지 않았다.
