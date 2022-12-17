# Halállabirintus

A feladat, egy régen népszerű „lapozgatós könyv” számítógépes verziójának elkészítése. Az eredeti könyv úgy működött, hogy elolvastad az 1. oldalt, majd választanod kellett, hogy hova lapozol tovább. Így ugrálva kellett végig haladni, és feltételezték, hogy nem lapozol vissza, ha rosszat választottál, illetve a csatákban sem csaltál.
A leírásban az eredeti oldalszámokat adom meg, de nekünk azzal nem kell foglalkozni, csak azzal, hogy mit választott a játékos. Pl.: 1. oldalon vagy, a végén a kérdés, hogy északra mész 66. oldal, egyébként 230. Ha a játékos északot választja, akkor azt kell megjeleníteni, ami a 66. oldalon olvasható. Annak az alján szintén lesz választási lehetőség…
A játék során lehetőség lesz csatázni, tárgyakat felvenni és ezek alapján változhatnak a képességeid (ügyesség, életerő, szerencse). Csata nem lesz a feladatban, de azért közlöm az eredeti leírás egyszerűsített verzióját. A képességek meghatározása viszont a feladat része!

## ÜGYESSÉG, ÉLETERŐ ÉS SZERENCSE

Dobj egy kockával, adj 6-ot a dobott számhoz, és az összeget írd be a Kalandlap ÜGYESSÉG négyzetébe.
Most dobj két kockával, és az eredményhez adjál12-t; a kapott számot írd be az ÉLETERŐ négyzetbe.
Van egy SZERENCSE rovat is. Ehhez egy kockával dobj, és 6-ot adj az eredményhez, majd az összeget írd a SZERENCSE rovatba.
Az értékeket el kell tárolni, most nincs kalandlap ahova beírjuk, de a program tartsa számon.

## A harc menete

1. Dobj két kockával a teremtmény nevében. A kapott számot add az ő ÜGYESSÉG pontjaihoz. Az összeg az ő TÁMADÓEREJE.
2. Dobj két kockával most magadnak, és az eredményt add saját jelenlegi ÜGYESSÉG pontjaidhoz. Ez a te TÁMADÓERŐD.
3. Ha a te TÁMADÓERŐD nagyobb, mint a teremtményé, akivel küzdesz, megsebezted. Menj tovább a 4. lépésre. Ha a teremtmény TÁMADÓEREJE nagyobb, ő sebzett meg téged, és haladj az 5. lépéshez. Ha a két TÁMADÓERŐ egyforma, kivédtétek egymáscsapását, és a következő Fordulót az 1. lépéstől elölről kezditek.
4. Megsebezted a teremtményt, ezért vonjál le 2 pontot ÉLETEREJÉBŐL. Felhasználhatod SZERENCSÉDET is, hogy további sebeket ejts rajta (lásd odébb).
Ha Szerencséd volt, akkor 4 pontot vonj le az életerejéből, ha balszerencséd volt, akkor csak 1 pontot. Mindkét esetben csökkennek a szerencse pontjaid eggyel. A Szerencsét nem kötelező használni.
5. A teremtmény sebzett meg téged, ezért vonjál le 2 pontot saját ÉLETERŐDBŐL. De ilyenkor is lehet SZERENCSÉD (lásd odébb). Ha szerencséd volt csak egy pontot sérülsz, ha nem volt, akkor 3 pontot sérülsz. A szerencsepontod mindkét esetben eggyel csökken. A Szerencsét nem kötelező használni.
6. Ellenőrizd a teremtmény vagy a saját ÉLET-ERŐ pontjaidat, és a SZERENCSE pontokat is, ha kell.
7. Kezdd el a következő Fordulót meglévő ÜGYESSÉG pontjaiddal, azaz ismételd meg a lépéseket 1-6-ig. Ezt mindaddig megteheted, amíg vagy a te, vagy a teremtmény ÉLETERŐ pontjai nem fogynak el (halál).

A SZERENCSE próbájáról összegezve:  2 kockával dobva, ha kevesebb, mint a SZERENCSE pontjaid, akkor szerencséd volt, egyébként balszerencséd. Minden esetben csökken eggyel a SZERENCSE pontod. Ha sebzésre használod, akkor duplázódik a sebzés, balszerencsénél csak 1 pont. Ha csökkenteni akarod a saját sebzésedet, akkor szerencsénél csak 1 pont, balszerencsénél összesen 3 pontot kel levonjál. Ne feledd, hogy minden használatnál csökken a szerencse pontod.
Alább következik a játék menete, ami nagyjából 10 választás után véget ér, mert az egész könyv 400 szituációból állna. A végén van még feladat, azt is olvasd el!

## Játék menete – ezt kell leprogramozni

Kezdés
Egy versenyre nevezel, aminek a lényege, hogy át kell kelni a halállabirintuson. A labirintusban tárgyakat találhatsz és szörnyekkel kell harcoljál.
1. oldal
Miután öt percet haladtál lassan az alagútban, egy kőasztalhoz érsz, amely a bal oldali fal mellett áll. Hat doboz van rajta, egyikükre a te neved festették. Ha ki akarod nyitni a dobozt, lapozz a 270-re. Ha inkább tovább haladsz észak felé, lapozz a 66-ra.
56. oldal
Látod, hogy az akadály egy széles, barna, sziklaszerű tárgy. Megérinted, és meglepve tapasztalod, hogy lágy, szivacsszerű. Ha át szeretnél mászni rajta, lapozz a 373-ra. Ha ketté akarod vágni a kardoddal, lapozz a 215-re.
66. oldal
Néhány perc gyaloglás után egy elágazáshoz érsz az alagútban. Egy, a falra festett fehér nyíl nyugatfelé mutat. A földön nedves lábnyomok jelzik, merre haladtak az előtted járók. Nehéz biztosan megmondani, de úgy tűnik, hogy három közülük a nyíl irányába halad, míg egyikük úgy döntött, hogy keletnek megy. Ha nyugat felé kívánsz menni, lapozz a 293-ra. Ha keletnek, lapozz a 56-re.
137. oldal
Ahogy végigmész az alagúton, csodálkozva látod, hogy egy jókora vasharang csüng alá a boltozatról.
215. oldal
Kardod könnyedén áthatol a spóragolyó vékonykülső burkán. Sűrű barna spórafelhő csap ki a golyóból, és körülvesz. Némelyik spóra a bőrödhöz tapad, és rettenetes viszketést okoz. Nagy daganatok nőnek az arcodon és karodon, és a bőröd mintha égne. 2 ÉLETERŐ pontot veszítesz. Vadul vakarózva átléped a leeresztett golyót, és keletnek veszed az utad.
270. oldal
A doboz teteje könnyedén nyílik. Benne két aranypénzt találsz, és egy üzenetet, amely egy kis pergamenen neked szól. Előbb zsebre vágod az aranyakat, aztán elolvasod az üzenetet: - „Jól tetted. Legalább volt annyi eszed, hogy megállj és elfogadd az ajándékot. Most azt tanácsolom neked, hogy keress és használj különféle tárgyakat, ha sikerrel akarsz áthaladni Halállabirintusomon.” Az aláírás Szukumvit. Megjegyzed a tanácsot, apró darabokra téped a pergament, és tovább mész észak felé. Lapozz a 66-ra.
293. oldal
A három pár nedves lábnyomot követve az alagút nyugati elágazásában hamarosan egy újabb el-ágazáshoz érsz. Ha továbbmész nyugat felé a lábnyomokat követve, lapozz a 137-re. Ha inkább észak felé mész a harmadik pár lábnyom után, lapozz a 387-re.
373. oldal
Fölmászol a lágy sziklára, attól tartasz, hogy bár-melyik pillanatban elnyelhet. Nehéz átvergődni rajta, mert puha anyagában alig tudod a lábadat emelni, de végül átvergődsz rajta. Megkönnyebbülten érsz újra szilárd talajra, és fordulsz kelet felé.
387. oldal
Hallod, hogy elölről súlyos lépések közelednek. Egy széles, állatbőrökbe öltözött, kőbaltás, primitív lény lép elő. Ahogy meglát, morog, a földre köp, majd a kőbaltát felemelve közeledik, és mindennek kinéz, csak barátságosnak nem. Előhúzod kardodat, és felkészülsz, hogy megküzdj a Barlangi Emberrel.
Barlangi Ember ÜGYESSÉG 7 ÉLETERŐ 7

## További feladatok

Nem folytatjuk tovább, akár merre is mentél, véget ér a kaland és az eredeti feladattól függetlenül itt most ki kell írni a jelenlegi állapotodat. Ha akarsz, lehet harcolni, tudtál aranypénzt gyűjteni, csökkenhetett az ÉLETERŐ pontod. Az eredetihez képest az új értékeket, helyzetet kell kiírni.
