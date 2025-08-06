# 🏢 AI 기반 기업 심층 분석 및 보고서 자동화 프로젝트

이 프로젝트는 OpenAI API를 활용하여 코스피 시가총액 상위 기업들을 심층 분석하고, 그 결과를 바탕으로 IT 신입 지원자 맞춤형 보고서를 자동으로 생성하는 파이썬 기반 솔루션입니다. GitHub Actions를 통해 매일 자동화된 분석 및 보고서 생성을 수행하며, 분석된 내용은 GitHub 저장소에 자동으로 커밋됩니다.

## 🚀 주요 기능

-   **기업 정보 스크레이핑**: 네이버 금융에서 코스피 시가총액 상위 100개 기업 목록을 자동으로 수집합니다.
-   **AI 기반 심층 분석**: OpenAI GPT-4o 모델을 사용하여 기업의 기술적 Legacy, 현재 주력 사업 및 기술 스택, 신규 IT 투자 분야, 그리고 미래 성장 동력에 대한 심층적인 분석을 수행합니다.
-   **맞춤형 보고서 생성**: 분석된 내용을 바탕으로 IT 신입 개발자(백엔드, 인프라, AI 엔지니어)의 자기소개서 작성에 도움이 되는 맞춤형 Word(.docx) 보고서를 생성합니다. 보고서 내 중요한 키워드는 **굵은 글씨**로 강조됩니다.
-   **자동화된 워크플로우**: GitHub Actions를 통해 매일 한국 시간 오전 8시에 자동으로 기업 분석 및 보고서 생성을 실행하고, 변경 사항을 저장소에 커밋합니다.
-   **진행 상황 관리**: `progress.txt` 파일을 통해 분석이 완료된 기업을 추적하고, 다음 분석 대상 기업을 자동으로 선정합니다.

## 📁 프로젝트 구조

```
company_research_project/
├── .github/
│   └── workflows/
│       └── daily-report.yml  # GitHub Actions 워크플로우 정의
├── output/                   # 생성된 Word 보고서 저장 폴더
├── .env                      # OpenAI API 키 및 환경 변수 저장 (Git에 포함되지 않음)
├── .gitignore                # Git 버전 관리에서 제외할 파일 목록
├── main.py                   # 메인 스크립트: 기업 분석 및 보고서 생성 로직
├── scraper.py                # 코스피 기업 목록 스크레이핑 스크립트
├── requirements.txt          # 프로젝트에 필요한 Python 라이브러리 목록
└── progress.txt              # 현재까지 분석된 기업의 순위를 기록 (자동 생성/업데이트)
```

## ⚙️ 설치 및 실행 방법

### 1. 저장소 클론

```bash
git clone https://github.com/HxWOO/comp_research_ops.git
cd comp_research_ops
```

### 2. 환경 설정

`.env` 파일을 프로젝트 루트 디렉토리에 생성하고, OpenAI API 키를 다음과 같이 추가합니다:

```
OPENAI_API_KEY="YOUR_OPENAI_API_KEY"
```

### 3. 의존성 설치

Python 가상 환경을 활성화한 후 필요한 라이브러리를 설치합니다:

```bash
python -m venv .venv
.env\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux
pip install -r requirements.txt
```

### 4. 수동 실행

#### 4.1. 기업 목록 스크레이핑

코스피 시가총액 상위 100개 기업 목록을 `kospi_top_100.txt` 파일로 저장합니다.

```bash
python scraper.py
```

#### 4.2. 기업 분석 및 보고서 생성

`kospi_top_100.txt`에 있는 다음 순서의 기업을 분석하고 보고서를 `output/` 폴더에 생성합니다. `progress.txt` 파일이 자동으로 업데이트됩니다.

```bash
python main.py
```

## 🤖 자동화 (GitHub Actions)

이 프로젝트는 GitHub Actions를 통해 완전 자동화되어 있습니다. `.github/workflows/daily-report.yml` 파일에 정의된 워크플로우는 다음을 수행합니다:

-   **매일 한국 시간 오전 8시 (UTC 23:00)** 에 자동으로 실행됩니다.
-   `scraper.py`를 실행하여 최신 기업 목록을 가져옵니다.
-   `main.py`를 실행하여 다음 분석 대상 기업에 대한 보고서를 생성합니다.
-   생성된 보고서 및 진행 상황 파일(`progress.txt`, `kospi_top_100.txt`)을 자동으로 저장소에 커밋하고 푸시합니다.

### GitHub Secrets 설정

GitHub Actions에서 OpenAI API 키를 사용하려면, 저장소 설정에서 `OPENAI_API_KEY`라는 이름으로 Secret을 추가해야 합니다. (저장소 -> Settings -> Security -> Secrets and variables -> Actions -> New repository secret)
