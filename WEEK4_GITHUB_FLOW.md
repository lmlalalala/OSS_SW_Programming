# Week 4 - GitHub Flow 및 코드 리뷰 실습

## 실습 목표
- Feature 브랜치를 활용한 독립적인 작업
- Conventional Commits 규칙 적용
- Pull Request 생성 및 코드 리뷰 실습

## 브랜치 전략
- 기준 브랜치: main
- 작업 브랜치: feature/week4-review
- 협업 방식: GitHub Flow

## 진행 과정
1. Feature 브랜치 생성
2. 변경 사항 커밋
3. Pull Request 생성
4. 리뷰 및 피드백 반영
5. main 브랜치로 병합

## GitHub Flow 실습 명령어

1. 브랜치 생성
   - git switch -c feature/week4-review

2. 파일 변경 및 커밋
   - git add WEEK4_GITHUB_FLOW.md
   - git commit -m "docs: add week4 GitHub Flow guide"

3. 원격 저장소에 업로드
   - git push -u origin feature/week4-review

4. Pull Request 생성
   - GitHub에서 feature 브랜치를 main으로 병합하도록 PR 생성

5. 코드 리뷰
   - [SHOULD] 피드백을 확인하고 수정 사항 반영