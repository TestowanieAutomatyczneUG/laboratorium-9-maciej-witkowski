from timer_and_mp3_player import TimerAndMP3Player


class Checker:

    def __init__(self):
        self.environment = TimerAndMP3Player()

    def remainder(self, file):
        time = self.environment.getTime()

        if int(time) > 17:
            self.environment.playWavFile(file)
            return self.environment.wavWasPlayed(file)
        else:
            return self.environment.resetWav(file)
