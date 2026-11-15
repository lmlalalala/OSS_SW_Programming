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
로컬 결과만으로 GitHub의 Matrix와 실제 토큰 주입까지 성공했다고 판단하지는 않았다.

진행 중 기본 권한의 원격 clone이 네트워크 오류로 실패했고, 로컬 clone도 Git 실행 오류로 실패하였다.
이후 허용된 별도 원격 clone으로 작업 폴더를 준비하였다. Lint와 테스트 실행에서는 실패가 없었다.
GitHub 전송은 자동 승인 검토에서 사용자 승인 필요로 차단되어 아직 수행하지 않았다.

## 5. GitHub 검증 상태와 제출 링크

현재 상태: **로컬 구현·검증 완료, 원격 브랜치 전송 승인 대기.**
GitHub Actions 실행 링크와 실제 성공 여부는 전송 후 확인하여 보완해야 한다.
아직 실제 API 수집, 6개 Matrix 실행, 최종 데모 ZIP 생성이 GitHub에서 성공했다는 기록은 없다.

- 저장소: https://github.com/lmlalalala/OSS_SW_Programming
- 워크플로우: 이 보고서의 상대 경로 링크로 로컬 파일 확인 가능
- Actions 실행 내역: 아직 실행하지 않아 특정 실행 URL 없음

## 6. 배운 점과 한계

작업 순서는 `needs`로 연결하고 파일은 Artifact로 전달해야 서로 다른 실행 환경에서도 같은 빌드 결과를 검사할 수 있었다.
OS와 Python 버전은 Matrix로 조합하고, 인증정보는 필요한 단계에만 환경변수로 전달하도록 구성하였다.

기존 DORA 코드는 main의 최근 실행 기록을 최대 100개 조회하며,
성공한 Actions 횟수와 실행 시간을 배포 횟수·Lead Time의 대체 지표로 사용한다.
실제 서비스 배포나 커밋부터 운영 반영까지의 시간을 측정한 값은 아니다.
여러 실패가 연속되면 마지막 실패부터 복구 시간을 계산하는 기존 방식도 그대로 유지하였다.
이번 실습은 기존 계산 방법을 바꾸기보다 자동 검사와 결과물 전달 흐름을 추가하는 범위로 진행하였다.
