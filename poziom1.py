print(  "Witaj u progu niezwykłej przygody, która na zawsze odmieni sposób, w jaki postrzegasz świat."
                        "Gra, w którą za chwile zagrasz, nosi nazwę \"Zaginiony\"."
        "Wcielisz się w 20letniego mężczyzne, który mimo upływu wielu lat, ciągle przeżywa zniknięcie ojca, który,"
        "podczas prowadzenia tajemniczych badań, znika w niewyjaśnionych okolicznościach."
        "Poszukiwania były bezowocne. Chcąc zmienić coś w swoim życiu, postanawiasz wreszcie opuścić rodzinne strony i zacząć życie gdzie indziej.")


print("\t\t\t\t\t\t\t\t\t\t\tZaczynajmy!")
print("*"*150)

print("Siedzisz wygodnie w fotelu rozglądając się po swoim pokoju. Nagle Twoją uwagę przykuwa zdjęcie, na którym razem ze swoim ojcem łowicie ryby. "
      "\nZalewa Cię fala wspomnień, która szybko zderza się z rzeczywistością. 4 lata temu, Twój ojciec zaginął. Mimo poszukiwań, nie udało się go odnaleźć."
      "\nDosyć! - Myślisz. - Najwyższy czas zacząć nowy rozdział w życiu! I takowy zaczynasz. "
      "\nJakiś czas temu postanowiłeś wyjechać z rodzinnego miasta i ten dzień właśnie nadszedł. Masz jeszcze do załatwienia kilka spraw."
      "\n Zacznijmy od tych najważniejszych!\n\n")


#Napisz funkcję postać, która realizuje tworzenie postaci

import random
# imię
name = input("Rozpoczynamy przygodę! Podaj imię swojego bohatera: ")
name = name.title()

# zawód
profession = input("Wybierz zawód - nauczyciel, trener, aktor, który będzie wykonywać: ")
profession = profession.lower()
while not(profession == "nauczyciel" or profession == "trener" or profession == "aktor"):
    profession = input("Wybierz zawód ponownie, tym razem poprawnie - nauczyciel, trener, aktor: ")
print("\n\nTwoja postać", name, "pracuje jako", profession + ".")
if profession == "nauczyciel":
    workplace = "szkoła"
elif profession == "trener":
    workplace = "siłownia"
elif profession == "aktor":
    workplace = "teatr"

# punkty życia
hit = 0
health_points = random.randint(50, 101)
print(name, "ma", health_points,"/100 punktów życia.\n\n")

if 50 <= health_points <= 65:
    hit += 4
elif 66 <= health_points <= 80:
    hit += 3
else:
    hit += 2

if health_points < 1:
    print("Koniec gry, Twoja postać nie żyje.")
    '''exit??'''
# cechy postaci
strength = 0
charisma = 0
intelligence = 0
abilities = [strength, charisma, intelligence]

decision = input("Chcesz samodzienie rozłożyć punkty do cech: siła, charyzma, inteligencja? ")
decision = decision.lower()
while not(decision == "tak" or decision == "nie"):
    decision = input("Odpowiedz tak/nie: ")
if decision == "tak":
    print("Masz do rozdania 10 punktów\n")
    strength = int(input("Ile punktów przenaczasz na siłę? "))
    charisma = int(input("Ile punktów przenaczasz na charyzmę? "))
    intelligence = int(input("Ile punktów przenaczasz na inteligencję? "))
    while not(strength+charisma+intelligence == 10):
        print("Spróbuj ponownie!")
        strength = int(input("Ile punktów przenaczasz na siłę? "))
        charisma = int(input("Ile punktów przenaczasz na charyzmę? "))
        intelligence = int(input("Ile punktów przenaczasz na inteligencję? "))
        if strength+charisma+intelligence == 10:
            continue
    if profession == "trener":
        abilities = [strength + 5, charisma + 2, intelligence + 3]
    elif profession == "nauczyciel":
        abilities = [strength + 2, charisma + 3, intelligence + 5]
    elif profession == "aktor":
        abilities = [strength + 2, charisma + 5, intelligence + 3]
elif decision == "nie":
    while not(strength+charisma+intelligence == 10):
        strength = random.randint(1, 11)
        charisma = random.randint(1, 11)
        intelligence = random.randint(1, 11)
        if strength+charisma+intelligence == 10:
            print("Wylosowano kolejno:", strength, charisma, intelligence)
    if profession == "trener":
        abilities = [strength + 5, charisma + 2, intelligence + 3]
    elif profession == "nauczyciel":
        abilities = [strength + 2, charisma + 3, intelligence + 5]
    elif profession == "aktor":
        abilities = [strength + 2, charisma + 5, intelligence + 3]

print("\n\nCechy Twojej postaci z dodatkowymi punktami za wybrany zawód:\nsiła:", abilities[0], "\ncharyzma:", abilities[1], "\ninteligencja:", abilities[2], "\n\n")

#mapa z poziomu 1
places1 = {
    1: {"name":"Dom",
        "prawo":2},
    2: {"name":"Sąsiadka",
        "lewo":1,
        "dół":3},
    3: {"name":"Droga do pracy",
        "górę":2,
        "dół":4},
    4:{"name":"Praca",
       "górę":3,
       "lewo":5},
    5:{"name":"Sklep",
       "prawo":4}
}

#czynności
action = ['otwórz', 'podnieś', 'włącz', 'wyłącz', 'użyj', 'daj']
print("Czynności, które możesz wykonywać podczas gry: ",action)



print("\n\nPrzypominasz sobie, że rzeczy z szuflady nie zostały spakowane. Chowasz je do plecaka.")
equipment = ["jabłko", "latarka", "nóż", "identyfikator"]
print("Twój ekwipunek to: ", equipment)
print("\nSprawdzasz godzinę, jest już późno, a masz wiele spraw do załatwienia! Najwyższa pora wyjść z domu")

#2 LOKACJA
"*"*40
print("Nagle słyszysz, jak sąsiadka woła: ",
      "\n-"+name+"!","Podejdź proszę, nie umiem...")
neighbourHelp = input("Chcesz się zatrzymać i jej pomóc? tak/nie" )
if neighbourHelp == "tak":
    print("To idź!")
else:
    print("I tak trzeba pójść, nie ma to tamto!")
print("\n-Oh, jak dobrze, że jesteś! Wiem, że wyjeżdżasz wieczorem, dlatego po raz ostatni chciałm poprosić Cię o przysługę, telewizor mi nie działa."
      "\nMógłbyś na to spojrzeć?")
print("\n-Jasne nie ma problemu!")
print(name,"podchodzi do telewizora")
'''MINIGRA do naprawienia telewizora
if tv == 1:
    print("Gotowe, telewizor działa!")
else:
    print("Niestety będzie musiała Pani zadzwonić po technika").
'''
print("-Dobrze, ja już muszę się zbierać, mam jeszcze trochę rzeczy do załatwienia."
      "\n-Bezpiecznej drogi, odezwij się czasem! Ah, zapomniałabym, miałam Ci to wręczyć na urodziny, "
      "\nale chyba będę musiała wcześniej."
      "\n\tPatrzysz ze zdumieniem, jest to haczyk z pamiętnego wędkowania z ojcem. Zdziwiony pytasz:"
      "\n-Skąd to Pani ma?"
      "\n-Twój ojciec pomagał mi kiedyś wynieść pudła na strych, musiał mu wypaść z kieszeni."
      "\nTo było tuż przed jego zaginięciem..."
      "\nW każdym razie, znalazłam to dopiero kilka dni temu, za jedną z szaf."
      "\nMam nadzieję, że prezent Ci się podoba!")
takePresent = input("Zabierz prezent ")
while takePresent != action[6]:
    print("Lepiej dobrze się zastanów.")
    takePresent = input("Zabierz prezent ")

print("\n-Tak, jasne, bardzo dziękuję! Za wszystko."
      "\n-Powodzenia drogi chłopcze!")
equipment.append("haczyk z wędkowania")
print("\n\nDobra, czas na załatwienie sprawy z pracą, muszę oddać identyfikator.")
#3 LOKACJA
"*"*40
print("\nRozmyślając, skąd haczyk wziął się u sąsiadki, prawie wpadasz pod samochód. "
      "\nOdskakując na bok, trafiasz na idącego z naprzeciwka przyjaciela.")
print("\n-Hej", name+"! Co Ty tu jeszcze robisz?"
      "\n-No mógłbyś zachować chociaż pozory, że jest Ci przykro!"
      "\n-Jakie przykro, wreszcie",workplace,"stoi przede mną otworem!"
      "\nMoże uda mi się w końcu zabrać za jakąś porządną pracę."
      "\n-Ha, akurat nie wytrwałbyś tam jednego dnia!"
      "\n-Oj nie bądź taki szybki Bill, udowodnię Ci, że będę nawet lepszy!")
'''
if profession == "nauczyciel":
    minigra na inteligencję 
elif profession == "trener":
    minigra na siłę
elif profession == "aktor":
    minigra na charyzmę 
'''
print("\n-Hej, to jak jeszcze tu jesteś, to może zostaniesz do jutra?"
    "\nI tak mamy do nadrobienia jeszcze..."
    "\n-Niee, co by nie było, muszę się dzisiaj stąd ruszyć i tak zbyt długo się zbieram."
    "\nWpadnę niedługo w odwiedziny."
    "\n\t-No nic, w takim razie trzymaj się i powodzenia!"
    "\nStojąc już samotnie na skrzyrzowaniu, czujesz, że ktoś Cię obserwuje."
    "\nA jesteś przecież sam. Postanawiasz zignorować ten oczywisty wymysł i kierujesz się dalej w kierunku pracy")
#4 LOKACJA - praca
"*"*40
print("\nWzdychasz. Praca tutaj często doprowadzała Cię na skraj załamania nerwowego."
      "\nI w sumie... Nie masz nic więcej do dodania. Cieszysz się niezmiernie, że to już koniec.")

if profession == "nauczyciel":
    print("\nPo raz ostatni postanawiasz skorzystać z jedynego pozytywnego aspektu tej szkoły - ")
elif profession == "trener":
    print("\nPo raz ostatni postanawiasz skorzystać z jedynego pozytywnego aspektu tej siłowni - ")
elif profession == "aktor":
    print("\nPo raz ostatni postanawiasz skorzystać z jedynego pozytywnego aspektu tego teatru - ")

#MINIGRA


print("\n\tNagle słyszysz chrząknięcie. To Twoja szefowa."
      "\n-To fascynujące jak tragiczną pamięć mają teraz młodzi ludzie."
      "\n-Też niezmiernie cieszę się, że Panią widzę! Oto identyfikator.")
id = input("Czy chcesz oddać identyfikator?tak/nie ")
while id.lower() != action[5]:
    print('Oddaj, bo nie dostaniesz kaucji!')
    id = input("Czy chcesz oddać identyfikator? ")

del equipment[3]
print("Z ekwipunku usunięty został identyfikator.")
print("\n-Proszę!"
      "\n-No, można było tak od razu! "
      "\n-Co do kaucji, biorąc pod uwagę wszystkie spowodowane przez Ciebie szkody, pozwoliłam sobie na małą interwencję."
      "\nCzęść została odliczona od wypłaty, część dostaniesz pod koniec przyszłego tygodnia, a resztę... "
      "\nPozostała część kwoty zostanie wydana w postaci żetonów do naszego sklepiku. Czyż to nie wspaniały pomysł!"
      "\n-Jak to nic... Jak to wymienić... JAKIE ŻETONY?!"
      "\n-Zawsze mogę po prostu je odliczyć od wszystkich spóźnień."
      "\n\tPo chwili zastanowienia..."
      "\n-Dobra, żetony nie brzmią w sumie tak źle!")

equipment.append(20)
print("Żetony są już w ekwipunku, zmierzaj do wyjścia czym prędzej!")

#4 LOKACJA
"*"*40
if profession == "nauczyciel":
    print("\nRozglądasz się po sklepie. Znajudją się tu wykonane z niesamowitym kunsztem figurki naukowców.")
elif profession == "trener":
    print("\nRozglądasz się po sklepie. Znajudją się tu wykonane z niesamowitym kunsztem figurki sportowców.")
elif profession == "aktor":
    print("\nRozglądasz się po sklepie. Znajudją się tu wykonane z niesamowitym kunsztem figurki aktorów.")

print("Nieco Cię przerażają, ale może po prostu nie znasz się na sztuce tak dobrze jak myślisz?"
      "\nKażda z nich kosztuje po 10 żetonów."
      "\nNa kolejnych półkach znajdujesz coś, co sprawia, że czujesz się bezpiecznie - jedzenie i picie."
      "\nCzas nagli. Musisz coś kupić. Masz do wykorzystania 20 żetonów, bezwartościowych poza sklepem."
      "\nOczywiście jeśli nie bierzemy pod uwagę wartości sentymentalnej..."
      "\nCo wybierasz?"
      "\nMożesz sobie pozwolić na zestaw: 1 - figurka; sok(jabłkowy) i minibaton, 2 - figurka; banan i baton lub 3 - sok; wrap(wegetariański) i baton")

shopping = input("Który numer zestawu wybierasz?")

if shopping == "1":
    equipment.append('figurka')
    equipment.append('sok')
    equipment.append('minibaton')
elif shopping == '2':
    equipment.append('figurka')
    equipment.append('banan')
    equipment.append('baton')
elif shopping == '3':
    equipment.append('sok')
    equipment.append('wrap')
    equipment.append('baton')
if charisma>10:
    print("Ze względu na swój urok osobisty, sprzedawczni dorzuciła Ci czekoladę gratis!")
    equipment.append('czekolada')

print("Zakupy zrobione, zostały dodane do ekwipunku. Ruszajmy dalej!")
equipment.remove(20)

#5 LOKACJA
"*"*40
print("\n\nNapawasz się widokiem, długo tutaj nie wrócisz. Z jednej strony czujesz żal, sentyment jest duży, w końcu stąd pochodzisz... ",
    "\nNatomiast towarzyszy Ci również ekscytacja i nadzieja, że wreszcie będziesz mógł zacząć nowy rozdział w życiu, niepokierowany zaginięciem ojca.",
    "\nNagle, zauważasz po prawej jak dwóch mężczyzn gra w jakąś zmodyfikowaną wersję kości.",
    "\nPostanawiasz do nich dołączyć, a nóż uda Ci się zarobić na dodatkowe paliwo.")
#MINIGRA
print("\nZaczynasz myśleć o spędzonym czasie w tych stronach. O wszystkich spotkaniach ze znajomymi, "
      "\no tym jak zawsze byliście z ojcem blisko, w sumie nic dziwnego w końcu wychowywał Cię samotnie."
      "\nPrzypomniało Ci się jak kiedyś... Nagle ktoś zaczepił Cię za ramię. Był to mężczyzna w średnim wieku,"
      "\nktóry normalnie nie budziłby podejrzeń, gdyby nie jeden szczegół. Miał w dłoni broń."
      "\nNiczym udało Ci się zareagować, słyszysz:"
      "\n-Witaj",name+".","Kopę lat!"
      "\nOstatnie co pamiętasz, to przerażający uśmiech porywacza. Później nastąpiła ciemność.")

'''***************************'''
#2 POZIOM
#1 LOKACJA
"*"*40
print("\nBudzisz się z ogromnym bólem z tyłu głowy. Instynktownie chcesz jej dotknąć, ale okazuje się, że masz związane ręce."
      "\nW panice przypominasz sobie ostatnie wydarzenia... "
      "\nPraca, sklep, żetony... PORWALI MNIE!"
      "\nPróbujesz się uspokoić. Wdech, wydech. Musisz się uwolnić."
      "\nNagle orientujesz się, że w zasięgu ręki jest plecak z Twoim ekwipunkiem."
      "\nZdecydowanie najbardziej przebiegli porywacze..."
      "\nMuszę uwolnić ręce.")
if strength>10:
    print("Dzięki swoim nadzwyczajnym mięśniom, udało Ci się rozerwać węzły, bez zużycia noża z ekwipunku.")
else:

    a = ['użyj']
    b = ['nóż']
    freeAct = input()
    freeEquip = input()
    while (freeAct != a[0]) and (freeEquip != b[0]):
        print("Chyba nie chcesz się uwolnić...")
        freeAct = input()
        freeEquip = input()
    print("Sukces!")








print("Przy użyciu noża, udało Ci się oswobodzić z węzłów. Niestety, gdy tylko spełnił swoje zadanie, rozpadł się.")
print("\nRozglądasz się po pomieszczeniu, ale niewiele widzisz, jest bardzo ciemno."
      "\nOkna są pozabijane deskami, ledwo przedostają się pojedyncze promyki słońca."
      "\nPrzynajmniej wiesz, że jest dzień. Sprawdzasz ekwipunek, wszystko co miałeś jest."
      "\nPróbujesz znaleźć coś przydatnego w pokoju, ale nic nie wygląda na użyteczne. "
      "\nZastanawiasz się o co w tym wszystkim chodzi, kim są ci ludzie..."
      "\nUspokajasz się, wiesz dobrze, że spanikowany niczego nie wymyślisz. Musisz się stąd wydostać, najlepiej w jednym kawałku."
      "\nOstrożnie podchodzisz do drzwi. Niepewnie chwytasz za klamkę, ale oczywiście, okazuje się, że są zamknięte."
      "\nZastanawiasz się w jaki sposób je otworzyć.")
if strength>10:
    print("Jesteś na tyle silny, że po prostu je wyłamujesz.")
else:
    print("Postanawiasz je stratować, udaje Ci się, ale kosztem 5hp")
    health_points -= 5
print("Twoim oczom ukazuje się długi korytarz, już z tej odległosci widzisz, że roi się w nim od pułapek."
      "\nWahasz się chwilę czy nie lepiej odpuścić i poczekać na pomoc, ale orientujesz się, że nikt już nie będzie na Ciebie czekać."
      "\nUdało Ci się pożegnać wszystkich. Cholera. To już naprawdę robi się niebezpieczne..."
      "\nMusisz ruszyć dalej, nie możesz na nikogo liczyć, jesteś swoim jedynym ratunkiem."
      "\nNarzucasz plecak na ramię i z ogromną gulą w gardle, stawiasz pierwszy krok poza bezpieczną strefę.")

#2 LOKACJA
"*"*40
if intelligence>10:
    print("Już na samym początku czekała pułapka, jednak dzięki swojej inteligencji, udało Ci się nie przebić stopy gwoździem.")
else:
    print("Już na samym początku czekała pułapka, która była prawie nie do unikcięcia. W jej wyniku Twoja dłoń została przytrzaśnięta."
          "\nTracisz",hit, "punkty życia.")
    health_points -= hit
print("Próbujesz cokolwiek zobaczyć, ale oprócz lekkiego światła w oddali, nic nie widzisz. Musisz iść po omacku. "
      "\nNie mija chwila, gdy czujesz, że Twoja stopa wylądowała gdzieś, gdzie nie powinna. Czy to jest mina?! "
      "\nSchylasz się i zauważasz, że na wyświetlaczu urządzenia, obok odliczającego zegara, jest opcja wyłączenia"
      "\nBez chwili wahania, klikasz. Twoim oczom ukazuje się zagadka do rozwiązania.")
#MINIGRA
print("Idąc dalej, napotykasz na swojej drodze przeszkodę. Nie jesteś w stanie przesunąć ogromnego automatu."
      "\nLicząc, że uda Ci się znaleźć jakiś przycisk wysuwający nóżki urzędzenia, co by było łatwiej je przesunąć,"
      "\nprzypadkiem je uruchamiasz. Patrzysz z zaciekawieniem co się wydarzy dalej. "
      "\nPo chwili już wiesz i jejku, ale żałujesz, że cokolwiek nacisnąłeś. Automat ewidentnie się uruchamia,"
      "\nkorytarz nieco się oświetlił, jednak nie było czasu, żeby się napawać tym widokiem,"
      "\nponieważ w parze z obrazem, szedł dźwięk. Musisz to jak najszybciej wyłączyć!")
#MINIGRA

print("Chyba już nic nie jest w stanie Cię zdziwić. Czujesz, że jesteś w sytuacji bez wyjścia. Dosłownie. "
      "\nWspierając się o ścianę,stawiasz ostrożnie kolejne kroki."
      "\nMyśląc, że udało Ci się znaleźć rozwiązanie idealne, szybko zostajesz sprowadzony na ziemię."
      "\nLampa, za którą chwyciłeś, przekręciła się. Świetnie, jakżeby inaczej. Czekając aż z podłogi wysuną się kolce"
      "\nalbo ze ścian wystrzelą włócznie, przeżywasz kolejne zdziwienie. Zamiast kolejnej tragedii, okazuje się, że lampa"
      "\nprowadzi do ukrytego pomieszczenia. Czujesz zastrzyk adrenaliny. Może jednak wcale tu nie zginiesz?")


#3 LOKACJA
"*"*40
print("Niepewnie wchodzisz do nowego pomieszczenia. Udaje Ci się znaleźć włącznik światła po lewej stronie."
      "\nWahasz się, czy to nie będzie zbyt niebezpieczne, ale dochodzisz do wniosku, że i tak jest już niebezpiecznie."
      "\nZapalasz światło. W oszołomieniu patrzysz na pokój. Pokój, a moze właściwie gabinet? "
      "\nNa ścianach znajduje się mnóstwo tablic korkowych, które są zapełnione notatkami, zdjęciami, zarysami map?"
      "\nNie zachowując już żadnych środków ostrożności idziesz prosto do serca gabinetu."
      "\nCzytając notatki zauważasz, że to jeden wielki bełkot. Ah, no tak! Autor użył szyfru. "
      "\nCiekawe czy go złamiesz... Szyfr, nie autora.")
#MINIGRA
print("Znasz już szyfr, teraz możesz przeanalizować gdzie te wszystkie nitki się zbiegają... "
      "\n-Proszę, proszę! Mówiłem, że chłopak rozwiąże to wszystko raz dwa!"
      "\nCo prawda czujesz się trochę wykorzystany i urażony, ale to nic w porównaniu z paraliżem, który Cię objął."
      "\nWidzisz przed sobą dwóch mężczyzn. Jeden z nich, najprowdopodniej mózg operacji,"
      "\nwymownie wskazuje na trzymaną w ręce wspólnika broń."
      "\n-Nie rób nic głupiego."
      "\n-Czego ode mnie chcecie? - Udaje Ci się wydusić."
      "\n-Cóż, - zaczął, podchodząc - chyba już mamy połowę roboty za sobą. Wiesz, że próbujemy odczytać te zapiski od prawie 4 lat?"
      "\nPowoli zacząłeś łączyć fakty. Dlaczego akurat mnie mieli porwać? Dlaczego złamanie szyfru zajęło mi nieco mniej niż te 4 lata?"
      "\nI dlaczego na słowa 4 lata, serce zabiło mi szybciej?"
      "\n-Tata-wyrzucasz po chwili ciszy."
      "\nPorywcz potakuje głową. "
      "\n-Od tak dawna szukamy tego przeklętego artefaktu! Mamy wszystkie składniki, żeby to odczytać, jedyne czego brakowało, to klucza."
      "\n-A ja wam go od tak podałem... Gdzie jest mój ojciec?"
      "\n-Przy odrobinie szczęścia, już odpoczywa sobie po drugiej stronie. Lepiej, żeby nie wpadł w nasze ręce."
      "\nAle mniejsza, nie mamy na to czasu. Popatrz na mapę."
      "\n-Na nic nie popatrzę, dopóki nie dostanę odpowiedzi!"
      "\n-Nie zapomniałeś przypadkiem, że jest nas dwóch, mamy broń, a Ty jesteś więźniem?"
      "\nCóż, może rzeczywiście trochę to umknęło, ale co się dziwić, po usłyszeniu takich rewelacji każdy by odpłynął!"
      "\nPowoli podchodzisz do mapy."
      "\n-Potrzebuję chwili ciszy."
      "\n-Byleby nie za długo!")
#MINIGRA
print("Porywacze popatrzyli na siebie z porozumieniem. Niczym zdążyłeś zareagować, po raz kolejny zobaczyłeś ten przerażający uśmiech."
      "Po nim ciemność. Tak, zostałeś znowu ogłuszony.")

#4 LOKACJA
"*"*40
print("Budzisz się w nieco jaśniejszym miejscu. Musisz przymróżyć oczy, żeby je przyzwyczaić do takiej zmiany."
      "\nCzyżby udało Ci się uciec?! Nic bardziej mylnego. "
      "\nPo lewej stronie widzisz jednego z porywaczy, a po prawej plecak i drzwi samochodowe. Jesteście w drodze. Ale gdzie?"
      "\nNo tak, przecież rozwiązałeś zagadkę. Pewnie jedziecie na miejsce. "
      "\nZ jednej strony czujesz ekscytację, może wreszcie dowiesz się co stało się z ojcem, a z drugiej strach, że nie będzie okazji tego przetrawić."
      "\n-O! Śpiąca królewna się obudziła! Dobrze się składa, jesteśmy prawie na miejscu.Zabijmy ten czas jakąś pogawędką."
      "\n-Co ze mną zrobicie?"
      "\n-Na pewno chcesz wiedzieć? Może jednak jakieś inne pytanie? Masz trzy trafy! ")



if charisma>10:
    i=-1
else:
    i = 0
while i<3:
    choosequestion = input("\n\nKtóre pytanie chcesz zadać? Podaj numer. Masz trzy próby. Chyba, że Twoja charyzma da się we znaki...Wtedy będziesz mógł zadać wszystkie pytania."
                                "\n1 - Gdzie jest mój ojciec?"
                                "\n2 - O co w tym wszystkim chodzi?"
                                "\n3 - Jak trzeba być ograniczonym, żeby przez tyle lat nie wpaść na coś tak oczywistego?"
                                "\n4 - Skąd wiedzieliście gdzie mnie znaleźć?")

    if choosequestion == '1':
        print("\n-Gdzie jest Twój ojciec? Oj", name, "chyba nie do końca słuchałeś. Nie wiemy gdzie jest, ale lepiej, żeby nie wpadł w nasze ręce...")
        i += 1

    elif choosequestion == '2':
        print("\n-O co w tym wszystkim chodzi? Tak bardzo z grubsza, Twój ojciec wpadł na trop starozytnego artefaktu. "
              "\nBEZCENNEGO starożytnego artefaktu, którego od lat szukaliśmy. "
              "\nGdy się z nim skontaktowaliśmy, z ojcem, nie artefaktem, to powiedział, żebyśmy spotkali się następnego dnia po drugiej stronie miasta."
              "\nPoszliśmy na jego warunki i co?! Wystawił nas! Mogliśmy z łatwością go wtedy sprzątnąć, ale nie, daliśmy mu szansę, a ten dureń nas oszukał."
              "\nOd tamtej pory nic o nim nie słyszeliśmy, a uwierz młody, szukaliśmy wszędzie...")
        i += 1
    elif choosequestion == '3':
        print("\n-Tobie naprawdę życie jest niemiłe, co?")
        i += 1
    elif choosequestion == '4':
        print("\n-Hmmm, powiedzmy, że nie działamy tylko we dwójkę, hehe...")
        i += 1


print("\n\n-Dobra, dosyć tego gadania. Lepiej oszczędzaj siły. Chociaż, mamy jeszcze chwilkę, także dla zabicia czasu proponuję małą rywalizację...")
#MINIGRA
print("\n-Szefie, jesteśmy na miejscu.")

#5 LOKACJA
"*"*40
print("\n\nNie wiesz czy bardziej powinieneś być zdzwiony, że zostałeś wyniesiony z samochodu czy że znajdujecie się na jakiejś polanie."
      "\n-Uwierz mi, lepiej dla Ciebie, żebyśmy coś tutaj znaleźli."
      "\nGłośno przełknąłeś ślinę. Na spokojnie próbujesz przypomnieć sobie fragment z notatnika..."
      "\n\"W Sępim jarze, przy Orlim głazie, pod starą sosną, gdzie gałąź rzuca cień wiewiórki\""
      "\nTeraz się załamujesz. Przecież tu nie ma żadnych sosen. Czując oddech śmierci na plecach, dosłownie, porywacz z bronią stał za Toba, wahasz się czy już się poddać czy jeszcze chwilę zwlekać."
      "\nRozważania przerwało nagłe wspomnienie z wędkowania. No tak! Przypominasz sobie, jak ojciec tłumaczył Ci gdzie będzie wasze miejsce spotkań, gdybyście się rozdzielili."
      "\nZaczął od tego sępiego jaru, ale to był tylko żart... Za tymi słowami kryło się miejsce, w którym element nie pasował do całości. Coś na widoku..."
      "\nTo mogło być wszystko, ale miałeś wrażenie, że to znajdziesz. Te niby nic nie znaczące fragmenty, to tak naprawdę poszlaki skierowane do Ciebie."
      "\n-I? Moja cierpliwość się już kończy, czego mamy szukać?"
      "\nNie mając niczego innego w głowie i nie wiedząc jak przyjmą Twoją odpowiedź, wypaliłeś:"
      "\n-Szukajmy kamienia w kształcie ryby."
      "\nKilka sekund patrzyli na Ciebie jakbyś zwariował, ale nie odezwali się ani słowem. Zaczęli szukać."
      "\nKorzystając z tej niespodziewanej okazji, postanowiłeś oprócz szukania kamienia-ryby, zorganizować sobie jakąś broń. "
      "\nPrzypominasz sobie, że po drodze mijaliście coś co mogłoby się nadać, ale gdzie to było...")
#MINIGRA
print("\n-Eeee, chyba coś takiego znalazłem. Chodź tu szybko. "
      "\nPodchodzisz do porywacza i rzeczywiście, Twoim oczom ukazuje się otoczony dziwnym ołtarzykiem, który miał chyba go ukryć, kamień-ryba."
      "\nWszyscy stoicie zmieszani. Co teraz? Mając w plecaku broń, czułeś się już pewniej, ale dalej dość kiepsko. "
      "\nKamień-ryba? Co ja mam teraz z tym zrobić? Przecież mnie zabiją. "
      "\nZ każdą kolejną sekundą czułeś jak Twoje szanse na przetrwanie drastycznie maleją. Może czas podjąć irracjonalną decyzję?"
      "\nW trójkę mierzyliście się spojrzeniem. "
      "\n-Ty smarkaczu..."
      "\nTeraz albo nigdy! Rzucasz się do ucieczki. Niestety, nie była ona zbyt brawurowa. Udało Ci się zrobić zaledwie jeden krok. "
      "\nUpadając na ziemię czułeś jak jeden z nich trzyma Cię za ramię. No pięknie. Czyli to już serio koniec. Spadając patrzyłeś w dół."
      "\nNa kamień. Jego rybi kształt w jakiś sposób Cię ukoił. Był na tyle kojący, że nagle zapragnąłęś za wszelką cenę go chwycić."
      "\nNawet jeśli to miała być ostatnia rzecz, którą zrobisz w życiu. Co swoją drogą jest bardzo prawdopodobne."
      "\nGdy wreszcie zacisnąłeś palce na tym kamieniu, poczułeś dziwne mrowienie, a krzyki porywaczy stały się zniekształcone.")
"*"*50

#POZIOM 3
#1 LOKACJA
print("\nO dziwo, nie zemdlałeś, chociaż biorąc pod uwagę co rzeczywiście się wydarzyło, chyba wolałbyś zemdleć."
      "\nPowoli podnosisz się z ziemi, która jakimś dziwnym trafem stała się jeszcze bardziej zielona."
      "\nPo lewej zauważasz jak leży jeden z oprychów, ten odpowiadający za „bezpieczeństwo”..."
      "\nJednak niczym zaczniesz się tym przejmować, masz nieco inne sprawy na głowie. Jedną z nich jest pytanie: gdzie ja jestem?!!"
      "\nDalej znajdowałeś się na polanie, ale wygląda zdecydowanie inaczej niż ta... poprzednia? Drzewa były inne, niektóre z nich otaczały kamienie..."
      "\nW ogóle przed Tobą rozciągała się swego rodzaju dżungla. A chyba największym znakiem, że coś jest nie tak, było nagłe zniknięcie drugiego oprycha."
      "\nPrzecież tylko się przewróciłeś...I raczej na pewno nie uderzyłeś o nic głową! Cóż, jak absurdalnie to nie zabrzmi, wygląda na to, że teleportowałeś się do innej rzeczywistości."
      "\nCzyli rzeczywiście artefaktem był kamień-ryba, tyle, że o jego wyjatkowości nie stanowił kształt, tylko fakt, że był bramą do innego świata."
      "\nSerce zabiło Ci szybciej. Może Twój ojciec też tu jest? Ale jeśli żyje i nic mu nie jest, to dlaczego nie wrócił?"
      "\nZ rozważań wyrwał Cię drugi ocalały."
      "\n-Ccccco, gdzie my jesteśmy?! Coś Ty zrobił? Jak stąd wrócić?"
      "\n-Nie wiem, nie wiem i hmmmm... NIE WIEM."
      "\nNie wiesz również, który z was jest bardziej przerażony. Próbujesz wprowadzić trochę normalności."
      "\n-Dobra, jak masz na imię?"
      "\nOprych patrzy na Ciebie podejrzliwie."
      "\n-Spokojnie, żeby wziąć chwilówkę potrzebuję nieco więcej danych. No dalej, nie będę wołał do Ciebie oprychu!"
      "\n-Mam na imię Gabriel.")
gunmanName = 'Gabriel'
gunmanHP = 70
gunmanStrength = 13
gunmanAttack = 7
print("\n-Dobra, Gabrielu, mamy dość nietypową sytuację.Proponuję zawrzeć sojusz na bliżej nieokreślony czas. Zgoda?"
      "\n-Zgoda. "
      "\n-Rozejrzymy się."
      "Przecierając czoło pomyślałes, że to jest naprawdę intensywny dzień. Rozglądając się po otoczeniu, zauważasz błyszczący się element.")
shinyThing = input("\n\nChcesz go podnieść?tak/nie: ")
if shinyThing == 'tak':
    print("\nOstrożnie podchodzisz do przedmiotu, kształtem przypomina... właściwie nic. To chyba jakiś kolczyk... Gdy już dosłownie miałeś go podnieść, zostajecie otoczeni.")
    intelligence -= 1
else:
    print("\nCoś Ci podpowiada, że to może być pułapka, dlatego postanawiasz jednak zachować czujność i pójść w drugim kierunku."
          "\nAle to Ty. Jest jeszcze z Tobą Gabriel, który gdy tylko zobaczył, że coś się błyszczy, od razu rzucił się w tym kierunku, jakby miało go to uwartować."
          "\nNiczym zdążyłeś zareagować, podniósł przedmiot. Zaledwie chwilę później, zostaliście otoczeni.")
    intelligence += 1
print("\nWidząc wycelowane w was włócznie, myślałeś czy od razu nastąpiła kumulacja Twojego szczęścia i zostaliście otoczeni przez kanibali."
      "\nJuż nawet nie liczyłeś, że Gabriel ma ze sobą broń. Zresztą, nawet jeśli by miał, to pewnie nie pomyślałby by jej użyć."
      "\nWyciągasz ręce w geście kapitulacji. Szybko okazuje się, że tutaj ten gest musi oznaczać coś obraźliwego. Pięknie."
      "\nChwilę po tym część atakujących rozsuwa się, wpuszczając przed siebie mężczyznę przepasanego lamparcią skórą. To chyba dowódca."
      "\nNie odzywa się słowem, chyba wie, że to nie ma sensu. Jednak próbuje podjąć rozmowę w inny sposób. Podaje mi pudełko. ")
openBox = input("Co chcesz zrobić z pudełkiem? ")
while openBox != action[0]:
    print("Lepiej dobrze się zastanów.")
    openBox = input("Co chcesz zrobić z pudełkiem? ")
print("Pudełko zostało otwarte!")
#MINIGRA

print("\nPatrząc na ich nad wyraz pozytywną reakcję, dochodzisz do wniosku, że urządzenie miało na celu powiedzieć im, czy masz dobre intencje, czy jednak złe."
      "\n")