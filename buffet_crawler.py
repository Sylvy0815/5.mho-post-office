# TODO. 매주 월요일 9시 부터 5분 간격으로 크롤링
# 9시부터 10시까지 총 13회 수행하면 될듯

# crontab -e
# */5 9-10 * * 1 python3 /경로/to/your/buffet_crawler.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

# headless 모드
# 크롬 옵션 설정
chrome_options = Options()
chrome_options.add_argument("--headless")  # 헤드리스 모드 활성화
chrome_options.add_argument("--no-sandbox")  # Sandbox 비활성화
chrome_options.add_argument("--disable-dev-shm-usage")  # 공유 메모리 사용 제한 해제
# 웹 드라이버 초기화
driver = webdriver.Chrome(options=chrome_options)

# # non-headless 모드
# # 웹 드라이버 초기화
# driver = webdriver.Chrome()

try:
    # 웹사이트 접속
    driver.get("https://blog.naver.com/iyongju0608")

    # iframe으로 전환
    iframe = driver.find_element(By.ID, 'mainFrame')
    driver.switch_to.frame(iframe)

    # postListBody 내의 첫 번째 a 태그를 찾아 클릭
    post_list_body = driver.find_element(By.ID, 'postListBody')
    first_link = post_list_body.find_element(By.CSS_SELECTOR, 'a')
    first_link.click()

    # 페이지 로딩 대기
    time.sleep(5)

    # 현재 페이지의 HTML 가져오기
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # 식단표 데이터 추출
    # 예: table = soup.find('table', {'class': '식단표 클래스 이름'})
    # 주의: 실제 클래스 이름은 사이트에 따라 다를 수 있음
    # ... 이전 코드 ...

    # BeautifulSoup을 사용하여 HTML 파싱
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # 식단표 데이터 추출
    table = soup.find('table', class_='se-table-content')
    rows = table.find_all('tr')

    menu_data = []
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        menu_data.append(cols)

    print(menu_data)

    # ... 이후 코드 ...


    # 데이터 처리 및 출력
    # 예: print(table.text)

except Exception as e:
    print(e)
finally:
    driver.quit()

# Teams Webhook
import requests
import json

from dotenv import load_dotenv
import os
load_dotenv()  # 환경 변수 로드
webhook_url = os.getenv('TEAMS_WEBHOOK_URL')

# 추출된 데이터에서 첫 번째 행을 헤더로 사용
headers = menu_data[0]
data_rows = menu_data[1:]

# Markdown 테이블 생성
markdown_table = "| " + " | ".join(headers) + " |\n"  # 테이블 헤더
markdown_table += "|---" * len(headers) + "|\n"  # 구분선

for row in data_rows:
    markdown_table += "| " + " | ".join(row) + " |\n"

# Teams 메시지로 전송할 준비
message = {
    "@type": "MessageCard",
    "@context": "http://schema.org/extensions",
    "summary": "주간 식단표",
    "sections": [{
        "activityTitle": "이번 주 식단표",
        "text": markdown_table  # Markdown 테이블 사용
    }]
}

# Teams로 데이터 전송
response = requests.post(
    webhook_url, 
    data=json.dumps(message), 
    headers={'Content-Type': 'application/json'}
)

# 응답 확인
print(response.status_code, response.text)
