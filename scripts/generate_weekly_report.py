import json
import os
from datetime import datetime

METRICS_FILE = "dora-metrics.json"
REPORT_DIR = "reports"
REPORT_FILE = os.path.join(REPORT_DIR, "weekly-report.md")

# JSON 읽기
with open(METRICS_FILE, "r", encoding="utf-8") as file:
    data = json.load(file)

os.makedirs(REPORT_DIR, exist_ok=True)

generated_at = data.get("generated_at", "")
lead_time = data.get("lead_time_minutes", 0)
deployment_frequency = data.get("deployment_frequency", 0)
mttr = data.get("mttr_minutes", 0)
change_failure_rate = data.get("change_failure_rate", 0)

today = datetime.now().strftime("%Y-%m-%d")

report = f"""# DORA 주간 보고서

생성일: {today}

## 이번 주 DORA 지표

| 지표 | 값 |
|---|---:|
| Lead Time | {lead_time}분 |
| Deployment Frequency | {deployment_frequency}회 |
| MTTR | {mttr}분 |
| Change Failure Rate | {change_failure_rate}% |

## 분석

- 최근 7일간 성공한 배포 횟수는 **{deployment_frequency}회**입니다.
- 평균 Lead Time은 **{lead_time}분**입니다.
- 장애 발생 후 평균 복구 시간(MTTR)은 **{mttr}분**입니다.
- Change Failure Rate는 **{change_failure_rate}%**입니다.

## 데이터 생성 정보

- 측정 기간: 최근 7일
- 생성 시각: {generated_at}
- 데이터 소스: GitHub Actions 실행 기록
"""

with open(REPORT_FILE, "w", encoding="utf-8") as file:
    file.write(report)

print(f"{REPORT_FILE} 생성 완료")