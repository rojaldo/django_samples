from samples.models import Beer, NasaAPOD
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
        response = requests.get("https://api.nasa.gov/planetary/apod?api_key=tqz634Z1x0LiJzjbhSyUoExrZaGKLM0MG1VnROR6")
        if response.status_code == 200:
            try:
                date = response.json()['date']
                myNasa = NasaAPOD(defaults= response.json())
                nasa = NasaAPOD.objects.update_or_create(date = date, defaults= response.json())
                nasa.save()
                return myNasa
            except Exception as e:
                print(e)
                return None
        else:
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
                print('Cervezas: ' + len(Beer.objects.all()))
                return Beer.objects.all()
            except Exception as e:
                print(e)
                return None
        else:
            return None
    

