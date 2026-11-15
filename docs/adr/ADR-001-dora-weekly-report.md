# ADR-001: DORA 주간 리포트 공유 방식 개선

## 1. 기본 정보

- **상태(Status):** Proposed
- **작성일(Date):** 2026-11-15
- **작성자(Author):** OSS_SW_Programming 프로젝트 담당자
- **관련 RFC:** RFC-001 - GitHub Actions 기반 DORA 주간 리포트 공유 방식 개선

## 2. 배경 (Context)

OSS_SW_Programming 프로젝트에서는 2주차 실습을 통해 GitHub Actions 기반 DORA 메트릭 수집 자동화를 구현했다.

Push, Workflow Dispatch, Schedule 이벤트를 활용하여 메트릭 수집을 자동화하고, 계산 결과를 JSON 파일과 Artifact로 저장하는 구조를 구성했다.

하지만 기존 방식은 GitHub Actions 실행 기록을 확인해야 결과에 접근할 수 있어, 주간 리포트를 공유하거나 이전 기록과 비교하는 데 불편함이 발생할 수 있다.

따라서 기존 메트릭 수집 기능을 유지하면서 비동기 협업 환경에서 결과를 더욱 쉽게 공유할 수 있는 방법을 검토한다.

## 3. 검토한 대안 (Alternatives)

### 대안 A. 기존 Artifact 저장 방식 유지

GitHub Actions 실행 결과를 JSON Artifact로 저장하고 필요한 경우 직접 다운로드하여 확인한다.

**장점**
- 기존 구현 구조 유지 가능
- 추가 개발 및 관리 부담이 적음
- 원본 데이터 확인 가능

**단점**
- 실행 내역에 접근해야 결과 확인 가능
- 주차별 비교 및 공유가 번거로울 수 있음

### 대안 B. Artifact 유지 및 Discussions 자동 게시

기존 JSON Artifact 저장 방식을 유지하면서, 주간 DORA 메트릭을 요약하여 GitHub Discussions에 자동으로 게시한다.

**장점**
- 원본 데이터와 요약 리포트 동시 관리
- 주간 개발 성과에 대한 접근성 향상
- 반복적인 공유 작업 자동화
- 비동기 협업 및 투명한 정보 공유 지원

**단점**
- 추가 GitHub Actions 워크플로우 작성 필요
- Discussions 게시 권한 및 API 연동 설정 필요
- 중복 게시 및 자동화 실패에 대한 예외 처리 필요

## 4. 결정 사항 (Decision)

**현재 상태: Proposed (검토 중)**

1차 검토 결과, 대안 B를 우선 권고한다.

기존 Artifact 저장 방식의 장점을 유지하면서 Discussions를 통해 주간 리포트 접근성과 공유 편의성을 높일 수 있기 때문이다.

다만 최종 채택 여부는 다음 사항을 확인한 후 결정한다.

- GitHub Actions에서 Discussions 게시가 가능한지
- 필요한 인증 및 권한을 안전하게 설정할 수 있는지
- 워크플로우 실패와 중복 게시에 대응할 수 있는지

최종 결정이 확정되면 ADR 상태를 Accepted 또는 Rejected로 변경한다.

## 5. 예상 영향 (Consequences)

### 긍정적 영향

- DORA 메트릭 결과에 대한 가시성 향상
- 주간 개발 성과 공유 절차 간소화
- 프로젝트 구성원 간 비동기 정보 공유 개선
- 개발 활동 기록의 체계적인 관리

### 부정적 영향 및 위험

- GitHub Actions 워크플로우 관리 범위 증가
- 자동 게시 과정에서 API 오류 발생 가능
- 자동 게시 권한의 적절한 관리 필요
- 동일 주차의 리포트가 중복 게시될 가능성

## 6. 후속 작업 (Follow-up Actions)

- [x] RFC-001 기술 개선 제안 작성
- [x] 대안 A와 대안 B 비교
- [x] RFC-001 1차 검토 의견 기록
- [ ] 최종 기술적 의사결정 확정
- [ ] 주간 요약 자동 게시 워크플로우 초안 작성
- [ ] 인증 및 권한 설정 검토
- [ ] 중복 게시 방지 방법 검토
- [ ] 자동화 실행 결과 검증
- [ ] ADR 상태 갱신

## 7. 참고 자료 (References)

- [OSS_SW_Programming Repository](https://github.com/lmlalalala/OSS_SW_Programming)
- [Project Wiki](https://github.com/lmlalalala/OSS_SW_Programming/wiki)
- [RFC-001 기술 토론](https://github.com/lmlalalala/OSS_SW_Programming/discussions/21)

---

본 ADR은 OSS_SW_Programming 프로젝트의 기술적 의사결정 과정과 검토 근거를 투명하게 기록하기 위해 작성되었다.
