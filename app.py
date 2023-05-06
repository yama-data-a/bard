#コマンドプロンプトで以下を入力すると開ける
#cd パス
#streamlit run app.py
#import streamlit as st
#import selenium
#from selenium import webdriver
#from selenium.webdriver.common.by import By

# Chrome Driverにセットするオプションの設定。
# やっとかないとエラーになるよ！
#options = webdriver.ChromeOptions()
#options.add_argument('--headless') # ヘッドレスモードを有効にする。
#options.add_argument('--no-sandbox') # sandboxモードを解除する。この記述がないとエラーになってしまう。 
#options.add_argument('--disable-dev-shm-usage') # /dev/shmパーティションの使用を禁止し、パーティションが小さすぎることによる、クラッシュを回避する。

#driver = webdriver.Chrome('chromedriver',options=options)
#driver.get('https://bard.google.com/?hl=en')


import streamlit as st
#ライブラリをインポート
from selenium import webdriver
import time
# Get the input text from the user
text = st.text_input("Enter your text here:")


# ブラウザをheadlessモード実行
print("\nブラウザを設定")
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('chromedriver',options=options)
driver.implicitly_wait(10)


# サイトにアクセス
print("サイトにアクセス開始")
driver.get("https://qiita.com/motoki1990/items/a59a09c5966ce52128be")
time.sleep(3)

# driver.find_elements_by_css_selector("xxx") 的な処理を自由に
print("サイトのタイトル：", driver.title)


# Set the path to the ChromeDriver executable
#CHROME_DRIVER_PATH = "/path/to/chromedriver"

# Create a new ChromeWebDriver instance
#driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

# Navigate to the Google search page
#driver.get("https://www.google.com/")

# Find the search input box
#search_input = driver.find_element_by_name("q")

# Enter a search query
#search_input.send_keys("What is the meaning of life?")

# Click the search button
#search_button = driver.find_element_by_xpath("//*[@id='tsf']/div[2]/div/div[3]/button")
#search_button.click()

# Wait for the search results to load
#driver.implicitly_wait(10)

# Get the search results
#search_results = driver.find_elements_by_xpath("//*[@id='srg']/div/div/div/h3/a")

# Print the search results
#for search_result in search_results:
#    print(search_result.text)

# Close the driver
#driver.quit()


















st.title('山アプリ')
st.caption('これは実験用のものです')
st.subheader('自己紹介')
st.text('こんにちは')

with st.form(key='profile_form'):
    #動画
    #video_file = open('https://www.youtube.com/watch?v=mmK_gRbb2lQ')
    #video_bytes = video_file.read()
    #st.video(video_bytes)

    #テキストボックス
    name = st.text_input('名前')
    #画面がリロードされると値が入ってくるが、カーソルがテキストボックスから外れるとリロードされる

    #ボタン
    submit_btn = st.form_submit_button('送信')
    cancel_btn = st.form_submit_button('キャンセル')

    #キャンセルか送信で分ける
    if submit_btn:
        st.text(f'ようこそ!{name}さん！')

    
    # Search for the text in Google Chrome
    url = "https://www.google.com/search?q=" + text

    # Open the search result in a new tab
    st.write("""<a href="""" + url + """" target="_blank">Open in Google Chrome</a>""")
    #st.write(""<a href="""" + url + """">Open in Google Chrome</a>""")