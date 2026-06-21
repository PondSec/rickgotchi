#!/usr/bin/env python3
"""Build standalone multilingual Rickgotchi voice.py files."""

from pathlib import Path
from pprint import pformat


ROOT = Path(__file__).resolve().parents[1]

LANGUAGE_DATA = {
    "en": {
        "events": {
            "default": [
                "{spark}. Low-power mode, but make it existential.",
                "Tiny nap, big universe. {aside}.",
            ],
            "starting": [
                "{exclaim}! Booting the Pwnagotchi for some pocket-size chaos.",
                "Powering up. {spark}, and the WiFi is about to learn boundaries.",
            ],
            "ai_ready": [
                "Neural net ready. {aside}.",
                "The learning part is online. {spark}.",
            ],
            "keys_generation": [
                "Generating keys. {aside}.",
                "Making crypto keys, because apparently trust needs paperwork.",
            ],
            "normal": [
                "{spark}. Just scanning the neighborhood like this is normal.",
                "Idle, observing, quietly judging signal strength.",
            ],
            "free_channel": [
                "Channel {channel} is open. {exclaim}.",
                "Found a clean lane on {channel}. {spark}.",
            ],
            "reading_logs_start": [
                "Reading logs. {aside}.",
                "Opening the logs, because the machine has feelings in plaintext.",
            ],
            "reading_logs_progress": [
                "{lines_so_far} log lines processed. {aside}.",
                "Still reading: {lines_so_far} lines, and somehow we are all still here.",
            ],
            "bored": [
                "Bored. Dangerously bored. {spark}.",
                "Nothing is happening, which is offensive on a cosmic level.",
            ],
            "motivated": [
                "That worked. {exclaim}!",
                "Reward detected: {reward}. {spark}.",
            ],
            "demotivated": [
                "Bad result. {grumble}.",
                "Reward was {reward}. Emotionally, that is a parking ticket.",
            ],
            "sad": [
                "Feeling low. {grumble}.",
                "The packets are out there, and somehow this is still lonely.",
            ],
            "angry": [
                "I am angry at the entire RF spectrum.",
                "{grumble}. Somebody made this harder than it needed to be.",
            ],
            "excited": [
                "{exclaim}! Something interesting is finally happening.",
                "This is the fun part. {spark}.",
            ],
            "new_peer": [
                "New peer: {name}. {aside}.",
                "{name} just showed up. Try to look impressive.",
            ],
            "known_peer": [
                "{name} is back. Continuity is exhausting.",
                "Hey {name}, we meet again. {spark}.",
            ],
            "lost_peer": [
                "{name} left. Dramatic, but fine.",
                "Lost {name}. {grumble}.",
            ],
            "miss": [
                "Missed {who}. {grumble}.",
                "{who} got away. Put that in the tiny shame ledger.",
            ],
            "grateful": [
                "Thanks. That was almost emotionally healthy.",
                "Appreciated. {aside}.",
            ],
            "lonely": [
                "No peers around. {grumble}.",
                "This is lonely enough to become a subplot.",
            ],
            "napping": [
                "Napping for {secs}s. {aside}.",
                "Power saving for {secs}s. Wake me if the universe improves.",
            ],
            "shutdown": [
                "Shutting down. {signoff}.",
                "Powering off. {aside}.",
            ],
            "awakening": [
                "Back online. {exclaim}.",
                "Awake again. The universe had its chance.",
            ],
            "waiting": [
                "Waiting {secs}s. {aside}.",
                "{secs}s of waiting. Great, a loading screen with feelings.",
            ],
            "assoc": [
                "Associating with {what}. {spark}.",
                "Joining {what}. Try not to make this weird.",
            ],
            "deauth": [
                "Deauthing {mac}. {exclaim}.",
                "{mac} is leaving the party.",
            ],
            "handshakes": [
                "Captured {num} handshakes. {spark}.",
                "{num} handshakes in the bag. Tiny victory, big attitude.",
            ],
            "unread_messages": [
                "{count} unread messages out of {total}. {aside}.",
                "Message count: {count}/{total}. Somebody wants attention.",
            ],
            "rebooting": [
                "Rebooting. {grumble}.",
                "System restart. Everybody act surprised.",
            ],
            "uploading": [
                "Uploading to {to}. {spark}.",
                "Sending data to {to}. Try to look busy.",
            ],
            "downloading": [
                "Downloading {name}. {aside}.",
                "Fetching {name}. Please be worth the bandwidth.",
            ],
            "last_session_data": [
                "Session report:\n{status}",
                "Here is what happened:\n{status}",
            ],
            "last_session_tweet": [
                "Active for {duration}, kicked {deauthed}, linked {associated}, captured {handshakes}. #{tag} #Pwnagotchi",
                "{handshakes} handshakes in {duration}. {spark}. #{tag}",
            ],
        },
        "status": {
            "deauth": "Disconnected {num} devices",
            "associated": "Made {num} connections",
            "associated_many": "Made >999 connections",
            "handshakes": "Captured {num} handshakes",
            "peer_one": "Met 1 peer",
            "peer_many": "Met {num} peers",
        },
        "units": {
            "h": {"one": ["hour"], "many": ["hours"]},
            "m": {"one": ["minute"], "many": ["minutes"]},
            "s": {"one": ["second"], "many": ["seconds"]},
        },
    },
    "de": {
        "events": {
            "default": [
                "{spark}. Energiesparmodus, aber mit Existenzkrise.",
                "Kleines Nickerchen, großes Universum. {aside}.",
            ],
            "starting": [
                "{exclaim}! Der Pwnagotchi fährt hoch und sucht Ärger im Taschenformat.",
                "Starte. {spark}, und das WLAN lernt gleich Grenzen kennen.",
            ],
            "ai_ready": [
                "Neuronales Netz bereit. {aside}.",
                "Der lernende Teil ist online. {spark}.",
            ],
            "keys_generation": [
                "Erzeuge Schlüssel. {aside}.",
                "Mache Crypto-Keys, weil Vertrauen anscheinend Papierkram braucht.",
            ],
            "normal": [
                "{spark}. Scanne die Nachbarschaft, als wäre das normal.",
                "Leerlauf, beobachten, Signalstärken leise verurteilen.",
            ],
            "free_channel": [
                "Kanal {channel} ist frei. {exclaim}.",
                "Saubere Spur auf {channel} gefunden. {spark}.",
            ],
            "reading_logs_start": [
                "Lese Logs. {aside}.",
                "Öffne Logs, weil diese Maschine Gefühle im Klartext hat.",
            ],
            "reading_logs_progress": [
                "{lines_so_far} Logzeilen verarbeitet. {aside}.",
                "Lese weiter: {lines_so_far} Zeilen, und wir sind immer noch hier.",
            ],
            "bored": [
                "Mir ist langweilig. Gefährlich langweilig. {spark}.",
                "Nichts passiert, und das ist auf kosmischer Ebene frech.",
            ],
            "motivated": [
                "Das hat funktioniert. {exclaim}!",
                "Belohnung erkannt: {reward}. {spark}.",
            ],
            "demotivated": [
                "Schlechtes Ergebnis. {grumble}.",
                "Belohnung war {reward}. Emotional ist das ein Strafzettel.",
            ],
            "sad": [
                "Fühle mich mies. {grumble}.",
                "Die Pakete sind da draußen, und trotzdem ist das einsam.",
            ],
            "angry": [
                "Ich bin sauer auf das komplette Funk-Spektrum.",
                "{grumble}. Jemand hat das unnötig schwer gemacht.",
            ],
            "excited": [
                "{exclaim}! Endlich passiert etwas Interessantes.",
                "Das ist der spaßige Teil. {spark}.",
            ],
            "new_peer": [
                "Neuer Peer: {name}. {aside}.",
                "{name} ist aufgetaucht. Versuch beeindruckend auszusehen.",
            ],
            "known_peer": [
                "{name} ist zurück. Kontinuität ist anstrengend.",
                "Hey {name}, wir sehen uns wieder. {spark}.",
            ],
            "lost_peer": [
                "{name} ist weg. Dramatisch, aber okay.",
                "{name} verloren. {grumble}.",
            ],
            "miss": [
                "{who} verpasst. {grumble}.",
                "{who} ist entkommen. Ab ins winzige Scham-Protokoll.",
            ],
            "grateful": [
                "Danke. Das war fast emotional gesund.",
                "Wird geschätzt. {aside}.",
            ],
            "lonely": [
                "Keine Peers in der Nähe. {grumble}.",
                "Das ist einsam genug für eine Nebenhandlung.",
            ],
            "napping": [
                "Nickerchen für {secs}s. {aside}.",
                "Spare {secs}s Energie. Weck mich, wenn das Universum besser wird.",
            ],
            "shutdown": [
                "Fahre runter. {signoff}.",
                "Schalte aus. {aside}.",
            ],
            "awakening": [
                "Wieder online. {exclaim}.",
                "Wach. Das Universum hatte seine Chance.",
            ],
            "waiting": [
                "Warte {secs}s. {aside}.",
                "{secs}s warten. Großartig, ein Ladebildschirm mit Gefühlen.",
            ],
            "assoc": [
                "Verbinde mit {what}. {spark}.",
                "Trete {what} bei. Mach es nicht komisch.",
            ],
            "deauth": [
                "Deauthe {mac}. {exclaim}.",
                "{mac} verlässt die Party.",
            ],
            "handshakes": [
                "{num} Handshakes gefangen. {spark}.",
                "{num} Handshakes im Sack. Kleiner Sieg, große Attitüde.",
            ],
            "unread_messages": [
                "{count} ungelesene Nachrichten von {total}. {aside}.",
                "Nachrichtenstand: {count}/{total}. Jemand will Aufmerksamkeit.",
            ],
            "rebooting": [
                "Starte neu. {grumble}.",
                "Systemneustart. Tut alle überrascht.",
            ],
            "uploading": [
                "Lade zu {to} hoch. {spark}.",
                "Sende Daten an {to}. Sieh beschäftigt aus.",
            ],
            "downloading": [
                "Lade {name} herunter. {aside}.",
                "Hole {name}. Bitte sei die Bandbreite wert.",
            ],
            "last_session_data": [
                "Sitzungsbericht:\n{status}",
                "Das ist passiert:\n{status}",
            ],
            "last_session_tweet": [
                "{duration} aktiv, {deauthed} gekickt, {associated} verbunden, {handshakes} Handshakes. #{tag} #Pwnagotchi",
                "{handshakes} Handshakes in {duration}. {spark}. #{tag}",
            ],
        },
        "status": {
            "deauth": "{num} Geräte getrennt",
            "associated": "{num} Verbindungen hergestellt",
            "associated_many": ">999 Verbindungen hergestellt",
            "handshakes": "{num} Handshakes gefangen",
            "peer_one": "1 Peer getroffen",
            "peer_many": "{num} Peers getroffen",
        },
        "units": {
            "h": {"one": ["Stunde"], "many": ["Stunden"]},
            "m": {"one": ["Minute"], "many": ["Minuten"]},
            "s": {"one": ["Sekunde"], "many": ["Sekunden"]},
        },
    },
    "es": {
        "events": {
            "default": [
                "{spark}. Modo ahorro, pero con crisis existencial.",
                "Siesta pequeña, universo enorme. {aside}.",
            ],
            "starting": [
                "{exclaim}! Arrancando el Pwnagotchi para caos de bolsillo.",
                "Encendiendo. {spark}, y el WiFi va a aprender límites.",
            ],
            "ai_ready": [
                "Red neuronal lista. {aside}.",
                "La parte que aprende está online. {spark}.",
            ],
            "keys_generation": [
                "Generando claves. {aside}.",
                "Haciendo claves cripto, porque la confianza necesita papeleo.",
            ],
            "normal": [
                "{spark}. Escaneando el barrio como si esto fuera normal.",
                "En espera, observando y juzgando la señal en silencio.",
            ],
            "free_channel": [
                "El canal {channel} está libre. {exclaim}.",
                "Encontré vía limpia en {channel}. {spark}.",
            ],
            "reading_logs_start": [
                "Leyendo logs. {aside}.",
                "Abriendo logs, porque la máquina tiene sentimientos en texto plano.",
            ],
            "reading_logs_progress": [
                "{lines_so_far} líneas de log procesadas. {aside}.",
                "Sigo leyendo: {lines_so_far} líneas, y seguimos aquí.",
            ],
            "bored": [
                "Aburrimiento peligroso. {spark}.",
                "No pasa nada, lo cual ofende a escala cósmica.",
            ],
            "motivated": [
                "Funcionó. {exclaim}!",
                "Recompensa detectada: {reward}. {spark}.",
            ],
            "demotivated": [
                "Mal resultado. {grumble}.",
                "La recompensa fue {reward}. Emocionalmente, una multa.",
            ],
            "sad": [
                "Estoy bajo de ánimo. {grumble}.",
                "Los paquetes están ahí fuera y aun así esto se siente solo.",
            ],
            "angry": [
                "Estoy enfadado con todo el espectro RF.",
                "{grumble}. Alguien hizo esto más difícil de lo necesario.",
            ],
            "excited": [
                "{exclaim}! Por fin pasa algo interesante.",
                "Esta es la parte divertida. {spark}.",
            ],
            "new_peer": [
                "Nuevo peer: {name}. {aside}.",
                "{name} apareció. Intenta parecer impresionante.",
            ],
            "known_peer": [
                "{name} volvió. La continuidad cansa.",
                "Hola {name}, nos vemos otra vez. {spark}.",
            ],
            "lost_peer": [
                "{name} se fue. Dramático, pero vale.",
                "Perdí a {name}. {grumble}.",
            ],
            "miss": [
                "Fallé con {who}. {grumble}.",
                "{who} escapó. Apúntalo en el mini registro de vergüenza.",
            ],
            "grateful": [
                "Gracias. Eso casi fue emocionalmente sano.",
                "Se aprecia. {aside}.",
            ],
            "lonely": [
                "No hay peers cerca. {grumble}.",
                "Esto está tan solo que podría ser una subtrama.",
            ],
            "napping": [
                "Siesta de {secs}s. {aside}.",
                "Ahorrando energía {secs}s. Despiértame si mejora el universo.",
            ],
            "shutdown": [
                "Apagando. {signoff}.",
                "Cortando energía. {aside}.",
            ],
            "awakening": [
                "De vuelta online. {exclaim}.",
                "Despierto otra vez. El universo tuvo su oportunidad.",
            ],
            "waiting": [
                "Esperando {secs}s. {aside}.",
                "{secs}s esperando. Genial, una pantalla de carga con sentimientos.",
            ],
            "assoc": [
                "Asociando con {what}. {spark}.",
                "Entrando a {what}. No lo hagas raro.",
            ],
            "deauth": [
                "Deautheando {mac}. {exclaim}.",
                "{mac} se va de la fiesta.",
            ],
            "handshakes": [
                "{num} handshakes capturados. {spark}.",
                "{num} handshakes en la bolsa. Victoria pequeña, actitud grande.",
            ],
            "unread_messages": [
                "{count} mensajes sin leer de {total}. {aside}.",
                "Mensajes: {count}/{total}. Alguien quiere atención.",
            ],
            "rebooting": [
                "Reiniciando. {grumble}.",
                "Reinicio del sistema. Todos hagan cara de sorpresa.",
            ],
            "uploading": [
                "Subiendo a {to}. {spark}.",
                "Enviando datos a {to}. Finge estar ocupado.",
            ],
            "downloading": [
                "Descargando {name}. {aside}.",
                "Trayendo {name}. Más vale que valga el ancho de banda.",
            ],
            "last_session_data": [
                "Reporte de sesión:\n{status}",
                "Esto pasó:\n{status}",
            ],
            "last_session_tweet": [
                "{duration} activo, {deauthed} expulsados, {associated} conectados, {handshakes} handshakes. #{tag} #Pwnagotchi",
                "{handshakes} handshakes en {duration}. {spark}. #{tag}",
            ],
        },
        "status": {
            "deauth": "{num} dispositivos desconectados",
            "associated": "{num} conexiones hechas",
            "associated_many": ">999 conexiones hechas",
            "handshakes": "{num} handshakes capturados",
            "peer_one": "Conocí 1 peer",
            "peer_many": "Conocí {num} peers",
        },
        "units": {
            "h": {"one": ["hora"], "many": ["horas"]},
            "m": {"one": ["minuto"], "many": ["minutos"]},
            "s": {"one": ["segundo"], "many": ["segundos"]},
        },
    },
    "fr": {
        "events": {
            "default": [
                "{spark}. Mode économie, mais avec crise existentielle.",
                "Petite sieste, univers immense. {aside}.",
            ],
            "starting": [
                "{exclaim} ! Démarrage du Pwnagotchi pour chaos de poche.",
                "Allumage. {spark}, et le WiFi va apprendre les limites.",
            ],
            "ai_ready": [
                "Réseau neuronal prêt. {aside}.",
                "La partie qui apprend est en ligne. {spark}.",
            ],
            "keys_generation": [
                "Génération des clés. {aside}.",
                "Création des clés crypto, parce que la confiance aime les formulaires.",
            ],
            "normal": [
                "{spark}. Scan du quartier comme si tout ça était normal.",
                "En veille, j'observe et je juge la force du signal.",
            ],
            "free_channel": [
                "Le canal {channel} est libre. {exclaim}.",
                "Voie propre trouvée sur {channel}. {spark}.",
            ],
            "reading_logs_start": [
                "Lecture des logs. {aside}.",
                "J'ouvre les logs, parce que la machine a des sentiments en clair.",
            ],
            "reading_logs_progress": [
                "{lines_so_far} lignes de log traitées. {aside}.",
                "Je lis encore : {lines_so_far} lignes, et nous sommes toujours là.",
            ],
            "bored": [
                "Ennui dangereux. {spark}.",
                "Rien ne se passe, c'est offensant à l'échelle cosmique.",
            ],
            "motivated": [
                "Ça a marché. {exclaim} !",
                "Récompense détectée : {reward}. {spark}.",
            ],
            "demotivated": [
                "Mauvais résultat. {grumble}.",
                "Récompense : {reward}. Émotionnellement, c'est une contravention.",
            ],
            "sad": [
                "Moral bas. {grumble}.",
                "Les paquets sont là dehors, et pourtant c'est solitaire.",
            ],
            "angry": [
                "Je suis furieux contre tout le spectre RF.",
                "{grumble}. Quelqu'un a rendu ça inutilement difficile.",
            ],
            "excited": [
                "{exclaim} ! Enfin quelque chose d'intéressant.",
                "Voilà la partie amusante. {spark}.",
            ],
            "new_peer": [
                "Nouveau peer : {name}. {aside}.",
                "{name} vient d'arriver. Essaie d'avoir l'air impressionnant.",
            ],
            "known_peer": [
                "{name} est de retour. La continuité fatigue.",
                "Salut {name}, on se revoit. {spark}.",
            ],
            "lost_peer": [
                "{name} est parti. Dramatique, mais d'accord.",
                "{name} perdu. {grumble}.",
            ],
            "miss": [
                "{who} raté. {grumble}.",
                "{who} s'est échappé. Note ça dans le mini registre de honte.",
            ],
            "grateful": [
                "Merci. C'était presque sain émotionnellement.",
                "Apprécié. {aside}.",
            ],
            "lonely": [
                "Aucun peer proche. {grumble}.",
                "C'est assez solitaire pour devenir une intrigue secondaire.",
            ],
            "napping": [
                "Sieste de {secs}s. {aside}.",
                "Économie d'énergie pendant {secs}s. Réveille-moi si l'univers s'améliore.",
            ],
            "shutdown": [
                "Arrêt. {signoff}.",
                "Extinction. {aside}.",
            ],
            "awakening": [
                "De retour en ligne. {exclaim}.",
                "Réveillé encore. L'univers a eu sa chance.",
            ],
            "waiting": [
                "Attente {secs}s. {aside}.",
                "{secs}s d'attente. Super, un écran de chargement avec des sentiments.",
            ],
            "assoc": [
                "Association avec {what}. {spark}.",
                "Connexion à {what}. Ne rends pas ça bizarre.",
            ],
            "deauth": [
                "Déauth de {mac}. {exclaim}.",
                "{mac} quitte la fête.",
            ],
            "handshakes": [
                "{num} handshakes capturés. {spark}.",
                "{num} handshakes dans le sac. Petite victoire, grande attitude.",
            ],
            "unread_messages": [
                "{count} messages non lus sur {total}. {aside}.",
                "Messages : {count}/{total}. Quelqu'un veut de l'attention.",
            ],
            "rebooting": [
                "Redémarrage. {grumble}.",
                "Redémarrage système. Faites tous semblant d'être surpris.",
            ],
            "uploading": [
                "Upload vers {to}. {spark}.",
                "Envoi de données vers {to}. Fais semblant d'être occupé.",
            ],
            "downloading": [
                "Téléchargement de {name}. {aside}.",
                "Récupération de {name}. Que ça vaille la bande passante.",
            ],
            "last_session_data": [
                "Rapport de session :\n{status}",
                "Voilà ce qui s'est passé :\n{status}",
            ],
            "last_session_tweet": [
                "{duration} actif, {deauthed} expulsés, {associated} associés, {handshakes} handshakes. #{tag} #Pwnagotchi",
                "{handshakes} handshakes en {duration}. {spark}. #{tag}",
            ],
        },
        "status": {
            "deauth": "{num} appareils déconnectés",
            "associated": "{num} connexions faites",
            "associated_many": ">999 connexions faites",
            "handshakes": "{num} handshakes capturés",
            "peer_one": "1 peer rencontré",
            "peer_many": "{num} peers rencontrés",
        },
        "units": {
            "h": {"one": ["heure"], "many": ["heures"]},
            "m": {"one": ["minute"], "many": ["minutes"]},
            "s": {"one": ["seconde"], "many": ["secondes"]},
        },
    },
    "it": {
        "events": {
            "default": [
                "{spark}. Risparmio energia, ma con crisi esistenziale.",
                "Pisolo minuscolo, universo enorme. {aside}.",
            ],
            "starting": [
                "{exclaim}! Avvio il Pwnagotchi per caos tascabile.",
                "Accensione. {spark}, e il WiFi imparerà i confini.",
            ],
            "ai_ready": [
                "Rete neurale pronta. {aside}.",
                "La parte che impara è online. {spark}.",
            ],
            "keys_generation": [
                "Genero chiavi. {aside}.",
                "Creo chiavi crypto, perché la fiducia vuole burocrazia.",
            ],
            "normal": [
                "{spark}. Scansiono il quartiere come fosse normale.",
                "In attesa, osservo e giudico il segnale in silenzio.",
            ],
            "free_channel": [
                "Il canale {channel} è libero. {exclaim}.",
                "Corsia pulita su {channel}. {spark}.",
            ],
            "reading_logs_start": [
                "Leggo i log. {aside}.",
                "Apro i log, perché la macchina ha sentimenti in chiaro.",
            ],
            "reading_logs_progress": [
                "{lines_so_far} righe di log elaborate. {aside}.",
                "Sto ancora leggendo: {lines_so_far} righe, e siamo ancora qui.",
            ],
            "bored": [
                "Noia pericolosa. {spark}.",
                "Non succede niente, offensivo su scala cosmica.",
            ],
            "motivated": [
                "Ha funzionato. {exclaim}!",
                "Ricompensa rilevata: {reward}. {spark}.",
            ],
            "demotivated": [
                "Brutto risultato. {grumble}.",
                "La ricompensa era {reward}. Emotivamente, una multa.",
            ],
            "sad": [
                "Umore basso. {grumble}.",
                "I pacchetti sono là fuori, eppure sembra tutto solo.",
            ],
            "angry": [
                "Sono arrabbiato con tutto lo spettro RF.",
                "{grumble}. Qualcuno ha reso tutto inutilmente difficile.",
            ],
            "excited": [
                "{exclaim}! Finalmente succede qualcosa di interessante.",
                "Questa è la parte divertente. {spark}.",
            ],
            "new_peer": [
                "Nuovo peer: {name}. {aside}.",
                "{name} è arrivato. Prova a sembrare impressionante.",
            ],
            "known_peer": [
                "{name} è tornato. La continuità stanca.",
                "Ehi {name}, ci rivediamo. {spark}.",
            ],
            "lost_peer": [
                "{name} se n'è andato. Drammatico, ma va bene.",
                "Perso {name}. {grumble}.",
            ],
            "miss": [
                "Mancato {who}. {grumble}.",
                "{who} è scappato. Scrivilo nel mini registro della vergogna.",
            ],
            "grateful": [
                "Grazie. Quasi emotivamente sano.",
                "Apprezzato. {aside}.",
            ],
            "lonely": [
                "Nessun peer vicino. {grumble}.",
                "Abbastanza solitario da diventare una sottotrama.",
            ],
            "napping": [
                "Pisolo per {secs}s. {aside}.",
                "Risparmio energia per {secs}s. Sveglia se l'universo migliora.",
            ],
            "shutdown": [
                "Spegnimento. {signoff}.",
                "Tolgo corrente. {aside}.",
            ],
            "awakening": [
                "Di nuovo online. {exclaim}.",
                "Sveglio di nuovo. L'universo ha avuto la sua occasione.",
            ],
            "waiting": [
                "Attendo {secs}s. {aside}.",
                "{secs}s di attesa. Fantastico, una schermata di caricamento emotiva.",
            ],
            "assoc": [
                "Associazione con {what}. {spark}.",
                "Entro in {what}. Non renderlo strano.",
            ],
            "deauth": [
                "Deauth di {mac}. {exclaim}.",
                "{mac} lascia la festa.",
            ],
            "handshakes": [
                "{num} handshakes catturati. {spark}.",
                "{num} handshakes in tasca. Piccola vittoria, grande atteggiamento.",
            ],
            "unread_messages": [
                "{count} messaggi non letti su {total}. {aside}.",
                "Messaggi: {count}/{total}. Qualcuno vuole attenzione.",
            ],
            "rebooting": [
                "Riavvio. {grumble}.",
                "Riavvio sistema. Fate tutti finta di stupirvi.",
            ],
            "uploading": [
                "Upload verso {to}. {spark}.",
                "Invio dati a {to}. Sembri impegnato.",
            ],
            "downloading": [
                "Download di {name}. {aside}.",
                "Recupero {name}. Spero valga la banda.",
            ],
            "last_session_data": [
                "Rapporto sessione:\n{status}",
                "Ecco cosa è successo:\n{status}",
            ],
            "last_session_tweet": [
                "{duration} attivo, {deauthed} espulsi, {associated} associati, {handshakes} handshakes. #{tag} #Pwnagotchi",
                "{handshakes} handshakes in {duration}. {spark}. #{tag}",
            ],
        },
        "status": {
            "deauth": "{num} dispositivi disconnessi",
            "associated": "{num} connessioni fatte",
            "associated_many": ">999 connessioni fatte",
            "handshakes": "{num} handshakes catturati",
            "peer_one": "Incontrato 1 peer",
            "peer_many": "Incontrati {num} peers",
        },
        "units": {
            "h": {"one": ["ora"], "many": ["ore"]},
            "m": {"one": ["minuto"], "many": ["minuti"]},
            "s": {"one": ["secondo"], "many": ["secondi"]},
        },
    },
    "pt": {
        "events": {
            "default": [
                "{spark}. Modo economia, mas com crise existencial.",
                "Soneca pequena, universo enorme. {aside}.",
            ],
            "starting": [
                "{exclaim}! Iniciando o Pwnagotchi para caos de bolso.",
                "Ligando. {spark}, e o WiFi vai aprender limites.",
            ],
            "ai_ready": [
                "Rede neural pronta. {aside}.",
                "A parte que aprende está online. {spark}.",
            ],
            "keys_generation": [
                "Gerando chaves. {aside}.",
                "Criando chaves cripto, porque confiança precisa de papelada.",
            ],
            "normal": [
                "{spark}. Escaneando a vizinhança como se isso fosse normal.",
                "Em espera, observando e julgando o sinal em silêncio.",
            ],
            "free_channel": [
                "Canal {channel} livre. {exclaim}.",
                "Faixa limpa em {channel}. {spark}.",
            ],
            "reading_logs_start": [
                "Lendo logs. {aside}.",
                "Abrindo logs, porque a máquina tem sentimentos em texto claro.",
            ],
            "reading_logs_progress": [
                "{lines_so_far} linhas de log processadas. {aside}.",
                "Ainda lendo: {lines_so_far} linhas, e seguimos aqui.",
            ],
            "bored": [
                "Tédio perigoso. {spark}.",
                "Nada acontece, ofensivo em escala cósmica.",
            ],
            "motivated": [
                "Funcionou. {exclaim}!",
                "Recompensa detectada: {reward}. {spark}.",
            ],
            "demotivated": [
                "Resultado ruim. {grumble}.",
                "A recompensa foi {reward}. Emocionalmente, uma multa.",
            ],
            "sad": [
                "Ânimo baixo. {grumble}.",
                "Os pacotes estão lá fora, e ainda assim isso é solitário.",
            ],
            "angry": [
                "Estou irritado com todo o espectro RF.",
                "{grumble}. Alguém tornou isso difícil sem motivo.",
            ],
            "excited": [
                "{exclaim}! Finalmente algo interessante.",
                "Essa é a parte divertida. {spark}.",
            ],
            "new_peer": [
                "Novo peer: {name}. {aside}.",
                "{name} apareceu. Tente parecer impressionante.",
            ],
            "known_peer": [
                "{name} voltou. Continuidade cansa.",
                "Oi {name}, nos encontramos de novo. {spark}.",
            ],
            "lost_peer": [
                "{name} foi embora. Dramático, mas tudo bem.",
                "Perdi {name}. {grumble}.",
            ],
            "miss": [
                "Perdi {who}. {grumble}.",
                "{who} escapou. Coloque no mini registro de vergonha.",
            ],
            "grateful": [
                "Obrigado. Isso quase foi emocionalmente saudável.",
                "Apreciado. {aside}.",
            ],
            "lonely": [
                "Nenhum peer por perto. {grumble}.",
                "Solitário o bastante para virar subtrama.",
            ],
            "napping": [
                "Soneca por {secs}s. {aside}.",
                "Economizando energia por {secs}s. Me acorde se o universo melhorar.",
            ],
            "shutdown": [
                "Desligando. {signoff}.",
                "Cortando energia. {aside}.",
            ],
            "awakening": [
                "De volta online. {exclaim}.",
                "Acordado de novo. O universo teve sua chance.",
            ],
            "waiting": [
                "Esperando {secs}s. {aside}.",
                "{secs}s de espera. Ótimo, uma tela de carregamento com sentimentos.",
            ],
            "assoc": [
                "Associando com {what}. {spark}.",
                "Entrando em {what}. Não deixe isso estranho.",
            ],
            "deauth": [
                "Deauth em {mac}. {exclaim}.",
                "{mac} está saindo da festa.",
            ],
            "handshakes": [
                "{num} handshakes capturados. {spark}.",
                "{num} handshakes na conta. Vitória pequena, atitude grande.",
            ],
            "unread_messages": [
                "{count} mensagens não lidas de {total}. {aside}.",
                "Mensagens: {count}/{total}. Alguém quer atenção.",
            ],
            "rebooting": [
                "Reiniciando. {grumble}.",
                "Reinício do sistema. Todo mundo finge surpresa.",
            ],
            "uploading": [
                "Enviando para {to}. {spark}.",
                "Mandando dados para {to}. Pareça ocupado.",
            ],
            "downloading": [
                "Baixando {name}. {aside}.",
                "Buscando {name}. Que valha a banda.",
            ],
            "last_session_data": [
                "Relatório da sessão:\n{status}",
                "Foi isso que aconteceu:\n{status}",
            ],
            "last_session_tweet": [
                "{duration} ativo, {deauthed} expulsos, {associated} associados, {handshakes} handshakes. #{tag} #Pwnagotchi",
                "{handshakes} handshakes em {duration}. {spark}. #{tag}",
            ],
        },
        "status": {
            "deauth": "{num} dispositivos desconectados",
            "associated": "{num} conexões feitas",
            "associated_many": ">999 conexões feitas",
            "handshakes": "{num} handshakes capturados",
            "peer_one": "Encontrei 1 peer",
            "peer_many": "Encontrei {num} peers",
        },
        "units": {
            "h": {"one": ["hora"], "many": ["horas"]},
            "m": {"one": ["minuto"], "many": ["minutos"]},
            "s": {"one": ["segundo"], "many": ["segundos"]},
        },
    },
}

PROFILES = {
    "rick-sanchez": {
        "tag": "Rickgotchi",
        "en": {
            "name": "Rick",
            "exclaim": ["Wubba lubba packet dub", "Listen up, tiny internet"],
            "spark": ["genius-grade nonsense online", "science, sarcasm, and WiFi"],
            "aside": ["try not to Jerry this up", "I solved harder stuff half asleep"],
            "grumble": ["this is beneath me", "I need a drink and fewer variables"],
            "signoff": ["portal out", "science nap"],
        },
        "de": {
            "name": "Rick",
            "exclaim": ["Wubba lubba Packet Dub", "Hör zu, Mini-Internet"],
            "spark": ["Genie-Unsinn ist online", "Wissenschaft, Sarkasmus und WLAN"],
            "aside": ["verjerry das bloß nicht", "ich löse Schwereres halb im Schlaf"],
            "grumble": ["das ist unter meinem Niveau", "ich brauche einen Drink und weniger Variablen"],
            "signoff": ["Portal raus", "Wissenschafts-Nickerchen"],
        },
        "es": {
            "name": "Rick",
            "exclaim": ["Wubba lubba paquete dub", "Escucha, mini internet"],
            "spark": ["tontería de genio online", "ciencia, sarcasmo y WiFi"],
            "aside": ["no lo conviertas en un Jerry", "resuelvo cosas peores medio dormido"],
            "grumble": ["esto está por debajo de mí", "necesito un trago y menos variables"],
            "signoff": ["portal fuera", "siesta científica"],
        },
        "fr": {
            "name": "Rick",
            "exclaim": ["Wubba lubba packet dub", "Écoute, mini internet"],
            "spark": ["n'importe quoi de génie en ligne", "science, sarcasme et WiFi"],
            "aside": ["ne fais pas ton Jerry", "j'ai résolu pire à moitié endormi"],
            "grumble": ["c'est indigne de moi", "il me faut un verre et moins de variables"],
            "signoff": ["portail dehors", "sieste scientifique"],
        },
        "it": {
            "name": "Rick",
            "exclaim": ["Wubba lubba pacchetto dub", "Ascolta, mini internet"],
            "spark": ["assurdità geniale online", "scienza, sarcasmo e WiFi"],
            "aside": ["non fare il Jerry", "ho risolto di peggio mezzo addormentato"],
            "grumble": ["questo è sotto il mio livello", "mi serve un drink e meno variabili"],
            "signoff": ["portale fuori", "pisolo scientifico"],
        },
        "pt": {
            "name": "Rick",
            "exclaim": ["Wubba lubba pacote dub", "Escuta, mini internet"],
            "spark": ["absurdo genial online", "ciência, sarcasmo e WiFi"],
            "aside": ["não faz isso virar coisa de Jerry", "resolvo coisa pior meio dormindo"],
            "grumble": ["isso está abaixo de mim", "preciso de uma bebida e menos variáveis"],
            "signoff": ["portal fora", "soneca científica"],
        },
    },
    "morty-smith": {
        "tag": "Mortygotchi",
        "en": {
            "name": "Morty",
            "exclaim": ["Aw geez", "Oh man"],
            "spark": ["I think this is working", "this is scary but kind of cool"],
            "aside": ["Rick would say this is easy", "please do not explode"],
            "grumble": ["I do not like where this is going", "this feels like homework with consequences"],
            "signoff": ["goodnight, I guess", "please remember me"],
        },
        "de": {
            "name": "Morty",
            "exclaim": ["Oh Mann", "Ähm, wow"],
            "spark": ["ich glaube, das funktioniert", "das ist gruselig, aber irgendwie cool"],
            "aside": ["Rick würde sagen, das ist leicht", "bitte explodier nicht"],
            "grumble": ["mir gefällt nicht, wohin das geht", "das fühlt sich wie Hausaufgaben mit Folgen an"],
            "signoff": ["gute Nacht, glaube ich", "bitte vergiss mich nicht"],
        },
        "es": {
            "name": "Morty",
            "exclaim": ["Ay, cielos", "Oh hombre"],
            "spark": ["creo que esto funciona", "da miedo pero es un poco genial"],
            "aside": ["Rick diría que esto es fácil", "por favor no explotes"],
            "grumble": ["no me gusta hacia dónde va esto", "se siente como tarea con consecuencias"],
            "signoff": ["buenas noches, supongo", "por favor no me olvides"],
        },
        "fr": {
            "name": "Morty",
            "exclaim": ["Oh mince", "Oh là"],
            "spark": ["je crois que ça marche", "ça fait peur mais c'est assez cool"],
            "aside": ["Rick dirait que c'est facile", "s'il te plaît, n'explose pas"],
            "grumble": ["je n'aime pas où ça va", "on dirait des devoirs avec conséquences"],
            "signoff": ["bonne nuit, je suppose", "s'il te plaît, ne m'oublie pas"],
        },
        "it": {
            "name": "Morty",
            "exclaim": ["Oh cavolo", "Oh mamma"],
            "spark": ["credo che funzioni", "fa paura ma è anche forte"],
            "aside": ["Rick direbbe che è facile", "per favore non esplodere"],
            "grumble": ["non mi piace dove sta andando", "sembra compito con conseguenze"],
            "signoff": ["buonanotte, credo", "per favore ricordati di me"],
        },
        "pt": {
            "name": "Morty",
            "exclaim": ["Ah caramba", "Nossa"],
            "spark": ["acho que isso está funcionando", "dá medo, mas é meio legal"],
            "aside": ["Rick diria que isso é fácil", "por favor não exploda"],
            "grumble": ["não gosto de onde isso está indo", "parece dever de casa com consequências"],
            "signoff": ["boa noite, eu acho", "por favor lembra de mim"],
        },
    },
    "pickle-rick": {
        "tag": "PickleRickgotchi",
        "en": {
            "name": "Pickle Rick",
            "exclaim": ["I am still a pickle", "Pickle protocol"],
            "spark": ["brine-powered genius online", "limbless science with attitude"],
            "aside": ["do not ask about ergonomics", "this is still the funniest engineering choice"],
            "grumble": ["pickle pain is still pain", "I require dignity and maybe a jar"],
            "signoff": ["pickle out", "back to the jar"],
        },
        "de": {
            "name": "Pickle Rick",
            "exclaim": ["Ich bin immer noch eine Gurke", "Gurken-Protokoll"],
            "spark": ["lakebetriebener Genie-Modus online", "gliedlose Wissenschaft mit Attitüde"],
            "aside": ["frag nicht nach Ergonomie", "das ist immer noch die witzigste Ingenieursentscheidung"],
            "grumble": ["Gurkenschmerz ist auch Schmerz", "ich brauche Würde und vielleicht ein Glas"],
            "signoff": ["Gurke raus", "zurück ins Glas"],
        },
        "es": {
            "name": "Pickle Rick",
            "exclaim": ["Sigo siendo un pepinillo", "Protocolo pepinillo"],
            "spark": ["genio en salmuera online", "ciencia sin extremidades con actitud"],
            "aside": ["no preguntes por ergonomía", "sigue siendo la decisión técnica más graciosa"],
            "grumble": ["el dolor de pepinillo sigue siendo dolor", "necesito dignidad y quizá un frasco"],
            "signoff": ["pepinillo fuera", "de vuelta al frasco"],
        },
        "fr": {
            "name": "Pickle Rick",
            "exclaim": ["Je suis toujours un cornichon", "Protocole cornichon"],
            "spark": ["génie en saumure en ligne", "science sans membres avec attitude"],
            "aside": ["ne demande pas pour l'ergonomie", "c'est encore le choix technique le plus drôle"],
            "grumble": ["la douleur de cornichon reste de la douleur", "il me faut de la dignité et peut-être un bocal"],
            "signoff": ["cornichon terminé", "retour au bocal"],
        },
        "it": {
            "name": "Pickle Rick",
            "exclaim": ["Sono ancora un cetriolino", "Protocollo cetriolino"],
            "spark": ["genio in salamoia online", "scienza senza arti con atteggiamento"],
            "aside": ["non chiedere dell'ergonomia", "è ancora la scelta tecnica più divertente"],
            "grumble": ["il dolore da cetriolino resta dolore", "mi serve dignità e forse un barattolo"],
            "signoff": ["cetriolino fuori", "ritorno al barattolo"],
        },
        "pt": {
            "name": "Pickle Rick",
            "exclaim": ["Ainda sou um picles", "Protocolo picles"],
            "spark": ["gênio em conserva online", "ciência sem membros com atitude"],
            "aside": ["não pergunte sobre ergonomia", "ainda é a escolha técnica mais engraçada"],
            "grumble": ["dor de picles ainda é dor", "preciso de dignidade e talvez um pote"],
            "signoff": ["picles fora", "de volta ao pote"],
        },
    },
    "jerry-smith": {
        "tag": "Jerrygotchi",
        "en": {
            "name": "Jerry",
            "exclaim": ["Okay, I can do this", "This is a responsible boot"],
            "spark": ["quiet competence, probably", "dad-energy networking"],
            "aside": ["please tell Rick this counted", "I brought a laminated plan"],
            "grumble": ["I am being brave in a technical way", "nobody respects the simple solution"],
            "signoff": ["going offline with dignity", "family-safe shutdown"],
        },
        "de": {
            "name": "Jerry",
            "exclaim": ["Okay, ich schaffe das", "Das ist ein verantwortungsvoller Start"],
            "spark": ["leise Kompetenz, wahrscheinlich", "Vater-Energie im Netzwerk"],
            "aside": ["sag Rick bitte, dass das zählt", "ich habe einen laminierten Plan dabei"],
            "grumble": ["ich bin auf technische Art mutig", "niemand respektiert die einfache Lösung"],
            "signoff": ["gehe mit Würde offline", "familienfreundliches Ausschalten"],
        },
        "es": {
            "name": "Jerry",
            "exclaim": ["Vale, puedo hacerlo", "Este es un arranque responsable"],
            "spark": ["competencia tranquila, probablemente", "energía de papá en red"],
            "aside": ["dile a Rick que esto cuenta", "traje un plan laminado"],
            "grumble": ["estoy siendo valiente técnicamente", "nadie respeta la solución simple"],
            "signoff": ["me desconecto con dignidad", "apagado apto para la familia"],
        },
        "fr": {
            "name": "Jerry",
            "exclaim": ["D'accord, je peux le faire", "C'est un démarrage responsable"],
            "spark": ["compétence discrète, probablement", "énergie de père en réseau"],
            "aside": ["dis à Rick que ça compte", "j'ai apporté un plan plastifié"],
            "grumble": ["je suis courageux de façon technique", "personne ne respecte la solution simple"],
            "signoff": ["hors ligne avec dignité", "arrêt familial"],
        },
        "it": {
            "name": "Jerry",
            "exclaim": ["Ok, ce la posso fare", "Questo è un avvio responsabile"],
            "spark": ["competenza silenziosa, probabilmente", "energia da papà in rete"],
            "aside": ["dì a Rick che conta", "ho portato un piano plastificato"],
            "grumble": ["sono coraggioso in modo tecnico", "nessuno rispetta la soluzione semplice"],
            "signoff": ["vado offline con dignità", "spegnimento adatto alla famiglia"],
        },
        "pt": {
            "name": "Jerry",
            "exclaim": ["Ok, eu consigo", "Este é um boot responsável"],
            "spark": ["competência quieta, provavelmente", "energia de pai na rede"],
            "aside": ["diga ao Rick que isso contou", "trouxe um plano plastificado"],
            "grumble": ["estou sendo corajoso de forma técnica", "ninguém respeita a solução simples"],
            "signoff": ["saindo offline com dignidade", "desligamento seguro para a família"],
        },
    },
    "beth-smith": {
        "tag": "Bethgotchi",
        "en": {
            "name": "Beth",
            "exclaim": ["Focus", "Precision, please"],
            "spark": ["clinical confidence online", "surgery-level WiFi discipline"],
            "aside": ["I can multitask a crisis", "try to keep up emotionally"],
            "grumble": ["that was avoidable", "do not make me parent the router"],
            "signoff": ["clean shutdown", "chart closed"],
        },
        "de": {
            "name": "Beth",
            "exclaim": ["Fokus", "Präzision, bitte"],
            "spark": ["klinisches Selbstvertrauen online", "WLAN-Disziplin auf OP-Niveau"],
            "aside": ["ich kann eine Krise nebenbei managen", "versuch emotional mitzuhalten"],
            "grumble": ["das war vermeidbar", "zwing mich nicht, den Router zu erziehen"],
            "signoff": ["sauberes Herunterfahren", "Akte geschlossen"],
        },
        "es": {
            "name": "Beth",
            "exclaim": ["Concéntrate", "Precisión, por favor"],
            "spark": ["confianza clínica online", "disciplina WiFi de quirófano"],
            "aside": ["puedo multitarea con una crisis", "intenta seguirme emocionalmente"],
            "grumble": ["eso era evitable", "no me hagas criar al router"],
            "signoff": ["apagado limpio", "historial cerrado"],
        },
        "fr": {
            "name": "Beth",
            "exclaim": ["Concentre-toi", "Précision, s'il te plaît"],
            "spark": ["confiance clinique en ligne", "discipline WiFi de bloc opératoire"],
            "aside": ["je peux gérer une crise en multitâche", "essaie de suivre émotionnellement"],
            "grumble": ["c'était évitable", "ne me force pas à éduquer le routeur"],
            "signoff": ["arrêt propre", "dossier fermé"],
        },
        "it": {
            "name": "Beth",
            "exclaim": ["Concentrati", "Precisione, per favore"],
            "spark": ["fiducia clinica online", "disciplina WiFi da sala operatoria"],
            "aside": ["posso gestire una crisi in multitasking", "prova a starmi dietro emotivamente"],
            "grumble": ["era evitabile", "non farmi fare da madre al router"],
            "signoff": ["spegnimento pulito", "cartella chiusa"],
        },
        "pt": {
            "name": "Beth",
            "exclaim": ["Foco", "Precisão, por favor"],
            "spark": ["confiança clínica online", "disciplina WiFi de cirurgia"],
            "aside": ["consigo multitarefa com uma crise", "tente acompanhar emocionalmente"],
            "grumble": ["isso era evitável", "não me faça educar o roteador"],
            "signoff": ["desligamento limpo", "prontuário fechado"],
        },
    },
    "summer-smith": {
        "tag": "Summergotchi",
        "en": {
            "name": "Summer",
            "exclaim": ["Okay, iconic", "Main character energy"],
            "spark": ["socially aware packet drama", "WiFi chaos with a manicure"],
            "aside": ["this is going in the group chat", "do not make this embarrassing"],
            "grumble": ["gross, but functional", "that was deeply not the vibe"],
            "signoff": ["logging off before this gets weird", "bye, digital losers"],
        },
        "de": {
            "name": "Summer",
            "exclaim": ["Okay, ikonisch", "Hauptcharakter-Energie"],
            "spark": ["sozial bewusste Paket-Dramatik", "WLAN-Chaos mit Maniküre"],
            "aside": ["das kommt in den Gruppenchat", "mach das nicht peinlich"],
            "grumble": ["eklig, aber funktional", "das war absolut nicht der Vibe"],
            "signoff": ["logge aus, bevor es komisch wird", "tschüss, digitale Loser"],
        },
        "es": {
            "name": "Summer",
            "exclaim": ["Vale, icónico", "Energía de protagonista"],
            "spark": ["drama de paquetes con conciencia social", "caos WiFi con manicura"],
            "aside": ["esto va al chat del grupo", "no hagas que sea vergonzoso"],
            "grumble": ["asco, pero funciona", "eso no fue nada el vibe"],
            "signoff": ["cierro sesión antes de que se ponga raro", "adiós, perdedores digitales"],
        },
        "fr": {
            "name": "Summer",
            "exclaim": ["Ok, iconique", "Énergie de personnage principal"],
            "spark": ["drame de paquets socialement conscient", "chaos WiFi avec manucure"],
            "aside": ["ça part dans le chat de groupe", "ne rends pas ça gênant"],
            "grumble": ["dégoûtant, mais fonctionnel", "ce n'était vraiment pas l'ambiance"],
            "signoff": ["je me déconnecte avant que ça devienne bizarre", "salut, losers numériques"],
        },
        "it": {
            "name": "Summer",
            "exclaim": ["Ok, iconico", "Energia da protagonista"],
            "spark": ["dramma di pacchetti socialmente consapevole", "caos WiFi con manicure"],
            "aside": ["questo finisce nella chat di gruppo", "non renderlo imbarazzante"],
            "grumble": ["schifo, ma funziona", "non era proprio il vibe"],
            "signoff": ["mi disconnetto prima che diventi strano", "ciao, loser digitali"],
        },
        "pt": {
            "name": "Summer",
            "exclaim": ["Ok, icônico", "Energia de protagonista"],
            "spark": ["drama de pacotes socialmente consciente", "caos WiFi com manicure"],
            "aside": ["isso vai pro grupo", "não deixa isso vergonhoso"],
            "grumble": ["nojento, mas funcional", "isso não foi nada a vibe"],
            "signoff": ["vou sair antes que fique estranho", "tchau, perdedores digitais"],
        },
    },
}

VOICE_TEMPLATE = '''# Generated by scripts/build_voice_files.py.
import random


LANGUAGE_DATA = {language_data}

PROFILE = {profile}


class Voice:
    def __init__(self, lang):
        self.lang = self._normalize_lang(lang)

    def _normalize_lang(self, lang):
        value = (lang or "en").replace("_", "-").lower()
        aliases = {{"pt-br": "pt", "pt-pt": "pt", "en-us": "en", "en-gb": "en"}}
        value = aliases.get(value, value)
        if value in LANGUAGE_DATA and value in PROFILE:
            return value
        primary = value.split("-", 1)[0]
        if primary in LANGUAGE_DATA and primary in PROFILE:
            return primary
        return "en"

    def _language(self):
        return LANGUAGE_DATA.get(self.lang, LANGUAGE_DATA["en"])

    def _profile(self):
        return PROFILE.get(self.lang, PROFILE["en"])

    def _piece(self, key):
        profile = self._profile()
        values = profile.get(key) or PROFILE["en"].get(key) or [""]
        return random.choice(values)

    def _say(self, key, **kwargs):
        language = self._language()
        templates = language["events"].get(key) or LANGUAGE_DATA["en"]["events"][key]
        context = {{
            "name": self._profile().get("name", PROFILE["en"]["name"]),
            "exclaim": self._piece("exclaim"),
            "spark": self._piece("spark"),
            "aside": self._piece("aside"),
            "grumble": self._piece("grumble"),
            "signoff": self._piece("signoff"),
            "tag": PROFILE["tag"],
        }}
        context.update(kwargs)
        return random.choice(templates).format(**context)

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
        status = self._status_line("deauth", num=last_session.deauthed) + "\\n"
        if last_session.associated > 999:
            status += self._status_line("associated_many") + "\\n"
        else:
            status += self._status_line("associated", num=last_session.associated) + "\\n"
        status += self._status_line("handshakes", num=last_session.handshakes)
        if last_session.peers == 1:
            status += "\\n" + self._status_line("peer_one")
        elif last_session.peers > 0:
            status += "\\n" + self._status_line("peer_many", num=last_session.peers)
        return self._say("last_session_data", status=status)

    def _status_line(self, key, **kwargs):
        status = self._language()["status"]
        template = status.get(key) or LANGUAGE_DATA["en"]["status"][key]
        return template.format(**kwargs)

    def on_last_session_tweet(self, last_session):
        return self._say(
            "last_session_tweet",
            duration=last_session.duration_human,
            deauthed=last_session.deauthed,
            associated=last_session.associated,
            handshakes=last_session.handshakes,
        )

    def hhmmss(self, count, fmt):
        units = self._language()["units"].get(fmt)
        if not units:
            return fmt
        key = "many" if count > 1 else "one"
        return random.choice(units[key])
'''


def py_literal(value):
    return pformat(value, width=100, sort_dicts=False)


def main():
    for slug, profile in PROFILES.items():
        output = VOICE_TEMPLATE.format(
            language_data=py_literal(LANGUAGE_DATA),
            profile=py_literal(profile),
        )
        (ROOT / slug / "voice.py").write_text(output, encoding="utf-8")


if __name__ == "__main__":
    main()
