import sys
DirApp = sys.argv[1]
Tsec = sys.argv[2]

def timeApp(Tsec, DirApp):
    import os #llibreria permet obrir arxius.exe
    import subprocess
    import time
    import sys
    import datetime # Ens fara falta al futur per cuan sigui la hora que executi la rutina.
    #Funciona!

    #xTime = int(5)
    #hor = int(input("hora: "))
    #Thor = hor*3600
    #mins = int(input("Minutos: " ))
    #Tmin = mins*60
    p = subprocess.Popen(str(DirApp))
    #p = subprocess.call(dirApp)
    #time.sleep(Thor)
    #time.sleep(Tmin)
    time.sleep(int(Tsec))
    subprocess.call(['taskkill', '/F', '/T', '/PID', str(p.pid)])
timeApp(Tsec, DirApp)