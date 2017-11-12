Rozszerzanie templatek
======================

Każda templatka powinna rozpoczynać się od tagu `{% extends 'base.html' %}`, gwarantuje nam to, że na podstronie którą tworzymy będzie się wyświetlać wspólna nawigacja.

Następnie nasz kod html wrzucamy pomiędzy tagi `{% block content %}` i `{% endblock %}`.

Dzięki temu możemy wyodrębnić navbar oraz stopkę i umieścić naszą templatkę pomiędzy tymi elementami.

Przykład można zobaczyć w templatce `users/login.html`