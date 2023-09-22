import os
import re


if __name__ == '__main__':
    for (path, _, filenames) in os.walk('.'):
        for filename in filenames:
            if re.match(r'^trash\..+$', filename):
                os.remove(os.path.join(path, filename))
