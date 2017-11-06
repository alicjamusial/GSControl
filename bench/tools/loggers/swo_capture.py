import subprocess
import time
from multiprocessing import Process

from tools.log import SimpleLogger, MainLog


class JlinkSWOLogger(object):
    def __init__(self):
        self.logger = SimpleLogger('swo.log', in_test=True)
        self.thread = Process(target=self._run)
        self.process = subprocess.Popen(['JLinkSWOViewer', '-device', 'EFM32GG280F1024', '-itmmask', '0x1FFFF'],
                                        stdout=subprocess.PIPE, universal_newlines=True)
        MainLog("Waiting for SWO startup...")

        while True:
            line = self.process.stdout.readline()
            self.logger.log(line)
            if line.find("Receiving SWO data") != -1:
                break
        MainLog("SWO logger started")

    def _run(self):
        while True:
            line = self.process.stdout.readline()
            self.logger.log(line)

    def start(self):
        self.thread.start()

    def stop(self):
        self.process.terminate()
        self.thread.terminate()

if __name__ == "__main__":
    swo = JlinkSWOLogger()
    swo.start()
    time.sleep(5)
    swo.stop()
