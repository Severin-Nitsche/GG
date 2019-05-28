# Zukunftswerkstatt Künstliche Intelligenz

Hier ist zusätzliches Material der Gruppe von Markus, Tuan und Severin.

**NEAT - Ablationen**

Beginnen wir mit der Kein Wachstumablation, in der die Netzwerke anstelle von einer minimal 
startenden Struktur, die sich dann nach und nach entwickelt, ausgeht, eine feste Struktur haben.
Hier haben Experimente gezeigt, dass diese Abwandlung bei einer Generationenanzahl von 1000 
nur in etwa 20% der Versuche eine Lösung ﬁnden konnte, die dann etwa 8.5 mal mehr 
Auswertungen brauchte als normales NEAT.

Machen wir weiter mit der Anfangs Zufällig Ablation, die anders als der normale NEAT Algorithmus 
Am Anfang mehrere zufällige Strukturen verwendet und somit näher an anderen TWEANNs ist.
Doch die Experimente haben auch hier gezeigt, dass der normale NEAT Algorithmus besser ist. 
Denn die Ableitung war immer etwa 7 mal langsamer und hat bei einer maximalen 
Generationsanzahl von 1000 in 5% aller Fälle überhaupt keine Lösung gefunden.
Miikulainen und Stanley führen diesen Effekt darauf zurück, dass der NE durch die zufälligen 
Startpunkte dazu veranlasst wird komplexere Lösungen als notwendig zu durchsuchen, was die 
Leistung verringert.

Kommen wir nun zu der Keine Spezialisierungsablation. Wie der Name schon vorschlägt lassen 
wir dieses mal die Spezialisierung raus. Doch auch hier zeigen die Experimente enttäuschende 
Ergebnisse. So ist diese Ableitung wieder 7 mal langsamer und fand in 25% aller Fälle überhaupt 
keine Lösung. Dieses mal führen Miikulainen und Stanley den Performanceverlust auf die 
Konvergenz zu einer bestimmten Netzwerkart zurück, die Anfangs am besten abschnitt. Was 
zuerst ähnlich wie in der Anfangs Zufällig Ablation dazu führt, dass der NE eine zu komplexe 
Lösung sucht und als zweites dazu führt, dass die ganze Varietät genommen wird, da nicht mehr 
an verschiedenen Lösungsansätzen gleichzeitig geforscht wird.


**Weiter Informationen und Quellen**

Webseiten:<br />
*NEAT:*<br />
https://towardsdatascience.com/neat-an-awesome-approach-to-neuroevolution-3eca5cc7930f<br />
http://nn.cs.utexas.edu/downloads/papers/stanley.ec02.pdf<br />
*Nvidia Inpainting:*<br />
https://news.developer.nvidia.com/new-ai-imaging-technique-reconstructs-photos-with-realistic-results/<br />

Bücher:<br />
*GAs:*<br />
Nature of Code: https://natureofcode.com/book/chapter-9-the-evolution-of-code/<br />
*Neuronale Netzwerke:*<br />
Make Your Own Neural Network: https://www.amazon.de/Make-Your-Own-Neural-Network/dp/1530826608<br />
