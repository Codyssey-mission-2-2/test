# m2-2 GitHub 협업 프로젝트

Git과 GitHub를 활용하여 이슈 기반 작업, 브랜치 관리, Pull Request(PR), 코드 리뷰, 충돌 해결을 실습하는 팀 프로젝트입니다. 사칙연산 유틸 함수를 함께 개발하며 협업 과정과 문제 해결 기록을 남깁니다.

## 1. 프로젝트 개요

| 항목 | 내용 |
| --- | --- |
| 팀명 | m2-2 |
| 진행 기간 | 2026.10.04 ~ 2026.10.21 |
| 팀 인원 | 3명 — 제출 인덱스와 PR 기록 기준 |
| 저장소 | Codyssey-mission-2-2/test |
| 결과물 유형 | A. 유틸 함수 모음 — 사칙연산 및 거듭제곱 |

### 프로젝트 목표

- GitHub Flow를 적용하여 main을 항상 정상 동작하는 상태로 유지합니다.
- Issue를 기준으로 작업을 나누고 PR을 통해 변경 사항을 병합합니다.
- 구체적인 리뷰와 피드백 반영을 통해 협업 경험을 쌓습니다.
- 충돌 및 Git 문제를 해결하고 재현 가능한 기록을 남깁니다.
- 모든 팀원이 결과물 작성과 리뷰에 참여합니다.

## 2. 팀원 및 역할

| 팀원 | GitHub 계정 | 구현 담당 |
| --- | --- | --- |
| 김병철 | andy1398 | 곱셈 및 거듭제곱 |
| 김병현 | rlaqudgus | 뺄셈 |
| 안중현 | JoongHyun-codyssey | 나눗셈 |

이름은 [제출 인덱스](docs/SUBMISSION.md), 계정과 구현 담당은 연결된 PR을 기준으로 정리했습니다. 트러블슈팅 문서의 ‘김병헌’ 표기와 제출 인덱스의 ‘김병현’ 표기는 최종 제출 전 확인이 필요합니다.

팀원별 PR은 [제출 및 기여 내역](docs/SUBMISSION.md), 실습 참여와 역할은 [트러블슈팅 기록](docs/troubleshooting-log.md)에서 확인할 수 있습니다.

## 3. 저장소 구성

| 경로 | 용도 |
| --- | --- |
| README.md | 프로젝트 소개, 결과물 사용법 및 진행 현황 |
| docs/ | 협업 문서 및 실습 기록 |
| docs/SUBMISSION.md | 팀원별 PR과 제출 문서·증빙 링크 |
| docs/CONTRIBUTING.md | 브랜치 전략, 네이밍 및 커밋 규칙 |
| docs/conflict-resolution.md | 충돌 상황과 해결 과정 |
| docs/troubleshooting-log.md | Git 트러블슈팅 실습 기록 |
| docs/git-log.txt | Git 커밋 이력 텍스트 |
| src/ | 사칙연산 및 거듭제곱 유틸 함수와 실행 예시 파일 |
| team/ | 팀 소개 선택 시 팀원별 소개 파일 |

team/ 안내는 유지하며, 현재 기준 브랜치에는 해당 폴더가 없습니다.

## 4. 결과물 및 사용 방법

Python 3.10 이상에서 사용하는 유틸 함수 모음입니다. 별도의 외부 패키지 설치는 필요하지 않습니다.

| 파일 | 함수 | 기능 및 입력 조건 |
| --- | --- | --- |
| [add.py](src/add.py) | add(a, b) | 정수 두 개의 덧셈 |
| [Subtract.py](src/Subtract.py) | subtract(a, b) | 정수·실수의 뺄셈, bool 및 숫자가 아닌 입력 거부 |
| [devide.py](src/devide.py) | add(a, b) | 정수 두 개의 나눗셈, 제수는 0이 아니어야 함 |
| [multiply.py](src/multiply.py) | multiply(a, b) | 곱셈 |
| [multiply.py](src/multiply.py) | Power1(a, b) | a의 b제곱 |
| [multiply.py](src/multiply.py) | pectori(a) | a의 제곱 |

나눗셈 파일명은 현재 devide.py, 함수명은 add입니다. 아래 예시는 실제 이름을 사용하며, 덧셈 함수와 구분하기 위해 divide라는 별칭으로 가져옵니다.

### 실행 예시

저장소를 내려받고 src 폴더에서 Python을 실행합니다.

```bash
git clone https://github.com/Codyssey-mission-2-2/test.git
cd test/src
python3
```

Python 대화형 환경에 아래 코드를 입력합니다.

```python
from add import add
from Subtract import subtract
from devide import add as divide
from multiply import multiply, Power1, pectori

print(add(8, 2))        # 10
print(subtract(8, 2))   # 6
print(divide(8, 2))     # 4.0
print(multiply(8, 2))   # 안내 문구 출력 후 16
print(Power1(2, 3))     # 안내 문구 출력 후 8
print(pectori(3))       # 안내 문구 출력 후 9
```

### 현재 실행 시 주의할 점

- devide.py에서 제수가 0이면 ZeroDivisionError가 발생합니다.
- src/main.py는 multiply.Power1()을 호출하지만 multiply를 import하지 않아 직접 실행 시 NameError가 발생합니다. 현재는 위 함수별 호출 예시로 결과물을 확인합니다.
- 곱셈·거듭제곱 함수는 계산 안내 문구를 출력한 뒤 계산값을 반환합니다.

## 5. 브랜치 전략 및 협업 흐름

### GitHub Flow 선택 이유

- main과 feature/* 중심의 단순한 구조로 팀원이 빠르게 익힐 수 있습니다.
- 작은 단위로 자주 병합하여 빠른 피드백을 받을 수 있습니다.
- 독립 브랜치에서 작업하고 PR 리뷰를 통해 변경 사항을 검토할 수 있습니다.

### 브랜치 규칙

[협업 가이드](docs/CONTRIBUTING.md)의 규칙을 따릅니다.

| 브랜치 | 역할과 규칙 |
| --- | --- |
| main | 정상 동작하는 기준 브랜치. 직접 push 금지, PR로만 병합 |
| feature/<이슈번호>-<작업-내용-요약> | 최신 main에서 분기하는 작업 브랜치. 병합 후 삭제 |

작업 내용은 영문 소문자·숫자·하이픈을 사용하고 한 브랜치에는 한 가지 작업만 담습니다. 예: feature/31-update-readme. 협업 가이드는 이슈번호 없는 이름도 허용하지만, 이 과제에서는 모든 작업을 Issue로 추적합니다.

### 작업 순서

1. 작업 목적과 완료 조건을 담은 Issue를 생성합니다.
2. 최신 main에서 작업 브랜치를 생성합니다.
3. 변경 사항을 검증한 뒤 팀 규칙에 맞춰 커밋하고 push합니다.
4. main 대상 PR에 What·Why·How와 Closes #이슈번호를 작성합니다.
5. 다른 팀원의 리뷰에 답하고 필요한 수정을 반영합니다.
6. 최소 1명의 승인과 검증을 거쳐 병합합니다.
7. 작업 브랜치를 삭제하고 [제출 인덱스](docs/SUBMISSION.md)에 증빙을 정리합니다.

### 커밋·리뷰·병합 규칙

- 커밋 형식은 <type>(<scope>): <subject>이며 scope는 선택입니다. 예: docs: README에 함수 사용 예시 추가.
- type은 영문 소문자, subject는 한글 중심의 구체적인 변경 내용으로 작성합니다. subject는 50자 이내이며 끝에 마침표를 붙이지 않습니다.
- update, fix, wip처럼 대상과 효과가 드러나지 않는 메시지는 사용하지 않습니다.
- 각 PR에는 파일·라인에 근거한 질문, 대안, 리스크 또는 개선 의견을 최소 1개 남깁니다. ‘LGTM’만으로 리뷰를 마치지 않습니다.
- 각 PR에서 작성자와 리뷰어의 답글 또는 수정 반영 등 상호작용을 최소 1회 남깁니다.
- 협업 가이드는 승인과 CI 통과, 최신 main 반영 후 병합을 권장합니다. 실제 보호 설정과 CI 구성 충족 여부는 제출 전 별도로 확인합니다.
- 공유 브랜치의 히스토리를 무리하게 재작성하지 않으며 팀 합의 없이 강제 push·rebase하지 않습니다.
커밋 유형과 상세 절차는 [CONTRIBUTING.md](docs/CONTRIBUTING.md)를 참고합니다.

## 6. 충돌 해결 및 Git 트러블슈팅

충돌이 발생하면 관련 작업자에게 공유하고 최종 내용을 협의합니다. 해결 후 실행·문서 검증을 수행하고 참여자, 명령어, 결과, PR·커밋 링크를 기록합니다.

### 충돌 기록

| 사례 | 내용 | 기록 |
| --- | --- | --- |
| README 충돌 | GitHub Flow 목표 문장의 동일 행 수정 | [해결 기록](docs/conflict-resolution.md), PR #13 |
| main.py 충돌 | 입력 안내 문구의 동일 구간 수정 | [해결 기록](docs/conflict-resolution.md), PR #16 |

문서에는 동일 hunk 수정 사례 2건이 기록되어 있습니다. 제출 전 해결 커밋과 검증 결과의 일치 여부를 확인합니다.

### 트러블슈팅 기록 현황

아래 상태는 [트러블슈팅 문서](docs/troubleshooting-log.md)의 본문 기준입니다.

| 시나리오 | 실습 내용 | 문서상 상태 |
| --- | --- | --- |
| git commit --amend | 최근 커밋 메시지 수정 | 기록 있음, 본문에 실행 결과 추가 확인 필요로 표시 |
| git reset --soft HEAD~1 | 로컬 커밋 취소 및 변경 유지 | 실행 기록 있음, 스테이징 유지 증빙 추가 확인 필요로 표시 |
| git revert | 원격에 push한 변경을 새 커밋으로 취소 | 완료로 기록 |
| git stash / git stash pop | 작업 보관, 브랜치 전환 및 복원 | 완료로 기록 |

문서 후반의 팀원별 캡처와 본문 상태를 대조하여 최종 제출 전에 정리합니다. amend와 reset은 아직 push하지 않은 로컬 커밋으로 실습하고, 공유된 변경을 취소할 때는 revert를 사용합니다.

## 7. 주요 문서 및 증빙

- [협업 가이드](docs/CONTRIBUTING.md)
- [충돌 해결 기록](docs/conflict-resolution.md)
- [Git 트러블슈팅 기록](docs/troubleshooting-log.md)
- [제출 및 팀원별 PR 내역](docs/SUBMISSION.md)
- [Git 커밋 이력](docs/git-log.txt)
현재 제출 인덱스에 기록된 로그 추출 명령은 그래프 옵션을 포함하지 않습니다. 과제의 히스토리 증빙 형식에 맞춰 최종 제출 전 아래 명령으로 갱신해야 합니다.

```bash
git log --oneline --graph --all > docs/git-log.txt
```

## 8. 제출 전 확인

아래 항목은 최종 검증용이며, 문서가 존재한다는 이유만으로 실습 완료를 표시하지 않습니다.

- [ ] 팀원 3명의 이름·계정과 역할을 최종 확인했다.
- [ ] main 직접 push 금지, PR 병합 및 최소 1명 승인 설정을 확인했다.
- [ ] 협업 가이드를 팀원이 분담하여 작성했다.
- [ ] 모든 작업의 Issue와 PR이 연결되어 있다.
- [ ] 모든 팀원이 PR 2개 이상을 생성하고 병합했다.
- [ ] 모든 팀원이 타인 PR 리뷰를 2개 이상 작성했다.
- [ ] 각 PR에 실질적인 리뷰 코멘트와 작성자·리뷰어 상호작용이 있다.
- [ ] 모든 팀원이 본인 PR에서 리뷰 의견을 1회 이상 반영했다.
- [ ] 충돌 해결 2회 이상과 비자명 충돌 1회 이상의 증빙을 확인했다.
- [ ] 트러블슈팅 4종의 수행 결과와 팀원별 기록 참여를 확인했다.
- [ ] 팀원별 함수 1개 이상과 결과물 기여 커밋 1건 이상을 확인했다.
- [ ] 함수 사용 예시와 실행 진입점의 동작을 확인했다.
- [ ] 제출 인덱스에 팀원별 Issue·PR·리뷰·반영 증빙을 정리했다.
- [ ] git log --oneline --graph --all 형식의 히스토리 증빙을 저장했다.
- [ ] 문서 링크와 기록 상태, 이름 표기의 일관성을 확인했다.
