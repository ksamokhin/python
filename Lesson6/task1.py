from time import sleep


class TrafficLigth:
    __color = {'\033[41mкрасный': 7, '\033[43mжелтый': 2, '\033[42mзелёный': 5}

    def _running(self):
        for k, t in self.__color.items():
            print(k)
            sleep(t)


TrafficLigth()._running()
