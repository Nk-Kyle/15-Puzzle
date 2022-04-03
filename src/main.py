import fpsolver as s
import puzzle as p
import os

if __name__ == '__main__':
    print('Current Working Directory: '+ os.getcwd() )
    #Membaca konfigurasi awal
    
    while (True):
        mode = input('Input from File? (y/n): ')
        if (mode == 'y' or mode == 'n'):
            break
    if(mode =='y'):
        while (True):
            try:
                initial_state = p.read()
                p.validate(initial_state)
                break
            except Exception as e:
                print(e)
    else:
        initial_state = p.random()

    # Initial State
    p.print_puzzle(initial_state)

    # Hitung Nilai Kurang State Matriks
    kurang,tot, blankidx, issolveable = s.solvable(initial_state)
    print("===============NILAI KURANG(i)===============")
    for i in range(16):
        print('KURANG('+str(i+1) + ') = ' + str(kurang[i]))
    print("============================")
    print("\u03a3(Kurang(i)) + X =", tot, '+', (blankidx%2),'=', tot+blankidx)

    #Melakukan Solve jika dapat disolve
    if (not issolveable):
        print('Configuration Can\'t Be Solved!')
    else:
        resultNode = s.solve(initial_state)
        print("done")
