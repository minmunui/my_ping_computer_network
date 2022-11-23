import time
from datetime import datetime
from ping3 import ping

# # Ping, RTT, 패킷 분실, 통계

repeat = 5

def my_ping(ip_address):
    list_response_time = []
    for i in range(repeat):
        result = None
        result = ping(ip_address)
        if result is None:
            print(ip_address + '\t' + ' Ping Check Fail : ' + str(datetime.now())[:19])
            pass
        else:
            print(ip_address + '\t' + ' Ping Check OK :',
                  '[ Response Time %.4f ] : ' % result + str(datetime.now())[:19])
            list_response_time.append(result)

    report_ping(list_response_time)


def report_ping(list_response_time):
    print("[My ping report]")
    print("Success : %d \t Fail : %d \t Success Rate : %.2f%%" % (
        len(list_response_time), repeat - len(list_response_time), len(list_response_time) * 100 / float(repeat)))
    if ( len(list_response_time) != 0):
        print("Mean response time : %.4f" % get_average(list_response_time))
        print("Shortest response time : %.4f" % min(list_response_time))
        print("Longest response time : %.4f" % max(list_response_time))
    else :
        print("All ping check failed ")


def get_average(list_to_average):
    if len(list_to_average) == 0:
        return 0.0
    return sum(list_to_average) / float(len(list_to_average))


def main():
    while (1):
        hostname = input("Enter IP address you want to ping >> ")
        try:
            my_ping(hostname)
        except:
            print("Wrong address format!")

main()
