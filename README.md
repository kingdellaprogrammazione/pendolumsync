# Sincronizzazione di due pendoli accoppiati

In questa repository è presente il materiale prodotto per l'esame di Sistemi Complessi della triennale in fisica di Bologna. L'oggetto dello studio è il fenomeno di sincronizzazione tra due pendoli accoppiati tramite un'asta.

# Analisi meccanica del moto di due pendoli accoppiati

![*Modello del sistema costruito con indicate le grandezze rilevanti. Le
lettere maiuscole in grassetto indicano dei punti, quelle in corsivo
delle costanti; le minuscole invece indicano le variabili.*
](./media/cad/sketch_2.pdf)

Senza considerare attriti, dalla figura si calcola la lagrangiana del sistema, a meno
di costanti, come
$$\mathcal{L} = \left(m+ \frac{M}{2}\right) \dot{d}^2 + \frac{m R^2}{2}  (\dot\theta_1^2 + \dot\theta_2^2) + m \dot{d} R (\cos\theta_1 \dot\theta_1 + \cos \theta_2 \dot \theta_2) + mgR(\cos\theta_1 + \cos \theta_2) \, .$$

## Equazioni del moto in assenza di attrito

Per proseguire è necessario approssimare la lagrangiana nel regime di
piccole oscillazioni:
$$\mathcal{L}_{PO} =  \left(m+ \frac{M}{2}\right) \dot{d}^2 + \frac{m R^2}{2}  (\dot\theta_1^2 + \dot\theta_2^2) + m \dot{d} R (\dot \theta_1 + \dot \theta_2) - \frac{m gR}{2} (\theta_1^2 + \theta_2^2) \, .
\label{lagrangianapo}$$ Si nota immediatamente che nella lagrangiana è
presente una coordinata ciclica, $d$; c'è quindi un integrale primo del
moto, cioè una quantità che resta costante durante l'evoluzione
temporale del sistema:
$$p_d = \frac{\partial \mathcal{L}_{PO}}{\partial \dot{d}} =(2m+M) \dot d + m R (\dot\theta_1 + \dot \theta_2) \, .
\label{ciclica}$$ Si può sfruttare adesso un conveniente cambio di
coordinate per gli angoli: $$\setlength\arraycolsep{0pt}
\renewcommand\arraystretch{1.25}
\left\{
\begin{array}{c}
h = \theta_1 + \theta_2  \\
q = \theta_1 - \theta_2
\end{array}
\right.
,
\label{definizionehq}$$ notando che
$$\theta_1^2 + \theta_2^2 = \frac{h^2 +q^2}{2} \, .$$ Le relazioni
precedenti valgono anche tra le derivate. Riscrivendo la lagrangiana si
ottiene
$$\mathcal{L}_{PO} =  \left(m+ \frac{M}{2}\right) \dot{d}^2 + \frac{mR^2}{4}  (\dot{h}^2 + \dot{q}^2) + m  R \dot{d}\dot{h} - \frac{mgR}{4}(h^2 + q^2) \, .$$
L'[\[ciclica\]](#ciclica){reference-type="ref" reference="ciclica"}
inoltre diventa
$$p_d = \frac{\partial \mathcal{L}_{PO}}{\partial \dot{d}} =(2m+M) \dot d + m R \dot h \, .$$
E' possibile utilizzare ora un'altra funzione, la funzione di Routh
$\mathcal{R}_{PO}$, per poter eliminare un grado di libertà nelle
equazioni del moto. Questa viene ricavata a partire dalla lagrangiana,
introducendo solamente il momento $p_d$:
$$\mathcal{R}_{PO}(h,\dot h, q, \dot q, d, p_d )  = 
p_d \dot{d}(d, p_d, h,\dot h, q, \dot q)- \mathcal{L}_{PO}(h,\dot h, q, \dot q, d, \dot{d}(d, p_d, h,\dot h, q, \dot q)) \, ,$$
dove sono state esplicitate le dipendenze dalle variabili. In
particolare si nota che nella lagrangiana bisogna scrivere $\dot d$
sfruttando l'[\[ciclica\]](#ciclica){reference-type="ref"
reference="ciclica"}. Si ottiene immediatamente
$$\mathcal{R}_{PO} = \frac{1}{2} \frac{(p_d -mR\dot h)^2}{2m + M}- \frac{mR^2}{4}  (\dot{h}^2 + \dot{q}^2) + \frac{mgR}{4}(h^2 + q^2) \, .$$
Da questa equazione si possono ricavare le equazioni del moto, le più
importanti sono $$\dot p_d = 0 \, ,
  \label{conservazione}$$ che è ovviamente coerente con la conservazione
di $p_d$ notata in [\[ciclica\]](#ciclica){reference-type="ref"
reference="ciclica"}, e $$\begin{split}
  \ddot h = -\frac{\alpha}{R} h \, ,\\
  \ddot q = - \frac{g}{R} q \, ,
  \end{split}
  \label{equazionifinalinondissipate}$$ utilizzando
l'[\[conservazione\]](#conservazione){reference-type="ref"
reference="conservazione"} e ponendo $\alpha = \frac{(2m + M) g}{M}$.
Con queste equazioni a disposizione si può completamente ricostruire il
moto del sistema. Si nota che, partendo da una situazione iniziale
arbitraria, la condizione di sincronizzazione in fase equivale alla
richiesta che $q$ tenda a zero, mentre quella in controfase equivale
alla richiesta che $h$ tenda a zero. Occorre fare attenzione al fatto
che però nella soluzione in
[\[equazionifinalinondissipate\]](#equazionifinalinondissipate){reference-type="ref"
reference="equazionifinalinondissipate"} sia $h$ che $q$ descrivono moti
oscillatori con frequenza rispettiva
$\omega_h = \sqrt{\frac{\alpha}{R} \vphantom{\frac{g}{R}}}$ e
$\omega_q = \sqrt[]{\frac{g}{R}}$. Le uniche soluzioni per cui i pendoli
oscillano sincronizzati sono quelle per cui una tra $h$ o $q$ è nulla
all'inizio del moto, restando quindi nulla per tutti gli istanti
successivi. Il moto evidentemente non converge ad una soluzione
particolare, attraversa invece entrambe le configurazioni di
sincronizzazione permanendo per il resto degli istanti in una
combinazione delle due soluzioni. []{#sezionesenzaattrito
label="sezionesenzaattrito"}

## Equazioni del moto in presenza di attrito {#sezioneattrito}

Affinchè il moto converga ad una soluzione particolare, come accade
nella realtà, è necessario tenere conto dei fenomeni dissipativi.
Potrebbe ad esempio essere considerato l'attrito che si sviluppa nel
perno dei pendoli, quello generato dal movimento delle ruote dei
carrelli, sia radente che volvente, e quello tra l'aria e le varie
componenti mobili. Si supponga di voler includere nelle equazioni del
moto un termine proporzionale alle velocità angolari $\dot \theta_1$ e
$\dot \theta_2$, con costante comune di proporzionalità $\gamma$, avente
le dimensioni di una frequenza. Riscrivendo le equazioni del moto per
queste due variabili, ricavandole dalla lagrangiana in
[\[lagrangianapo\]](#lagrangianapo){reference-type="ref"
reference="lagrangianapo"} e semplificando i fattori in comune si
ottiene $$R \ddot \theta_i + \ddot d = - g  \theta_i , \qquad i =1,2$$ e
si nota che è possibile aggiungere al secondo membro, in cui sono
scritte le forze generalizzate, l'attrito citato sopra, agente
ovviamente in verso opposto alla velocità:
$$R \ddot \theta_i + \ddot d = - g \theta_i  - \gamma   \dot \theta_i, \qquad i =1,2 \, .$$
Sostituendo la derivata
dell'[\[ciclica\]](#ciclica){reference-type="ref" reference="ciclica"}
$$(2m + M) \ddot d = -mR (\ddot \theta_1 + \ddot \theta_2)$$
nell'equazione precedente si giunge alla coppia di equazioni:
$$R \ddot \theta_i -\frac{m}{2m + M}R (\ddot \theta_1 + \ddot \theta_2) 
  = - g \theta_i  - \gamma   \dot \theta_i \, , \qquad i =1,2 \, ,$$ che
dopo qualche passaggio algebrico si possono riscrivere con le variabili
$h$ e $q$: $$\begin{split}
  (R- \frac{2m}{2m + M}R) \ddot h + \gamma \dot h + g h  = 0 \, , \\
  R \ddot q +\gamma \dot q + g q = 0 \, .
  \end{split}$$ Manipolando algebricamente questa equazione, ridefinendo
la costante $\gamma$ e utilizzando le frequenze definite in precedenza
si giunge infine a $$\begin{split}
  \ddot h + \gamma \dot h + \omega_h^2 h  = 0 \, ,\\
  \ddot q +\gamma \dot q + \omega_q^2 q = 0 \, .
  \end{split}$$ La considerazione decisiva per osservare il fenomeno
della sincronizzazione consiste nel considerare la costante $\gamma$
diversa per i due modi di oscillazione; differenziando le nuove costanti
con un pedice, si tiene conto di effetti dissipativi che influenzano in
modo differente il modo di oscillazione in fase rispetto a quello in
controfase. Le soluzioni generali di queste equazioni sono del tipo:
$$\begin{aligned}
    h(t) &= A_h e^{- \frac{\gamma_h}{2} t} \cos(\tilde{\omega}_h t + \beta_h) \label{equazionefinaleh} \, , \\
    q(t) &= A_q e^{- \frac{\gamma_q}{2} t} \cos(\tilde{\omega}_q t + \beta_q) \label{equazionefinaleq} \, ,
\end{aligned}$$ con $A_h$, $A_q$, $\beta_h$ e $\beta_q$ costanti reali,
e dove
$$\tilde{\omega}_i = \sqrt{\omega_i^2 -\left( \frac{\gamma_i}{2} \right)^2} \qquad 
i = h,q 
\, .
\label{equation:omegadef}$$ È evidente quindi che se le costanti
$\gamma$ sono diverse, l'ampiezza di uno di questi due modi va a zero
più velocemente rispetto all'altro, sincronizzando il moto.

# Apparato sperimentale

## Materiale utilizzato

Durante l'esperimento sono stati coinvolti diversi elementi, tra cui:

1.  rotaia e carrellini[^1], mostrati in
    [3](#photo_crane){reference-type="ref" reference="photo_crane"}, con
    basso coefficiente di attrito solitamente utilizzati in esperimenti
    relativi alla conservazione della quantità di moto;

2.  due alte sedie in legno;

3.  filo di nylon trasparente;

4.  due strutture identiche, mostrate in
    [3](#photo_crane){reference-type="ref" reference="photo_crane"},
    progettate autonomamente e stampate in 3D;

5.  scotch di carta;

6.  monete varie;

7.  spago da cucina;

8.  supporti in legno per spiedini.

<figure id="photo_crane">
<img src="../../media/img/rail_processed.png" style="width:90.0%" />
<img src="../../media/img/crane_rail-processed.png"
style="width:90.0%" />
<figcaption><em>Il pendolo (sinistra) e la struttura stampata in 3D dopo
l’assemblaggio (destra).</em></figcaption>
</figure>

## Strumenti di misura

Per quanto riguarda gli strumenti di misura, sono stati invece
utilizzati:

1.  bilancia da cucina (risoluzione 1 g);

2.  macchina fotografica semi-professionale;

3.  treppiede per macchina fotografica;

4.  metro estendibile (risoluzione 1 mm);

5.  livella a bolla;

6.  libreria di object tracking della suite OpenCV[^2].

## Realizzazione pratica del modello

Inizialmente la realizzazione del progetto era stata pensata tramite una
rotaia a cuscino d'aria, per poter studiare il fenomeno, nella sua parte
transiente, per un periodo di tempo lungo, grazie al poco attrito;
questa idea però è stata abbandonata dopo alcuni tentativi per le
numerose difficoltà sperimentali. In
[\[photo_crane_air\]](#photo_crane_air){reference-type="ref"
reference="photo_crane_air"} è mostrato uno dei modelli di supporto
progettati e stampati in 3D montabili sui carrellini della rotaia. In
seguito si è provato ad usare delle costruzioni giocattolo per la
creazione di una rotaia e carrellini; purtroppo anche questo tentativo è
stato accantonato a causa di notevoli imperfezioni e mancanza di
allineamento tra i vari pezzi di rotaia. Un esempio di una parte della
costruzione è mostrato in [4](#photo_lego){reference-type="ref"
reference="photo_lego"}.

<figure id="photo_lego">
<img src="../../media/img/crane_air-processed.png"
style="width:90.0%" />
<img src="../../media/img/lego_cart-processed.png"
style="width:90.0%" />
<figcaption><em>Il modellino realizzato a partire da costruzioni
giocattolo.</em></figcaption>
</figure>

In seguito si è pensato quindi di utilizzare un'altro tipo di rotaia di
laboratorio, dotata di carrellini con ruote. La progettazione del
modello si è rivolta, una volta recuperata l'apparecchiatura di
laboratorio, alla costruzione dei supporti, disegnati tramite un
software di modellizzazione tridimensionale e stampati con una stampante
3D. Una volta stampati diversi prototipi e scelto quello migliore sono
state incollate tra loro le due parti costituenti il pezzo finale
indicato in [3](#photo_crane){reference-type="ref"
reference="photo_crane"}, i cui modelli sono mostrati in
[5](#photo_piece){reference-type="ref" reference="photo_piece"}, e,
incastrato il pezzo sopra ciascun carrellino, si è costruito il supporto
tramite due alte sedie sopra le quali è stata posta la rotaia.

![*Le parti della struttura mostrata in
[3](#photo_crane){reference-type="ref" reference="photo_crane"},
visualizzate nel programma di modellazione
3D.*](../../media/img/fusion_project_cut.png){#photo_piece width="90%"}

È fondamentale sottolineare come si siano scelte le sedie più alte
disponibili, in quanto la lunghezza del pendolo doveva essere grande per
permettere poi l'uso dell'approssimazione di piccole oscillazioni, non
impedendo la chiara manifestazione del fenomeno della sincronizzazione.
I carrellini sono poi stati collegati tra loro tramite due bastoncini di
legno solitamente utilizzati per la cottura degli spiedini. La massa
complessiva dei due carrellini, considerando il connettore trascurabile,
è risultata essere pari a 160 ± 1 g. È stato controllato che lo sfondo
presente dietro le due sedie fosse inoltre fisso, ossia privo di oggetti
in movimento, per favorire il processo di tracking. A questo punto sono
stati costruiti i due pendoli identici, tramite svariate monete
raggruppate saldamente insieme grazie all'uso dello scotch di carta,
pesanti ciascuno 139 ± 1 g. Le monete sono state scelte per la loro
elevata densità e modularità: è stato possibile infatti costruire
diversi pendoli, di dimensioni pressochè uguali ma di masse
sensibilmente diverse gli uni dagli altri. Sono quindi stati tagliati
due pezzi approssimativamente uguali di filo di nylon, lunghi abbastanza
da sfruttare l'intera altezza fornita dalle due sedie, e sono poi stati
agganciati ai pendoli tramite un pezzo di una nota marca di costruzioni
giocattolo. Questi due tratti di filo sono stati poi regolati, con
l'ausilio del metro, tramite la realizzazione di un numero adeguato di
avvolgimenti nel perno di aggancio, fino ad ottenere una lunghezza del
pendolo $R$ = 85 ± 1 cm ciascuno (l'incertezza è maggiore della
risoluzione del metro per tenere conto di errori nella valutazione del
centro di massa dei pendoli). È importante notare che, per far sì che i
pendoli oscillassero nello stesso piano spaziale per tutta la durata
dell'esperimento, i pendoli stessi fossero liberi di muoversi lungo
l'ansa creata dal filo di nylon appeso ai carrellini. A questo punto al
pendolo di destra è stato collegato un breve tratto di spago per
consentirne la manovra da una posizione che non interferisse con il
tracking. Di fronte a questa apparecchiatura, a una distanza di circa
1.5 m, è stato posizionato il treppede con sopra la macchina
fotografica, per l'acquisizione del video. L'obiettivo della macchina
fotografica è stato accuratamente posizionato, per evitare offset
prospettici in un unico verso, su un piano parallelo a quello di
oscillazione dei pendoli e la sua proiezione è stata fatta
approssimativamente coincidere con il centro della circonferenza
passante per i due carrellini e i due pendoli a riposo. L'apparato
sperimentale completo è mostrato in [6](#setup_exp){reference-type="ref"
reference="setup_exp"}

![*Schema dell'apparato sperimentale visto dalla
fotocamera.*](../../media/img/setup_exp.png){#setup_exp width="60%"}

## Esecuzione dell'esperimento

Una volta sistemati tutti gli elementi, sono stati acquisiti differenti
video del fenomeno, avendo la cura di avere una condizione iniziale
statica, con i tutti gli elementi fermi rispetto al sistema di
riferimento della stanza. Questa ipotesi è stata realizzata inizialmente
collegando, dopo aver fermato il pendolo di sinistra, con un lungo spago
fatto circolare attorno all'apparato, il pendolo e il carrello di
destra. In questo modo si puntava ad eliminare l'errore dato dalla non
coincidenza degli istanti di rilascio dei due elementi, che sarebbero
invece stati messi in moto nello stesso momento al taglio dello spago.
Questo sistema, però, è risultato inadatto in quanto lo spago, una volta
tagliato, continuava a disturbare il movimento dell'apparecchio
introducendo un nuovo attrito e distorcendo il fenomeno. Si è provato
quindi ad agire nel modo più semplice: fermando il pendolo di sinistra,
trattenendo con una mano il carrellino di destra e con l'altra lo spago
collegato al rispettivo pendolo. Successivamente sono stati effettuati
diversi rilasci, ed è stato scelto per l'analisi il video in cui il
pendolo e il carrellino di sinistra venivano sganciati
approssimativamente nello stesso istante. I video sono stati registrati
con la risoluzione di 1920 x 1080 pixel, ad un framerate di 25 FPS.
[]{#sezione_realizz label="sezione_realizz"}

## Scrittura dei programmi per l'acquisizione e l'elaborazione dati

Per quanto riguarda la scrittura dei programmi, si è scelto di
utilizzare la libreria OpenCV, che sta per Open Computer Vision, una
libreria open source utilizzabile in particolare nel linguaggio di
programmazione C++, destinata all'analisi di immagini e video. In questo
esperimento la libreria è stata utilizzata nel per tracciare il
movimento nel tempo dei pendoli e dei carrellini, in maniera
automatizzata. E' stato utilizzato il C++ per la nota velocità in
esecuzione rispetto a python. Il codice è listato in
[\[listatocpp\]](#listatocpp){reference-type="ref"
reference="listatocpp"}. Il codice inizialmente acquisisce il percorso
di memorizzazione del file video, per poi permettere all'utente di
scegliere prima l'oggetto da tracciare e poi il numero progressivo
dell'acquisizione. In seguito viene chiesto all'utente di disegnare un
rettangolo attorno all'oggetto di interesse, partendo dal suo centro.
L'algoritmo di tracking, in questo caso KCF[^3], inizia poi a processare
i vari frame, seguendo l'oggetto e scrivendo nel file le coordinate in
pixel del centro del rettangolo (l'origine è nell'angolo in alto a
sinistra e gli assi sono diretti verso destra e verso il basso). Vari
momenti del processo appena descritto sono mostrati in
[7](#photo_tracking){reference-type="ref" reference="photo_tracking"}.

<figure id="photo_tracking">
<img src="../../media/img/tracking_1.png" style="width:90.0%" />
<img src="../../media/img/tracking_2.png" style="width:90.0%" />
<img src="../../media/img/tracking_3.png" style="width:90.0%" />
<figcaption><em>Tre istanti del processo di tracking dell’oggetto.
Nell’immagine a sinistra si osserva il momento di selezione del pendolo,
tracciando un rettangolo blu attorno allo stesso. Nelle altre due
immagini sono mostrati due screenshot effettuati alla finestra di
tracking, mentre l’algoritmo traccia l’oggetto desiderato, spostando il
rettangolo blu. Nell’immagine a sinistra si nota anche un istante del
processo di rilascio descritto in <a href="#sezione_realizz"
data-reference-type="ref"
data-reference="sezione_realizz">[sezione_realizz]</a></em></figcaption>
</figure>

L'utente può e deve fermare l'acquisizione nel caso noti che il
rettangolo scompaia, accompagnato dal messaggio *Tracking failure
detected*, relativo al caso in cui l'algoritmo non riesca a identificare
la posizione dell'oggetto in un determinato frame.

In seguito all'acquisizione di vari set dati, nel nostro caso 4 per ogni
oggetto, per cercare di limitare eventuali errori di posizione, è stata
fatta una media tramite il programma in
[\[listatoavg\]](#listatoavg){reference-type="ref"
reference="listatoavg"}, stavolta scritto in python per elasticità nella
gestione dei dati in lettura e scrittura. Sono così stati prodotti
quattro files finali, uno per ogni elemento mobile.

Infine, nel listato in
[\[listatoplotter\]](#listatoplotter){reference-type="ref"
reference="listatoplotter"}, sono stati letti i quattro files citati
sopra, e sono stati poi ricavati con considerazioni trigonometriche gli
angoli indicati in [2](#pendolicorpolibero){reference-type="ref"
reference="pendolicorpolibero"} come $\theta_1$ e $\theta_2$. Sono
quindi stati scelti degli intervalli temporali appropriati per
effettuare i fit di funzioni del tipo presentato in
[\[equazionefinaleh,equazionefinaleq\]](#equazionefinaleh,equazionefinaleq){reference-type="ref"
reference="equazionefinaleh,equazionefinaleq"}, in particolare scartando
i punti iniziali in cui l'apparecchio è fermo, oppure gli ultimi qualora
il fenomeno da osservare non fosse più presente.

# Risultati e discussione

Il grafico degli angoli $\theta_1$ e $\theta_2$ di
[2](#pendolicorpolibero){reference-type="ref"
reference="pendolicorpolibero"} al trascorrere del tempo, mediato sul
numero di acquisizioni effettuate, è mostrato in
[8](#angles_full){reference-type="ref" reference="angles_full"}, mentre
è presente uno zoom sugli istanti iniziali in
[9](#anlges_accurate){reference-type="ref" reference="anlges_accurate"},
e uno zoom sui massimi in [10](#angles_decrease){reference-type="ref"
reference="angles_decrease"}, in cui i punti sono stati collegati da
linee continue.

![*Grafico completo dei due angoli $\theta_1$ e $\theta_2$ al
trascorrere del tempo.* ](../../media/plot/angles_full.pdf){#angles_full
width="80%"}

![*Grafico dei due angoli $\theta_1$ e $\theta_2$ al trascorrere del
tempo. Zoom sugli istanti iniziali.*
](../../media/plot/angles_accurate.pdf){#anlges_accurate width="80%"}

![*Grafico dei due angoli $\theta_1$ e $\theta_2$ al trascorrere del
tempo, dettaglio delle creste. Si nota come la diminuzione delle
ampiezze sia di intensità differente.*
](../../media/plot/angles_decrease.pdf){#angles_decrease width="80%"}

In [8](#angles_full){reference-type="ref" reference="angles_full"} si
nota come, dopo un breve periodo iniziale di quiete, in cui il pendolo
$\mathbf{P}_1$ si trova in quiete, mentre il pendolo $\mathbf{P}_2$
descrive piccole oscillazioni dell'ampiezza di circa 1°, che si è
cercato di ridurre il più possibile manualmente, il sistema viene
lasciato libero di evolvere: il dettaglio è presente in
[9](#anlges_accurate){reference-type="ref" reference="anlges_accurate"}.
Dopo un momento di transizione, in cui i pendoli e i carrellini
descrivono il loro complicato moto, circa dall'istante 4.6 all'istante
8.5, il sistema mantiene il suo moto nella condizione di oscillazioni in
controfase, quindi con i carrellini necessariamente fermi, per la
conservazione della quantità di moto iniziale, nulla. I pendoli quindi
sono stati sincronizzati. È facile osservare come $\mathbf{P}_1$, che
parte da fermo, non ha delle oscillazioni centrate sugli 0°, errore
probabilmente dovuto al tracciamento effettuato in prospettiva. Si
tratta di un errore che, seppur minimo, è sistematico e si continua a
manifestare in tutto il moto, con la traslazione verso l'alto di tutto
il grafico di circa 1°. Nella
[10](#angles_decrease){reference-type="ref"
reference="angles_decrease"}, dove i punti sono stati collegati da una
linea continua nell' intento di essere più chiari, si nota come sia
presente un'evidente differenza nelle oscillazioni dei due pendoli:
l'ampiezza del pendolo $\mathbf{P}_2$ risulta decrescere più rapidamente
rispetto all'altra: un probabile effetto di un maggiore attrito
influente sul pendolo stesso, ad esempio a livello del perno. Non si
tratta infatti di un offset prospettico in quanto dalla
[8](#angles_full){reference-type="ref" reference="angles_full"} è
evidente come la diminuzione dell'ampiezza sia presente simmetricamente,
anche a livello dei minimi di oscillazione.

Possono quindi essere costruite e analizzate le variabili $h$ e $q$,
definite nel sistema e mostrate al variare del tempo nelle
[\[fit_h,fit_q\]](#fit_h,fit_q){reference-type="ref"
reference="fit_h,fit_q"}. In queste due figure sono anche presenti i due
fit delle equazioni teoriche che dovrebbero regolare, secondo le ipotesi
indicate in [2.2](#sezioneattrito){reference-type="ref"
reference="sezioneattrito"}, il moto delle due variabili, ossia le
[\[equazionefinaleh,equazionefinaleq\]](#equazionefinaleh,equazionefinaleq){reference-type="ref"
reference="equazionefinaleh,equazionefinaleq"}. In basso nelle figure
sono mostrati anche i residui, ossia la differenza , calcolata punto per
punto, tra i valori del fit e quelli dei punti acquisiti.

![*Modello del sistema costruito con indicate le grandezze rilevanti. Le
lettere maiuscole in grassetto indicano dei punti, quelle in corsivo
delle costanti; le minuscole invece indicano le variabili. In basso il
grafico dei residui.* ](../../media/plot/fit_h.pdf){#fit_h width="80%"}

![*Modello del sistema costruito con indicate le grandezze rilevanti. Le
lettere maiuscole in grassetto indicano dei punti, quelle in corsivo
delle costanti; le minuscole invece indicano le variabili. In basso il
grafico dei residui.* ](../../media/plot/fit_q.pdf){#fit_q width="80%"}

È evidente come non siano presenti pattern che possano dare l'idea di un
qualche effetto sistematico che si potrebbe star trascurando; invece si
può ragionevolmente ipotizzare la sola presenza di errori casuali, anche
dovuti all'imprecisione del metodo di acquisizione, come si nota dalla
distribuzione più o meno casuale dei punti.

Alcuni dubbi sorgono osservando la [11](#fit_h){reference-type="ref"
reference="fit_h"} , in particolare gli istanti successivi agli 8 s:
sembra permanga un'oscillazione residua, che si traduce in una non
esatta sincronia nel movimento dei pendoli; praticamente quando un
pendolo si trova in una posizione l'altro non si trova nella posizione
simmetrica, ma leggermente spostato da questa. L'origine di questo
fenomeno non sembra essere dovuto al differente attrito presente sui due
perni, mostrato in [10](#angles_decrease){reference-type="ref"
reference="angles_decrease"}, in quanto l'oscillazione residua si
mantiene anche al diminuire dell'ampiezza delle oscillazioni del pendolo
più smorzato; il fenomeno potrebbe invece essere provocato dalla minima
differenza di lunghezza dei pendoli, o semplicemente dalla predominanza
di fenomeni di attrito statico su quelli dinamici. Infatti, quando i
carrellini si fermano, circa agli 8.5 s, interviene non più l'attrito
dinamico ma quello statico, che è caratterizzato da una maggiore
intensità è quindi immune a minime deviazioni che si potrebbero
manifestare nella asincronia del moto.

Per quanto riguarda gli errori sulle acquisizioni di posizione, questi
non sono stati stimati a causa della mancanza di informazioni sulla
confidenza dell'algoritmo di tracking.

I parametri delle funzioni $h(t)$ e $q(t)$ , stimati dal fit, sono
elencati rispettivamente nelle
[\[parametrih,parametriq\]](#parametrih,parametriq){reference-type="ref"
reference="parametrih,parametriq"}. In tabella è indicata anche la somma
degli scarti quadratici tra il fit e i punti, il $\chi^2_h$, indicatore
numerico della bontà del fit.

::: {#parametriq}
    Parametri $h(t)$   
  -------------------- ----------------
         $A_h$            92 \\pm 5°
       $\gamma_h$       0.77 ± 0.02 Hz
   $\tilde{\omega}_h$   5.17 ± 0.01 Hz
       $\beta_h$         1.63 ± 0.06
       $\chi^2_h$            29.6

  : *Parametri ottenuti dal fit della funzione $q(t)$ .*
:::

::: {#parametriq}
    Parametri $q(t)$   
  -------------------- ----------------------
         $A_q$            14.85 \\pm 0.01°
       $\gamma_q$       0.00631 ± 0.00006 Hz
   $\tilde{\omega}_q$   3.40231 ± 0.00003 Hz
       $\beta_q$           0.275 ± 0.001
       $\chi^2_q$               26.1

  : *Parametri ottenuti dal fit della funzione $q(t)$ .*
:::

In realtà il fit è stato effettuato anche con un ulteriore grado di
libertà, aggiungendo un parametro responsabile della traslazione dei
grafici delle funzioni rispetto all'asse $y$; questo non è stato però
riportato in quanto per il miglior fit tale parametro restava nullo.

Calcolando poi i valori delle frequenze $\omega$, definite in
[\[sezionesenzaattrito\]](#sezionesenzaattrito){reference-type="ref"
reference="sezionesenzaattrito"}, e notando che per i valori di $\gamma$
ottenuti dai fit $\omega_i^2 \gg \left( \frac{\gamma_i}{2} \right)^2$, e
conseguentemente in
[\[equation:omegadef\]](#equation:omegadef){reference-type="ref"
reference="equation:omegadef"} si ha $\tilde{\omega}_i \approx \omega_i$
per $i=h,q$, si ottiene: $$\begin{aligned}
\tilde{\omega}_h \approx \omega_h = \SI{5.62 \pm 0.04}{\hertz} \, , \\
\tilde{\omega}_q \approx \omega_q = \SI{3.40 \pm 0.02}{\hertz} \, ,
\end{aligned}$$ dati che risultano essere in accordo quasi soddisfacente
con i risultati del fit delle
[\[parametrih,parametriq\]](#parametrih,parametriq){reference-type="ref"
reference="parametrih,parametriq"}. È presente una maggiore discordanza
per quanto riguarda $\omega_h$, dell'8%, dovuta alle varie sorgenti di
errore citate in precedenza ma anche al minor numero di punti
disponibili per il fit.

Notiamo infine che la stima dei coefficienti di attrito data dal fit è
in accordo con l'idea intuitiva legata alla caratteristica del modo di
oscillazione in cui il carrello è fermo, ossia alla minor dissipazione
di energia rispetto a quello in cui il carrello oscilla in opposizione
di fase rispetto ai pendoli; ciò è dovuto soprattutto al maggiore
attrito generato durante lo scorrimento sulla rotaia che si somma al
normale attrito generato sul perno dalle oscillazioni dei pendoli.
Questa sorgente di attrito è circa di 2 ordini di grandezza superiore
rispetto all'altra.

# Conclusioni

In conclusione, è stata osservata con successo la sincronizzazione di
due pendoli, ossia la diminuzione dell'ampiezza a zero di un modo
normale di oscillazione del sistema, fatto dovuto a differenti tassi di
dissipazione di energia nei due modi appena citati. I due coefficienti
$\gamma_h$ e $\gamma_q$ sono stati stimati essere pari rispettivamente a
0.77 ± 0.02 Hz e 0.00631 ± 0.00006 Hz.

# Appendice

Nei seguenti listati sono presenti i file con i quali sono stati
estratti e visualizzati i dati dell'esperimento.

[]{#listatoplotter label="listatoplotter"}

[^2]: https://opencv.org/

[^3]: https://arxiv.org/abs/1404.7584
