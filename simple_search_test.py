from dotenv import load_dotenv
load_dotenv()

import os
from langchain_google_community import GoogleSearchAPIWrapper

def test_google_search():
    try:
        # API 키와 CSE ID 확인
        api_key = os.getenv('GOOGLE_API_KEY')
        cse_id = os.getenv('GOOGLE_CSE_ID')
        
        print("=== 환경 설정 확인 ===")
        print(f"API 키: {api_key[:10]}...")
        print(f"CSE ID: {cse_id}")
        
        # 검색 클라이언트 초기화
        search = GoogleSearchAPIWrapper(
            google_api_key=api_key,
            google_cse_id=cse_id
        )
        
        # 테스트 검색
        query = "파이썬 LangGraph 예제"
        print(f"\n=== '{query}' 검색 중... ===")
        
        results = search.results(query, num_results=3)
        
        # 결과 출력
        for i, result in enumerate(results, 1):
            print(f"\n[결과 {i}]")
            print(f"제목: {result.get('title', '제목 없음')}")
            print(f"링크: {result.get('link', '링크 없음')}")
            print(f"설명: {result.get('snippet', '설명 없음')}")
        
    except Exception as e:
        print(f"오류 발생: {str(e)}")
        print("\n디버그 정보:")
        print(f"API 키 설정됨: {'예' if api_key else '아니오'}")
        print(f"CSE ID 설정됨: {'예' if cse_id else '아니오'}")

if __name__ == "__main__":
    print("Google Search API 테스트 시작...")
    test_google_search()
