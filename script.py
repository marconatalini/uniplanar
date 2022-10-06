from ordine import Ordine

def main():
    # testo = open(r"c:\Users\marco\Documents\Stampe\1.txt", 'r').read()
    testo = open(r"1.txt", 'r').read()

    ordine = Ordine(testo)

    for s in ordine.serramenti:
        print(s)

    ordine.esporta()

if __name__ == '__main__':
    main()