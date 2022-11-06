#!/usr/bin/env python3


#Na wzór przykładu proszę przygotować implementację "printf" wykorzystująca #g jako zamiennik %d, który dodatkowo
#  dla drukowanej liczby zmienia kolejność cyfr (np. dla 1234 drukuje 4321).

#Proszę załączyć całość projektu spakowaną zipem. Równocześnie projekt musi 
# się znajdować na githubie z odpowiednią nazwą katalogu (z tytułu zadania w nawiasach - 
# ta część która jest w nawiasach z tytułu zadania(np "labX")). Przykładowo jeśli tytuł 
# zadania to "Zadanie xyz (abc)" to proszę umieścić Makefile ( i resztę plików) w katalogu 
# "abc". Państwa projekt powinien zawierać 10 testów i wszystkie testy powinny przechodzić poprawnie.

#Na samej górze pola tekstowego powinien się znajdować link("REPO") do tego 
# konkretnego projektu z Państwa githuba, a  (oddzielony SHIFT+ENTEREM) niżej 
# link do pliku zawierającego "główny" kod źródłowy ("KOD"). Podsumowując dwie 
# pierwsze linie pola tekstowego to dwa słowa: REPO i KOD. Oba jako linki. Wklejone 
# linki mają być "klikalne", w przeciwnym razie zadanie nie zostanie sprawdzone. Proszę 
# opisać z czym w zadaniu mieli Państwo największy problem (nawet jeśli wykonali 
# Państwo całość zadania). W polu tekstowym przy zgłaszaniu zadania należy napisać, 
# jeśli nie udało się zrealizować całego zadania, to proszę opisać, co jest zrobione, a czego brakuje.

# Uruchamianie

#Use `make all` to build project

#Use `make tests` to test project

#Use `make all && make tests` to build and test project
import sys




def my_printf(format_string,param):
    #print(format_string)
    shouldDo=True
    for idx in range(0,len(format_string)):
        if shouldDo:
            if format_string[idx] == '#' and format_string[idx+1] == 'd':
                print(param,end="")
                shouldDo=False
            else:
                print(format_string[idx],end="")
        else:
            shouldDo=True
    print("")

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
