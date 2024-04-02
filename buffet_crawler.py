# TODO. 매주 월요일 9시 부터 5분 간격으로 크롤링
# 9시부터 10시까지 총 13회 수행하면 될듯

# crontab -e
# */5 9-10 * * 1 python3 /경로/to/your/buffet_crawler.py

# 월~금 9시 10분에 수행.
# 10 9 * * 1-5 /home/containus/Sylvy_workspace/5.mho-post-office/5.mho/bin/python3 /home/containus/Sylvy_workspace/5.mho-post-office/buffet_crawler.py >> /home/containus/Sylvy_workspace/5.mho-post-office/log.txt 2>&1

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import datetime
import traceback

# 에러 로그 파일 경로
log_file_path = './error_log.txt'

# 이전 날짜 문자열 생성
yesterday = datetime.date.today() - datetime.timedelta(days=1)
yesterday_str = yesterday.strftime('%Y-%m-%d')

<<<<<<< HEAD
# 에러 로그 확인
try:
    with open(log_file_path, 'r') as file:
        logs = file.readlines()
    # 이전 날짜에 해당하는 에러 로그가 있는지 확인
    error_found = any(yesterday_str in log for log in logs)
except FileNotFoundError:
    error_found = False  # 로그 파일이 없는 경우, 에러 없음으로 처리

# # FOR TEST
=======
import datetime

# 현재 요일을 확인 (월요일은 0, 화요일은 1, ...)
today_weekday = datetime.datetime.now().weekday()

# 월요일인 경우
if today_weekday == 0:
    error_found = False
else:
    # 에러 로그 확인
    try:
        with open(log_file_path, 'r') as file:
            logs = file.readlines()
        # 이전 날짜에 해당하는 에러 로그가 있는지 확인
        error_found = any(yesterday_str in log for log in logs)
    except FileNotFoundError:
        error_found = False  # 로그 파일이 없는 경우, 에러 없음으로 처리

# # For Test
>>>>>>> develop
# error_found = True

# 에러가 발견되었을 경우에만 작업 수행
if error_found:
    print("이전 날 에러 발생, 작업 수행")
    # 여기에 크롤링 및 데이터 처리 로직 추가
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
        error_message = f"{datetime.datetime.now()}: 에러 발생 - {str(e)}\n"
        # 에러 스택 트레이스와 함께 로그 파일에 기록
        error_message += traceback.format_exc()
        with open(log_file_path, 'a') as log_file:  # 'a' 모드로 열어 새로운 에러를 추가
            log_file.write(error_message)
        print(error_message)
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

    ##################### 기존 markdown 형식의 table ##########################
    # # 데이터에서 '\u200b' 문자를 공백으로 치환
    # for i, row in enumerate(data_rows):
    #     data_rows[i] = [cell.replace('\u200b', '.') for cell in row]

    # # Markdown 테이블 생성
    # markdown_table = "| " + " | ".join(headers) + " |\n"  # 테이블 헤더
    # markdown_table += "|---" * len(headers) + "|\n"  # 구분선

    # for row in data_rows:
    #     markdown_table += "| " + " | ".join(row) + " |\n"

    # # Teams 메시지로 전송할 준비
    # message = {
    #     "@type": "MessageCard",
    #     "@context": "http://schema.org/extensions",
    #     "summary": "주간 식단표",
    #     "sections": [{
    #         "activityTitle": "이번 주 식단표",
    #         "text": markdown_table  # Markdown 테이블 사용
    #     }]
    # }

    # # Teams로 데이터 전송
    # response = requests.post(
    #     webhook_url, 
    #     data=json.dumps(message), 
    #     headers={'Content-Type': 'application/json'}
    # )

    # # 응답 확인
    # print(response.status_code, response.text)
    ##################### 기존 markdown 형식의 table ##########################

    ####################### Adaptive Card로 변환 #############################
    def create_adaptive_card_with_columns(headers, data_rows):
        # Adaptive Card 초기 구성
        adaptive_card = {
            "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
            "type": "AdaptiveCard",
            "version": "1.3",
            "body": [
                {
                    "type": "TextBlock",
                    "text": "이번 주 식단표",
                    "size": "Large",
                    "weight": "Bolder"
                },
                {
                    "type": "ColumnSet",
                    "separator": True,
                    "spacing": "medium",
                    "columns": []
                }
            ]
        }

        # 각 요일별로 열(Column) 추가
        for header in headers:
            items = [{"type": "TextBlock", "separator": True, "text": header, "wrap": True, "weight": "Bolder"}]

            # 해당 요일의 모든 메뉴 항목 추가
            menu_index = headers.index(header)
            for row in data_rows:
                menu_text = row[menu_index].replace('\u200b', ' ')  # '\u200b'를 공백으로 치환
                if menu_text:  # 메뉴 텍스트가 비어있지 않은 경우에만 추가
                    items.append({"type": "TextBlock", "text": menu_text, "wrap": True})

            # 열 구성 및 추가
            column = {
                "type": "Column",
                "separator": True,
                "width": "20",
                "items": items
            }
            adaptive_card["body"][1]["columns"].append(column)

        return adaptive_card

    # Adaptive Card 생성 및 Teams에 전송하는 부분
    adaptive_card = create_adaptive_card_with_columns(headers, data_rows)
    response = requests.post(
        webhook_url,
        data=json.dumps({
            "type": "message",
            "attachments": [
                {
                    "contentType": "application/vnd.microsoft.card.adaptive",
                    "content": adaptive_card
                }
            ]
        }),
        headers={'Content-Type': 'application/json'}
    )

    # 응답 확인
    print(response.status_code, response.text)
    ####################### Adaptive Card로 변환 #############################


else:
    print("이전 날 에러 없음, 작업 중지")

