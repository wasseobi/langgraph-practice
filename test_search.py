"""Google Search API 테스트 스크립트"""
from dotenv import load_dotenv
load_dotenv()

import os
import datetime
from langchain_google_community import GoogleSearchAPIWrapper

def google_search(topic: str, num_results: int = 3):
    """
    Perform a Google search and retrieve the results.
    """
    try:
        # API 키와 CSE ID 확인
        api_key = os.getenv('GOOGLE_API_KEY')
        cse_id = os.getenv('GOOGLE_CSE_ID')
        
        if not api_key or not cse_id:
            raise ValueError("GOOGLE_API_KEY 또는 GOOGLE_CSE_ID가 설정되지 않았습니다.")
            
        print(f"\n🔍 검색 시작: '{topic}'")
        
        # 검색 실행
        search = GoogleSearchAPIWrapper(
            google_api_key=api_key,
            google_cse_id=cse_id
        )
        
        # 결과 가져오기
        results = search.results(topic, num_results=num_results)
        
        if not results:
            print("⚠️ 검색 결과가 없습니다.")
            return []
            
        print(f"✅ {len(results)}개의 결과를 찾았습니다.")
        return results
        
    except Exception as e:
        print(f"⚠️ 검색 중 오류 발생: {str(e)}")
        raise

def test_google_search():
    """Google Search 기능을 테스트합니다."""
    
    # 환경 변수 확인
    api_key = os.getenv('GOOGLE_API_KEY')
    cse_id = os.getenv('GOOGLE_CSE_ID')
    
    print("=== 환경 설정 확인 ===")
    print(f"API 키 설정됨: {'예' if api_key else '아니오'}")
    print(f"CSE ID 설정됨: {'예' if cse_id else '아니오'}")
    
    # 테스트할 검색어
    search_query = "오늘 전주 날씨"
    num_results = 3
    
    print("\n=== 검색 실행 ===")
    print(f"검색어: {search_query}")
    print(f"요청할 결과 수: {num_results}")
    print("\n검색 결과:")
    
    try:
        results = google_search(search_query, num_results)
        
        for i, result in enumerate(results, 1):
            print(f"\n[결과 {i}]")
            print(f"제목: {result.get('title', 'No title')}")
            print(f"링크: {result.get('link', 'No link')}")
            print(f"요약: {result.get('snippet', 'No snippet')}")
            
    except Exception as e:
        print(f"\n⚠️ 오류 발생: {str(e)}")
        print("\n다음 사항을 확인해주세요:")
        print("1. .env 파일에 GOOGLE_API_KEY가 설정되어 있나요?")
        print("2. .env 파일에 GOOGLE_CSE_ID가 설정되어 있나요?")
        print("3. API 키가 유효한가요?")

if __name__ == "__main__":
    test_google_search()
