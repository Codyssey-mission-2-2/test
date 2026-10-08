# Git 병합 충돌 해결 기록

> **프로젝트:** Codyssey B2_2 GitHub 팀 협업 미션  
> **기록 근거:** PyCharm 충돌 해결 화면·충돌 마커 화면·GitHub 변경 내역 캡처 4장  
> **작성 상태:** 충돌 발생 및 변경 내용은 캡처로 확인됨 / 해결 후 검증 결과와 PR·커밋 증빙은 추가 확인 필요

## 1. 개요

GitHub Flow로 협업하며 서로 다른 브랜치에서 같은 파일의 같은 부분을 수정했을 때 발생하는 **병합 충돌(edit/edit)**을 확인했다. `README.md`와 `src/main.py`에서 충돌이 확인되었고, 두 파일 모두 `HEAD`(병합을 실행한 현재 브랜치)와 `origin/main`의 변경이 겹쳤다.

| 사례 | 충돌 파일     | 충돌한 부분                             | 유형                      | 확인 가능한 증거                 |
| ---- | ------------- | --------------------------------------- | ------------------------- | -------------------------------- |
| 1차  | `README.md`   | `프로젝트 목표`의 GitHub Flow 설명 문장 | 동일 행 수정(edit/edit)   | 충돌 마커 및 GitHub diff         |
| 2차  | `src/main.py` | `main()` 함수의 `a`, `b` 입력 안내 문구 | 동일 구간 수정(edit/edit) | PyCharm 3-way merge 및 충돌 마커 |

두 사례 모두 미션의 **같은 파일·같은 hunk 수정 충돌** 유형에 해당한다. 다만 _사진만으로는 각각 독립된 병합에서 해결·커밋까지 완료했는지 확인할 수 없으므로_, 최종 제출 전 커밋·PR을 대조한다.

## 2. 1차 충돌 — `README.md`의 프로젝트 목표 문장 수정

### 2.1 충돌 상황

- **파일:** `README.md`
- **충돌 위치:** `### 프로젝트 목표` 아래 GitHub Flow를 설명하는 첫 번째 목록 항목(캡처 기준 20~24행)
- **충돌한 쪽:** `HEAD` ↔ `origin/main`
- **충돌 유형:** 동일 행의 문구 수정(edit/edit)
- **발생일:** 2026.10.06
- **충돌을 일으킨 브랜치:** `feature-divide`
- **참여자:** 안중현, 김병현

캡처에서 확인되는 두 문장의 차이:

| `HEAD`                                  | `origin/main`   |
| --------------------------------------- | --------------- |
| `- GitHub Flow를 적용하여 \`main\` ...` | `- GitHub Flow` |

`HEAD`에서는 GitHub Flow의 적용 대상과 목적을 보충한 표현을 사용했고, `origin/main`에서는 간단한 표현을 사용했다. 양쪽이 **같은 목록 항목**을 수정하여 충돌이 발생했다.

```text
<<<<<<< HEAD
- GitHub Flow를 적용하여 `main` ...
=======
- GitHub Flow
>>>>>>> origin/main
```

> 위 코드의 `...`는 캡처에서 오른쪽으로 이어지는 문구를 임의로 확정하지 않기 위한 생략 표기다.

![1차 충돌: README.md 충돌 마커](screenshots/conflicts/README_crash.png)

### 2.2 GitHub 변경 내용 비교

GitHub의 `README.md` diff 캡처에는 **1개 행 삭제(-), 1개 행 추가(+)**가 나타난다.

- **삭제된 문장:** `- GitHub Flow`
- **추가된 문장:** `- GitHub Flow를 적용하여 \`main\` ...`

이 화면은 두 버전 사이의 **수정 내역**을 보여주는 증거다. 이 화면만으로 충돌 해결 커밋이나 최종 병합 완료까지 확인되는 것은 아니다.

![1차 충돌: GitHub README.md diff](screenshots/conflicts/README_crash_merge.png)

### 2.3 해결 방법 및 수행 결과

**해결 기준:** 팀의 실제 GitHub Flow 사용 방식을 더 정확히 설명하는 문장을 선택하거나 두 버전의 의도를 반영해 하나의 항목으로 정리한다. 충돌 마커를 삭제한 뒤 README의 목록 형식을 유지한다.

**권장 최종 문장 예시(실제 채택 문장 아님):**

```markdown
- GitHub Flow를 적용하여 `main` 브랜치를 안정적으로 유지합니다.
```

**실제로 선택한 최종 문장:** [확인 후 입력]

**해결 절차:**

1. 현재 작업 브랜치에서 `git fetch origin` 및 `git merge origin/main`으로 최신 변경을 병합한다.
2. `README.md`의 충돌 마커와 양쪽 문장을 확인한다.
3. 팀원과 문구를 협의한 후 최종 문장 하나를 남기고 충돌 마커를 모두 제거한다.
4. `git add README.md` 후 `git status`로 미해결 충돌이 없는지 확인한다.
5. 병합 커밋을 완료하고 작업 브랜치에 push한 뒤 PR에서 변경 내용을 검토한다.

**검증할 사항:**

- [x] `README.md`의 충돌 마커와 양쪽 문구 차이를 캡처로 확인했다.
- [x] GitHub에서 해당 줄의 삭제·추가 diff를 확인했다.
- [x] 최종 README에 충돌 마커가 남지 않았음을 확인했다.
- [x] 프로젝트 목표 목록과 Markdown 렌더링이 정상인지 확인했다.
- [x] 충돌 해결 커밋과 PR 병합 여부를 확인했다.

**관련 Issue:** https://github.com/Codyssey-mission-2-2/test/issues/10
**충돌 참여자 / 역할:** 안중현(`feature-divide`에서 이미 `main`에 병합된 내용과 충돌을 발생시킴), 김병현(변경 내용을 `main`에 최초 병합)  
**충돌 해결 커밋:** https://github.com/Codyssey-mission-2-2/test/pull/13/changes/8d084d07efa8b81828669f594365b54901b17795  
**관련 PR:** [https://github.com/Codyssey-mission-2-2/test/pull/13]  
**최종 검증 결과:** README.md의 충돌 마커가 제거되었고, 프로젝트 목표 문장이 의도한 내용으로 반영되어 Markdown이 정상적으로 표시됨을 확인했다.

## 3. 2차 충돌 — `src/main.py`의 입력 문구 수정

### 3.1 충돌 상황

- **파일:** `src/main.py`
- **화면에서 확인되는 브랜치:** `feature-divide` ↔ `origin/main`
- **충돌 내용:** 두 브랜치가 동일한 `main()` 함수의 `input()` 안내 문구를 다르게 수정함
- **충돌 확인:** PyCharm 병합 화면에 `충돌 1개` 표시; 파일에 `<<<<<<< HEAD`, `=======`, `>>>>>>> origin/main` 마커가 나타남
- **발생일:** 2026.10.06
- **충돌을 일으킨 브랜치:** `feature-divide`
- **참여자:** 안중현, 김병철

**`feature-divide` 측(HEAD)의 변경 내용 — 핵심 부분**

```python
a = int(input("a값은 무엇일까요????: "))
b = int(input("b값은 무엇일까요????: "))
```

**`origin/main` 측 변경 내용 — 핵심 부분**

```python
a = int(input("a값: "))
b = int(input("b값: "))
```

두 버전 모두 `multiply.Power1(a, b)`를 호출해 결과를 출력하지만, 같은 위치의 입력 메시지를 다르게 수정했으므로 Git이 어느 쪽을 최종 코드로 채택할지 자동으로 판단할 수 없었다.

### 3.2 충돌 원인과 확인 과정

1. `feature-divide` 작업 브랜치와 `origin/main`에 서로 다른 수정 내용이 존재했다.
2. `origin/main`을 현재 작업 브랜치에 병합하는 과정에서 `src/main.py`의 동일 구간이 충돌했다.
3. PyCharm 3-way merge 화면에서 왼쪽(`feature-divide`), 오른쪽(`origin/main`)의 입력 문구 차이를 비교했다.
4. 파일 편집 화면에서 Git 충돌 마커를 확인했다.

![2차 충돌: PyCharm 병합 비교 화면](screenshots/conflicts/crash2_before_merge.png)

![2차 충돌: src/main.py 충돌 마커](screenshots/conflicts/crash2_before_merge2.png)

```bash
git switch feature-divide
git fetch origin
git merge origin/main
# src/main.py의 충돌 마커 제거 및 최종 코드 저장
git add src/main.py
git diff --cached --check
git status
git commit       # 병합 진행 중이라면 병합 커밋 생성
git push origin feature-divide
```

> `git commit`은 충돌 마커 제거와 `git add`가 완료된 후에 실행한다. 위 명령은 실습 과정을 설명하기 위한 것으로, 화면에서 실제로 모두 실행된 것은 확인되지 않았다.

**검증할 사항:**

- [x] `src/main.py`에서 충돌 발생을 캡처로 확인했다.
- [x] 충돌 마커가 제거되고 `main()` 함수가 하나만 남았음을 확인했다.
- [x] `python -m py_compile src/main.py`로 문법 오류가 없음을 확인했다.
- [x] 실행 시 입력과 계산 결과가 의도대로 출력되는지 확인했다.
- [x] 병합 커밋 및 PR에서 최종 반영 결과를 확인했다.

**관련 Issue:** https://github.com/Codyssey-mission-2-2/test/issues/15  
**충돌 참여자 / 역할:** 안중현(`feature-divide`에서 이미 `main`에 병합된 내용과 충돌을 발생시킴), 김병철(변경 내용을 `main`에 최초 병합)  
**충돌 해결 커밋:** https://github.com/Codyssey-mission-2-2/test/pull/16/changes/80cd7db0e9d6f41b0fef74a8ef01feb3afad6c57
**관련 PR:** https://github.com/Codyssey-mission-2-2/test/pull/16
**최종 검증 결과:** src/main.py의 충돌 마커가 제거되었고, 프로그램이 정상 실행되어 입력값에 따른 계산 결과가 출력됨을 확인했다

## 4. 공통 문제 해결 및 배운 점

### `Already up to date.` 메시지가 나왔을 때

이전 실습에서 `git fetch origin` 후 `git merge origin/main`을 실행했는데 `Already up to date.`가 나타난 적이 있었다. 이 메시지는 **현재 브랜치가 지정된 병합 대상의 변경을 이미 포함하고 있어 새로 병합할 커밋이 없다**는 의미로, 충돌 자체를 뜻하지 않는다.

```bash
git branch --show-current
git fetch origin
git log --oneline --graph --all -n 20
git merge origin/main
```

현재 브랜치가 예상한 작업 브랜치인지, 다른 작업자의 PR이 `main`에 실제로 병합되었는지, 두 브랜치에 각각 충돌할 변경이 커밋되어 있는지 확인해야 한다. `git merge origin main`이 아니라 **`git merge origin/main`**으로 원격 추적 브랜치를 지정한다.

### 학습한 내용

- 동일 파일의 같은 부분을 양쪽에서 다르게 수정하면 Git은 자동 병합하지 못할 수 있다.
- 충돌 마커의 `HEAD`는 현재 브랜치 쪽 내용, `origin/main`은 병합하려는 원격 추적 브랜치 쪽 내용이다.
- `README.md`처럼 문서 한 줄의 차이도 병합 충돌을 만들 수 있다.
- 충돌 해결은 마커 삭제로 끝나지 않으며 코드 실행, 문서 확인, 커밋·PR 검증이 필요하다.
- `main` 직접 push 대신 작업 브랜치에서 해결 내용을 정리하고 PR로 검토한다.

## 5. 제출 전 확인 사항

- [x] 두 사례가 실제로 **서로 다른 충돌 해결 작업**인지 Git 커밋/PR 이력으로 확인한다.
- [x] 각 사례의 해결 후 최종 내용과 검증 결과를 작성한다.
- [x] 두 사례의 참여자 이름 및 충돌 발생 과정에서 맡은 역할을 기입한다.
- [x] 각 사례의 Issue, PR, 충돌 해결 커밋 링크를 추가한다.
- [ ] `README.md` 및 `SUBMISSION.md`에서 충돌 해결 기록으로 연결되는 링크를 확인한다.
