import sys
import subprocess
import time

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
        if result == predicted:
            ac = 'AC'
    
    if ac == 'WA':
        print('eg', i+1, ac, '\n input:\n', stdins, 'predicted:\n', predicted, 'result:\n', result)
    else:
        print('eg', i+1, ac)

print('Test Finished')
