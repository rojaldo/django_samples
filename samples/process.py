from samples.models import NasaAPOD
import requests
import datetime

def json_to_nasa_APOD():
    today = datetime.date.today()
    today = today.strftime('%Y-%m-%d')
    # check NasaAPOD table for today's date
    result = None
    if NasaAPOD.objects.filter(date=today).exists():
        try:
            result = NasaAPOD.objects.get(date=today)
        except NasaAPOD.DoesNotExist:
            result = None
    if result is None:
        response = requests.get("https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY")
        if response.status_code == 200:
            try:
                date = response.json()['date']
                nasa = NasaAPOD.objects.update_or_create(date = date, defaults= response.json())
                nasa.save()
                return nasa
            except Exception as e:
                print(e)
                return None
        else:
            return None
    else:
        return result
    

