# [7주차] GitHub Actions 기반 CI/CD 실습

## 1. 실습 내용

2주차의 DORA Python 스크립트와 대시보드를 활용하여 CI/CD 워크플로우를 작성하였다.
`feature/week7-ci-cd` 브랜치에서 작업했으며, 기존 주차 문서와 README 및 기존 워크플로우는 수정하지 않았다.

이번 Deploy 단계는 결과물을 ZIP Artifact로 보관하는 데모 단계이다.
실서버, GitHub Pages, Release로 배포하는 기능은 넣지 않았다.

## 2. 워크플로우 구성

파일: [week7-ci-cd.yml](.github/workflows/week7-ci-cd.yml)

| 단계 | 구성 |
|---|---|
| Build | Ruff로 기존 scripts와 week7 코드를 검사하고, 스크립트와 대시보드를 ZIP으로 압축 |
| Test | Build의 ZIP을 다운로드·압축 해제한 뒤 unittest 실행 |
| Matrix | Ubuntu, Windows, macOS × Python 3.11, 3.12의 6개 조합 |
| Deploy | 모든 Test 성공 후 실제 Actions 데이터를 수집하고 보고서·대시보드·JSON을 데모 ZIP으로 보관 |

`needs: build`와 `needs: test`로 실행 순서를 연결하였다.
Lint 또는 Build가 실패하면 Test와 Deploy가 실행되지 않고, Matrix 중 하나라도 실패하면 Deploy가 실행되지 않는다.
`fail-fast: false`는 한 조합이 실패해도 다른 조합의 결과를 확인하기 위한 설정이다.

브랜치 Push와 main 대상 PR에서 실행하며, PR에서는 Deploy를 건너뛴다.
`workflow_dispatch`도 정의했지만, 기본 브랜치에 없는 새 워크플로우는 수동 실행 UI에 바로 표시되지 않을 수 있다.
현재 첫 실행은 브랜치 Push를 기준으로 한다. 보고서만 수정한 Push는 경로 필터에 의해 재실행하지 않는다.

## 3. Secrets와 Artifact

수집 단계에서만 `env`로 `GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}`을 전달한다.
GitHub가 발급하는 기본 토큰을 사용하므로 개인 PAT나 별도 사용자 Secret은 등록하지 않았다.
기본 권한은 `contents: read`이고, 실제 API를 호출하는 Deploy 작업에만 `actions: read`를 추가하였다.
토큰 값을 출력하거나 ZIP에 넣지 않는다. 테스트에서는 실제 토큰 대신 테스트 전용 문자열과 가짜 API 응답을 사용한다.

- `week7-source`: Build가 올리고 Test와 Deploy가 내려받는 소스 ZIP
- `week7-demo-package`: 실제 수집 JSON, 주간 보고서, 대시보드를 담는 데모 ZIP
- 보관 기간: 각각 7일. 결과 파일이 없으면 Artifact 업로드를 실패 처리한다.

데모 ZIP은 고정된 파일 목록만 포함한다. 내려받아 압축을 풀고 해당 폴더에서
`python -m http.server 8080`을 실행한 뒤 `http://localhost:8080/dashboard/`에서 확인하는 구조이다.
대시보드의 Chart.js는 기존 외부 CDN을 사용하므로 인터넷 연결이 필요하다.

## 4. 로컬 검증 기록

Windows / Python 3.13.2 환경에서 다음을 실제 실행하였다.

```text
python -m ruff check --config week7/ruff.toml scripts week7
All checks passed!

python week7/package_demo.py build --output dist/dora-source.zip
Created dist\dora-source.zip (3 files). No external deployment.

python -m zipfile -e dist/dora-source.zip package
# DORA_SOURCE_ROOT=package로 설정한 뒤 실행
python -m unittest discover -s week7/tests -v
Ran 7 tests
OK
```

테스트에서는 지표 계산값, 최근 7일 필터, 진행 중인 실행 제외, 빈 기록,
환경변수 누락, API 요청의 인증 헤더, 보고서 생성, ZIP 파일 구성과 불필요한 파일 제외를 확인하였다.
YAML은 PyYAML로 읽고 Build → Test → Deploy 의존성도 확인하였다.
로컬 검증 이후 GitHub에서도 Matrix와 실제 토큰을 사용하는 수집 단계를 실행하여 확인하였다.

진행 중 기본 권한의 원격 clone이 네트워크 오류로 실패했고, 로컬 clone도 Git 실행 오류로 실패하였다.
이후 허용된 별도 원격 clone으로 작업 폴더를 준비하였다. Lint와 테스트 실행에서는 실패가 없었다.
GitHub 전송은 처음에 사용자 승인 필요로 중단되었고, 승인 후 7주차 브랜치만 전송하였다.

## 5. GitHub 검증 상태와 제출 링크

2026년 11월 15일(KST), 브랜치 Push로 시작한 실행 `43721651623`의 최종 상태가
`completed / success`인 것을 확인하였다. 검증 대상 커밋은
`f536c7dfcea4249d02d346be0df2aa51a32a49f3`이다.

| 확인 항목 | 실제 결과 |
|---|---|
| Build | Lint, 소스 ZIP 생성 및 업로드 성공 |
| Ubuntu / Python 3.11, 3.12 | 두 조합 모두 테스트 성공 |
| Windows / Python 3.11, 3.12 | 두 조합 모두 테스트 성공 |
| macOS / Python 3.11, 3.12 | 두 조합 모두 테스트 성공 |
| Deploy (demo ZIP only) | 토큰을 이용한 API 수집, 보고서 생성, 데모 ZIP 업로드 성공 |
| Artifact | `week7-source`, `week7-demo-package` 두 개 생성 확인 |

총 8개 작업(Build 1개, Test 6개, Deploy 1개)이 모두 성공하였다.
이 실행에서 실패한 작업은 없었다. Artifact 목록과 만료되지 않은 상태도 확인하였다.
보관 기간은 7일이므로 제출 시점에 따라 다운로드가 만료될 수 있다.
이번 확인은 실행 상태와 단계 결과, Artifact 목록을 기준으로 하였으며,
다운로드한 데모 대시보드를 브라우저로 여는 확인은 수행하지 않았다.

- [저장소](https://github.com/lmlalalala/OSS_SW_Programming)
- [워크플로우 YAML](https://github.com/lmlalalala/OSS_SW_Programming/blob/feature/week7-ci-cd/.github/workflows/week7-ci-cd.yml)
- [Actions 성공 실행 내역](https://github.com/lmlalalala/OSS_SW_Programming/actions/runs/43721651623)
- [제출용 보고서](https://github.com/lmlalalala/OSS_SW_Programming/blob/feature/week7-ci-cd/WEEK7_CI_CD.md)

보고서만 갱신한 후속 커밋에는 코드 변경이 없으며, 경로 필터에 따라 Actions를 다시 실행하지 않는다.
main 병합과 실서버 배포는 수행하지 않았다.

## 6. 배운 점과 한계

작업 순서는 `needs`로 연결하고 파일은 Artifact로 전달해야 서로 다른 실행 환경에서도 같은 빌드 결과를 검사할 수 있었다.
OS와 Python 버전은 Matrix로 조합하고, 인증정보는 필요한 단계에만 환경변수로 전달하도록 구성하였다.

기존 DORA 코드는 main의 최근 실행 기록을 최대 100개 조회하며,
성공한 Actions 횟수와 실행 시간을 배포 횟수·Lead Time의 대체 지표로 사용한다.
실제 서비스 배포나 커밋부터 운영 반영까지의 시간을 측정한 값은 아니다.
여러 실패가 연속되면 마지막 실패부터 복구 시간을 계산하는 기존 방식도 그대로 유지하였다.
이번 실습은 기존 계산 방법을 바꾸기보다 자동 검사와 결과물 전달 흐름을 추가하는 범위로 진행하였다.
