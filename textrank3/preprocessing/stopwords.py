# encoding: UTF-8

import json
import os.path

base_path = os.path.dirname(__file__)

english = """
all six eleven just less being indeed over both anyway detail four front already through yourselves fify
mill still its before move whose one system also somewhere herself thick show had enough should to only
seeming under herein ours two has might thereafter do them his around thereby get very de none cannot
every whether they not during thus now him nor name regarding several hereafter did always cry whither
beforehand this someone she each further become thereupon where side towards few twelve because often ten
anyhow doing km eg some back used go namely besides yet are cant our beyond ourselves sincere out even
what throughout computer give for bottom mine since please while per find everything behind does various
above between kg neither seemed ever across t somehow be we who were sixty however here otherwise whereupon
nowhere although found hers re along quite fifteen by on about didn last would anything via of could thence
put against keep etc s became ltd hence therein onto or whereafter con among own co afterwards formerly
within seems into others whatever yourself down alone everyone done least another whoever moreover couldnt
must your three from her their together top there due been next anyone whom much call too interest thru
themselves hundred was until empty more himself elsewhere mostly that fire becomes becoming hereby but
else part everywhere former don with than those he me forty myself made full twenty these bill using up us
will nevertheless below anywhere nine can theirs toward my something and sometimes whenever sometime then
almost wherever is describe am it doesn an really as itself at have in seem whence ie any if again hasnt
inc un thin no perhaps latter meanwhile when amount same wherein beside how other take which latterly you
fill either nobody unless whereas see though may after upon therefore most hereupon eight amongst never
serious nothing such why a off whereby third i whole noone many well except amoungst yours rather without
so five the first having once
"""

spanish = """
un una unas unos uno sobre todo tambien tras otro algun alguno alguna algunos algunas ser es soy eres somos
sois estoy esta estamos estais estan como en para atras porque por que estado estaba ante antes siendo ambos
pero por poder puede puedo podemos podeis pueden fui fue fuimos fueron hacer hago hace hacemos haceis hacen
cada fin incluso primero desde conseguir consigo consigue consigues conseguimos consiguen ir voy va vamos
vais van vaya gueno ha tener tengo tiene tenemos teneis tienen el la lo las los su aqui mio tuyo ellos ellas
nos nosotros vosotros vosotras si dentro solo solamente saber sabes sabe sabemos sabeis saben ultimo largo
bastante haces muchos aquellos aquellas sus entonces tiempo verdad verdadero verdadera cierto ciertos cierta
ciertas intentar intento intenta intentas intentamos intentais intentan dos bajo arriba encima usar uso usas
usa usamos usais usan emplear empleo empleas emplean ampleamos empleais valor muy era eras eramos eran modo
bien cual cuando donde mientras quien con entre sin trabajo trabajar trabajas trabaja trabajamos trabajais
trabajan podria podrias podriamos podrian podriais yo aquel a acabar actualmente acuerdo adelante ademas
ademas adrede afirmo agrego ahi ahora ahi al algo alguna algunas alguno algunos algun alla alli alli alrededor
ambos antano antano ante anterior antes apenas aproximadamente aquel aquella aquellas aquello aquellos aqui
aquel aquella aquellas aquellos aqui arribaabajo aseguro asi asi aun aunque ayer anadio aun b bajo bastante
bien breve buen buena buenas bueno buenos c cada casi cerca cierto cinco claro comento como con conmigo
conocer considera considero contigo contra cosa cosas creo cual cuales cualquier cuando cuanta cuantas cuanto
cuantos cuatro cuenta cuyo cual cuales cuando cuanta cuantas cuanto cuantos como d da dado dan dar de debajo
debe deben deber debido decir dejo del delante demasiado demas dentro deprisa desde despacio despues despues
detras detras dia dias dice dicen dicho dieron diferente diferentes dijeron dijo dio donde dos durante dia
dias donde e ejemplo el ella ellas ello ellos embargo en encima encuentra enfrente enseguida entonces entre
era erais eramos eran eras eres es esa esas ese eso esos esta estaba estabais estabamos estaban estabas estad
estada estadas estado estados estais estamos estan estando estar estara estaran estaras estare estareis
estaremos estaria estariais estariamos estarian estarias estara estas este esteis estemos esten estes esto
estos estoy estuve estuviera estuvierais estuvieramos estuvieran estuvieras estuvieron estuviese estuvieseis
estuviesemos estuviesen estuvieses estuvimos estuviste estuvisteis estuvo esta estan ex excepto existe existen
explico expreso f fin final fue fuera fuerais fueramos fueran fueras fueron fuese fueseis fuesemos fuesen
fueses fui fuimos fuiste fuisteis g general gran grande grandes gustar h ha habeis haber habia habiais habiamos
habian habias habida habidas habido habidos habiendo habla hablan habra habran habras habre habreis habremos
habria habriais habriamos habrian habrias habra habia habian hace hacen hacer hacerlo hacia haciendo han has
hasta hay haya hayais hayamos hayan hayas he hecho hemos hicieron hizo horas hoy hube hubiera hubierais
hubieramos hubieran hubieras hubieron hubiese hubieseis hubiesemos hubiesen hubieses hubimos hubiste hubisteis
hubo i igual incluso indico informo informo ir j jamas junto k l la lado las le lejos les llego lleva llevar
lo los luego lugar m mal manera manifesto mas mayor me mediante medio mejor menciono menos menudo mi mia mias
mientras mio mios mis misma mismas mismo mismos momento mucha muchas mucho muchos muy mas mi mia mias mio mios
n nada nadie ni ningun ninguna ningunas ninguno ningunos ningun no nos nosotras nosotros nuestra nuestras
nuestro nuestros nueva nuevas nuevo nuevos nunca o ocho os otra otras otro otros p pais para parece parte
partir pasada pasado pasar pais peor pequeno pero pesar poca pocas poco pocos podemos poder podra podran podria
podrian poner por porque posible primer primera primero primeros principalmente pronto propia propias propio
propios proximo proximo proximos pudo pueda puede pueden pues q qeu que quedo queremos querer quien quienes
quiere quiza quizas quiza quizas quien quienes que r raras realizado realizar realizo repente respecto s saber
salvo se sea seais seamos sean seas seguir segun segunda segundo segun seis senor senora ser sera seran seras
sere sereis seremos seria seriais seriamos serian serias sera seran seria senalo si sido siempre siendo siete
sigue siguiente sin sino sisi sobre sois sola solamente solas solo solos somos son soy soyos su supuesto sus
suya suyas suyo suyos se si solo t tal tambien tambien tampoco tan tanto tarde te temprano tendra tendran
tendras tendre tendreis tendremos tendria tendriais tendriamos tendrian tendrias tendra tendran tened teneis
tenemos tener tenga tengais tengamos tengan tengas tengo tenia teniais teniamos tenian tenias tenida tenidas
tenido tenidos teniendo tenia tercera ti tiene tienen tienes toda todas todavia todavia todo todos tomar total
tras trata traves tres tu tus tuve tuviera tuvierais tuvieramos tuvieran tuvieras tuvieron tuviese tuvieseis
tuviesemos tuviesen tuvieses tuvimos tuviste tuvisteis tuvo tuya tuyas tuyo tuyos tu u un una unas uno unos
usted ustedes v va vamos van varias varios veces venir ver vez volver vosotras vosotros vuestra vuestras vuestro
vuestros w x y ya yo z el esa esas ese esos esta estas este estos ultima ultimas ultimo ultimos
"""

german = """
aber als am an auch auf aus bei bin bis bist da dadurch daher darum das daß dass dein deine dem den der des
dessen deshalb die dies dieser dieses doch dort du durch ein eine einem einen einer eines er es euer eure fur
hatte hatten hattest hattet hierhinter ich ihr ihre im in ist ja jede jedem jeden jeder jedes jener jenes jetzt
kann kannst konnen konnt machen mein meine mit muß mußt musst mussen mußt nach nachdem nein nicht nun oder seid
sein seine sich sie sind soll sollen sollst sollt sonst soweit sowie und unserunsere unter vom von vor wann
warum was weiter weitere wenn wer werde werden werdet weshalb wie wieder wieso wir wird wirst wo woher wohin zu
zum zur uber
"""

portuguese = """
de a o que e do da em um para é com não uma os no se na por mais as dos como mas foi ao ele das tem à seu
sua ou ser quando muito há nos já está eu também só pelo pela até isso ela entre era depois sem mesmo aos ter
seus quem nas me esse eles estão você tinha foram essa num nem suas meu às minha têm numa pelos elas havia seja
qual será nós tenho lhe deles essas esses pelas este fosse dele tu te vocês vos lhes meus minhas teu tua teus
tuas nosso nossa nossos nossas dela delas esta estes estas aquele aquela aqueles aquelas isto aquilo estou está
estamos estão estive esteve estivemos estiveram estava estávamos estavam estivera estivéramos esteja estejamos
estejam estivesse estivéssemos estivessem estiver estivermos estiverem hei há havemos hão houve houvemos houveram
houvera houvéramos haja hajamos hajam houvesse houvéssemos houvessem houver houvermos houverem houverei houverá
houveremos houverão houveria houveríamos houveriam sou somos são era éramos eram fui foi fomos foram fora fôramos
seja sejamos sejam fosse fôssemos fossem for formos forem serei será seremos serão seria seríamos seriam tenho
tem temos tém tinha tínhamos tinham tive teve tivemos tiveram tivera tivéramos tenha tenhamos tenham tivesse
tivéssemos tivessem tiver tivermos tiverem terei terá teremos terão teria teríamos teriam
"""

danish = """
ad af aldrig alle alt anden andet andre at bare begge blev blive bliver da de dem den denne der deres det dette
dig din dine disse dit dog du efter ej eller en end ene eneste enhver er et far fem fik fire flere fleste for fordi
forrige fra få får før god godt ham han hans har havde have hej helt hende hendes her hos hun hvad hvem hver hvilken
hvis hvor hvordan hvorfor hvornår i ikke ind ingen intet ja jeg jer jeres jo kan kom komme kommer kun kunne lad lav
lidt lige lille man mand mange med meget men mens mere mig min mine mit mod må ned nej ni nogen noget nogle nu ny nyt
når nær næste næsten og også okay om op os otte over på se seks selv ser ses sig sige sin sine sit skal skulle som
stor store syv så sådan tag tage thi ti til to tre ud under var ved vi vil ville vor vores være været
"""

dutch = """
aan aangaande aangezien achte achter achterna af afgelopen al aldaar aldus alhoewel alias alle allebei alleen alles
als alsnog altijd altoos ander andere anders anderszins beetje behalve behoudens beide beiden ben beneden bent bepaald
betreffende bij bijna bijv binnen binnenin blijkbaar blijken boven bovenal bovendien bovengenoemd bovenstaand
bovenvermeld buiten bv daar daardoor daarheen daarin daarna daarnet daarom daarop daaruit daarvanlangs dan dat de
deden deed der derde derhalve dertig deze dhr die dikwijls dit doch doe doen doet door doorgaand drie duizend dus
echter een eens eer eerdat eerder eerlang eerst eerste eigen eigenlijk elk elke en enig enige enigszins enkel er
erdoor erg ergens etc etcetera even eveneens evenwel gauw ge gedurende geen gehad gekund geleden gelijk gemoeten
gemogen genoeg geweest gewoon gewoonweg haar haarzelf had hadden hare heb hebben hebt hedden heeft heel hem hemzelf
hen het hetzelfde hier hierbeneden hierboven hierin hierna hierom hij hijzelf hoe hoewel honderd hun hunne ieder iedere
iedereen iemand iets ik ikzelf in inderdaad inmiddels intussen inzake is ja je jezelf jij jijzelf jou jouw jouwe juist
jullie kan klaar kon konden krachtens kun kunnen kunt laatst later liever lijken lijkt maak maakt maakte maakten maar
mag maken me meer meest meestal men met mevr mezelf mij mijn mijnent mijner mijzelf minder miss misschien missen mits
mocht mochten moest moesten moet moeten mogen mr mrs mw na naar nadat nam namelijk nee neem negen nemen nergens net
niemand niet niets niks noch nochtans nog nogal nooit nu nv of ofschoon om omdat omhoog omlaag omstreeks omtrent omver
ondanks onder ondertussen ongeveer ons onszelf onze onzeker ooit ook op opnieuw opzij over overal overeind overige
overigens paar pas per precies recent redelijk reeds rond rondom samen sedert sinds sindsdien slechts sommige spoedig
steeds tamelijk te tegen tegenover tenzij terwijl thans tien tiende tijdens tja toch toe toen toenmaals toenmalig tot
totdat tussen twee tweede u uit uitgezonderd uw vaak vaakwat van vanaf vandaan vanuit vanwege veel veeleer veertig
verder verscheidene verschillende vervolgens via vier vierde vijf vijfde vijftig vol volgend volgens voor vooraf
vooral vooralsnog voorbij voordat voordezen voordien voorheen voorop voorts vooruit vrij vroeg waar waarom
waarschijnlijk wanneer want waren was wat we wederom weer weg wegens weinig wel weldra welk welke werd werden werder
wezen whatever wie wiens wier wij wijzelf wil wilden willen word worden wordt zal ze zei zeker zelf zelfde zelfs zes
zeven zich zichzelf zij zijn zijne zijzelf zo zoals zodat zodra zonder zou zouden zowat zulk zulke zullen zult
"""

finnish = """
aiemmin aika aikaa aikaan aikaisemmin aikaisin aikajen aikana aikoina aikoo aikovat aina ainakaan ainakin ainoa
ainoat aiomme aion aiotte aist aivan ajan alas alemmas alkuisin alkuun alla alle aloitamme aloitan aloitat aloitatte
aloitattivat aloitettava aloitettevaksi aloitettu aloitimme aloitin aloitit aloititte aloittaa aloittamatta aloitti
aloittivat alta aluksi alussa alusta annettavaksi annetteva annettu ansiosta antaa antamatta antoi aoua apu asia asiaa
asian asiasta asiat asioiden asioihin asioita asti avuksi avulla avun avutta edelle edelleen edellä edeltä edemmäs edes
edessä edestä ehkä ei eikä eilen eivät eli ellei elleivät ellemme ellen ellet ellette emme en enemmän eniten ennen ensi
ensimmäinen ensimmäiseksi ensimmäisen ensimmäisenä ensimmäiset ensimmäisiksi ensimmäisinä ensimmäisiä ensimmäistä ensin
entinen entisen entisiä entisten entistä enää eri erittäin erityisesti eräiden eräs eräät esi esiin esillä esimerkiksi
et eteen etenkin etessa ette ettei että haikki halua haluaa haluamatta haluamme haluan haluat haluatte haluavat halunnut
halusi halusimme halusin halusit halusitte halusivat halutessa haluton he hei heidän heidät heihin heille heillä heiltä
heissä heistä heitä helposti heti hetkellä hieman hitaasti hoikein huolimatta huomenna hyvien hyviin hyviksi hyville
hyviltä hyvin hyvinä hyvissä hyvistä hyviä hyvä hyvät hyvää hän häneen hänelle hänellä häneltä hänen hänessä hänestä
hänet häntä ihan ilman ilmeisesti itse itsensä itseään ja jo johon joiden joihin joiksi joilla joille joilta joina
joissa joista joita joka jokainen jokin joko joksi joku jolla jolle jolloin jolta jompikumpi jona jonka jonkin jonne
joo jopa jos joskus jossa josta jota jotain joten jotenkin jotenkuten jotka jotta jouduimme jouduin jouduit jouduitte
joudumme joudun joudutte joukkoon joukossa joukosta joutua joutui joutuivat joutumaan joutuu joutuvat juuri jälkeen
jälleen jää kahdeksan kahdeksannen kahdella kahdelle kahdelta kahden kahdessa kahdesta kahta kahteen kai kaiken
kaikille kaikilta kaikkea kaikki kaikkia kaikkiaan kaikkialla kaikkialle kaikkialta kaikkien kaikkin kaksi kannalta
kannattaa kanssa kanssaan kanssamme kanssani kanssanne kanssasi kauan kauemmas kaukana kautta kehen keiden keihin
keiksi keille keillä keiltä keinä keissä keistä keitten keittä keitä keneen keneksi kenelle kenellä keneltä kenen
kenenä kenessä kenestä kenet kenettä kennessästä kenties kerran kerta kertaa keskellä kesken keskimäärin ketkä ketä
kiitos kohti koko kokonaan kolmas kolme kolmen kolmesti koska koskaan kovin kuin kuinka kuinkan kuitenkaan kuitenkin
kuka kukaan kukin kukka kumpainen kumpainenkaan kumpi kumpikaan kumpikin kun kuten kuuden kuusi kuutta kylliksi kyllä
kymmenen kyse liian liki lisäksi lisää lla luo luona lähekkäin lähelle lähellä läheltä lähemmäs lähes lähinnä lähtien
läpi mahdollisimman mahdollista me meidän meidät meihin meille meillä meiltä meissä meistä meitä melkein melko menee
meneet menemme menen menet menette menevät meni menimme menin menit menivät mennessä mennyt menossa mihin mikin miksi
mikä mikäli mikään mille milloin milloinkan millä miltä minkä minne minua minulla minulle minulta minun minussa minusta
minut minuun minä missä mistä miten mitkä mitä mitään moi molemmat mones monesti monet moni moniaalla moniaalle
moniaalta monta muassa muiden muita muka mukaan mukaansa mukana mutta muu muualla muualle muualta muuanne muulloin
muun muut muuta muutama muutaman muuten myöhemmin myös myöskin myöskään myötä ne neljä neljän neljää niiden niihin
niiksi niille niillä niiltä niin niinä niissä niistä niitä noiden noihin noiksi noilla noille noilta noin noina noissa
noista noita nopeammin nopeasti nopeiten nro nuo nyt näiden näihin näiksi näille näillä näiltä näin näinä näissä
näissähin näissälle näissältä näissästä näistä näitä nämä ohi oikea oikealla oikein ole olemme olen olet olette oleva
olevan olevat oli olimme olin olisi olisimme olisin olisit olisitte olisivat olit olitte olivat olla olleet olli ollut
oma omaa omaan omaksi omalle omalta oman omassa omat omia omien omiin omiksi omille omilta omissa omista on onkin onko
ovat paikoittain paitsi pakosti paljon paremmin parempi parhaillaan parhaiten perusteella peräti pian pieneen pieneksi
pienelle pienellä pieneltä pienempi pienestä pieni pienin poikki puolesta puolestaan päälle runsaasti saakka sadam sama
samaa samaan samalla samallalta samallassa samallasta saman samat samoin sata sataa satojen se seitsemän sekä sen
seuraavat siellä sieltä siihen siinä siis siitä sijaan siksi sille silloin sillä silti siltä sinne sinua sinulla
sinulle sinulta sinun sinussa sinusta sinut sinuun sinä sisäkkäin sisällä siten sitten sitä ssa sta suoraan suuntaan
suuren suuret suuri suuria suurin suurten taa taas taemmas tahansa tai takaa takaisin takana takia tallä tapauksessa
tarpeeksi tavalla tavoitteena te teidän teidät teihin teille teillä teiltä teissä teistä teitä tietysti todella toinen
toisaalla toisaalle toisaalta toiseen toiseksi toisella toiselle toiselta toisemme toisen toisensa toisessa toisesta
toista toistaiseksi toki tosin tuhannen tuhat tule tulee tulemme tulen tulet tulette tulevat tulimme tulin tulisi
tulisimme tulisin tulisit tulisitte tulisivat tulit tulitte tulivat tulla tulleet tullut tuntuu tuo tuohon tuoksi
tuolla tuolle tuolloin tuolta tuon tuona tuonne tuossa tuosta tuota tuotä tuskin tykö tähän täksi tälle tällä tällöin
tältä tämä tämän tänne tänä tänään tässä tästä täten tätä täysin täytyvät täytyy täällä täältä ulkopuolella usea
useasti useimmiten usein useita uudeksi uudelleen uuden uudet uusi uusia uusien uusinta uuteen uutta vaan vahemmän vai
vaiheessa vaikea vaikean vaikeat vaikeilla vaikeille vaikeilta vaikeissa vaikeista vaikka vain varmasti varsin varsinkin
varten vasen vasenmalla vasta vastaan vastakkain vastan verran vielä vierekkäin vieressä vieri viiden viime viimeinen
viimeisen viimeksi viisi voi voidaan voimme voin voisi voit voitte voivat vuoden vuoksi vuosi vuosien vuosina vuotta
vähemmän vähintään vähiten vähän välillä yhdeksän yhden yhdessä yhteen yhteensä yhteydessä yhteyteen yhtä yhtäälle
yhtäällä yhtäältä yhtään yhä yksi yksin yksittäin yleensä ylemmäs yli ylös ympäri älköön älä
"""

def plain_stopwords(json_filename):
    json_file = os.path.abspath(os.path.join(base_path, 'languages', json_filename))
    data = json.load(open(json_file))
    return ' '.join(data)


LANGUAGES = {
    "english": 'stopwords-en.json',
    "german": 'stopwords-de.json',
    "spanish": 'stopwords-es.json',
    "french": 'stopwords-fr.json',
    "italian": 'stopwords-it.json',
    "portuguese": 'stopwords-pt.json',
    "russian": 'stopwords-ru.json',
    "danish": 'stopwords-da.json',
    "dutch": 'stopwords-nl.json',
    "finnish": 'stopwords-fi.json',
    "norwegian": 'stopwords-no.json',
    "hungarian": 'stopwords-hu.json',
    "romanian": 'stopwords-ro.json',
    "swedish": 'stopwords-sv.json',
    "albanian": 'stopwords-sq.json',
}


def get_stopwords_by_language(language):
    language = language.lower()
    if language in LANGUAGES:
        return plain_stopwords(LANGUAGES[language]) #LANGUAGES[language]
    return plain_stopwords(LANGUAGES["english"]) #LANGUAGES["english"]
