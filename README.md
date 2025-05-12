### `.env` 파일 내용

사용할 모델 이름과 해당 LLM 제공자의 API 키를 설정합니다.
```
DEFAULT_MODEL = <model_name>

OPENAI_API_KEY = <your_openai_api_key>
ANTHROPIC_API_KEY = <your_anthropic_api_key>
AZURE_OPENAI_API_KEY = <your_azure_openai_api_key>
GOOGLE_API_KEY = <your_google_api_key>
...
```

예시:
```
DEFAULT_MODEL = google_genai:gemini-2.0-flash
GOOGLE_API_KEY = **********************************
```
