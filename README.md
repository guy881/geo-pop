Projekt geo-pop
===============

**Aspekty techniczne:**
- Używamy Pythona 3, najlepiej 3.6
- Wymagane paczki są spisane w pliku requirements.txt
- Użytkownik ma specjalny model nazwany CustomUser, aby można go było rozszerzać o kolejne pola
- Ustawienia (settings.py) oraz główny plik URL znajdują się w katalogu config

**Zasady tworzenia kodu:**
- Kod oraz wiadomości commintów piszemy w języku angielskim
- Używamy widoków opartych na klasach - https://docs.djangoproject.com/en/1.11/topics/class-based-views/ atrybuty widoków: https://ccbv.co.uk/ 
- API dla aplikacji mobilnej będzie napisane przy pomocy django-rest-framework
- Pracujemy na branchach
- Po zmianach w modelu uruchamiamy polecenie `python manage.py makemigrations` i dodajemy pliki, które zostały wygenerowane do gita
- W razie wątpliwości, lepiej zapytać

**Aplikacje odpowiadają tym z diagramu modułów:**
- cars - zarządzanie samochodami
- drivers - zarządanie kierowcami
- regions - zarządzanie obszarami
- updates - zarządzanie aktualizacjami (kiepska nazwa, wiem)
- users - zarządzanie użytkownikami

**Pierwsze uruchomienie:**
- stawiamy virtualenva dla pythona 3 (jest wiele metod, więc nie piszę komend)
- w virtualenv-ie instalujemy zależności `pip install -r requirements.txt`
- Tworzymy migracje `python manage.py makemigrations`
- Tworzymy bazę i instalujemy migracje `python manage.py migrate`
- Uruchamiamy serwer django `python manage.py runserver`
