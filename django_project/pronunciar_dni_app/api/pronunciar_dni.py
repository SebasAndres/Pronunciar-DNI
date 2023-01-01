## ¿De que forma es + eficiente decir el DNI?
## @ssebas.andres

print () # de cortesia

## Primero armo un modulo que pueda contar
numeros_unidad = ["", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve", "diez"]
numeros_decena = ["e", "veinti", "treinti", "cuarenti", "cincuenti", "sesenti", "setenti", "ochenti", "noventi"]
numeros_centena = ["ciento", "doscientos", "trescientos", "cuatrocientos", "quinientos", "seiscientos", "setecientos", "ochocientos", "novecientos"]
# casos excepcion
decenas_perfectas = ["diez", "veinte", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"]
decena_problematica = ["once", "doce", "trece", "catorce", "quince", "dieciseis", "diecisiete", "dieciocho", "diecinueve"]

def Pronunciar (numero):
    # Funcional para numeros entre (0, 10**9)
    pronunciacion = ""
    if 0 <= numero < 10**9:
        if numero < 10: # una cifra
            if numero == 0: pronunciacion = "cero"
            else: pronunciacion = numeros_unidad[numero]

        elif 10 <= numero < 100: # dos cifras
            if numero % 10 == 0:
                pronunciacion = decenas_perfectas [(numero // 10)-1]
            elif 11 <= numero <= 19:
                pronunciacion = decena_problematica[(numero % 10)-1]
            else: 
                digito2 = numero % 10
                digito1 = (numero - digito2) // 10
                pronunciacion = numeros_decena[digito1-1] + numeros_unidad[digito2]
        
        elif 100 <= numero < 1000: # tres cifras 
            if numero % 100 == 0:
                if numero == 100: pronunciacion = "cien"
                else: pronunciacion = numeros_centena[(numero//100)-1]
            else:
                pronunciacion = numeros_centena[(numero//100)-1] + Pronunciar(numero-(numero//100)*100)

        elif 1000 <= numero < 10**6: # cuatro a seis cifras
            if numero == 1000: pronunciacion = "mil"
            else:
                mil_i = numero // 1000
                if mil_i == 1:
                    pronunciacion = "mil" + Pronunciar (numero - mil_i*1000)
                else:
                    units = numero % (10**3)
                    if units == 0:
                        pronunciacion = Pronunciar (mil_i) + "mil"
                    else:
                        pronunciacion = Pronunciar (mil_i) + "mil" + Pronunciar (numero - mil_i*1000)

        elif 10**6 <= numero < 10**9: # siete cifras
            units = numero % (10**6)
            if units == 0:
                if numero == 10**6: pronunciacion = "un millon" 
                else:
                    pronunciacion = Pronunciar(numero // 10**6) + "millones" 
            else:
                pronunciacion = Pronunciar((numero // 10**6)*10**6) + Pronunciar (units)
    else:
        pronunciacion = "Fuera de rango"    
    return pronunciacion

def contar (desde, hasta):
    for numero in range(desde, hasta, 1):
        print (numero, Pronunciar(numero))

## Voy a medir la eficiencia de c/ metodo de pronunciacion en base a las letras que necesita

def vectorizeDni (dni):
    return list(str(dni)) 

def PronunciarPorPatron (dni, patron):
    pronunciacion = "" # inicializo vacia
    vectDni = vectorizeDni(dni) # paso de int --> list
    # cuento cuántos grupos me configura el patron y con cuantos caracteres c/u
    grupos_lengths = [] 
    n_chars_grupo = 0
    for ch in patron+"-":
        if ch == "-":
            grupos_lengths.append(n_chars_grupo)
            n_chars_grupo = 0
        else: 
            n_chars_grupo += 1
    # armo cada grupo con los caracteres del dni
    grupos = []
    init_index = 0
    for grupo_length in grupos_lengths:
        list_group = vectDni[init_index : init_index + grupo_length]
        number_group = strJoin (list_group)
        grupos.append (number_group)        
        init_index += grupo_length
    # agrego a pronunciacion la pronunciacion de cada grupo, separada por un guion
    for grupo in grupos:
        pronunciacion += strPronunciar(grupo) + "-"   
    return pronunciacion[:-1] # elimino el guion extra y devuelvo la pronunciacion

def strPronunciar (strNumero):
    if len(strNumero) > 1:
        nCerosIzquierda = strNumero[:-1].count('0')
        if strNumero[0] == '0':
            return nCerosIzquierda * Pronunciar(0) + Pronunciar(int(strNumero[1:]))
    return Pronunciar(int(strNumero))

def strJoin (listaNumeros_str):
    return "".join(listaNumeros_str)

def Join (listaNumeros):
    # Pasar de lista de numeros a numero
    ## Ej::: [1, 2] --> 12
    nro = 0
    if len(listaNumeros) == 1: nro += listaNumeros[0]
    else:
        for j, n in enumerate(reversed(listaNumeros)):
            nro += n * 10**(j)
    return nro

## Me queda armar todas las permutaciones de patrones posibles, filtradas por la limitacion de mi contador para pronunciar

def PermutarPatrones (nDigitos):
    # Devuelve todas las permutaciones de patrones posibles 
    # Obs. Hay 2**(nDigitos-1) permutaciones posibles
    # Agrego una barrera media entre cada numero y vario su estado
    # Para esto hago un loop desde i=0 a i=2^(n-1) y traduzco ese numero i en estados de los bits. 
    # Cada i esta relacionado biyectivamente con un patron
    patterns = list ()

    for i in range(2**(nDigitos-1)):
        # itero cada patron posible
        bits = format(i, "b") # lo paso a un str con los bits (ej."0101101")
        bits_list = [int(n) for n in list(bits)] # [0, 1, 0, 1, 1]
        bits_list = adaptToNBits (bits_list, nDigitos-1)
        # Creo el i_esimo patron siguiendo el bit
        patron_i = byte_to_patron_v1 (bits_list)
        patterns.append (patron_i)

    return patterns

def adaptToNBits (bits_list, n):
    ## Hacer que el bit tenga n digitos sin importar su tamaño
    ## Agregar ceros a la izquierda
    for n in range(n - len(bits_list)):
        bits_list.insert(0, 0)
    return bits_list

def byte_to_patron_v1 (byte):
    patron_i = "X"
    for n in range (len(byte)):
        if byte[n] == 1:
            patron_i += "-X"
        else:
            patron_i += "X"    
    return patron_i

class Pattern:
    def __init__ (self, _patr, _pron, _score):
        self.patr = _patr
        self.pron = _pron
        self.score = _score

def GET_BESTS_PATTERNS (dni, n_depth):
    """
    Returns topN best patterns for your DNI
        dni = number (int)
        topN = number (int),
        Output = [[level_1], ..., level_n]
        level_i = [(pattern, pronunciaton, characters)_0, ..., (pattern, pronunciaton, characters)_k]
    """
    vectDni = vectorizeDni(dni)
    PatronesAProbar = PermutarPatrones(len(vectDni)) # n-1 barreras

    Patterns = list () # misma estructura que level

    for patron in PatronesAProbar:
        pron = PronunciarPorPatron(dni, patron)
        Patterns.append(Pattern(patron, pron, len(pron)))

    OrderedPatterns = OrderPatterns (Patterns)
    Levels = GET_N_LEVELS_DEPTH(OrderedPatterns, n_depth)

    return Levels

def OrderPatterns (lst):
    if len(lst) == 1:
        return lst
    else:
        middle = len(lst) // 2
        left, right = lst[:middle], lst[middle:]
        left = OrderPatterns(left)
        right = OrderPatterns(right)
        if left[-1].score < right[0].score:
            left.extend(right)
            return left
        else:
            return merge(left, right)

def merge (left, right):
    ret = []
    while (len(left) != 0 and len(right) != 0):
        if (left[0].score <= right[0].score):
            ret.append(left[0])
            left.pop(0)
        else:
            ret.append(right[0])
            right.pop(0)
    # Lo restante deberia estar ordenado y ser mayor a todo elemento en ret
    if len(left) > 0:
        ret.extend(left)
    elif len(right) > 0:
        ret.extend(right)
    return ret

def GET_N_LEVELS_DEPTH (Patterns, n_depth):
    j = 1
    Levels = [[Patterns[0]]]
    for _ in range (n_depth):
        while ((Patterns[j].score == Levels[-1][0].score)):
            Levels[-1].append(Patterns[j])
            if (j < len (Patterns)-1):
                j += 1
            else:
                break
        if len(Levels) < n_depth:
            Levels.append([Patterns[j]])
            j += 1
        else: 
            break
    return Levels