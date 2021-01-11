import requests
from bs4 import BeautifulSoup


def data_scraper():

    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9,hi;q=0.8",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Referer": "https://www.bloomberg.com/",
        "Accept-Encoding": "gzip, deflate, br",
        "Pragma": "no-cache"
    }

    response = requests.get(
        "https://www.bloomberg.com/billionaires/", headers=header)

    soup = BeautifulSoup(response.text, 'html.parser')

    response_rank = soup.find_all('div', attrs={'table-cell t-rank'})
    ranks = [rank.get_text().strip() for rank in response_rank][:100]

    response_name = soup.find_all('div', attrs={'table-cell t-name'})
    names = [name.get_text().strip() for name in response_name][:100]

    links = []
    for div in soup.findAll('div', attrs={'table-cell t-name'}):
        links.append((div.find('a')['href']).replace("./",""))

    response_worth = soup.find_all('div', attrs={'table-cell active t-nw'})
    worths = [worth.get_text().strip() for worth in response_worth][1:101]

    # response_last_change = soup.find_all('div', attrs={'table-cell t-lcd pos'})
    # last_changes = [change.get_text().strip()
    #                 for change in response_last_change][:100]

    # response_ytd = soup.find_all('div', attrs={'table-cell t-ycd pos'})
    # ytds = [ytd.get_text().strip() for ytd in response_ytd][:100]

    response_country = soup.find_all('div', attrs={'table-cell t-country'})
    countries = [country.get_text().strip()
                 for country in response_country][1:101]

    response_industry = soup.find_all('div', attrs={'table-cell t-industry'})
    industries = [industry.get_text().strip()
                  for industry in response_industry][1:101]
    print(ranks)
    return ranks, names, links[:100], worths, countries, industries
