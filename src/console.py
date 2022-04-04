import fpsolver as s
import puzzle as p
import os
from time import time

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
                filepath = input('Input file path (ex: test/in1.txt): ')
                initial_state = p.read(filepath)
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
    print("\u03a3(Kurang(i)) + X =", tot, '+', (blankidx%2),'=', tot+(blankidx%2))

    #Melakukan Solve jika dapat disolve
    if (not issolveable):
        print('\nConfiguration Can\'t Be Solved!')
    else:
        begin = time()
        (path, comp) = s.solve(initial_state)
        end = time()
        path.reverse()
        print('\n========Initial State========')
        for mat in path:
            if (mat.dir != None):
                print('========MOVE '+ mat.dir+ '========')
            p.print_puzzle(mat.state)
        print('Total Gerakan =', len(path)-1)
        print("Total simpul dibangkitkan =", comp)
        print("Elapsed time =", end-begin)
        
