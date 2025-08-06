import requests
from bs4 import BeautifulSoup

def get_kospi_top_100():
    """네이버 금융에서 코스피 시가총액 상위 100개 기업 목록을 스크레이핑합니다."""
    print("Fetching KOSPI top 100 companies...")
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = "https://finance.naver.com/sise/sise_market_sum.naver?sosok=0"
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        company_list = []
        # 시총 50위까지 가져오기
        table = soup.find('table', class_='type_2')
        rows = table.find_all('tr', onmouseover="mouseOver(this)")
        for row in rows:
            if len(company_list) >= 100:
                break
            cols = row.find_all('td')
            company_name = cols[1].find('a').text.strip()
            company_list.append(company_name)

        # 시총 100위까지 가져오기 (2페이지)
        if len(company_list) < 100:
            page2_url = f"{url}&page=2"
            response = requests.get(page2_url, headers=headers)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            table = soup.find('table', class_='type_2')
            rows = table.find_all('tr', onmouseover="mouseOver(this)")
            for row in rows:
                if len(company_list) >= 100:
                    break
                cols = row.find_all('td')
                company_name = cols[1].find('a').text.strip()
                company_list.append(company_name)

        print(f"Successfully fetched {len(company_list)} companies.")
        return company_list

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return []

if __name__ == "__main__":
    top_100 = get_kospi_top_100()
    if top_100:
        with open("kospi_top_100.txt", "w", encoding="utf-8") as f:
            for company in top_100:
                f.write(f"{company}\n")
        print("kospi_top_100.txt file has been created.")
