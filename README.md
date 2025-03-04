# 💡 프로젝트 주제 : 문서 요약 웹 퍼블리케이션 💡

 ------------------------------------------------

## 1. 팀 소개

### 팀명 : 좋은 밥상

| **신동익**          | **박민혁**           | **나성호**               | **송문택**         |
|--------------------|----------------------|--------------------------|--------------------|
| Django Backend/Frontend | Django Backend/Frontend |                   |                    |
| DB (MySQL)         | DB (MySQL)           |                        |                    |
| API                | API                  |                        |                    |
| LLM 테스트         | LLM 테스트           | LLM 테스트             |                    |
| RAG 모델           | RAG 모델              | RAG 모델               |                    |
|                    |                      | 요구사항 정의서        |                    |
|                    |화면 설계서            | 화면 설계서            |                    |
|                    |                      | 시스템 구성도          |                    |
|                    |                      | App 테스트             |                    |
|                    |                      |                        | 프로젝트 참여 및 논의 |
|                    |                      |                        |                      |
| 발표               |                      |                        |                      |


------------------------------------------------
 
# 2. 프로젝트 개요

## 📌 주제  
문서 요약 웹 퍼블리케이션을 활용하여 PDF, TXT 등의 문서를 업로드하면  
AI가 자동으로 핵심 내용을 요약해주는 서비스  

## 💡 주제를 선택한 이유  
- 장문의 문서를 빠르게 이해하고 싶은 사용자에게 도움 제공  
- 논문, 기사, 보고서 등 다양한 문서 형식을 효과적으로 요약하여 **정보 접근성 향상**  
- AI를 활용하여 사용자의 시간을 절약하고, 중요한 정보를 쉽게 정리할 수 있도록 지원  

## 🚀 주요 기능  

### 🔹 회원 관리  
- 회원가입 및 로그인 기능을 제공하여 사용자 맞춤형 환경 제공  
- 사용자별 요약 내역을 저장하고 관리 가능  

### 🔹 문서 요약 기능  
- PDF, TXT 파일 업로드 시 **AI가 자동으로 요약**하여 핵심 내용 제공  
- GPT 기반 자연어 처리(NLP)를 활용하여 높은 정확도의 요약 결과 제공  
- 요약본을 다운로드하거나 클립보드에 복사 가능  

### 🔹 추가 기능 (향후 업데이트 예정)  
- 업로드된 문서의 **다국어 요약 지원**  
- 문서별 **요약 스타일 선택 가능** (간략 요약 / 상세 요약)  

------------------------------------------------
 
## 3. 기술 스택

### 🖥️ 개발 환경 & 프로그래밍 언어
| 기술 스택 | 로고 |
|-----------|------|
| **Python** | <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" /> |
| **VSCode** | <img src="https://img.shields.io/badge/VSCode-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white" /> |
| **Jupyter** | <img src="https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white" /> |

### 🤖 AI 모델 & 라이브러리
| 기술 스택 | 로고 |
|-----------|------|
| **OpenAI** | <img src="https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white" /> |
| **LangChain** | <img src="https://img.shields.io/badge/LangChain-FF9900?style=for-the-badge" /> |
| **GPT-3.5 Turbo** | <img src="https://img.shields.io/badge/GPT--3.5--Turbo-412991?style=for-the-badge" /> |
| **GPT-4** | <img src="https://img.shields.io/badge/GPT--4-412991?style=for-the-badge" /> |

### 🗄️ 데이터베이스 & 벡터DB
| 기술 스택 | 로고 |
|-----------|------|
| **ChromaDB** | <img src="https://img.shields.io/badge/ChromaDB-009688?style=for-the-badge" /> |

### 🔧 버전 관리 & 협업 도구
| 기술 스택 | 로고 |
|-----------|------|
| **GitHub** | <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" /> |

------------------------------------------------

## 4. 요구사항 정의서  
![요구사항 정의서](https://github.com/user-attachments/assets/f389e93d-d887-43fa-bcef-8e024bbde132)

------------------------------------------------

## 5. 화면 설계서
![화면설계서(1)](https://github.com/user-attachments/assets/ea34bdf7-5d58-481b-9447-f5a7b1158aac)
![화면설계서(2)](https://github.com/user-attachments/assets/35ad69d4-bc79-4960-a4df-a2f91d2cfb28)
![화면설계서(3)](https://github.com/user-attachments/assets/92bcdfbe-e8df-4d02-8427-80cbd9c26eb9)
![화면설계서(4)](https://github.com/user-attachments/assets/a5abfd87-8189-4ab4-bdf9-1ddd5fe5e713)
![화면설계서(5)](https://github.com/user-attachments/assets/ea09c4a5-297b-45f1-878f-607a175d8c00)

------------------------------------------------

## 6. 시스템 구성도
                           +--------------------------+
                           |         User             |
                           |    (웹 브라우저)         |
                           +-----------+--------------+
                                       |
                                       v
                           +--------------------------+
                           |       Frontend           |
                           |    (Django, HTML, CSS)   |
                           +-----------+--------------+
                                       |
                                       v
                           +--------------------------+
                           |         Backend          |
                           |      (Django API)        |
                           +-----------+--------------+
                                       |
                                       v
                      +----------------+-----------------+
                      |                                      |
                      v                                      v
           +---------------------+                +----------------------+
           |     MySQL Database   |                |     ChromaDB (벡터 DB) |
           |  (사용자 정보 및     |                |  (문서 및 요약 내용 저장)|
           |   요약 내역 저장)    |                +----------------------+
           +---------------------+
                                       |
                                       v
                           +--------------------------+
                           |      AI Model Server     |
                           |   (GPT-3.5, GPT-4, LangChain)|
                           |      (문서 요약 처리)    |
                           +--------------------------+
                                       |
                                       v
                           +--------------------------+
                           |   Document Upload &      |
                           |   Processing Module      |
                           | (PDF, TXT 파일 처리)     |
                           +--------------------------+


------------------------------------------------

## 7. 수행결과(테스트/시연 페이지)
![test(1)](https://github.com/user-attachments/assets/3ae605de-897e-4ab9-8986-c1a8473c01c3)
![test(2)](https://github.com/user-attachments/assets/7308ed25-bc14-4642-b1e0-0fab3c005a7f)
![test(3)](https://github.com/user-attachments/assets/55c7164a-fbc5-4c1f-864f-3ea2117bf311)
![test(4)](https://github.com/user-attachments/assets/b1661ec5-1aa1-44d5-bb1c-884b24862d92)
![test(5)](https://github.com/user-attachments/assets/b5ed760e-16cc-4833-9f72-5f3f8a295e3a)

------------------------------------------------
 
## 📝 한 줄 회고  

| 이름   | 회고 |
|--------|--------------------------------------------------------------|
| **박민혁** | 처음 다뤄보는 기술 스택이 많았지만, 팀원들과 협력하며 성장할 수 있었던 의미 있는 경험. |
| **나성호** | 실전 프로젝트를 통해 개발 과정의 흐름을 이해하고, 협업의 중요성을 다시 한번 깨달았다. |
| **신동익** | 예상치 못한 오류도 많았지만, 문제를 해결해 나가는 과정이 가장 값진 배움이었다. |
