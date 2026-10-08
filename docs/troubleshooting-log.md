# Git 트러블슈팅 실습 기록

## 1. 실습 개요

- **실습 주제:** Git 트러블슈팅 4종
- **참여자:** 김병철,김병헌, 안중현
- **담당 역할:** Git 명령어 실습, 문제 해결, 실행 결과 확인 및 문서화
- **실습 환경:** macOS, VS Code, Git, GitHub
- **사용 브랜치:** `feature-multiply`, `practice/stash-test`

Git 명령어를 사용하여 커밋 수정, 로컬 커밋 취소, 원격에 반영된 커밋 취소, 임시 작업 보관 및 복원 방법을 학습하였다.

---

## 2. git commit --amend (최근 커밋 메시지 수정)

### 문제 상황
최근 커밋을 생성한 이후 커밋 메시지를 잘못 작성했거나 수정해야 하는 상황을 가정하였다.

### 해결 방법
```bash
git commit --amend -m "수정할 커밋 메시지"
```

### 실행 결과
- 기존 커밋 메시지를 수정할 수 있는 명령어를 확인하였다.
- 기존 커밋을 새로운 커밋으로 대체하므로 커밋 해시가 변경된다.

**진행 상태:** 실제 명령어 실행 및 변경 결과 추가 확인 필요

---

## 3. git reset --soft HEAD~1 (로컬 커밋 취소)

### 문제 상황
최근 생성한 로컬 커밋을 취소하되, 수정한 코드와 스테이징된 변경 사항은 그대로 유지해야 하는 상황을 가정하였다.

### 해결 과정
```bash
git reset --soft HEAD~1
git log --oneline -1
```

### 실행 결과
- `git reset --soft HEAD~1` 명령어를 실행하였다.
- 최근 커밋을 취소하고 이전 커밋을 가리키도록 HEAD를 이동시키는 명령어임을 확인하였다.
- `--soft` 옵션은 작업 파일과 스테이징 영역을 유지한다.

**진행 상태:** 명령어 실행 확인, 스테이징 유지 결과는 추가 증빙 필요

---

## 4. git revert (원격에 push된 커밋 취소)

### 문제 상황
이미 원격 저장소에 push한 커밋의 변경 사항을 취소해야 하는 상황이 발생하였다.

공유된 커밋 기록을 삭제하는 대신 새로운 취소 커밋을 생성하는 방법을 사용하였다.

### 해결 과정
```bash
git revert <취소할-커밋해시>
git push origin feature-multiply
git log --oneline -3
```

### 실행 결과
기존 커밋:

```text
86d2ee6 feat: main.py 및 SUBMISSION.md 수정
```

취소 커밋:

```text
c552471 Revert "feat: main.py 및 SUBMISSION.md 수정"
```

- 기존 변경 사항을 되돌리는 Revert 커밋을 생성하였다.
- 원격 저장소에 push한 기록을 확인하였다.
- 원래 커밋 기록은 유지하면서 반대 변경 사항을 적용하는 방법을 학습하였다.

**진행 상태:** 완료

---

## 5. git stash / git stash pop (작업 임시 보관 및 복원)

### 문제 상황
`src/multiply.py`를 수정하던 중 다른 브랜치로 이동해야 하는 상황을 가정하였다.

수정 내용을 커밋하지 않고 임시로 보관한 후 새로운 브랜치에서 복원하는 실습을 진행하였다.

### 해결 과정

**1단계: 보관된 작업 확인**

```bash
git stash list
git stash show --stat 'stash@{0}'
```

실행 결과:

```text
src/multiply.py | 4 +++-
1 file changed, 3 insertions(+), 1 deletion(-)
```

**2단계: 실습 브랜치 생성 및 전환**

```bash
git switch -c practice/stash-test
```

실행 결과:

```text
Switched to a new branch 'practice/stash-test'
```

**3단계: 보관된 변경 내용 확인**

```bash
git stash show -p 'stash@{0}'
```

`src/multiply.py`에 출력 문장을 추가한 변경 사항을 확인하였다.

**4단계: 보관된 작업 복원**

```bash
git stash pop
```

실행 결과:

```text
On branch practice/stash-test

Changes not staged for commit:
    modified: src/multiply.py

Dropped refs/stash@{0}
```

**5단계: 복원 결과 확인**

```bash
git status
```

실행 결과:

```text
On branch practice/stash-test

Changes not staged for commit:
    modified: docs/troubleshooting-log.md
    modified: src/multiply.py
```

### 최종 결과
- stash에 보관된 파일을 확인하였다.
- 새로운 브랜치를 생성하고 전환하였다.
- `git stash pop`으로 변경 사항을 복원하였다.
- `src/multiply.py`가 수정된 상태로 나타나는 것을 확인하였다.
- 정상 복원 후 stash 항목이 제거된 것을 확인하였다.

**진행 상태:** 완료

---

## 6. 실습을 통해 배운 점

| 명령어 | 역할 |
|---|---|
| `git commit --amend` | 최근 커밋을 수정하여 대체 |
| `git reset --soft HEAD~1` | 최근 커밋 취소, 변경 사항과 스테이징 유지 |
| `git revert` | 기존 기록을 유지하며 변경을 취소하는 새 커밋 생성 |
| `git stash` | 커밋하지 않은 변경 사항 임시 보관 |
| `git stash pop` | 보관한 변경 사항 복원 및 stash 항목 제거 |

Git에서는 작업 상황에 따라 적절한 명령어를 선택하는 것이 중요하다. 특히 팀 프로젝트에서는 이미 공유된 커밋을 취소할 때 `git revert`를 사용하는 것이 안전하다.

또한 `git stash`를 활용하면 커밋하지 않은 작업을 임시로 보관하고 브랜치를 전환할 수 있다는 점을 학습하였다.

---

## 7. 팀원별 실습 참여 및 역할

- 김병헌: git commit --amend (최근 커밋 메시지 수정) 

<img width="2241" height="810" alt="Image" src="https://github.com/user-attachments/assets/f66caec5-6efa-4564-8368-4e98e81e62ce" />

<img width="871" height="428" alt="Image" src="https://github.com/user-attachments/assets/df8cf8cc-7847-4aaa-af74-1d0347f219ea" />


- 안중현:  git reset --soft HEAD~1 (로컬 커밋 취소 + 변경 유지), git revert (원격에 push된 커밋 취소)

reset

before
<img width="757" height="301" alt="Image" src="https://github.com/user-attachments/assets/5c835b20-8b89-43b9-8ab5-9493b915502f" />
after
<img width="589" height="207" alt="Image" src="https://github.com/user-attachments/assets/9a7531da-49bf-4f6f-9d15-99b3077c48b7" />

revert
before
<img width="770" height="628" alt="Image" src="https://github.com/user-attachments/assets/118e4492-1cc9-4222-9957-58218ae01ab4" />
after
<img width="770" height="613" alt="Image" src="https://github.com/user-attachments/assets/242abe01-ab14-40e0-b292-004f7e3f9811" />


- 김병철: git stash / git stash pop (작업 보관 후 전환): 김병철

<img width="520" height="133" alt="Image" src="https://github.com/user-attachments/assets/43e06c30-8e3c-4af3-934e-e7fbebfbd8c1" />

<img width="520" height="133" alt="Image" src="https://github.com/user-attachments/assets/d72e7672-42f1-4d3f-860f-efab9b7dfc17" />
