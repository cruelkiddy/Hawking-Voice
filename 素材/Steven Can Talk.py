import winsound
n=''
cun=[]
while n!='STOP':
    n=input('要说什么')
    winsound.PlaySound('beepHigh', winsound.SND_FILENAME)
    cun=n.split(' ')
    for i in cun:
        winsound.PlaySound(i,winsound.SND_FILENAME)



