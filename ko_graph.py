import streamlit as st
import spacy
from spacy import displacy
from io import StringIO

nlp = spacy.load("ko_core_news_lg")

stopwords = ['은', '는', '이', '가', '을', '를', '에', '에서', '으로', '로', '와', '과', '아', '야', '이어', '여', '이나', '나', '에게', '한테', '께', '에게서', '이랑', '랑', '만큼', '만큼은', '이든', '든', '이야', '야', '이나마', '나마']

def analyze_text(text):
    doc = nlp(text)
    morphs_words = [token.text for token in doc if token.text not in stopwords]
    noun_words = [token.text for token in doc if token.text not in stopwords and token.pos_ == 'NOUN']
    tag_words = [(token.text, token.pos_) for token in doc if token.text not in stopwords]
    return morphs_words, noun_words, tag_words, doc

def render_image(doc):
    svg = displacy.render(doc, style="dep", options={"compact": True, "bg": "#09a3d5", "color": "white", "font": "Source Sans Pro"}, jupyter=False)
    return svg

def main():
    st.title("한국어 텍스트 분석 웹 애플리케이션")
    text = st.text_input("분석할 텍스트를 입력하세요.")
    if text:
        morphs_words, noun_words, tag_words, doc = analyze_text(text)

        st.subheader("형태소 분석 결과")
        st.write(morphs_words)

        st.subheader("명사 추출 결과")
        st.write(noun_words)

        st.subheader("품사 태깅 결과")
        st.write(tag_words)

        st.subheader("의존 구문 분석 결과")
        svg = render_image(doc)
        st.components.v1.html(svg, width=800, height=400, scrolling=True)

if __name__ == "__main__":
    main()