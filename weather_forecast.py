import pandas as pd
import requests
from bs4 import BeautifulSoup


def weather_forecast():

    print("\t1. San Francisco, CA" +
          "\n\t2. Los Angeles, CA" +
          "\n\t3. San Diego, CA" +
          "\n\t4. New York, NY" +
          "\n\t5. Chicago, IL" +
          "\n\t6. Washington, DC" +
          "\n\t7. Dallas, TX" +
          "\n\t8. Austin, TX" +
          "\n\t9. Miami, FL" +
          "\n\t10. Denver, CO\n")
    user_in = int(input("> "))
    weather_link = ['none', 'https://forecast.weather.gov/MapClick.php?lat=37.79105500000003&lon=-122.40174999999999#.YAyia3ZKi02',
                    'https://forecast.weather.gov/MapClick.php?lat=34.0536&lon=-118.2455#.YAyii3ZKi00',
                    'https://forecast.weather.gov/MapClick.php?lat=32.7157&lon=-117.1617',
                    'https://forecast.weather.gov/MapClick.php?lat=40.7146&lon=-74.0071#.YAyirHZKi00',
                    'https://forecast.weather.gov/MapClick.php?lat=41.8843&lon=-87.6324#.YAyivnZKi00',
                    'https://forecast.weather.gov/MapClick.php?lat=38.8904&lon=-77.032#.YAyi0nZKi00',
                    'https://forecast.weather.gov/MapClick.php?lat=32.7782&lon=-96.7951#.YAyi8HZKi00',
                    'https://forecast.weather.gov/MapClick.php?lat=30.2676&lon=-97.743#.YAyi_3ZKi00',
                    'https://forecast.weather.gov/MapClick.php?lat=25.7748&lon=-80.1977#.YAyjD3ZKi00',
                    'https://forecast.weather.gov/MapClick.php?lat=39.74&lon=-104.992']

    page = requests.get(weather_link[user_in])
    soup = BeautifulSoup(page.content, 'html.parser')
    week = soup.find(id='seven-day-forecast')

    items = week.find_all(class_='tombstone-container')

    period_names = [item.find(class_='period-name').get_text() for item in items]
    short_descriptions = [item.find(class_='short-desc').get_text() for item in items]
    temperatures = [item.find(class_='temp').get_text() for item in items]

    weather_stuff = pd.DataFrame({
        'period': period_names,
        'short-descriptions': short_descriptions,
        'temperatures': temperatures
    })
    print(weather_stuff)

    print('\nDo you want to extract the data to excel ?\n\t1.Yes\n\t2.No')
    sel = int(input("> "))
    if sel == 1:
        file_name = input("Enter file name to save as: ")
        weather_stuff.to_csv(file_name + ".csv")
        print("File has saved as" + file_name + ".cvs")
    elif sel == 2:
        pass
    else:
        print('Invalid Choice')
        weather_forecast()


weather_forecast()
