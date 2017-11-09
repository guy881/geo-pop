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





Style guide
===============

**Rozszerzanie templatek**

Każda templatka powinna rozpoczynać się od tagu `{% extends 'base.html' %}`, gwarantuje nam to, że na podstronie którą tworzymy będzie się wyświetlać wspólna nawigacja.

Następnie nasz kod html wrzucamy pomiędzy tagi `{% block content %}` i `{% endblock %}`.

Dzięki temu możemy wyodrębnić navbar oraz stopkę i umieścić naszą templatkę pomiędzy tymi elementami.

Przykład można zobaczyć w templatce `users/login.html`

**Podstawowe elementy, CSS**

* Jako podstawowy szablon stylów używamy Bootstrap CSS zaimportowany w pliku `base.html`.

* Korzystamy z grida (i ogólnie layoutów) Bootstrapa (i dążymy do tego aby np. mały formularz nie był rozciągnięty na całą stronę tylko znajdował się mniej więcej po środku i zajmował powiedzmy 8 na 12 kolumn grida)

* Nie zmieniamy kolorów tła oraz divów, szczególnie na kolory jaskrawe - trzymamy się jasnej kolorystyki (odcienie szarości)

* Jeśli ktoś chce użyć jakiegokolwiek akcentu kolorystycznego poza skalą szarości to nasza aplikacja ma kolor przewodni fioletowy, dokładnie `#5000B2` (pasek pod `navbarem` jest właśnie w tym kolorze). Możecie użyć albo dokładnie tego koloru albo jego odcieni. Tyczy się to zarówno aplikacji webowej jak i aplikacji mobilnej.

* Alerty (do wyświetlania błędów) dajemy podstawowe, np.:
```html
<div class="alert alert-warning" role="alert">
  This is a warning alert—check it out!
</div>
```

* Buttony wybieramy w stylu `outline`, tzn. z tego zestawu (bez 'light' z uwagi na to że używamy jasnych kolorów):
```html
<button type="button" class="btn btn-outline-primary">Primary</button>
<button type="button" class="btn btn-outline-secondary">Secondary</button>
<button type="button" class="btn btn-outline-success">Success</button>
<button type="button" class="btn btn-outline-danger">Danger</button>
<button type="button" class="btn btn-outline-warning">Warning</button>
<button type="button" class="btn btn-outline-info">Info</button>
<button type="button" class="btn btn-outline-dark">Dark</button>
```

* Rozmiar inputów w formularzach (oraz w zasadzie wszystkich innych elementów) powinien być domyślny.

* Proponujemy również standardowe `modale` bootstrapowe: http://getbootstrap.com/docs/4.0/components/modal/#live-demo

* Do prezentacji postępów aktualizacji obszarów proponujemy użyć ten `progress bar`: http://getbootstrap.com/docs/4.0/components/progress/#labels

* Jakby ktoś chciał używać jakichkolwiek ikonek (np. na guzikach przy 'Dodaj kierowcę') to śmiało, ale proszę korzystać tylko i wyłącznie z tego Bootstrapowego zbioru: https://getbootstrap.com/docs/3.3/components/

#### Do pozostałych elementów, które nie zostały powyżej opisane należy używać innych komponentów Bootstrapowych (nie należy pisać nowej biblioteki oraz najlepiej nie dodawać innych bibliotek CSS).

###### Wzorem do naśladowania i bardzo dobrym przykładem wysokiej jakości stylu UI/UX jest ta strona: http://tumanski.pl/ . Możecie kierowiać się nią w chwilach zwątpienia (:

