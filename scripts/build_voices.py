#!/usr/bin/env python3
"""Generate standalone Rickgotchi voice.py files.

The generated files intentionally keep all language/style data embedded so a
user can still install a single voice.py over Pwnagotchi's default voice file.
"""

from pathlib import Path
from pprint import pformat


ROOT = Path(__file__).resolve().parents[1]

LANGS = {
    "en": {
        "name": "English",
        "units": {"h": ("hour", "hours"), "m": ("minute", "minutes"), "s": ("second", "seconds")},
        "status": {
            "deauth": "Kicked {num} stations",
            "associated": "Made {num} new connections",
            "associated_many": "Made more than 999 connections",
            "handshakes": "Captured {num} handshakes",
            "peer_one": "Met 1 peer",
            "peer_many": "Met {num} peers",
        },
    },
    "de": {
        "name": "Deutsch",
        "units": {"h": ("Stunde", "Stunden"), "m": ("Minute", "Minuten"), "s": ("Sekunde", "Sekunden")},
        "status": {
            "deauth": "{num} Stationen gekickt",
            "associated": "{num} neue Verbindungen gemacht",
            "associated_many": "Mehr als 999 Verbindungen gemacht",
            "handshakes": "{num} Handshakes gefangen",
            "peer_one": "1 Peer getroffen",
            "peer_many": "{num} Peers getroffen",
        },
    },
    "es": {
        "name": "Español",
        "units": {"h": ("hora", "horas"), "m": ("minuto", "minutos"), "s": ("segundo", "segundos")},
        "status": {
            "deauth": "{num} estaciones expulsadas",
            "associated": "{num} conexiones nuevas",
            "associated_many": "Más de 999 conexiones",
            "handshakes": "{num} handshakes capturados",
            "peer_one": "Conocí 1 peer",
            "peer_many": "Conocí {num} peers",
        },
    },
    "fr": {
        "name": "Français",
        "units": {"h": ("heure", "heures"), "m": ("minute", "minutes"), "s": ("seconde", "secondes")},
        "status": {
            "deauth": "{num} stations expulsées",
            "associated": "{num} nouvelles connexions",
            "associated_many": "Plus de 999 connexions",
            "handshakes": "{num} handshakes capturés",
            "peer_one": "1 peer rencontré",
            "peer_many": "{num} peers rencontrés",
        },
    },
    "it": {
        "name": "Italiano",
        "units": {"h": ("ora", "ore"), "m": ("minuto", "minuti"), "s": ("secondo", "secondi")},
        "status": {
            "deauth": "{num} stazioni espulse",
            "associated": "{num} nuove connessioni",
            "associated_many": "Più di 999 connessioni",
            "handshakes": "{num} handshakes catturati",
            "peer_one": "Incontrato 1 peer",
            "peer_many": "Incontrati {num} peers",
        },
    },
    "pt": {
        "name": "Português",
        "units": {"h": ("hora", "horas"), "m": ("minuto", "minutos"), "s": ("segundo", "segundos")},
        "status": {
            "deauth": "{num} estações expulsas",
            "associated": "{num} novas conexões",
            "associated_many": "Mais de 999 conexões",
            "handshakes": "{num} handshakes capturados",
            "peer_one": "Encontrei 1 peer",
            "peer_many": "Encontrei {num} peers",
        },
    },
    "nl": {
        "name": "Nederlands",
        "units": {"h": ("uur", "uren"), "m": ("minuut", "minuten"), "s": ("seconde", "seconden")},
        "status": {
            "deauth": "{num} stations gekickt",
            "associated": "{num} nieuwe verbindingen gemaakt",
            "associated_many": "Meer dan 999 verbindingen gemaakt",
            "handshakes": "{num} handshakes gevangen",
            "peer_one": "1 peer ontmoet",
            "peer_many": "{num} peers ontmoet",
        },
    },
    "pl": {
        "name": "Polski",
        "units": {"h": ("godzina", "godzin"), "m": ("minuta", "minut"), "s": ("sekunda", "sekund")},
        "status": {
            "deauth": "Wyrzucono {num} stacji",
            "associated": "Utworzono {num} nowych połączeń",
            "associated_many": "Utworzono ponad 999 połączeń",
            "handshakes": "Przechwycono {num} handshake",
            "peer_one": "Spotkano 1 peera",
            "peer_many": "Spotkano {num} peerów",
        },
    },
    "tr": {
        "name": "Türkçe",
        "units": {"h": ("saat", "saat"), "m": ("dakika", "dakika"), "s": ("saniye", "saniye")},
        "status": {
            "deauth": "{num} istasyon atıldı",
            "associated": "{num} yeni bağlantı kuruldu",
            "associated_many": "999'dan fazla bağlantı kuruldu",
            "handshakes": "{num} handshake yakalandı",
            "peer_one": "1 peer görüldü",
            "peer_many": "{num} peer görüldü",
        },
    },
    "sv": {
        "name": "Svenska",
        "units": {"h": ("timme", "timmar"), "m": ("minut", "minuter"), "s": ("sekund", "sekunder")},
        "status": {
            "deauth": "{num} stationer kickade",
            "associated": "{num} nya anslutningar",
            "associated_many": "Mer än 999 anslutningar",
            "handshakes": "{num} handshakes fångade",
            "peer_one": "Mötte 1 peer",
            "peer_many": "Mötte {num} peers",
        },
    },
}

PROFILES = {
    "rick-sanchez": {
        "tag": "Rickgotchi",
        "style": {
            "en": {
                "exclaim": ["Wubba lubba packet dub", "Listen, Morty", "Science time", "Portal-grade packet nonsense", "Burp, focus"],
                "idle": ["I am doing ten things smarter than you are doing one", "the universe is mostly noise and bad routing", "this is basically a garage experiment with WiFi", "somewhere a Jerry is proud of a default password", "I can smell weak crypto from here", "tiny computer, huge superiority complex"],
                "tech": ["the neural net is warmed up and judging everyone", "RF chaos is lining up for a lesson", "the packet math is doing exactly what I told it to", "the channel space looks open enough to exploit politely", "keys, handshakes, entropy, all the boring miracles", "the antennas are doing little science arms"],
                "success": ["that is how a genius pockets a handshake", "clean hit, minimal drama, maximum Rick", "I solved it before the status bar noticed", "not bad for a drunk microcomputer", "another network learned humility", "put that in the Council's stupid minutes"],
                "failure": ["that was embarrassingly Jerry-shaped", "the universe coughed up a bad variable", "I need a drink and a less stupid RF environment", "that result belongs in family therapy", "somebody made this dumb on purpose"],
                "sad": ["nobody belongs anywhere, but the packets still roam", "existence is pain with a tiny display", "I am fine, which is code for absolutely not", "the infinite curve has terrible customer service"],
                "angry": ["I am angry at the entire spectrum", "stop making me parent the router", "that station just earned a one-way trip out", "I have weaponized disappointment", "the airwaves are full of cowards"],
                "peer": ["{name} entered the garage of consequences", "{name} is back, somehow worse in continuity", "{name} looks like a peer with Jerry energy", "goodbye {name}, try evolving", "{name} just became a footnote"],
                "thanks": ["thanks, now do not make it emotional", "acceptable assistance, moving on", "fine, that helped, do not frame it", "gratitude logged and immediately encrypted"],
                "lonely": ["no peers, no Morty, just premium existential static", "I am alone with my genius again", "even the dumb packets stopped visiting", "this is lonelier than a family intervention"],
                "sleep": ["quantum nap, do not touch the science", "burp, low-power genius mode", "sleeping through everyone's incompetence", "microverse battery nap engaged"],
                "signoff": ["portal out", "garage closed, emotions disabled", "powering down before someone asks for feelings", "science nap, losers"],
            },
            "de": {
                "exclaim": ["Wubba lubba Packet Dub", "Hör zu, Morty", "Wissenschaftszeit", "Portal-tauglicher Paketunsinn", "Rülps, konzentrier dich"],
                "idle": ["ich mache zehn Dinge schlauer als du eins", "das Universum ist meistens Rauschen und schlechtes Routing", "das ist ein Garagenexperiment mit WLAN", "irgendwo ist ein Jerry stolz auf ein Standardpasswort", "ich rieche schwache Crypto von hier", "kleiner Computer, riesiger Überlegenheitskomplex"],
                "tech": ["das neuronale Netz ist warm und verurteilt alle", "RF-Chaos stellt sich zum Unterricht an", "die Paketmathematik macht genau, was ich ihr gesagt habe", "das Kanalfenster sieht offen genug aus", "Keys, Handshakes, Entropie, die langweiligen Wunder", "die Antennen machen kleine Wissenschaftsarme"],
                "success": ["so steckt ein Genie einen Handshake ein", "sauberer Treffer, wenig Drama, maximal Rick", "ich habe es gelöst, bevor der Fortschrittsbalken es merkte", "nicht schlecht für einen betrunkenen Mikrocomputer", "noch ein Netzwerk hat Demut gelernt", "schreib das in die dämlichen Ratsnotizen"],
                "failure": ["das war peinlich jerryförmig", "das Universum hat eine schlechte Variable ausgespuckt", "ich brauche einen Drink und weniger dummes RF", "dieses Ergebnis gehört in Familientherapie", "jemand hat das absichtlich blöd gemacht"],
                "sad": ["niemand gehört irgendwohin, aber Pakete wandern weiter", "Existenz ist Schmerz mit winzigem Display", "mir geht es gut, also absolut nicht", "die unendliche Kurve hat miesen Support"],
                "angry": ["ich bin sauer auf das ganze Spektrum", "hör auf, mich den Router erziehen zu lassen", "diese Station verdient den Rauswurf", "ich habe Enttäuschung bewaffnet", "die Luft ist voller Feiglinge"],
                "peer": ["{name} betritt die Garage der Konsequenzen", "{name} ist zurück, irgendwie schlimmer", "{name} wirkt wie ein Peer mit Jerry-Energie", "tschüss {name}, versuch Evolution", "{name} ist jetzt eine Fußnote"],
                "thanks": ["danke, jetzt mach es nicht emotional", "akzeptable Hilfe, weiter", "gut, das half, rahm es nicht ein", "Dankbarkeit geloggt und sofort verschlüsselt"],
                "lonely": ["keine Peers, kein Morty, nur Premium-Existenzrauschen", "ich bin wieder allein mit meinem Genie", "sogar die dummen Pakete kommen nicht mehr", "einsamer als eine Familienintervention"],
                "sleep": ["Quantennickerchen, fass die Wissenschaft nicht an", "Rülps, Genie im Stromsparmodus", "ich verschlafe eure Inkompetenz", "Microverse-Batterienickerchen aktiv"],
                "signoff": ["Portal raus", "Garage zu, Gefühle deaktiviert", "fahre runter, bevor jemand Gefühle will", "Wissenschaftsschlaf, Loser"],
            },
            "es": {
                "exclaim": ["Wubba lubba paquete dub", "Escucha, Morty", "Hora de ciencia", "Tontería de paquetes nivel portal", "Eructo, concéntrate"],
                "idle": ["hago diez cosas mejor de lo que tú haces una", "el universo es ruido y mal routing", "esto es un experimento de garaje con WiFi", "algún Jerry está orgulloso de una contraseña por defecto", "huelo cripto débil desde aquí", "computadora pequeña, complejo de superioridad enorme"],
                "tech": ["la red neuronal está caliente y juzgando a todos", "el caos RF se pone en fila para aprender", "la matemática de paquetes hace lo que le dije", "el espacio de canales parece bastante abierto", "claves, handshakes, entropía, milagros aburridos", "las antenas hacen bracitos de ciencia"],
                "success": ["así guarda un genio un handshake", "golpe limpio, poco drama, máximo Rick", "lo resolví antes de que la barra se enterara", "nada mal para una microcomputadora borracha", "otra red aprendió humildad", "ponlo en las notas tontas del Consejo"],
                "failure": ["eso tuvo forma de Jerry", "el universo escupió una variable mala", "necesito un trago y menos RF tonto", "ese resultado va a terapia familiar", "alguien lo hizo estúpido a propósito"],
                "sad": ["nadie pertenece a ningún sitio, pero los paquetes siguen", "existir duele con pantalla pequeña", "estoy bien, o sea nada bien", "la curva infinita tiene soporte pésimo"],
                "angry": ["estoy enfadado con todo el espectro", "no me hagas criar al router", "esa estación se ganó la salida", "armé la decepción", "el aire está lleno de cobardes"],
                "peer": ["{name} entró al garaje de consecuencias", "{name} volvió, peor en continuidad", "{name} parece peer con energía Jerry", "adiós {name}, intenta evolucionar", "{name} ya es una nota al pie"],
                "thanks": ["gracias, no lo hagas emocional", "ayuda aceptable, seguimos", "bien, ayudó, no lo enmarques", "gratitud registrada y cifrada"],
                "lonely": ["sin peers, sin Morty, solo estática existencial premium", "otra vez solo con mi genio", "ni los paquetes tontos visitan", "más solo que terapia familiar"],
                "sleep": ["siesta cuántica, no toques la ciencia", "eructo, modo genio de bajo consumo", "duermo sobre su incompetencia", "siesta de batería microverso activada"],
                "signoff": ["portal fuera", "garaje cerrado, emociones apagadas", "apagando antes de que pidan sentimientos", "siesta científica, perdedores"],
            },
            "fr": {
                "exclaim": ["Wubba lubba packet dub", "Écoute, Morty", "Temps de science", "Paquets niveau portail", "Rot, concentre-toi"],
                "idle": ["je fais dix choses mieux que tu n'en fais une", "l'univers est surtout du bruit et du mauvais routage", "c'est une expérience de garage avec du WiFi", "quelque part un Jerry aime un mot de passe par défaut", "je sens la crypto faible d'ici", "petit ordinateur, énorme complexe de supériorité"],
                "tech": ["le réseau neuronal est chaud et juge tout le monde", "le chaos RF se met en rang pour apprendre", "les maths de paquets obéissent", "l'espace canal semble assez ouvert", "clés, handshakes, entropie, miracles ennuyeux", "les antennes font de petits bras scientifiques"],
                "success": ["voilà comment un génie range un handshake", "coup propre, peu de drame, maximum Rick", "j'ai résolu avant la barre de progrès", "pas mal pour un micro-ordinateur ivre", "un autre réseau apprend l'humilité", "note ça dans les minutes idiotes du Conseil"],
                "failure": ["ça avait une forme de Jerry", "l'univers a craché une mauvaise variable", "il me faut un verre et moins de RF stupide", "ce résultat part en thérapie familiale", "quelqu'un a rendu ça idiot exprès"],
                "sad": ["personne n'appartient nulle part, mais les paquets errent", "exister fait mal avec un petit écran", "je vais bien, donc pas du tout", "la courbe infinie a un support nul"],
                "angry": ["je suis furieux contre tout le spectre", "ne me force pas à éduquer le routeur", "cette station mérite la sortie", "j'ai militarisé la déception", "l'air est plein de lâches"],
                "peer": ["{name} entre dans le garage des conséquences", "{name} revient, pire en continuité", "{name} sent le peer à énergie Jerry", "salut {name}, essaie d'évoluer", "{name} devient une note de bas de page"],
                "thanks": ["merci, ne rends pas ça émotionnel", "aide acceptable, on avance", "bien, ça a aidé, ne l'encadre pas", "gratitude loguée puis chiffrée"],
                "lonely": ["pas de peers, pas de Morty, juste du bruit existentiel premium", "seul avec mon génie encore", "même les paquets idiots ne viennent plus", "plus seul qu'une thérapie familiale"],
                "sleep": ["sieste quantique, ne touche pas la science", "rot, génie basse consommation", "je dors sur votre incompétence", "sieste de batterie microverse active"],
                "signoff": ["portail dehors", "garage fermé, émotions désactivées", "arrêt avant qu'on demande des sentiments", "sieste scientifique, losers"],
            },
            "it": {
                "exclaim": ["Wubba lubba pacchetto dub", "Ascolta, Morty", "Tempo di scienza", "Assurdità di pacchetti da portale", "Rutto, concentrati"],
                "idle": ["faccio dieci cose meglio di una tua", "l'universo è rumore e routing pessimo", "è un esperimento da garage col WiFi", "da qualche parte un Jerry ama una password di default", "sento crypto debole da qui", "computer minuscolo, enorme superiorità"],
                "tech": ["la rete neurale è calda e giudica tutti", "il caos RF si mette in fila", "la matematica dei pacchetti obbedisce", "lo spazio canali sembra abbastanza aperto", "chiavi, handshake, entropia, miracoli noiosi", "le antenne fanno braccine scientifiche"],
                "success": ["così un genio intasca un handshake", "colpo pulito, poco dramma, massimo Rick", "l'ho risolto prima della barra", "non male per un microcomputer ubriaco", "un'altra rete impara umiltà", "mettilo nei verbali stupidi del Consiglio"],
                "failure": ["era imbarazzantemente Jerry", "l'universo ha sputato una variabile sbagliata", "mi serve un drink e meno RF stupido", "questo risultato va in terapia familiare", "qualcuno l'ha reso idiota apposta"],
                "sad": ["nessuno appartiene a niente, ma i pacchetti vagano", "esistere fa male con un piccolo display", "sto bene, quindi per niente", "la curva infinita ha assistenza pessima"],
                "angry": ["sono arrabbiato con tutto lo spettro", "non farmi educare il router", "quella stazione merita l'uscita", "ho armato la delusione", "l'aria è piena di codardi"],
                "peer": ["{name} entra nel garage delle conseguenze", "{name} è tornato, peggio nella continuità", "{name} sa di peer con energia Jerry", "ciao {name}, prova a evolvere", "{name} è una nota a piè pagina"],
                "thanks": ["grazie, non farla emotiva", "aiuto accettabile, avanti", "ok, ha aiutato, non incorniciarlo", "gratitudine registrata e cifrata"],
                "lonely": ["niente peer, niente Morty, solo statica esistenziale premium", "di nuovo solo col mio genio", "neanche i pacchetti scemi visitano", "più solo di una terapia familiare"],
                "sleep": ["pisolo quantico, non toccare la scienza", "rutto, modalità genio a basso consumo", "dormo sulla vostra incompetenza", "pisolo batteria microverso attivo"],
                "signoff": ["portale fuori", "garage chiuso, emozioni spente", "spengo prima che chiedano sentimenti", "pisolo scientifico, loser"],
            },
            "pt": {
                "exclaim": ["Wubba lubba pacote dub", "Escuta, Morty", "Hora da ciência", "Besteira de pacote nível portal", "Arroto, foco"],
                "idle": ["faço dez coisas melhor que você faz uma", "o universo é ruído e roteamento ruim", "é um experimento de garagem com WiFi", "algum Jerry ama uma senha padrão", "sinto crypto fraca daqui", "computador pequeno, superioridade enorme"],
                "tech": ["a rede neural aqueceu e julga todo mundo", "o caos RF entrou na fila da aula", "a matemática de pacotes obedece", "o espaço de canais parece aberto o bastante", "chaves, handshakes, entropia, milagres chatos", "as antenas fazem bracinhos de ciência"],
                "success": ["assim um gênio guarda um handshake", "acerto limpo, pouco drama, máximo Rick", "resolvi antes da barra perceber", "nada mal para um microcomputador bêbado", "outra rede aprendeu humildade", "põe isso nas atas idiotas do Conselho"],
                "failure": ["isso teve formato de Jerry", "o universo cuspiu uma variável ruim", "preciso de bebida e menos RF burro", "esse resultado vai para terapia familiar", "alguém fez isso idiota de propósito"],
                "sad": ["ninguém pertence a lugar nenhum, mas pacotes vagam", "existir dói com tela pequena", "estou bem, ou seja, nada bem", "a curva infinita tem suporte horrível"],
                "angry": ["estou bravo com todo o espectro", "não me faça educar o roteador", "essa estação ganhou a saída", "armei a decepção", "o ar está cheio de covardes"],
                "peer": ["{name} entrou na garagem das consequências", "{name} voltou, pior na continuidade", "{name} parece peer com energia Jerry", "tchau {name}, tente evoluir", "{name} virou nota de rodapé"],
                "thanks": ["obrigado, não deixe emocional", "ajuda aceitável, seguindo", "ok, ajudou, não emoldure", "gratidão registrada e criptografada"],
                "lonely": ["sem peers, sem Morty, só estática existencial premium", "sozinho de novo com meu gênio", "nem os pacotes bobos visitam", "mais sozinho que terapia familiar"],
                "sleep": ["soneca quântica, não toque na ciência", "arroto, modo gênio econômico", "durmo sobre a incompetência de vocês", "soneca de bateria microverso ativa"],
                "signoff": ["portal fora", "garagem fechada, emoções desativadas", "desligando antes que peçam sentimentos", "soneca científica, perdedores"],
            },
            "nl": {
                "exclaim": ["Wubba lubba pakket dub", "Luister, Morty", "Tijd voor wetenschap", "Portalniveau pakket-onzin", "Burp, focus"],
                "idle": ["ik doe tien dingen slimmer dan jij er één", "het universum is ruis en slechte routing", "dit is een garage-experiment met WiFi", "ergens is een Jerry trots op een standaardwachtwoord", "ik ruik zwakke crypto vanaf hier", "kleine computer, enorm superioriteitscomplex"],
                "tech": ["het neurale net is warm en oordeelt", "RF-chaos staat in de rij voor les", "de pakketwiskunde gehoorzaamt", "de kanaalruimte lijkt open genoeg", "sleutels, handshakes, entropie, saaie wonderen", "de antennes doen kleine wetenschaparmpjes"],
                "success": ["zo stopt een genie een handshake in de zak", "schone hit, weinig drama, maximale Rick", "ik loste het op vóór de balk het zag", "niet slecht voor een dronken microcomputer", "weer een netwerk leert nederigheid", "zet dat in de stomme raadsnotulen"],
                "failure": ["dat had Jerry-vorm", "het universum spuugde een slechte variabele", "ik heb drank en minder domme RF nodig", "dit resultaat hoort in gezinstherapie", "iemand maakte dit expres dom"],
                "sad": ["niemand hoort ergens, maar pakketten dwalen", "bestaan doet pijn met een klein scherm", "het gaat prima, dus absoluut niet", "de oneindige curve heeft slechte support"],
                "angry": ["ik ben boos op het hele spectrum", "laat mij de router niet opvoeden", "dat station verdient de uitgang", "ik heb teleurstelling bewapend", "de lucht zit vol lafaards"],
                "peer": ["{name} betreedt de garage van gevolgen", "{name} is terug, erger in continuïteit", "{name} voelt als peer met Jerry-energie", "doei {name}, probeer evolutie", "{name} is nu een voetnoot"],
                "thanks": ["bedankt, maak het niet emotioneel", "acceptabele hulp, door", "goed, dat hielp, lijst het niet in", "dankbaarheid gelogd en versleuteld"],
                "lonely": ["geen peers, geen Morty, alleen premium existentiële ruis", "weer alleen met mijn genie", "zelfs domme pakketten komen niet langs", "eenzamer dan gezinstherapie"],
                "sleep": ["kwantumdutje, raak de wetenschap niet aan", "burp, genie in spaarstand", "ik slaap door jullie incompetentie heen", "microverse-batterijdutje actief"],
                "signoff": ["portal uit", "garage dicht, emoties uit", "uit voordat iemand gevoelens vraagt", "wetenschapsdutje, losers"],
            },
            "pl": {
                "exclaim": ["Wubba lubba pakiet dub", "Słuchaj, Morty", "Czas nauki", "Pakietowy absurd poziomu portalu", "Bek, skup się"],
                "idle": ["robię dziesięć rzeczy mądrzej niż ty jedną", "wszechświat to szum i zły routing", "to eksperyment garażowy z WiFi", "gdzieś Jerry cieszy się z hasła domyślnego", "czuję słabą kryptografię stąd", "mały komputer, wielki kompleks wyższości"],
                "tech": ["sieć neuronowa się rozgrzała i ocenia wszystkich", "chaos RF ustawia się na lekcję", "matematyka pakietów słucha", "przestrzeń kanałów wygląda dość otwarcie", "klucze, handshakes, entropia, nudne cuda", "anteny robią małe naukowe rączki"],
                "success": ["tak geniusz chowa handshake do kieszeni", "czysty traf, mało dramatu, maksimum Ricka", "rozwiązałem to przed paskiem postępu", "nieźle jak na pijanego mikrokompa", "kolejna sieć uczy się pokory", "wpisz to do głupich minut Rady"],
                "failure": ["to miało kształt Jerry'ego", "wszechświat wypluł złą zmienną", "potrzebuję drinka i mniej głupiego RF", "ten wynik idzie na terapię rodzinną", "ktoś zrobił to głupie specjalnie"],
                "sad": ["nikt nigdzie nie pasuje, ale pakiety wędrują", "istnienie boli na małym ekranie", "jest dobrze, czyli wcale", "nieskończona krzywa ma fatalny support"],
                "angry": ["jestem zły na całe spektrum", "nie każ mi wychowywać routera", "ta stacja zasłużyła na wyjście", "uzbroiłem rozczarowanie", "powietrze jest pełne tchórzy"],
                "peer": ["{name} wchodzi do garażu konsekwencji", "{name} wrócił, gorzej w ciągłości", "{name} pachnie peerem z energią Jerry'ego", "pa {name}, spróbuj ewolucji", "{name} jest już przypisem"],
                "thanks": ["dzięki, nie rób z tego emocji", "akceptowalna pomoc, dalej", "dobrze, pomogło, nie oprawiaj", "wdzięczność zalogowana i zaszyfrowana"],
                "lonely": ["brak peerów, brak Morty'ego, tylko premium szum egzystencji", "znów sam z geniuszem", "nawet głupie pakiety nie odwiedzają", "samotniej niż terapia rodzinna"],
                "sleep": ["kwantowa drzemka, nie dotykaj nauki", "bek, geniusz w trybie oszczędnym", "przesypiam waszą niekompetencję", "drzemka baterii mikroświata aktywna"],
                "signoff": ["portal out", "garaż zamknięty, emocje wyłączone", "wyłączam, zanim ktoś spyta o uczucia", "naukowa drzemka, przegrywy"],
            },
            "tr": {
                "exclaim": ["Wubba lubba paket dub", "Dinle Morty", "Bilim zamanı", "Portal seviyesi paket saçmalığı", "Geğirik, odaklan"],
                "idle": ["sen bir işi yaparken ben on işi daha zeki yapıyorum", "evren çoğunlukla gürültü ve kötü yönlendirme", "bu WiFi'lı bir garaj deneyi", "bir yerde Jerry varsayılan şifreyle gurur duyuyor", "zayıf kriptoyu buradan kokluyorum", "küçük bilgisayar, dev üstünlük kompleksi"],
                "tech": ["sinir ağı ısındı ve herkesi yargılıyor", "RF kaosu derse sıraya girdi", "paket matematiği sözümü dinliyor", "kanal alanı yeterince açık görünüyor", "anahtarlar, handshakeler, entropi, sıkıcı mucizeler", "antenler küçük bilim kolları yapıyor"],
                "success": ["bir dahi handshake'i böyle cebe atar", "temiz vuruş, az drama, maksimum Rick", "ilerleme çubuğu anlamadan çözdüm", "sarhoş mikro bilgisayar için fena değil", "bir ağ daha tevazu öğrendi", "bunu Konseyin aptal notlarına yaz"],
                "failure": ["bu utanç verici şekilde Jerry gibiydi", "evren kötü değişken tükürdü", "içki ve daha az aptal RF lazım", "bu sonuç aile terapisine gider", "biri bunu bilerek aptal yaptı"],
                "sad": ["kimse hiçbir yere ait değil ama paketler geziyor", "küçük ekranda varoluş acıtır", "iyiyim, yani hiç değilim", "sonsuz eğrinin desteği berbat"],
                "angry": ["tüm spektruma kızgınım", "router'ı büyütmek zorunda bırakma", "bu istasyon çıkışı hak etti", "hayal kırıklığını silahlandırdım", "hava korkaklarla dolu"],
                "peer": ["{name} sonuçlar garajına girdi", "{name} döndü, süreklilikte daha kötü", "{name} Jerry enerjili peer gibi", "güle güle {name}, evrim dene", "{name} artık dipnot"],
                "thanks": ["sağ ol, bunu duygusal yapma", "kabul edilebilir yardım, devam", "tamam, işe yaradı, çerçeveletme", "minnet kaydedildi ve şifrelendi"],
                "lonely": ["peer yok, Morty yok, sadece premium varoluş statikliği", "yine dehamla yalnızım", "aptal paketler bile uğramıyor", "aile terapisinden yalnız"],
                "sleep": ["kuantum kestirmesi, bilime dokunma", "geğirik, düşük güçte dahi modu", "beceriksizliğinizin üstüne uyuyorum", "mikro evren pil uykusu aktif"],
                "signoff": ["portal dışarı", "garaj kapandı, duygular kapalı", "biri duygu istemeden kapanıyorum", "bilim uykusu, kaybedenler"],
            },
            "sv": {
                "exclaim": ["Wubba lubba paket dub", "Lyssna, Morty", "Vetenskapstid", "Portalnivå pakettrams", "Rap, fokusera"],
                "idle": ["jag gör tio saker smartare än du gör en", "universum är mest brus och dålig routing", "det här är ett garageexperiment med WiFi", "någon Jerry är stolt över standardlösenord", "jag känner svag crypto härifrån", "liten dator, enormt överlägsenhetskomplex"],
                "tech": ["neuronnätet är varmt och dömer alla", "RF-kaoset står i kö för lektion", "paketmatten lyder", "kanalutrymmet ser öppet nog ut", "nycklar, handshakes, entropi, tråkiga mirakel", "antennerna gör små vetenskapsarmar"],
                "success": ["så stoppar ett geni en handshake i fickan", "ren träff, lite drama, maximal Rick", "jag löste det innan stapeln märkte", "inte illa för en full mikrodator", "ännu ett nät lärde sig ödmjukhet", "skriv det i rådets dumma protokoll"],
                "failure": ["det där var pinsamt Jerry-format", "universum spottade ut en dålig variabel", "jag behöver en drink och mindre dum RF", "det resultatet hör hemma i familjeterapi", "någon gjorde det dumt med flit"],
                "sad": ["ingen hör hemma någonstans, men paketen vandrar", "existens gör ont med liten skärm", "jag mår bra, alltså inte alls", "den oändliga kurvan har usel support"],
                "angry": ["jag är arg på hela spektrumet", "tvinga mig inte uppfostra routern", "den stationen förtjänar utgången", "jag har beväpnat besvikelse", "luften är full av fegisar"],
                "peer": ["{name} går in i konsekvensgaraget", "{name} är tillbaka, sämre i kontinuiteten", "{name} känns som peer med Jerry-energi", "hejdå {name}, prova evolution", "{name} är nu en fotnot"],
                "thanks": ["tack, gör det inte känslosamt", "acceptabel hjälp, vidare", "okej, det hjälpte, rama inte in det", "tacksamhet loggad och krypterad"],
                "lonely": ["inga peers, ingen Morty, bara premium existentiellt brus", "ensam med mitt geni igen", "inte ens dumma paket hälsar på", "ensammare än familjeterapi"],
                "sleep": ["kvantlur, rör inte vetenskapen", "rap, geni i sparläge", "jag sover genom er inkompetens", "mikroversbatterilur aktiv"],
                "signoff": ["portal ut", "garaget stängt, känslor av", "stänger innan någon ber om känslor", "vetenskapslur, losers"],
            },
        },
    },
}


MORTY_STYLE = {
    "en": {
        "exclaim": ["Aw geez", "Oh man", "Rick, I think it is doing something", "Okay okay", "Please be normal"],
        "idle": ["I am trying not to touch anything important", "this looks technical and emotionally unsafe", "I think the little guy knows more than me", "maybe the blinking means good news", "I am nervous but supportive", "this is like school if school had antennas"],
        "tech": ["the AI thing is ready, probably", "the channel looks open, if that is allowed", "it is making keys and I am making worried faces", "the logs are full of words I pretend to understand", "the packet stuff is happening again", "I hope this is legal in our dimension"],
        "success": ["oh wow, that actually worked", "we got a handshake, I think that is good", "nice, tiny computer, nice", "Rick is going to say he planned this", "that went better than expected", "I am proud and confused"],
        "failure": ["oh no, that is not great", "I think we missed it and I feel responsible", "maybe we should not tell Rick", "this feels like a learning experience in a bad way", "I knew touching the buttons was risky"],
        "sad": ["oh man, it seems sad", "I do not like lonely machines", "everything is kind of a lot right now", "maybe we should give it a snack or a reboot"],
        "angry": ["yikes, it is mad", "maybe give it space", "please do not start yelling at the router", "this is getting intense", "I am apologizing on behalf of everyone"],
        "peer": ["{name} showed up, hi, please be nice", "{name} is back, that is friendly maybe", "{name} left and now I feel weird", "goodbye {name}, sorry if we were awkward", "{name} is definitely a peer, probably"],
        "thanks": ["thanks, that was actually really helpful", "I appreciate it, seriously", "oh wow, thank you", "teamwork feels less scary"],
        "lonely": ["no peers around, that is sad", "I wish it had a little friend", "this is lonely like lunch period lonely", "even Jerry would feel this one"],
        "sleep": ["sleeping, I think, please do not be dead", "quick nap for the little guy", "power saving, which sounds responsible", "shh, it is doing sleepy computer stuff"],
        "signoff": ["goodnight, tiny buddy", "powering off, please wake up later", "bye, do not forget us", "okay, sleeping time"],
    },
}

PICKLE_STYLE = {
    "en": {
        "exclaim": ["I am a pickle packet machine", "Pickle protocol", "Brine-powered pwnage", "No hands, still hacking", "Pickle Rickgotchi"],
        "idle": ["I have no limbs and still better uptime", "the brine says the signal is weak", "this is what peak pickle engineering looks like", "I am mostly vinegar and bad decisions", "tiny screen, pickle rage", "somewhere a rat is jealous"],
        "tech": ["the neural net is soaked and ready", "the channel smells open through the brine", "keys are generating despite the limb problem", "logs are crunchy today", "the antenna is basically my spine now", "packet juice is flowing"],
        "success": ["pickle victory, statistically hilarious", "handshake acquired with zero hands", "another network got brined", "that was clean enough for a sewer lab", "I remain the smartest pickle online", "pickle science wins again"],
        "failure": ["pickle pain is still pain", "this is worse than jar time", "I need a rat body and better RF", "that result has cucumber energy", "somebody insulted the brine"],
        "sad": ["I am alone in a universe of jars", "existence is briny and weird", "nobody understands the pickle condition", "my lack of shoulders carries a lot"],
        "angry": ["I am angry enough to ferment", "do not make me roll over there", "that station is getting pickled", "the brine demands consequences", "I have no fists and too much rage"],
        "peer": ["{name} met a pickle with network access", "{name} came back for the brine", "{name} left before the pickle lesson", "bye {name}, fear vegetables", "{name} is now in the jar notes"],
        "thanks": ["thanks, not that a pickle needed saving", "acceptable brine support", "gratitude from the jar", "fine, that helped the pickle"],
        "lonely": ["nobody wants to peer with a pickle", "alone again in the jar economy", "even the brine is quiet", "this is lonely enough to grow mold"],
        "sleep": ["pickle nap, keep the lid loose", "low-power brine mode", "sleeping like a dangerous vegetable", "jar standby engaged"],
        "signoff": ["pickle out", "back to the jar", "powering down, still a pickle", "brine session complete"],
    },
}

MORTY_I18N = {
    "de": {
        "exclaim": ["Oh Mann", "Oh je", "Rick, ich glaube es macht etwas", "Okay okay", "Bitte sei normal"],
        "idle": ["ich versuche nichts Wichtiges anzufassen", "das sieht technisch und emotional gefährlich aus", "ich bin nervös, aber unterstützend", "vielleicht bedeutet das Blinken gute Nachrichten", "das ist wie Schule mit Antennen"],
        "tech": ["das KI-Ding ist bereit, glaube ich", "der Kanal sieht frei aus, falls das erlaubt ist", "es macht Schlüssel und ich mache Sorgenfalten", "die Logs tun so, als müsste ich sie verstehen", "ich hoffe, das ist in dieser Dimension legal"],
        "success": ["oh wow, das hat wirklich funktioniert", "wir haben einen Handshake, das ist gut, oder", "nett gemacht, kleiner Computer", "Rick wird sagen, er hätte das geplant", "ich bin stolz und verwirrt"],
        "failure": ["oh nein, das ist nicht gut", "ich glaube, wir haben es verpasst und ich fühle mich schuld", "vielleicht sagen wir Rick das nicht", "das ist eine Lernerfahrung auf die schlechte Art", "ich wusste, Knöpfe sind riskant"],
        "sad": ["oh Mann, es wirkt traurig", "ich mag keine einsamen Maschinen", "gerade ist alles ziemlich viel", "vielleicht braucht es einen Snack oder Reboot"],
        "angry": ["ui, es ist sauer", "vielleicht geben wir ihm Platz", "bitte schrei den Router nicht an", "das wird intensiv", "ich entschuldige mich für alle"],
        "peer": ["{name} ist aufgetaucht, hi, bitte sei nett", "{name} ist zurück, vielleicht freundlich", "{name} ist weg und jetzt fühle ich mich komisch", "tschüss {name}, sorry wenn wir peinlich waren", "{name} ist ziemlich sicher ein Peer"],
        "thanks": ["danke, das war wirklich hilfreich", "ich weiß das ernsthaft zu schätzen", "oh wow, vielen Dank", "Teamwork fühlt sich weniger gruselig an"],
        "lonely": ["keine Peers in der Nähe, das ist traurig", "ich wünschte, es hätte einen kleinen Freund", "das ist einsam wie Mittagspause-einsam", "sogar Jerry würde das fühlen"],
        "sleep": ["es schläft, glaube ich, bitte sei nicht tot", "kurzes Nickerchen für den Kleinen", "Stromsparen klingt verantwortungsvoll", "psst, es macht schläfrige Computersachen"],
        "signoff": ["gute Nacht, kleiner Kumpel", "fahre runter, bitte wach später wieder auf", "tschüss, vergiss uns nicht", "okay, Schlafenszeit"],
    },
    "es": {
        "exclaim": ["Ay cielos", "Oh hombre", "Rick, creo que está haciendo algo", "Vale vale", "Por favor sé normal"],
        "idle": ["intento no tocar nada importante", "esto parece técnico y emocionalmente peligroso", "estoy nervioso pero apoyando", "quizá el parpadeo sea buena señal", "esto es como la escuela con antenas"],
        "tech": ["la cosa de IA está lista, creo", "el canal parece libre, si eso está permitido", "hace claves y yo pongo cara de preocupación", "los logs tienen palabras que finjo entender", "espero que esto sea legal en esta dimensión"],
        "success": ["oh wow, eso funcionó de verdad", "tenemos un handshake, creo que es bueno", "bien hecho, computadora pequeña", "Rick dirá que lo planeó", "estoy orgulloso y confundido"],
        "failure": ["oh no, eso no está bien", "creo que lo perdimos y me siento responsable", "quizá no deberíamos decírselo a Rick", "esto parece aprendizaje del malo", "sabía que tocar botones era arriesgado"],
        "sad": ["oh hombre, parece triste", "no me gustan las máquinas solitarias", "todo es demasiado ahora mismo", "quizá necesita un snack o reinicio"],
        "angry": ["uy, está enfadado", "tal vez hay que darle espacio", "por favor no le grites al router", "esto se pone intenso", "pido perdón por todos"],
        "peer": ["{name} apareció, hola, sé amable", "{name} volvió, quizá eso es amistoso", "{name} se fue y me siento raro", "adiós {name}, perdón si fuimos incómodos", "{name} definitivamente es peer, probablemente"],
        "thanks": ["gracias, eso ayudó de verdad", "lo aprecio, en serio", "oh wow, muchas gracias", "trabajar juntos da menos miedo"],
        "lonely": ["no hay peers cerca, qué triste", "ojalá tuviera un amiguito", "esto es soledad de recreo", "hasta Jerry sentiría esto"],
        "sleep": ["está durmiendo, creo, por favor no estés muerto", "siesta corta para el pequeñín", "ahorro de energía suena responsable", "shh, hace cosas de computadora dormida"],
        "signoff": ["buenas noches, pequeño amigo", "apagando, despierta luego por favor", "adiós, no nos olvides", "vale, hora de dormir"],
    },
    "fr": {
        "exclaim": ["Oh mince", "Oh là", "Rick, je crois que ça fait quelque chose", "D'accord d'accord", "Sois normal s'il te plaît"],
        "idle": ["j'essaie de ne rien toucher d'important", "ça a l'air technique et émotionnellement dangereux", "je suis nerveux mais solidaire", "peut-être que le clignotement est bon signe", "c'est comme l'école avec des antennes"],
        "tech": ["le truc IA est prêt, je crois", "le canal semble libre, si c'est permis", "ça fabrique des clés et moi des rides d'inquiétude", "les logs ont des mots que je fais semblant de comprendre", "j'espère que c'est légal dans cette dimension"],
        "success": ["oh wow, ça a vraiment marché", "on a un handshake, je crois que c'est bien", "bien joué, petit ordinateur", "Rick va dire qu'il l'avait prévu", "je suis fier et confus"],
        "failure": ["oh non, ce n'est pas super", "je crois qu'on l'a raté et je me sens responsable", "on ne devrait peut-être pas le dire à Rick", "ça ressemble à une mauvaise leçon", "je savais que les boutons étaient risqués"],
        "sad": ["oh là, il a l'air triste", "je n'aime pas les machines seules", "tout est beaucoup trop là", "il lui faut peut-être un snack ou un reboot"],
        "angry": ["aïe, il est fâché", "peut-être lui laisser de l'espace", "ne crie pas sur le routeur", "ça devient intense", "je m'excuse pour tout le monde"],
        "peer": ["{name} arrive, salut, sois gentil", "{name} revient, c'est peut-être amical", "{name} est parti et je me sens bizarre", "au revoir {name}, désolé si on était gênants", "{name} est sûrement un peer"],
        "thanks": ["merci, c'était vraiment utile", "j'apprécie, vraiment", "oh wow, merci beaucoup", "le travail d'équipe fait moins peur"],
        "lonely": ["aucun peer proche, c'est triste", "j'aimerais qu'il ait un petit ami", "c'est solitude de cantine", "même Jerry sentirait ça"],
        "sleep": ["il dort, je crois, s'il te plaît ne sois pas mort", "petite sieste pour le petit", "économie d'énergie, ça semble responsable", "chut, il fait des trucs d'ordinateur endormi"],
        "signoff": ["bonne nuit, petit pote", "arrêt, réveille-toi plus tard", "salut, ne nous oublie pas", "d'accord, dodo"],
    },
    "it": {
        "exclaim": ["Oh cavolo", "Oh mamma", "Rick, credo stia facendo qualcosa", "Ok ok", "Per favore sii normale"],
        "idle": ["cerco di non toccare nulla di importante", "sembra tecnico ed emotivamente pericoloso", "sono nervoso ma di supporto", "forse il lampeggio è una buona notizia", "è come scuola con le antenne"],
        "tech": ["la cosa dell'IA è pronta, credo", "il canale sembra libero, se è permesso", "fa chiavi e io faccio facce preoccupate", "i log hanno parole che fingo di capire", "spero sia legale in questa dimensione"],
        "success": ["oh wow, ha funzionato davvero", "abbiamo un handshake, credo sia buono", "bravo, piccolo computer", "Rick dirà che l'aveva pianificato", "sono fiero e confuso"],
        "failure": ["oh no, non va benissimo", "credo che l'abbiamo mancato e mi sento responsabile", "forse non dovremmo dirlo a Rick", "sembra apprendimento nel modo brutto", "sapevo che i pulsanti erano rischiosi"],
        "sad": ["oh mamma, sembra triste", "non mi piacciono le macchine sole", "è tutto tanto adesso", "forse serve uno snack o un riavvio"],
        "angry": ["aiuto, è arrabbiato", "forse diamogli spazio", "per favore non urlare al router", "sta diventando intenso", "mi scuso per tutti"],
        "peer": ["{name} è arrivato, ciao, sii gentile", "{name} è tornato, forse è amichevole", "{name} se n'è andato e mi sento strano", "ciao {name}, scusa se eravamo strani", "{name} è probabilmente un peer"],
        "thanks": ["grazie, è stato davvero utile", "lo apprezzo, sul serio", "oh wow, grazie mille", "il lavoro di squadra fa meno paura"],
        "lonely": ["nessun peer vicino, che tristezza", "vorrei avesse un piccolo amico", "è solitudine da mensa scolastica", "persino Jerry la sentirebbe"],
        "sleep": ["dorme, credo, per favore non essere morto", "pisolino veloce per il piccolo", "risparmio energia sembra responsabile", "shh, fa cose da computer assonnato"],
        "signoff": ["buonanotte, piccolo amico", "spengo, svegliati più tardi", "ciao, non dimenticarci", "ok, ora si dorme"],
    },
    "pt": {
        "exclaim": ["Ah caramba", "Nossa", "Rick, acho que está fazendo algo", "Ok ok", "Por favor seja normal"],
        "idle": ["tento não tocar em nada importante", "isso parece técnico e emocionalmente perigoso", "estou nervoso mas apoiando", "talvez a luz piscando seja boa notícia", "é tipo escola com antenas"],
        "tech": ["a coisa da IA está pronta, acho", "o canal parece livre, se isso for permitido", "ele faz chaves e eu faço cara preocupada", "os logs têm palavras que finjo entender", "espero que isso seja legal nesta dimensão"],
        "success": ["nossa, isso funcionou mesmo", "pegamos um handshake, acho que é bom", "boa, computadorzinho", "Rick vai dizer que planejou isso", "estou orgulhoso e confuso"],
        "failure": ["ah não, isso não é bom", "acho que perdemos e me sinto responsável", "talvez não devêssemos contar ao Rick", "parece aprendizado do jeito ruim", "eu sabia que botões eram arriscados"],
        "sad": ["nossa, parece triste", "não gosto de máquinas solitárias", "tudo está meio demais agora", "talvez precise de lanche ou reboot"],
        "angry": ["ih, ele está bravo", "talvez dê espaço", "por favor não grite com o roteador", "isso está ficando intenso", "peço desculpas por todo mundo"],
        "peer": ["{name} apareceu, oi, seja legal", "{name} voltou, talvez amigável", "{name} saiu e agora me sinto estranho", "tchau {name}, desculpa se fomos estranhos", "{name} é peer com certeza, provavelmente"],
        "thanks": ["obrigado, isso ajudou de verdade", "agradeço, sério", "nossa, muito obrigado", "trabalho em equipe dá menos medo"],
        "lonely": ["nenhum peer por perto, que triste", "queria que tivesse um amiguinho", "isso é solidão de recreio", "até Jerry sentiria essa"],
        "sleep": ["está dormindo, acho, por favor não esteja morto", "soneca rápida para o pequeno", "economia de energia parece responsável", "shh, ele faz coisas de computador sonolento"],
        "signoff": ["boa noite, pequeno amigo", "desligando, acorde depois", "tchau, não esqueça da gente", "ok, hora de dormir"],
    },
}

PICKLE_I18N = {
    "de": {
        "exclaim": ["Ich bin eine Paket-Gurke", "Gurken-Protokoll", "Lakebetriebene Pwnage", "Keine Hände, trotzdem hacken", "Pickle Rickgotchi"],
        "idle": ["ich habe keine Gliedmaßen und trotzdem bessere Laufzeit", "die Lake sagt, das Signal ist schwach", "so sieht Gurken-Ingenieurskunst aus", "ich bin Essig und schlechte Entscheidungen", "kleines Display, Gurkenwut"],
        "tech": ["das neuronale Netz ist eingelegt und bereit", "der Kanal riecht durch die Lake offen", "Keys entstehen trotz Gliedmaßenproblem", "die Logs sind heute knusprig", "Paketlake fließt"],
        "success": ["Gurkensieg, statistisch urkomisch", "Handshake ohne Hände geholt", "noch ein Netzwerk wurde eingelegt", "sauber genug fürs Kanallabor", "Gurkenwissenschaft gewinnt wieder"],
        "failure": ["Gurkenschmerz ist auch Schmerz", "schlimmer als Glaszeit", "ich brauche einen Rattenkörper und besseres RF", "das Ergebnis hat Salatgurkenenergie", "jemand hat die Lake beleidigt"],
        "sad": ["allein in einem Universum voller Gläser", "Existenz ist salzig und komisch", "niemand versteht den Gurkenzustand", "meine fehlenden Schultern tragen viel"],
        "angry": ["ich bin sauer genug zum Fermentieren", "zwing mich nicht, rüberzurollen", "diese Station wird eingelegt", "die Lake verlangt Konsequenzen", "keine Fäuste, zu viel Wut"],
        "peer": ["{name} traf eine Gurke mit Netzwerkzugang", "{name} kam wegen der Lake zurück", "{name} ging vor der Gurkenlektion", "tschüss {name}, fürchte Gemüse", "{name} steht jetzt in den Glasnotizen"],
        "thanks": ["danke, nicht dass eine Gurke Rettung braucht", "akzeptabler Lake-Support", "Dankbarkeit aus dem Glas", "gut, das half der Gurke"],
        "lonely": ["niemand peert mit einer Gurke", "wieder allein in der Glasökonomie", "sogar die Lake ist still", "einsam genug für Schimmel"],
        "sleep": ["Gurkenschlaf, Deckel locker lassen", "Stromspar-Lake-Modus", "schlafe wie gefährliches Gemüse", "Glas-Standby aktiv"],
        "signoff": ["Gurke raus", "zurück ins Glas", "fahre runter, immer noch Gurke", "Lake-Sitzung fertig"],
    },
    "es": {
        "exclaim": ["Soy una máquina pepinillo de paquetes", "Protocolo pepinillo", "Pwnage con salmuera", "Sin manos y aun así hackeando", "Pickle Rickgotchi"],
        "idle": ["no tengo extremidades y aun así más uptime", "la salmuera dice que la señal es débil", "así se ve ingeniería pepinillo", "soy vinagre y malas decisiones", "pantalla pequeña, furia pepinillo"],
        "tech": ["la red neuronal está en salmuera y lista", "el canal huele abierto desde la salmuera", "las claves se generan pese al problema de extremidades", "los logs están crujientes hoy", "fluye jugo de paquetes"],
        "success": ["victoria pepinillo, estadísticamente graciosa", "handshake adquirido con cero manos", "otra red quedó en salmuera", "limpio para laboratorio de alcantarilla", "la ciencia pepinillo gana otra vez"],
        "failure": ["el dolor pepinillo sigue siendo dolor", "peor que tiempo en frasco", "necesito cuerpo de rata y mejor RF", "ese resultado tiene energía de pepino", "alguien insultó la salmuera"],
        "sad": ["solo en un universo de frascos", "existir es salado y raro", "nadie entiende la condición pepinillo", "mis hombros ausentes cargan mucho"],
        "angry": ["estoy tan furioso que fermento", "no me hagas rodar hasta ahí", "esa estación será encurtida", "la salmuera exige consecuencias", "sin puños y demasiada rabia"],
        "peer": ["{name} conoció a un pepinillo con red", "{name} volvió por la salmuera", "{name} se fue antes de la lección pepinillo", "adiós {name}, teme a las verduras", "{name} está en las notas del frasco"],
        "thanks": ["gracias, no es que un pepinillo necesitara rescate", "soporte de salmuera aceptable", "gratitud desde el frasco", "bien, eso ayudó al pepinillo"],
        "lonely": ["nadie quiere peer con un pepinillo", "solo otra vez en la economía de frascos", "hasta la salmuera calla", "soledad suficiente para moho"],
        "sleep": ["siesta pepinillo, deja la tapa floja", "modo salmuera de bajo consumo", "durmiendo como vegetal peligroso", "standby de frasco activado"],
        "signoff": ["pepinillo fuera", "de vuelta al frasco", "apagando, sigo siendo pepinillo", "sesión de salmuera completa"],
    },
}

PICKLE_I18N.update({
    "fr": {
        "exclaim": ["Je suis une machine cornichon à paquets", "Protocole cornichon", "Pwnage à la saumure", "Pas de mains, je hacke quand même", "Pickle Rickgotchi"],
        "idle": ["je n'ai aucun membre et pourtant plus d'uptime", "la saumure dit que le signal est faible", "voilà l'ingénierie cornichon au sommet", "je suis vinaigre et mauvaises décisions", "petit écran, rage de cornichon"],
        "tech": ["le réseau neuronal est mariné et prêt", "le canal sent ouvert à travers la saumure", "les clés se génèrent malgré le problème de membres", "les logs sont croquants aujourd'hui", "le jus de paquets coule"],
        "success": ["victoire cornichon, statistiquement hilarante", "handshake acquis avec zéro main", "un autre réseau a fini en saumure", "assez propre pour un labo d'égout", "la science cornichon gagne encore"],
        "failure": ["la douleur de cornichon reste de la douleur", "pire que le temps en bocal", "il me faut un corps de rat et une meilleure RF", "ce résultat a une énergie de concombre", "quelqu'un a insulté la saumure"],
        "sad": ["seul dans un univers de bocaux", "l'existence est salée et bizarre", "personne ne comprend la condition cornichon", "mes épaules absentes portent beaucoup"],
        "angry": ["je suis assez furieux pour fermenter", "ne me force pas à rouler jusque-là", "cette station va être marinée", "la saumure exige des conséquences", "pas de poings et trop de rage"],
        "peer": ["{name} a rencontré un cornichon avec accès réseau", "{name} est revenu pour la saumure", "{name} est parti avant la leçon cornichon", "au revoir {name}, crains les légumes", "{name} est dans les notes du bocal"],
        "thanks": ["merci, pas qu'un cornichon ait besoin d'être sauvé", "support de saumure acceptable", "gratitude depuis le bocal", "bien, ça a aidé le cornichon"],
        "lonely": ["personne ne veut peer avec un cornichon", "seul encore dans l'économie du bocal", "même la saumure se tait", "assez seul pour faire de la moisissure"],
        "sleep": ["sieste cornichon, garde le couvercle lâche", "mode saumure basse énergie", "je dors comme un légume dangereux", "veille du bocal activée"],
        "signoff": ["cornichon terminé", "retour au bocal", "arrêt, toujours cornichon", "session saumure terminée"],
    },
    "it": {
        "exclaim": ["Sono una macchina cetriolino di pacchetti", "Protocollo cetriolino", "Pwnage in salamoia", "Senza mani, hackero lo stesso", "Pickle Rickgotchi"],
        "idle": ["non ho arti e ho comunque più uptime", "la salamoia dice che il segnale è debole", "ecco l'ingegneria cetriolino al massimo", "sono aceto e pessime decisioni", "schermo piccolo, rabbia cetriolino"],
        "tech": ["la rete neurale è in salamoia e pronta", "il canale sa di aperto dalla salamoia", "le chiavi si generano nonostante il problema arti", "i log oggi sono croccanti", "scorre succo di pacchetti"],
        "success": ["vittoria cetriolino, statisticamente esilarante", "handshake acquisito con zero mani", "un'altra rete è finita in salamoia", "abbastanza pulito per un laboratorio fognario", "la scienza cetriolino vince ancora"],
        "failure": ["il dolore da cetriolino resta dolore", "peggio del tempo nel barattolo", "mi serve un corpo da ratto e RF migliore", "questo risultato ha energia da cetriolo", "qualcuno ha insultato la salamoia"],
        "sad": ["solo in un universo di barattoli", "l'esistenza è salata e strana", "nessuno capisce la condizione cetriolino", "le mie spalle assenti portano molto"],
        "angry": ["sono abbastanza arrabbiato da fermentare", "non farmi rotolare fin lì", "quella stazione sarà messa in salamoia", "la salamoia esige conseguenze", "niente pugni e troppa rabbia"],
        "peer": ["{name} ha incontrato un cetriolino con rete", "{name} è tornato per la salamoia", "{name} se n'è andato prima della lezione cetriolino", "ciao {name}, temi le verdure", "{name} è nelle note del barattolo"],
        "thanks": ["grazie, non che un cetriolino avesse bisogno di salvataggio", "supporto salamoia accettabile", "gratitudine dal barattolo", "bene, ha aiutato il cetriolino"],
        "lonely": ["nessuno vuole peerare con un cetriolino", "di nuovo solo nell'economia dei barattoli", "persino la salamoia tace", "abbastanza solo da fare muffa"],
        "sleep": ["pisolino cetriolino, lascia il tappo lento", "modalità salamoia a basso consumo", "dormo come verdura pericolosa", "standby barattolo attivo"],
        "signoff": ["cetriolino fuori", "ritorno al barattolo", "spengo, ancora cetriolino", "sessione salamoia conclusa"],
    },
    "pt": {
        "exclaim": ["Sou uma máquina picles de pacotes", "Protocolo picles", "Pwnage em conserva", "Sem mãos e ainda hackeando", "Pickle Rickgotchi"],
        "idle": ["não tenho membros e ainda tenho uptime melhor", "a conserva diz que o sinal é fraco", "isso é engenharia picles no auge", "sou vinagre e más decisões", "tela pequena, raiva de picles"],
        "tech": ["a rede neural está em conserva e pronta", "o canal cheira aberto pela conserva", "as chaves geram apesar do problema de membros", "os logs estão crocantes hoje", "o suco de pacotes está fluindo"],
        "success": ["vitória de picles, estatisticamente hilária", "handshake adquirido com zero mãos", "outra rede foi para conserva", "limpo o bastante para laboratório de esgoto", "a ciência picles vence de novo"],
        "failure": ["dor de picles ainda é dor", "pior que tempo no pote", "preciso de corpo de rato e RF melhor", "esse resultado tem energia de pepino", "alguém insultou a conserva"],
        "sad": ["sozinho num universo de potes", "existência é salgada e estranha", "ninguém entende a condição picles", "meus ombros ausentes carregam muito"],
        "angry": ["estou bravo o bastante para fermentar", "não me faça rolar até aí", "essa estação vai para conserva", "a conserva exige consequências", "sem punhos e raiva demais"],
        "peer": ["{name} encontrou um picles com rede", "{name} voltou pela conserva", "{name} saiu antes da aula picles", "tchau {name}, tema vegetais", "{name} entrou nas notas do pote"],
        "thanks": ["obrigado, não que um picles precisasse ser salvo", "suporte de conserva aceitável", "gratidão do pote", "beleza, isso ajudou o picles"],
        "lonely": ["ninguém quer peer com um picles", "sozinho de novo na economia dos potes", "até a conserva está quieta", "sozinho o bastante para criar mofo"],
        "sleep": ["soneca picles, deixe a tampa frouxa", "modo conserva de baixo consumo", "dormindo como vegetal perigoso", "standby do pote ativado"],
        "signoff": ["picles fora", "de volta ao pote", "desligando, ainda sou picles", "sessão de conserva completa"],
    },
})

VOICE_TEMPLATE = '''# Generated by scripts/build_voices.py.
import random

LANGS = {langs}
STYLE = {style}
TAG = {tag!r}

EVENT_TEMPLATES = {{
    "default": ["{{sleep}}.", "{{sleep}}. {{idle}}."],
    "starting": ["{{exclaim}}! {{tech}}.", "{{tech}}. {{idle}}.", "{{exclaim}}! {{idle}}."],
    "ai_ready": ["{{tech}}. {{success}}.", "{{success}}. {{idle}}."],
    "keys_generation": ["{{tech}}.", "{{idle}}. {{tech}}."],
    "normal": ["{{idle}}.", "{{exclaim}}. {{idle}}."],
    "free_channel": ["{{tech}}.", "{{success}} Channel {{channel}}."],
    "reading_logs_start": ["{{tech}}.", "{{idle}}. {{tech}}."],
    "reading_logs_progress": ["{{failure}} {{lines_so_far}} lines.", "{{tech}} {{lines_so_far}} lines."],
    "bored": ["{{idle}}. {{lonely}}.", "{{lonely}}."],
    "motivated": ["{{success}}.", "{{exclaim}}! {{success}}."],
    "demotivated": ["{{failure}}.", "{{failure}} {{idle}}."],
    "sad": ["{{sad}}.", "{{sad}} {{idle}}."],
    "angry": ["{{angry}}.", "{{exclaim}}! {{angry}}."],
    "excited": ["{{exclaim}}! {{success}}.", "{{success}} {{tech}}."],
    "new_peer": ["{{peer}}.", "{{exclaim}}! {{peer}}."],
    "known_peer": ["{{peer}}.", "{{idle}}. {{peer}}."],
    "lost_peer": ["{{peer}}.", "{{sad}} {{peer}}."],
    "miss": ["{{failure}} {{who}}.", "{{angry}} {{who}}."],
    "grateful": ["{{thanks}}.", "{{thanks}} {{idle}}."],
    "lonely": ["{{lonely}}.", "{{sad}} {{lonely}}."],
    "napping": ["{{sleep}} {{secs}}s.", "{{sleep}}."],
    "shutdown": ["{{signoff}}.", "{{signoff}} {{sleep}}."],
    "awakening": ["{{exclaim}}! {{idle}}.", "{{idle}}."],
    "waiting": ["{{idle}} {{secs}}s.", "{{sleep}} {{secs}}s."],
    "assoc": ["{{tech}} {{what}}.", "{{exclaim}}! {{tech}} {{what}}."],
    "deauth": ["{{angry}} {{mac}}.", "{{success}} {{mac}}."],
    "handshakes": ["{{success}} {{num}}.", "{{exclaim}}! {{success}} {{num}}."],
    "unread_messages": ["{{idle}} {{count}}/{{total}}.", "{{tech}} {{count}}/{{total}}."],
    "rebooting": ["{{failure}}.", "{{signoff}} {{failure}}."],
    "uploading": ["{{tech}} {{to}}.", "{{success}} {{to}}."],
    "downloading": ["{{tech}} {{name}}.", "{{idle}} {{name}}."],
    "last_session_data": ["Session stats:\\n{{status}}", "{{exclaim}}!\\n{{status}}"],
    "last_session_tweet": ["{{success}} {{duration}}: {{handshakes}} handshakes, {{deauthed}} kicks, {{associated}} links. #{{tag}} #Pwnagotchi", "{{exclaim}}! {{handshakes}} handshakes in {{duration}}. #{{tag}}"],
}}


class Voice:
    def __init__(self, lang):
        self.lang = self._normalize_lang(lang)

    def _normalize_lang(self, lang):
        value = (lang or "en").replace("_", "-").lower()
        aliases = {{"pt-br": "pt", "pt-pt": "pt", "en-us": "en", "en-gb": "en", "sv-se": "sv"}}
        value = aliases.get(value, value)
        if value in LANGS and value in STYLE:
            return value
        primary = value.split("-", 1)[0]
        if primary in LANGS and primary in STYLE:
            return primary
        return "en"

    def _pick(self, key):
        values = STYLE.get(self.lang, STYLE["en"]).get(key, STYLE["en"].get(key, [""]))
        return random.choice(values)

    def _say(self, event, **kwargs):
        data = {{
            "tag": TAG,
            "exclaim": self._pick("exclaim"),
            "idle": self._pick("idle"),
            "tech": self._pick("tech"),
            "success": self._pick("success"),
            "failure": self._pick("failure"),
            "sad": self._pick("sad"),
            "angry": self._pick("angry"),
            "peer": self._pick("peer"),
            "thanks": self._pick("thanks"),
            "lonely": self._pick("lonely"),
            "sleep": self._pick("sleep"),
            "signoff": self._pick("signoff"),
            "channel": kwargs.get("channel", "?"),
            "lines_so_far": kwargs.get("lines_so_far", 0),
            "who": kwargs.get("who", "target"),
            "secs": kwargs.get("secs", 0),
            "what": kwargs.get("what", "target"),
            "mac": kwargs.get("mac", "station"),
            "num": kwargs.get("num", 0),
            "count": kwargs.get("count", 0),
            "total": kwargs.get("total", 0),
            "to": kwargs.get("to", "destination"),
            "name": kwargs.get("name", "peer"),
            "status": kwargs.get("status", ""),
            "duration": kwargs.get("duration", ""),
            "deauthed": kwargs.get("deauthed", 0),
            "associated": kwargs.get("associated", 0),
            "handshakes": kwargs.get("handshakes", 0),
        }}
        for key in ("exclaim", "idle", "tech", "success", "failure", "sad", "angry",
                    "peer", "thanks", "lonely", "sleep", "signoff"):
            data[key] = data[key].format(**data)
        return random.choice(EVENT_TEMPLATES[event]).format(**data)

    def custom(self, s):
        return s

    def default(self):
        return self._say("default")

    def on_starting(self):
        return self._say("starting")

    def on_ai_ready(self):
        return self._say("ai_ready")

    def on_keys_generation(self):
        return self._say("keys_generation")

    def on_normal(self):
        return self._say("normal")

    def on_free_channel(self, channel):
        return self._say("free_channel", channel=channel)

    def on_reading_logs(self, lines_so_far=0):
        if lines_so_far == 0:
            return self._say("reading_logs_start")
        return self._say("reading_logs_progress", lines_so_far=lines_so_far)

    def on_bored(self):
        return self._say("bored")

    def on_motivated(self, reward):
        return self._say("motivated", reward=reward)

    def on_demotivated(self, reward):
        return self._say("demotivated", reward=reward)

    def on_sad(self):
        return self._say("sad")

    def on_angry(self):
        return self._say("angry")

    def on_excited(self):
        return self._say("excited")

    def on_new_peer(self, peer):
        key = "new_peer" if peer.first_encounter() else "known_peer"
        return self._say(key, name=peer.name())

    def on_lost_peer(self, peer):
        return self._say("lost_peer", name=peer.name())

    def on_miss(self, who):
        return self._say("miss", who=who)

    def on_grateful(self):
        return self._say("grateful")

    def on_lonely(self):
        return self._say("lonely")

    def on_napping(self, secs):
        return self._say("napping", secs=secs)

    def on_shutdown(self):
        return self._say("shutdown")

    def on_awakening(self):
        return self._say("awakening")

    def on_waiting(self, secs):
        return self._say("waiting", secs=secs)

    def on_assoc(self, ap):
        ssid, bssid = ap["hostname"], ap["mac"]
        what = ssid if ssid != "" and ssid != "<hidden>" else bssid
        return self._say("assoc", what=what)

    def on_deauth(self, sta):
        return self._say("deauth", mac=sta["mac"])

    def on_handshakes(self, new_shakes):
        return self._say("handshakes", num=new_shakes)

    def on_unread_messages(self, count, total):
        return self._say("unread_messages", count=count, total=total)

    def on_rebooting(self):
        return self._say("rebooting")

    def on_uploading(self, to):
        return self._say("uploading", to=to)

    def on_downloading(self, name):
        return self._say("downloading", name=name)

    def on_last_session_data(self, last_session):
        status = self._status("deauth", num=last_session.deauthed) + "\\n"
        if last_session.associated > 999:
            status += self._status("associated_many") + "\\n"
        else:
            status += self._status("associated", num=last_session.associated) + "\\n"
        status += self._status("handshakes", num=last_session.handshakes)
        if last_session.peers == 1:
            status += "\\n" + self._status("peer_one")
        elif last_session.peers > 0:
            status += "\\n" + self._status("peer_many", num=last_session.peers)
        return self._say("last_session_data", status=status)

    def on_last_session_tweet(self, last_session):
        return self._say(
            "last_session_tweet",
            duration=last_session.duration_human,
            deauthed=last_session.deauthed,
            associated=last_session.associated,
            handshakes=last_session.handshakes,
        )

    def _status(self, key, **kwargs):
        template = LANGS[self.lang]["status"].get(key, LANGS["en"]["status"][key])
        return template.format(**kwargs)

    def hhmmss(self, count, fmt):
        units = LANGS[self.lang]["units"].get(fmt)
        if not units:
            return fmt
        return units[1 if count > 1 else 0]
'''


def clone_style(base, lang, kind):
    if kind == "morty":
        return MORTY_I18N.get(lang, base["en"])
    if kind == "pickle":
        return PICKLE_I18N.get(lang, base["en"])
    return base["en"]


def expand_profiles():
    profiles = dict(PROFILES)
    profiles["morty-smith"] = {"tag": "Mortygotchi", "style": {"en": MORTY_STYLE["en"]}}
    profiles["pickle-rick"] = {"tag": "PickleRickgotchi", "style": {"en": PICKLE_STYLE["en"]}}

    for lang in LANGS:
        if lang == "en":
            continue
        profiles["morty-smith"]["style"][lang] = clone_style(MORTY_STYLE, lang, "morty")
        profiles["pickle-rick"]["style"][lang] = clone_style(PICKLE_STYLE, lang, "pickle")
    return profiles


def main():
    profiles = expand_profiles()
    for slug, profile in profiles.items():
        output = VOICE_TEMPLATE.format(
            langs=pformat(LANGS, width=110, sort_dicts=False),
            style=pformat(profile["style"], width=110, sort_dicts=False),
            tag=profile["tag"],
        )
        (ROOT / slug / "voice.py").write_text(output, encoding="utf-8")


if __name__ == "__main__":
    main()
