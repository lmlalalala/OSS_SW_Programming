# 8주차 캐시 적용 전후 실측

## 실험 조건

- 동일 커밋 `df7251c`, Ubuntu / Python 3.12, `ruff==0.14.3`.
- 캐시 없음 → 최초 저장(cold) → 재사용(warm)을 서로 다른 GitHub 호스팅 작업에서 순서대로 실행했다.
- 세 작업 모두 같은 코드 검사와 unittest 7개를 통과했다.
- 캐시 없음은 `pip install --no-cache-dir`로 실행했다.
- 최초 저장과 재사용은 같은 키를 쓴다. 키에 run_id와 run_attempt를 넣어 다른 실험과 분리했다.
- 실제 CI의 Build에도 같은 Composite Action을 통해 pip 다운로드 캐시를 적용했다. 테스트는 외부 패키지가 필요 없어 캐시하지 않았다.

## 실제 결과

| 조건 | 캐시 상태 | 환경 준비·설치 | 작업 전체 |
|---|---|---:|---:|
| 캐시 없음 | 비활성 | 2초 | 23초 |
| 최초 저장 | miss → 저장 | 4초 | 23초 |
| 재사용 | exact hit | 2초 | 19초 |

시간은 GitHub Jobs API의 started_at과 completed_at 차이로 계산했다.
환경 준비·설치는 `Prepare Python and install lint tool` 단계이며 Python 설정과 캐시 복원, 설치가 포함된다.
작업 전체는 checkout, 검사, 테스트, 후처리를 포함하고 실행 대기 시간은 제외한다.

개선률 = (적용 전 시간 - 적용 후 시간) / 적용 전 시간 × 100

- 환경 준비·설치: (2 - 2) / 2 × 100 = **0.0%**
- 작업 전체 관측값: (23 - 19) / 23 × 100 = **17.4%**

## 해석과 한계

캐시 적중과 Ruff 다운로드 재사용은 로그로 확인했다. 그러나 설치 대상이 Ruff 하나여서 환경 준비·설치 단계의 시간 감소는 이번 측정에서 확인되지 않았다.
전체 작업의 checkout 시간도 16초에서 12초로 달랐다. 따라서 전체 17.4% 감소를 캐시의 효과라고 단정할 수 없다.
조건별 1회 측정이며 단계 시각은 초 단위이므로 작은 차이와 실행 환경 변동을 구분하기 어렵다.
최초 저장에는 복원 확인과 캐시 업로드 비용도 발생한다. 이번 결과는 캐시 기능 구현과 적중 검증의 근거이며 안정적인 속도 개선을 입증하는 결과는 아니다.
추가 패키지나 불필요한 지연을 넣어 개선률을 부풀리지 않았다.

## 확인 링크와 원자료

- [비교 실험 전체](https://github.com/lmlalalala/OSS_SW_Programming/actions/runs/43725114162)
- [캐시 없음](https://github.com/lmlalalala/OSS_SW_Programming/actions/runs/43725114162/job/132845250798)
- [최초 저장](https://github.com/lmlalalala/OSS_SW_Programming/actions/runs/43725114162/job/132845374485)
- [재사용](https://github.com/lmlalalala/OSS_SW_Programming/actions/runs/43725114162/job/132845499782)
- [캐시 적용 후 CI 전체 성공](https://github.com/lmlalalala/OSS_SW_Programming/actions/runs/43725114049)
- [Jobs API 시각 및 캐시 로그 발췌](cache-measurements.json)
- [캐시 Action 공식 문서](https://github.com/actions/cache)

선택적 배포 조건 검증과 최종 통합 보고서는 다음 단계에서 작성한다.
