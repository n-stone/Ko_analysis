# 한국어 구문 분석 웹

이 웹 애플리케이션은 한국어 텍스트의 형태소 분석, 명사 추출, 품사 태깅, 그리고 Word Cloud 생성을 수행합니다.

## 기능

- 형태소 분석 결과: 입력된 텍스트를 형태소로 분석한 결과를 코드로 출력합니다.
- 명사 추출 결과: 입력된 텍스트에서 추출된 명사를 코드로 출력합니다.
- 품사 태깅 결과: 입력된 텍스트를 품사로 태깅한 결과를 표로 출력합니다.
- Word Cloud: 입력된 텍스트에서 추출된 명사를 기반으로 Word Cloud를 생성하여 이미지로 출력합니다.

## 실행 방법

1. 필요한 패키지 설치:

- pip install -r requirements.txt

2. 실행:

- streamlit run ko_graph.py
- streamlit run ko_wordcloud.py

3. 웹 브라우저 실행:

- http://localhost:8501 으로 접속

4. DEMO

- https://n-stone-ko-analysis-ko-analysis-uxe0a4.streamlit.app/