'''
This module scrapes data from wa's commerce website and displays the holiday names and dates and stores them
in a python dictionary. There are three entries for every holiday with the first one referring to the current year and
the next two referring to the subsequent years
'''
import requests
import datetime
from bs4 import BeautifulSoup


def scrape_public_holidays():
    html = requests.get('https://www.commerce.wa.gov.au/labour-relations/public-holidays-western-australia')
    soup = BeautifulSoup(html.content, 'html.parser')
    holiday_dict = {}
    dates_list = []

    curr_year = datetime.date.today().year
    list_of_years = [curr_year, curr_year + 1, curr_year + 2]
    for table in soup.find_all(attrs={"summary": "A table listing the public holiday dates for 2020, 2021 and 2022."}):
        soup = table
        for item in soup.find_all("tr"):
            temp_list = []
            soup = item
            for holiday in soup.find_all("th", attrs={"scope": "row"}):
                if holiday is not None:
                    # printing the name of the holiday
                    print(holiday.get_text())
                    if holiday.get_text() != "\xa0":
                        holiday_dict[holiday.get_text()] = []
            for dates in soup.find_all("td"):
                if dates.string is None:
                    temp_list.append(dates.get_text().replace("&amp;<br/>", "").replace("\n\t\t\t", "").split("&"))
                else:
                    temp_list.append(dates.get_text())
            if len(temp_list) > 0:
                dates_list.append(temp_list)
                # printing the holiday dates
                print(dict(zip(list_of_years, temp_list)))
            print("########################")
        result = dict(zip(holiday_dict, dates_list))
        final_dict = dict(result)
        # printing the dictionary containing all the information
        print(final_dict)
        # testing by fetching dates for one of the holidays
        print(result["Queen's Birthday #"])
        return final_dict


