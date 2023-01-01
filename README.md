# ¿Cuál es la forma mas eficiente de decir tu dni?

- Esta pagina tiene un algoritmo que chequea todos los patrones posibles para decir el dni y te devuelve la lista de los mejores casos, ordenados por nivel.

Para esto, se implementaron diferentes modulos: 

- PronunciarNumero : Numero (int) -> Pronunciacion (String)

- PronunciarPorPatron : Numero (int), Patron (byte) -> Pronunciacion (String)

- PermutarPatrones : N_DIGITOS (int) -> Permutaciones (List)

- GET_N_DEPTH : DNI, Patrones -> Levels (List)

- OrderPatterns (mergesort) : Patterns (List) -> Patterns (List) 

- GET_BEST_PATTERNS : DNI (int), N_DEPTH (int) -> Levels (List)
