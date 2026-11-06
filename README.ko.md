# Agent Engineering Lab

**언어:** [English](README.md) | [한국어](README.ko.md)

OpenAI Agents SDK의 기본 개념 학습부터 신뢰할 수 있는 커머스 고객지원 에이전트 구현까지, AI 에이전트 엔지니어링을 직접 실습하며 기록하는 저장소입니다.

## 진행 현황

- `01-quickstart/` — 기본 예제 준비 완료 (실제 LLM API를 통한 실행은 아직 검증하지 않음)
- `02-commerce-cs-agent/` — MVP 구현 예정 (기능을 단계적으로 추가할 계획)

## 학습 로드맵

| 단계 | 학습 내용 | 결과물 |
| --- | --- | --- |
| 01 | Agent / Runner / Function Tool | 실행 가능한 예제 코드와 학습 기록 |
| 02 | Tool Calling, 상태 관리, 사람 승인, 오류 복구, 평가 | 커머스 고객지원 에이전트 및 테스트 결과 |

## 시작하기

Python 3.11 이상 및 API 과금이 활성화된 OpenAI API Key가 필요합니다.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export OPENAI_API_KEY='your-api-key' # 로컬 환경에서만 설정하고 Git에는 커밋하지 마세요.
python 01-quickstart/01_basic_agent.py
python 01-quickstart/02_tool_calling.py
```

위 예제를 실행하면 **유료 OpenAI API 요청**이 발생합니다. 실행 전에 OpenAI API 계정에서 사용 모델 및 예산 한도를 확인하세요.

## 공식 참고 자료

- [OpenAI Agents SDK Quickstart](https://openai.github.io/openai-agents-python/quickstart/)
- [OpenAI Agents SDK Tools](https://openai.github.io/openai-agents-python/tools/)

## 보안

이 저장소의 데이터는 모두 가상 예제 데이터입니다. API Key, 로컬 데이터베이스 파일, 민감정보를 가리지 않은 Trace는 Git에 업로드하지 마세요.

## 참고 사항

실제 로컬 실행 후에만 구현 결과와 정량 평가 결과를 추가합니다. 현재 단계에서 상용 서비스 배포나 평가 성공을 주장하지 않습니다.
