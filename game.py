import time

class GameTimer(object):
    """
    This class starts with the game, in order to countdown how many
    sentences can you type before the time is over
    """
    def countdown(self, setTime:int):
        self.setTime = setTime

        while self.setTime:
            minutes, seconds = divmod(self.setTime, 60)
            timer = '{:02d}:{:02d}'.format(minutes, seconds)
            print(timer, end="\r")
            time.sleep(1)
            self.setTime -= 1

        print("'End Game!")


