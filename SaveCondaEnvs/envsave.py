#!/usr/bin/env python

import time
import argh
import sys
import subprocess


# options
@argh.arg('--all', default=False, help='Saves all the environments')
@argh.arg('--mark', default=False, help='Adds a .env file containing the name of the yml file')
def main(**kwargs):
    """
    This simple program saves conda environments
    By default it saves the active environment
    """

    CondaQuery = "conda env list"
    result = []
    process = subprocess.Popen(CondaQuery, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    for line in process.stdout:
        result.append(line)

    if not kwargs['all']:
        for envn in range(3, len(result) - 1):
            if result[envn].decode().split()[1].strip() == "*":
                currentenv = result[envn].decode().split()[0].strip()
                print("Saving current environment (%s)..." % currentenv, end='')
                cmd = "conda env export --name %s > %s.yml" % (currentenv, currentenv)
                res = []
                proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                # Saving a mark
                if kwargs['mark']:
                    with open('.env', 'w') as f:
                        f.write(currentenv + ".yml")
                print("Done")
                break
    else:
        print("Saving all environments")
        for envn in range(3, len(result) - 1):
            currentenv = result[envn].decode().split()[0].strip()
            # Status progress for terminal
            sys.stdout.write('\r')
            sys.stdout.write("%d/%d %s\t\t\t" % (envn, len(result) - 2, currentenv))
            sys.stdout.flush()

            cmd = "conda env export --name %s > %s.yml" % (currentenv, currentenv)
            res = []
            proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            for lin in process.stdout:
                res.append(lin)
            for i in res:
                print(res[i].decode())
            time.sleep(0.2)
        sys.stdout.write('\r')
        sys.stdout.write("Done\t\t\t")
        sys.stdout.flush()


if __name__ == '__main__':
    argh.dispatch_command(main)
