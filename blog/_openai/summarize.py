import os
import environ
import openai
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pathlib import Path

# 환경 변수 설정
BASE_DIR = Path(__file__).resolve().parent.parent.parent
print(f" [Info:] BASE_DIR: {BASE_DIR}")
env = environ.Env()
environ.Env.read_env(
    env_file=os.path.join(BASE_DIR, '.env')
)
openai.api_key = env('OPENAI_API_KEY')

# FastAPI 애플리케이션 생성
app = FastAPI()

# Pydantic 모델 - 입력 데이터 형식 정의
class TextRequest(BaseModel):
    text: str  # 요약할 텍스트

# 텍스트 요약 함수
def summarize_text_with_openai(text: str, max_tokens=150):
    """OpenAI API를 사용해 텍스트를 요약하는 함수"""
    try:
        """OpenAI API를 사용해 텍스트를 요약하는 함수"""
        prompt = f"다음 텍스트를 3문장으로 요약해 주세요:\n\n{text}"

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # 최신 GPT-3.5-turbo 모델 사용
            messages=[  
                {"role": "system", "content": "너는 문서의 텍스트를 받아서 요약해주는 역할을 해야 돼."},
                {"role": "user", "content": f"다음 텍스트를 3문장으로 요약해 주세요:\n\n{text}"},
                {"role": "user", "content": """ 형식은 아래를 참고해서 작성해줘.
                    문서 제목 
                - 문장1
                - 문장2
                - 문장3
                """}
            ],
            max_tokens=max_tokens,  # 최대 토큰 수 제한
                temperature=0.7  # 창의성 정도
            )

        # 응답에서 요약된 텍스트 추출
        summary = response['choices'][0]['message']['content'].strip()

        return summary
    except Exception as e:
        summary = f"Error in summarizing text: {str(e)}"
        # raise HTTPException(status_code=500, detail=f"Error in summarizing text: {str(e)}")
    
    return summary  

# FastAPI 엔드포인트 - POST로 텍스트 받아서 요약
@app.post("/summarize/")
async def summarize(request: TextRequest):
    # 요약 생성
    summary = summarize_text_with_openai(request.text)
    return {"summary": summary}



if __name__ == "__main__":
    ...