from samples.models import Beer, NasaAPOD
import requests
import datetime

def json_to_nasa_APOD(date):
    if(date == None):
        today = datetime.date.today()
        today = today.strftime('%Y-%m-%d')
    else:
        today = date
    # check NasaAPOD table for today's date
    result = None
    # if NasaAPOD.objects.filter(date=today).exists():
    #     try:
    #         result = NasaAPOD.objects.get(date=today)
    #     except NasaAPOD.DoesNotExist:
    #         print('NasaAPOD.DoesNotExist')
    #         result = None
    if result is None:
        response = requests.get("https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY&date=" + today)
        if response.status_code == 200:
            try:
                date = response.json()['date']
                myNasa = NasaAPOD(date=date, title=response.json()['title'], explanation=response.json()['explanation'], url=response.json()['url'], media_type=response.json()['media_type'], service_version=response.json()['service_version'])
                myNasa.save()
                return response.json()
            except Exception as e:
                print(e)
                return None
        else:
            print('Error: ' + str(response.status_code))
            return None
    else:
        return result

def get_beers():
    if Beer.objects.all().exists():
        return Beer.objects.all()
    else:
        response = requests.get("https://api.punkapi.com/v2/beers?per_page=80")
        if response.status_code == 200:
            try:
                data = response.json()
                for beer in data:
                    myBeer = Beer(name=beer['name'],tagline=beer['tagline'],description=beer['description'],image_url=beer['image_url'],abv=beer['abv'], first_brewed=beer['first_brewed'])
                    myBeer.save()
                print('Cervezas: ' + str(len(Beer.objects.all())))
                return Beer.objects.all()
            except Exception as e:
                print(e)
                return None
        else:
            return None
    
def get_unsaved_beers():

    response = requests.get("https://api.punkapi.com/v2/beers?per_page=80")
    if response.status_code == 200:
        try:
            data = response.json()            
            return data
        except Exception as e:
            print(e)
            return None
    else:
        return None

