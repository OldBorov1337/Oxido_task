Georgii Gorokhovskyi 

Dzień dobry, wykonałem to zadanie w Pythonie, zainstalowałem bibliotekę requests,
ponieważ pomoże ona wysyłać żądania HTTP do API OpenAI i utworzyłem plik requirements.txt, 
który określa biblioteki, aby je zainstalować, użyj polecenia:

pip install -r requirements.txt

Zanim zaczniesz, musisz wstawić klucz API do .env (usunąłem go ze względów bezpieczeństwa)

Aby aktywować program, należy użyć polecenia:
python main.py


Rozpocząłem kod od zainstalowania wymaganych bibliotek i zdefiniowania klucza API,
który uprzejmie mi dostarczyłeś, za co bardzo dziękuję
i ścieżkę do jego użycia

Następnie stworzyłem funkcję (read), która otworzy i odczyta plik z tekstem artykułu i zwróci jego zawartość

Następnie utworzyłem funkcję (gen_html_openai),
która wyśle tekst artykułu i monit (prompt) do interfejsu API OpenAI,
a następnie przetworzy odpowiedź 
utworzyła nagłówki (headers) i dane (data) dla żądania, a następnie wysłała je do API OpenAI

Po wysłaniu żądania sprawdziłem odpowiedź i wyodrębniłem kod HTML

Stworzyłem funkcję, która zapisze wygenerowany HTML do pliku artykul.html

A na końcu stworzyłem główną funkcję, która połączy wszystkie kroki.

Dość długo zastanawiałem się nad wyborem modelu i ostatecznie wybrałem gpt-4, ponieważ uważam,
że jest to najlepsza opcja pod względem jakości (jeśli zadanie jest złożone lub wymaga maksymalnej dokładności).



Użyłem również tych linii na końcu,

if __name__ == "__main__":
    main()

ponieważ Python przypisuje wartość "__main__" do tej zmiennej. Oznacza to, że kod w bloku if __name__ == "__main__": zostanie wykonany tylko wtedy,
gdy plik zostanie uruchomiony jako samodzielny program, a nie zaimportowany jako moduł do innego pliku


Postanowiłem również nie wstawiać znaczników <body> w pliku artykul.html, ponieważ zostałyby one zduplikowane w pliku podglad.html,
oczywiście mógłbym usunąć te znaczniki w pliku szablon.html, ale uznałem, że będzie to bardziej poprawne.  

To tyle, mam nadzieję, że wszystko szczegółowo opisałem i nie zanudziłem Was zbytnio czytaniem :)

