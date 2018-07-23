# bytes.cat Dokuwiki sidebar

Codi per generar automàticament la sidebar de la wiki bytes.cat, basada en Dokuwiki.

Els arxius de dades originals estan a la carpeta ```dades```, son excels del departarment d'educació.

S'ha fet un extracció i l'arxiu amb tots els cicles, mòduls i UFs estan ```MPs.csv```.


## Sidebar

Per generar la sidebar i emmagatzemar-la en l'arxiu ```sidebar.txt``` fem:

    $ python genera_sidebar.py > sidebar.txt


## Arxius de cerca

Els enllaços del menú de la sidebar ens porten a pàgines que han de cercar a la wiki per tags. Per generar aquestes pàgines fem:

    $ python genera_cercadors.py

...i generarà una sèrie d'arxius a la carpeta ```pages``` que queden enllaçats amb els de la sidebar.

