import os
import json
import urllib.request
from datetime import datetime, timezone, timedelta

# GitHub Actions 환경변수
repository = os.environ.get("GITHUB_REPOSITORY")
token = os.environ.get("GITHUB_TOKEN")

if not repository:
    raise Exception("GITHUB_REPOSITORY 환경변수가 없습니다.")

if not token:
    raise Exception("GITHUB_TOKEN 환경변수가 없습니다.")


# GitHub Actions 실행 기록 API
url = (
    f"https://api.github.com/repos/{repository}/actions/runs"
    "?branch=main&per_page=100"
)

request = urllib.request.Request(url)

request.add_header(
    "Authorization",
    f"Bearer {token}"
)

request.add_header(
    "Accept",
    "application/vnd.github+json"
)


# GitHub API 호출
with urllib.request.urlopen(request) as response:
    data = json.loads(response.read().decode())


workflow_runs = data["workflow_runs"]


# 최근 7일 기준
now = datetime.now(timezone.utc)
week_ago = now - timedelta(days=7)


recent_runs = []

for run in workflow_runs:

    created_at = datetime.fromisoformat(
        run["created_at"].replace("Z", "+00:00")
    )

    if created_at >= week_ago:
        recent_runs.append(run)


# -------------------------
# Deployment Frequency
# -------------------------

successful_runs = [
    run for run in recent_runs
    if run["conclusion"] == "success"
]

deployment_frequency = len(successful_runs)


# -------------------------
# Change Failure Rate
# -------------------------

completed_runs = [
    run for run in recent_runs
    if run["conclusion"] is not None
]

failed_runs = [
    run for run in completed_runs
    if run["conclusion"] == "failure"
]

if len(completed_runs) > 0:
    change_failure_rate = (
        len(failed_runs)
        / len(completed_runs)
        * 100
    )
else:
    change_failure_rate = 0


# -------------------------
# Lead Time
# -------------------------

lead_times = []

for run in successful_runs:

    created_at = datetime.fromisoformat(
        run["created_at"].replace("Z", "+00:00")
    )

    updated_at = datetime.fromisoformat(
        run["updated_at"].replace("Z", "+00:00")
    )

    lead_time = (
        updated_at - created_at
    ).total_seconds() / 60

    lead_times.append(lead_time)


if lead_times:
    average_lead_time = sum(lead_times) / len(lead_times)
else:
    average_lead_time = 0


# -------------------------
# MTTR
# -------------------------

mttr_values = []

sorted_runs = sorted(
    completed_runs,
    key=lambda run: run["created_at"]
)

failure_time = None

for run in sorted_runs:

    created_at = datetime.fromisoformat(
        run["created_at"].replace("Z", "+00:00")
    )

    if run["conclusion"] == "failure":
        failure_time = created_at

    elif (
        run["conclusion"] == "success"
        and failure_time is not None
    ):

        recovery_time = (
            created_at - failure_time
        ).total_seconds() / 60

        mttr_values.append(recovery_time)

        failure_time = None


if mttr_values:
    mttr = sum(mttr_values) / len(mttr_values)
else:
    mttr = 0


# -------------------------
# JSON 결과
# -------------------------

dora_metrics = {

    "generated_at":
        datetime.now(timezone.utc).isoformat(),

    "period":
        "last_7_days",

    "lead_time_minutes":
        round(average_lead_time, 2),

    "deployment_frequency":
        deployment_frequency,

    "mttr_minutes":
        round(mttr, 2),

    "change_failure_rate":
        round(change_failure_rate, 2)

}


print("=== DORA Metrics ===")

print(
    f"Lead Time: "
    f"{dora_metrics['lead_time_minutes']} minutes"
)

print(
    f"Deployment Frequency: "
    f"{deployment_frequency}"
)

print(
    f"MTTR: "
    f"{dora_metrics['mttr_minutes']} minutes"
)

print(
    f"Change Failure Rate: "
    f"{change_failure_rate:.2f}%"
)


with open(
    "dora-metrics.json",
    "w",
    encoding="utf-8"
) as file:

    json.dump(
        dora_metrics,
        file,
        indent=4,
        ensure_ascii=False
    )


print("dora-metrics.json 생성 완료")