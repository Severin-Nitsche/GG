**Was ist KI**

Eine KI ist ein Computerprogramm, dass dazu entwickelt wurde Aufgaben zu übernehmen. Sie unterscheidet sich von einem traditionellem Algorithmus in der Hinsicht, dass sie die Logik, die zur Lösung des Problems führt, nicht vorgegeben bekommt sondern selbst herausfindet.

Diese Methode hat gleich mehrere Vorteile:

Erstens muss man bei komplexen Problemen, wie zum Beispiel der Vorhersage des Wetters oder der Börse, nicht die zu Grunde liegenden Regeln herausfinden. Und
zweitens kann sie sich an veränderte Umstände anpassen.

Generell werden KIs in zwei Gruppen eingeteilt:

**schwache KIs**, das sind künstliche Intelligenzen, die auf ein Problem spezialisiert sind und daher nicht anderweitig anwendbar sind.

und **starke KIs**, diese sollen im Gegensatz zu ihren spezialisierten Gegenstücken generell anwendbar sein und den mentalen Fähigkeiten eines Menschen entsprechen oder diese sogar übersteigen. Jedoch war es der Wissenschaft bis heute leider noch nicht möglich eine solch starke KI zu erschaffen.

**Genetic Algorithms, NEAT and Neural Networks**

Sicherlich hast du wenigstens einen dieser Ausdrücke schon einmal gehört, doch vermutlich nicht verstanden, was dahinter steckt. Das wollen wir jetzt ändern.

Fangen wir mit dem Genetic Algorithm an.<br />
Der Ausdruck Genetischer Algorithmus, kurz GA, mag Anfangs ein bisschen verwirrend klingen, schließlich können Computer Programme nicht mal eben Kinder machen. Dennoch ist genau das die Idee hinter einem solchem GA, der bereits in den 50er Jahren von John Holland, einem Professor der University of Michigan, beschrieben wurde: Der Code soll sich durch Rekombination zur optimalen Lösung hin entwickeln. Also wird nach den drei Prinzipien, der Evolution gehandelt: Vererbung, Variation und Selektion.

Konkret sieht der Algorithmus dann folgendermaßen aus:

**Schritt 1:** *Initialisieren. Erstelle eine Population mit zufälligen Elementen*

**Schritt 2:** *Selektion. Errechne die Fitness der einzelnen Elemente und erstelle einen entsprechenden Paarungspool.*

**Schritt 3:** *Reproduktion. Wiederhole N mal:*
	
	a) Wähle Eltern aus dem Mating pool aus
	b) Überkreuzung—erzeuge ein Kind aus der DNA der Eltern
	c) Mutation—verändere die DNA des Kindes anhand einer gewissen Mutationsrate
	d) Füge das Kind zu einer neuen Population hinzu

**Schritt 4:** *Tausche die alte mit der neuen Population aus und kehre zu Schritt zwei zurück.*

Keine Sorge, wenn das jetzt alles ein bisschen verwirrend klingt. Gehen wir die Schritte mal anhand eines kleinen Beispiels durch.

**Der tippende Affe**

Stell dir vor du hast einen Käfig voller Affen und Schreibmaschinen. In diesem Käfig schreiben die Affen alle unterschiedliche Dinge mit den Schreibmaschinen, jedoch schreibt jeder Affe immer nur das gleiche. Dein Ziel ist es einen Affen zu züchten, der den berühmten Satz: "Sein, oder nicht sein: Das ist hier die Frage" aus Hamlet aufschreibt. Zugegebenermaßen ein etwas komisches Vorhaben, doch erstmal ein gutes Beispiel um die Funktionsweise eines GA zu beschreiben.<br />
Um jetzt einen Sinnvollen Algorithmus schreiben zu können beginnen wir zuerst damit die Affen auf ihren Kern, beziehungsweise ihre DNA, zu reduzieren. Den Text den sie schreiben. Codetechnisch sind unsere Affen jetzt also Strings.<br />
Beginnen wir mit *Schritt 1*, dem Erstellen einer Population mit zufälligen Elementen, sagen wir 1000. Diese Population lässt sich gut in einem Array darstellen, den wir im Anschluss nun mit Hilfe einer for-Schleife initialisieren können.<br />
In *Schritt 2* heißt es, dass wir die Fitness der einzelnen Elemente berechnen und anschließend einen entsprechenden Paarungsool erstellen sollen. Da wir das Ziel der Affen kennen lässt sich die Fitness-Funktion ganz einfach mit der Anzahl der richtigen Buchstaben abbilden. Das müssen wir jetzt nur noch für alle Elemente machen, also Zeit für eine weitere for-Schleife. Der Teil mit dem Paarungspool hingegen ist schon etwas schwieriger umzusetzen, dennoch ist auch er kein Problem. Allerdings müssen wir zuerst klarstellen, was ein Paarungspool überhaupt ist.<br />
Hierfür könnt ihr euch das ein bisschen vorstellen, wie auf dem Jahrmarkt beim Lose kaufen. Dort habt ihr einen Eimer in dem viele Nieten und  wenig Gewinne sind. Und unser Paarungspool ist im Prinzip das selbe, nur wollen wir anstelle von ganz vielen Nieten, ganz viele Gewinne hinein tun. In anderen Worten: Je fitter ein Affe ist, desto öfter kommt er in den Pool.<br />
Alles in allem wird unser Paarungspool also wieder als weiteres Array umgesetzt.<br />
Zeit für *Schritt 3*.<br />
Hier sollen wir für jedes neue Element Eltern festlegen, die dann so freundlich sind und das Ungeborene zeugen.
Und um diesen Zeugungsakt besser zu verstehen begeben wir uns nun auf einen kleinen Ausflug in die Biologie der Meiose.
Hier wird die DNA der Eltern jeweils aufgeteilt und mit der vom Partner zusammengeführt um die des Kindes zu bilden.
Wenn wir dieses Prinzip jetzt auf unsere Affen anwenden nehmen wir uns also einen beliebigen Trennpunkt, der bestimmt, welche DNA von Elter A und welche von Elter B stammen wird.<br />
Fast geschafft.<br />
Jetzt müssen wir das Kind nur noch mutieren und anschließend zur neuen Generation hinzufügen.
Dafür gehen wir nun alle Buchstaben beziehungsweise Gene des Affen durch und entscheiden basierend auf einer gewissen Mutationsrate, ob der Buchstabe bleibt, oder ob er durch einen neuen ersetzt wird.<br />
Schnell das Kind noch in die neue Population eingefügt und diese Prozedur für alle Zukünftigen Elemente wiederholt.
Und schon sind wir bei *Schritt 4*.<br />
Hier tauschen wir dann die alte Generation mit der neuen aus und kehren anschließend zu *Schritt 2* zurück.

Wenn wir diesen Algorithmus jetzt mit einer Mutationsrate von 1% und einer Populationsgröße von 1000 für etwa 2 Sekunden laufen lassen bekommen wir auch schon den gewünschten Satz heraus, was wesentlich besser ist als die erwarteten 9.719.096.182.010.563.073.125.591.133.903.305.625.605.017 Jahre, die der Algorithmus voraussichtlich gebraucht hätte, wenn wir versucht hätten diesen Satz (in engl. ohne Satzzeich.) komplett zufällig zu generieren.

Kommen wir nun zu **Neuronalen Netzwerken**, oder besser gesagt zu künstlichen Neuronalen Netzwerken, denn wenn wir in den Computer Wissenschaften von einem solchem sprechen meinen wir weniger das Aktuelle Gehirn eines biologischen Wesens, sondern eher den Versuch seine Funktionsweise nachzubilden.
Aber zuerst: *Was ist ein Neuronales Netzwerk überhaupt und wofür brauchen wir es?*

Um diese Frage zu beantworten begeben wir uns nun ein weiters Mal auf einen Exkurs in die Biologie und klären den Begriff Neuron.
Ein Neuron besteht aus:<br />
[Dendriten, Soma und dem Axon](https://de.serlo.org/biologie/biologie-menschen/nervensystem-neuron/aufbau-neurons).
Die Dendriten kann man als eingaben in das Neuron betrachten, sie feuern nämlich basierend auf äußerlichen Einwirkungen, wie zum Beispiel Licht, kleine elektrische Impulse, die, wenn sie im Soma einen gewissen Schwellwert überschreiten das Axon dazu veranlassen weitere Signale an andere Neuronen oder Muskeln zu senden.
Damit haben wir dann auch schon fast die Netze abgedeckt. Sie sind einfach Verbindungen zwischen verschiedenen Neuronen, die von uns einen Input, z.B. eine Handgeschriebene Zahl bekommen, und am Ende einen Output liefern, in unserem Fall also dann den Wert der Zahl.

Aufgrund ihrer strukturellen Ähnlichkeit zum menschlichen Gehirn finden neuronale Netze dann Anwendung in Bereichen, die bisher schwer für Computer, aber einfach für Menschen waren. Die sogenannten easy-for-a-human, difficult-for-a-machine tasks, wie zum Beispiel Gesichtserkennung, oder andere Klassifizierungsprobleme.

Doch bevor wir jetzt mit *NEAT* weitermachen, sollten wir uns als erstes die Frage stellen, wie neuronale Netzwerke überhaupt lernen. Und um das zu verstehen müssen wir nochmal einen genaueren Blick auf ihre Struktur werfen.<br />
Bis jetzt wissen wir, dass ein Neuron genau dann feuert, wenn die vereinten Inputs einen gewissen [Schwellwert](https://de.wikipedia.org/wiki/Sigmoidfunktion "Modellierung mithilfe der Sigmoidfunktion") überschreiten und durch mehrere verbundene Neuronen komplexe Entscheidungen getroffen werden können. Doch das ist nicht alles, denn verschiedene Verbindungen können unterschiedlich stark dein. So kann es dann sein, dass zwei Verbindungen, die an ein und das selbe Neuron angeschlossen sind unterschiedlich große Signale weitertragen, und das nur, weil ihre Stärke, oder wie man es in der Fachsprache sagen würde Gewichtung unterschiedlich ist.

Traditionelle Lernalgorithmen, wie Backpropagation mit Gradient descent oder Neuroevolution (NE), setzen dann genau hier an der Stelle an und verändern diese Gewichtungen je nach bedarf um ein möglichst optimales Ergebnis zu erzielen. Dazu verwenden sie dann eine vorbestimmte Netzstruktur, die mit zufälligen Gewichten initialisiert wurde.<br />
**NEAT**, oder in lang: Neuro Evolution of Augmenting Topologies, geht noch einen Schritt weiter hier wird nämlich die Netzwerkstruktur, also die Verbindungen zwischen den Neuronen, sowie deren Anzahl, nicht vorgegeben, sondern durch einen genetischen Algorithmus während der Gewichtsoptimierung herausgefunden herausgefunden. Dies sorgt für eine wesentlich schnellere Lösungsfindung, die zudem darauf fokussiert ist möglichst einfache Netzwerke zu entwickeln. Dies zeigt sich dann insbesondere in komplexeren Problemen oder Benchmarks (double Pole experiment without velocities), in denen NEAT bis zu fünf mal besser abschneidet als traditionelle NEs. Auch zeigen sich durch die inkrementell wachsende Netzwerkstruktur parallelen zu incremental evolution, was eine Methode ist um neuronale Netzwerke Probleme lösen zu lassen, zu dem sie normalerweise nicht fähig sind. Dies geschieht durch die Unterteilung des Problems in mehrere Stufen, die nach und nach immer schwerer werden. Das bringt das Netzwerk dann dazu, dass es weiterkommt und nicht in einer Sackgasse stecken bleibt. Der große Performance Vorteil von NEAT ist in diesem Fall allerdings, dass es im Gegensatz zu incremental evolution keine menschliche Vorgabe notwendig hat und somit Zeit und Aufwand spart.

Doch kommen wir zu den 3 Grundfragen NEATs, deren Antwort *Kenneth O. Stanley* und *Rist Miikulainen* 2002 dazu gebracht hat NEAT zu entwickeln.

- Gibt es eine einheitliche Repräsentation, die es erlaubt unterschiedliche Strukturen auf sinnvolle Weise zu kreuzen?
- Wie können strukturelle Innovationen, die ein paar Generationen brauchen um optimiert zu werden geschützt werden, sodass sie nicht von der population verschwinden?
- Wie können Strukturen, ohne die Notwendigkeit einer speziell angepassten Fitnessfunktion, die Komplexität misst, während der evolution minimiert werden.

Miikulainen und Stanley haben darauf folgendes Schlüsselelemente Gefunden: Historische Kennzeichnungen, minimalen Ausgangspunkt, Wachstum und Spezialisierung führt dies dazu alle Fragen befriedigend zu beantworten.<br />
Somit findet sich die Antwort auf die erste Frage direkt in den Kennzeichnungen, denn auch wenn es schwer sein kann scheinbar inkompatible Netze miteinander zu verbinden kann man durch die Kennzeichnungen immer den gemeinsamen Nenner herausfinden, der dann Rekombination ermöglicht.<br />
Ihre Antwort auf die zweite Frage findet sich dann in der Spezialisierung, die eine Population aufgrund von strukturellen Ähnlichkeiten in verschiedene Spezies einteilt. Aufgrund deren Größe die fitness der einzelnen Elemente moduliert wird und keine Spezies die Population an sich reißen kann.<br />
Die dritte Frage wird mit dem minimalen Ausgangspunkt sowie dem Wachstum beantwortet, anders formuliert heißt das, dass die Population, wenn sie mit der minimalsten Netzwerkstruktur anfängt und langsam immer verschiedene komplexer werdende Strukturen entwickelt, die Minimalstruktur die zur Lösung Notwendig ist immer entdeckt und somit keine unnötig komplexen Lösungen wie andere TWEANNs (Topology and Weight Evolving Artificial Neural Networks) verwendet.<br />


Genug von der Theorie, jetzt gehts los. Wir schauen uns Nvidia Inpainting an. Eine KI aus dem echtem Leben.<br />
Hiermit kann man Masken auf Bilder anwenden, deren Inhalte dann ausgeschnitten werden und von einem Neuronen Netzwerk neu ausgerechnet werden.<br />
Auch, wenn sich das jetzt nach einer unglaublich komplexen Tätigkeit anhört war die Vorgehensweise des NVIDIA Teams recht einfach. Sie haben ein neuronales Netzwerk genommen und es mithilfe verschieden generierter Masken trainiert und die Farbwerte der neu ausgerechneten Pixel anhand ihres Umfeldes neu normiert (partial convolution).<br />
Und voilla, schon war die aktuell fortschrittlichste Image Inpainting Methode fertig.


Kommen wir nun zu einem Punkt der vermutlich viele beschäftigt: Die Risiken von KIs.<br />
Doch bevor wir jetzt alle in Panik ausbrechen und uns einen Lebenslangen Vorrat an Dosenfutter zu legen und uns den Rest unseres Lebens in Bunkern verschanzen um uns vor Skynet zu schützen muss ich an dieser ein lautes >>Halt ihr Affen>> sagen, denn so etwas ist schlicht und einfach Schwachsinn. Zwar gibt es Risiken bei der Verwendung von starken KIs, doch wir werden uns wohl kaum Sorgen um die Weltherrschaft machen müssen, oder, dass wir irgendwann als riesige Bio-batterie enden werden. Denn die Risiken sind viel greifbarer. Daher nur ein kleines Beispiel:<br />
Stell dir vor du hast dir die den neuen Haushaltsroboter von Global AI im Early Access gekauft und gibst ihm den Auftrag dir einen Kaffe zu machen. Er geht in die Küche und trampelt auf dem Weg deinen Dreijährigen Transgender tot. Denn das war der schnellste Weg dir einen Kaffe zu machen.<br />
Das ist ein reales Problem, doch auch nur ein Problem, ein Problem, an dem jetzt geforscht wird, für das schon heute eine Lösung gesucht wird. Ein Problem, das, genauso wie viele andere seiner Art, dann schon lange gelöst sein wird, wenn es wirklich starke KIs geben wird.<br />

Daher sollten wir anstelle uns Sorgen um surreale Fantasien [norddeutscher Comedy Autoren](https://de.wikipedia.org/wiki/Marc-Uwe_Kling "Marc Uwe Kling") zu machen lieber darüber freuen, dass die Forschung in den letzten Dekaden immense Fortschritte im Bereich des machine learning gemacht hat. Und wir sollten mit großer Freude und Begeisterung in eine Zukunft blicken, die uns viel Gutes und hoffentlich weitere Fortschritte bescheren wird.
