from buildings import chicken_coop
from farms import farm
from time import sleep



'''
startowanie watkow tutaj sie odbywa, dodawanie do listy
i uruchamianie roznych workerow
'''

def loop():
    try:
        farm_obj = farm()
        while True:
            farm_obj.collect_timers()
            compare_timers([11, 15, 0])
            sleep(1)
    except KeyboardInterrupt:
        print 'interrupted!'

def compare_timers(timers):
    print 'check if "Done" visible????'

if __name__ == '__main__':
    loop()
