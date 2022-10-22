# This is a sample Python script.
from banco import ContaCorrente


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def metodo1():
    print('início	do	metodo1')
    metodo2()
    print('fim	do	metodo1')


def metodo2():
    print('início	do	metodo2')
    cc = ContaCorrente('José', '123')
    for i in range(1, 15):
        cc.deposita(i + 1000)
        print(cc.saldo)
        if (i == 5):
            cc = None
    print('fim	do	metodo2')


if __name__ == '__main__':
    print('início	do	main')
    metodo1()
    print('fim	do	main')
