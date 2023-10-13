import time
import sys


if __name__ == "__main__":
    seconds, minutes, hours = 0, 0, 0

    while True:
        seconds += 1
        if seconds == 60:
            seconds = 0
            minutes += 1
        if minutes == 60:
            minutes = 0
            hours += 1
        time.sleep(1)
        sys.stdout.write(f'\rTime: {hours}:{minutes}:{seconds}')
        sys.stdout.flush()
