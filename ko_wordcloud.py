import konlpy
import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image
from konlpy.tag import Kkma
from wordcloud import WordCloud

def analyze_sentence(sentence):
    kkma = Kkma()
    
    morphs = kkma.morphs(sentence)
    st.subheader("형태소 분석 결과")
    st.write(morphs)
    
    nouns = kkma.nouns(sentence)
    st.subheader("명사 추출 결과")
    st.write(nouns)
    
    pos_tags = kkma.pos(sentence)
    st.subheader("품사 태깅 결과")
    for word, tag in pos_tags:
        st.write(f"{word}/{tag}")
    
    word_frequencies = {}
    for word in nouns:
        word_frequencies[word] = word_frequencies.get(word, 0) + 1

    st.subheader('Word Cloud')
    cand_mask=np.array(Image.open('/home/dmjeong/source/analysis/circle.png'))
    wordcloud = WordCloud(width=800, height=400, background_color='white', font_path = "/home/dmjeong/source/analysis/GamjaFlower-Regular.ttf", mask=cand_mask).generate_from_frequencies(word_frequencies)

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()
    plt.savefig('/home/dmjeong/source/analysis/world_cloud.png', bbox_inches='tight')
    image = Image.open("/home/dmjeong/source/analysis/world_cloud.png")
    st.image(image)

def main():
    st.title("한국어 구문 분석 웹")
    text = st.text_input("분석할 텍스트를 입력하세요.")
    if text:
        analyze_sentence(text)
        
if __name__ == '__main__':
    main()