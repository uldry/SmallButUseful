### trstat.py
Small utility to get the file statistics for the tree on a given path

Gives the number of files, folders, maximum tree depth and also details the size for each file extension,
 number of files, total size occupied, min, max and average file size.
It can be useful to find files that shouldn't be in this path or that have an abnormal size.

    usage: trstat.py [-h] [-H] [-s {ext,count,size}] [-a] path

    walks the filesystem tree from the given path and gives basic size stats for each file extension.
    positional arguments:

    path                  Path to process`

    optional arguments:
    -h, --help            show this help message and exit
    -H, --human           Human readable display (default: False)
    -s {ext,count,size}, --sort {ext,count,size}
                        Sorting according to extension name, file count or total size (default: 'count')
    -a, --asc             Ascending order (default: False)
