# mestint

**plusz irodalom:**

- [Várterész Magdolna - Mesterséges Intellegincia 1 előadások](https://arato.inf.unideb.hu/varteresz.magda/mi1folia/foliafo.pdf)
  - pl: procedure ALAP-BACKTRACK (megoldást kereső rendszerek)

**Notes:**

- week8 orai anyag: alpha, béta esés nem lesz benne zh-ban (csak a vizsgában)

zh-ban elméletből is lesz rész:

- főleg alap definiciok (alapot tér def., megoldás)

zh írott jegyzet lehet hogy lehet használni (??).

gyakorlati resz: week7ig (egyesített dolgok) bármi (pl: egészítsd ki a fuggvényeket a többi alapján, szélességi keresőnél kiterjesztés, is_goal_state ...).

zh:
papir nem lesz, csak kod:

- allapot ter reprezentacioja kodolas (reszlete)
- keresok (implementalas, csak reszletet)
- neurális háló
- reinforcment learning
- elméleti kérdések (ez már papiron) bármi
- (nem lehet semmilyen segítséget használni)

nem lesz a zhban a gyakorlati anyagbol:

- naive bayes
- lépés ajánló

gitfrontos repo-k: 1-6. 9-10.

ponthatarok:

- 60%: 2
- ...
- 90%: 5

máj 13
maj 20-ai héten javító, vagy nem....

**11th week notes:**

**regression.ipynb**

- adathalmaz beolvasasa (read csv)
- StandardScaler()
- split (nem kell?)
- .fit_transform
- !: neuralis halo definialasa : model = Sequential([Dense ...])

optimalizacio:

- model.compile(optimizer=keras.optimizers.Adam(learning_rate=0.0003), loss="mean_square_error")...

**reinforcment**

tictactoe.py

- definiicio episode?
- zh pl: act()
- ?? epsilon
- zh : def learn
- zh: formulából függvény (pl def learn) (pass részét kitölteni...)

game_search_algorithm 66-91. line (class QLearningAgent)

## 12th week:

- TEOKJ 2.sz 112 H18
- nincs segedeszköz (csak elearning?, ZIP download, ZIP upload)
- notebook/nem notebook ugy lesz ahogy a AI-2024 repo-ba
- elmélet: 1db 2pont, fóliákból, tulelokészlet: **elméleti kérdések** elearningen!
- zh pl: tobbosztályos osztályozás, egy osztáloyos nem lesz

## zh feladatok types:

- elso feladat zh: állapottér repr. egy része implementációja (minden is, bármelyik része) (első 4-5 óra kb)
- kereső algoritmus masodik feladat: oran tanultak kozul, foleg implementalni kell tudni
- harmadik: neuralis halo, regresszio vagy tobbosztályos osztályozás, nem kell adatok betoltese, maga a train test split alkalmazasa, validation nem kell
- negyedik: neuralis halo definialasa (rétegek), loss fuggveny, kimeneti rétegek, bemeneti rétegek száma
- otodik reinforcment learning: nem kornyezetet kell implementalni, QLearningAgent
- hatodik: elméleti rész, elméleti kérdések elearningen kb ...

neuralis halobol kell: model = Sequential([]), bemeneti réteg, rejtett rétegek (köztes rétegek), kimeneti réteg, kell csak kb.. , aktivacios fuggveny minden rétegben kell!! minden rétegben relu, kivéve a kimeneti rétegben ahol osztályozásnál több ostályozásnál softmax kell, ha regresszio -> akkor nincs aktivacios fuggveny
Dropout nem kell, csak Dense kell.

bemeneti akkor 1, ha X_train[0] 1 elemű?? (pl MNIST), vagy annyi amennyi darabszám van ott X_train[0]-ba
vagy X_train.shape (sor, oszlop)

better way to run jupyter notebook: save -> clear all outputs -> run all

foleg a feltoltott kodok a fontosak

pót zh nem lesz.

windows: Anaconda Prompt !,
rész pontok lesznek,
max 10 pont
