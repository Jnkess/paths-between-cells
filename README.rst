Ścieżki komunikacyjne w tkankach między komórkami o jednakowych masach jądra komórkowego
##############
Autor: Jakub Jankowski, 150195 Politechnika Poznańska sem 6
+++++++++

**Wstęp toretyczny**

* Użytkownik podaje liczbę komórek w tkance, punkt startowy i końcowy, oraz masę jaką ma przyjąć ścieżka między podanymi punktami.
* Następnie program tworzy graf reprezentujący tkankę, gdzie dodatkowo zaimplementowane jest sąsiedztwo brzegowe, czyli zamknięcie układu w torus tak, aby każdy wierzchołek(komórka) miał 6 sąsiadów.
* Program losuje masę dla wszystkich wierzchołków zgodnie z rozkładem Gaussa, z wyjątkiem dwóch podanych przez użytkownika(początkowego i końcowego).
* Tworzona jest lista sąsiedztwa, Na jej podstawie program tworzy ścieżkę od punktu startowego, gdzie w każdej kolejnej iteracji zmieniana jest wartość wszystkich wierzchołków, oprócz tych które znajdują się w ścieżce i mają taką samą masę jak ta podana przez użytkownika.


[tu zdjecie problemu]

Przykładowe rozwiązanie problemu
++++++++++


**Przedstawienie połączeń komórek za pomocą grafu**

Tworzona jest siatka hexagonalna, w której każdy wierzchołek reprezentuje jedną komórkę.
*Każdy wierzchołek. który nie jest na skraju siatki posiada 6 sąsiadów.
*Następnie tworzymy torus zamykając cały układ, dzięki czemu każdy wierzchołek posiada dokładnie 6 sąsiadów.

[tu zdjecie rozwiazania]
