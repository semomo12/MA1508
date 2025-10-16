import math
import heapq

def huffmankod_entropi(p):
    # Räkna Entropin
    total = 0
    for pi in p:
        if pi  > 0:
            term = pi * math.log2(pi)
            total += term
    H = -total
    print(f"Entropin: {H:.4f} bitar")

    # Huffmanträd
    heap = [] 
    for i, x in enumerate(p):
        nod = [x, [i, ""]]
        heap.append(nod)
        
    while len(heap) > 1:
        lagst1 = heapq.heappop(heap)
        lagst2 = heapq.heappop(heap)
        for symbol in lagst1[1:]:
            symbol[1] = '0' + symbol[1]
        for symbol in lagst2[1:]:
            symbol[1] = '1' + symbol[1]
        nya_noden = [lagst1[0] + lagst2[0]] + lagst1[1:] + lagst2[1:]
        heapq.heappush(heap, nya_noden)

    # Huffmankoder
    resultat = heapq.heappop(heap)
    symbol_koder = resultat[1:]
    symbol_koder.sort(key=lambda x: x[0])
    koder = []
    for symbol in symbol_koder:
        index, kod = symbol
        koder.append(kod)
    print("Huffmankoder:", koder)

    # genomsnittslängden
    summa = 0
    for pi, kod in zip(p, koder):
        summa += pi * len(kod)
    print(f"Genomsnittslängd: {summa:.4f} bitar")


p = [0.35, 0.35, 0.30]
huffmankod_entropi(p)

p2 = [0.1, 0.1, 0.2, 0.3, 0.3]
huffmankod_entropi(p2)