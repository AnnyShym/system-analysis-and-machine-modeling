from Mediator import Mediator

def main():

    print()	
    p1 = float(input('p1: '))
    p2 = float(input('p2: '))
    c = int(input('c: '))
    print()

    mediator = Mediator(p1, p2, c)
    mediator.run()

if __name__ == "__main__":
    main()