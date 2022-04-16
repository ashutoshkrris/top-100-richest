import requests
from bs4 import BeautifulSoup
from selenium import webdriver


BROWSER = webdriver.Chrome(executable_path="chromedriver.exe")


def data_scraper(num):

    BROWSER.get("https://www.bloomberg.com/billionaires/")
    html_source = BROWSER.page_source
    BROWSER.close()

    soup = BeautifulSoup(html_source, 'html.parser')

    response_rank = soup.find_all('div', class_='table-cell t-rank')
    ranks = [rank.get_text().strip() for rank in response_rank][:num]

    response_name = soup.find_all('div', class_='table-cell t-name')
    names = [name.get_text().strip() for name in response_name][:num]

    links = [(name.find('a')['href']).replace("./", "") for name in response_name]

    response_worth = soup.find_all('div', class_='table-cell active t-nw')
    worths = [worth.get_text().strip() for worth in response_worth][1:num+1]

    response_last_change = soup.find_all('div', class_='t-lcd')
    last_changes = [change.get_text().strip()
                    for change in response_last_change][1:num+1]

    response_ytd = soup.find_all('div', class_='t-ycd')
    ytds = [ytd.get_text().strip() for ytd in response_ytd][1:num+1]

    response_country = soup.find_all('div', class_='table-cell t-country')
    countries = [country.get_text().strip()
                 for country in response_country][1:num+1]

    response_industry = soup.find_all('div', class_='table-cell t-industry')
    industries = [industry.get_text().strip()
                  for industry in response_industry][1:num+1]
    return ranks, names, links[:num], worths, last_changes, ytds, countries, industries
