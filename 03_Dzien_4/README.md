![Coders-Lab-1920px-no-background](https://user-images.githubusercontent.com/152855/73064373-5ed69780-3ea1-11ea-8a71-3d370a5e7dd8.png)


## Zadanie 1

Napisz już Ci znaną funkcję, która przyjmuje liczbę całkowitą. 
Funkcja wypisuje w kolejności liczby od 1 do podanej liczby, ale:

* w miejsce liczb podzielnych przez 3 wypisuje Fizz,
* w miejsce liczb podzielnych przez 5 wypisuje Buzz,
* w miejsce liczb podzielnych przez 3 **oraz** 5 wypisuje BuzzFizz.

Na przykład dla argumentu x = 15 wynik ma być następujący:
```
12Fizz4BuzzFizz78FizzBuzz11Fizz1314FizzBuzz
```
Napisz testy do tej funkcji.

## Zadanie 2

Napisz funkcję, która przyjmuje liczbę całkowitą (oznaczającą rok) i zwraca `True` – jeżeli rok jest przestępny, 
`False` jeżeli nie. Napisz testy do tej funkcji.

## Zadanie 3

Napisz funkcję `word_wrap(string, length)`, której zadaniem jest skrócić napis do podanej długości 
i dodać na końcu wielokropek). Funkcja ma działać w taki sposób żeby, żadne słowo nigdy nie zostało przecięte. 
Napisz testy do tej funkcji.

## Zadanie 4

Napisz klasę mającą jedną statyczną metodę `prime_factors(n)`, która wygeneruje wszystkie dzielniki podanej liczby **n** 
w kolejności numerycznej (od najmniejszego). Do tego zadania użyj w pełni metodologii TDD.

## Zadanie 5 (*)

Wybierz jeden z projektów, które robiłeś w django na któryś z poprzednich zajęć. Dopisz testy do widoków,
w których sprawdzisz:
* czy `status code` odpowiedzi jest odpowiedni (najczęściej 200),
* czy widoki, których zadaniem jest dodanie czegoś do bazy danych, dodają to faktycznie do bazy,
* czy widoki, które wyświetlają coś na stronie, przekazują odpowiedni kontekst do szablonu.