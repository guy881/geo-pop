Projekt geo-pop
===============

Aspekty techniczne:
- Używamy Pythona 3, najlepiej 3.6
- Wymagane paczki są spisane w pliku requirements.txt
- Panel administrator jest oparty na django admin panel
- Użytkownik ma specjalny model nazwany CustomUser, aby można go było rozszerzać o kolejne pola


Zasady tworzenia kodu:
- Kod piszemy w języku angielskim
- Używamy widoków opartych na klasach - https://docs.djangoproject.com/en/1.11/topics/class-based-views/
- API dla aplikacji mobilnej będzie napisane przy pomocy django-rest-framework
- W razie wątpliwości, lepiej zapytać

Aplikacje odpowiadają tym z diagramu modułów:
- cars - zarządzanie samochodami
- drivers - zarządanie kierowcami
- regions - zarządzanie obszarami
- updates - zarządzanie aktualizacjami (kiepska nazwa, wiem)
- users - zarządzanie użytkownikami
