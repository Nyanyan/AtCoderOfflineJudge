import sys
import subprocess
import time

floatthreshold = pow(10, -4)

args = sys.argv

if len(args) != 2:
    print('args error exit')
    sys.exit()

fil = args[1]

egs = [[[]], [[]]]
flag = 0
for i in range(2):
    if i == 0:
        print('input the eg input, then return 2 times')
    else:
        print('input the eg output, then return 2 times')
    while flag < 2:
        eg = input()
        if eg == '':
            flag += 1
            egs[i].append([])
        else:
            flag = 0
            egs[i][len(egs[i]) - 1].append(eg)
    del egs[i][len(egs[i]) - 2:]
    flag = 0
    if i == 0:
        print('eg input finished\n')
    else:
        print('eg output finished\n')

if len(egs[0]) != len(egs[1]):
    print('eg input and output error exit')
    sys.exit()

mode = 1 #0: str mode, 1: float or int mode
numstr = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.']
for i in range(len(egs[1][0])):
    for j in range(len(egs[1][0][i])):
        if egs[1][0][i][j] in numstr and mode:
            mode = 1
        else:
            mode = 0
if mode == 0:
    print('output mode is str\n')
else:
    print('output mode is float or int\n')

print('Testing...')

for i in range(len(egs[0])):
    cmd = 'python ' + fil
    stdins = ''
    for eg_row in egs[0][i]:
        stdins += eg_row + '\n'
    
    ac = 'WA'
    
    run = subprocess.Popen(cmd.split(), stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    try:
        result = run.communicate(input=stdins.encode('utf-8'), timeout=2)[0].decode('utf-8')
    except subprocess.TimeoutExpired:
        run.kill()
        ac = 'TLE'
        result = ''
    result = result.replace('\r\n', '\n')
    result = result.replace('\r', '\n')
    #result_proc = result.replace(' ', '\n')
    
    if ac != 'TLE':
        predicted = ''
        for eg_row in egs[1][i]:
            predicted += eg_row + '\n'
        #predicted_proc = predicted.replace(' ', '\n')
        if mode == 0: #str mode
            if result == predicted:
                ac = 'AC'
        else: #float or int mode
            predicted = predicted[:len(predicted) - 1]
            result = result[:len(result) - 1]
            predictedarr = [float(i) for i in predicted.split('\n')]
            resultarr = [i for i in result.split('\n')]
            flag = True
            for j in range(len(resultarr)):
                for k in range(len(resultarr[j])):
                    if not resultarr[j][k] in numstr:
                        flag = False
                        break
            if len(predictedarr) == len(resultarr) and flag:
                resultarr = [float(i) for i in resultarr]
                ac = 'AC'
                for j in range(len(predictedarr)):
                    if abs(predictedarr[j] - resultarr[j]) > floatthreshold:
                        ac = 'WA'
                        break


    if ac == 'WA':
        print('eg', i+1, ac)
        print('input:')
        print(stdins)
        print('predicted:')
        print(predicted)
        print('result:')
        print(result)
    else:
        print('eg', i+1, ac)

print('Test Finished')
