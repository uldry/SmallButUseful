#!/usr/bin/env python

import argh
import os, sys


def sizeformat(sizeBytes):
    '''
    :param sizeBytes: File size in Bytes
    :return:  Human readable string from Bytes to Terabytes
    '''
    MB = 1024 * 1024
    GB = MB * 1024
    TB = GB * 1024

    if sizeBytes < 1024:
        sizestr = str(round(sizeBytes, 2)) + " B"
    elif sizeBytes < MB:
        sizestr = "%.5s" % (str(round(sizeBytes / 1024, 2))) + " KB"
    elif sizeBytes < GB:
        sizestr = "%.5s" % (str(round(sizeBytes / MB, 2))) + " MB"
    elif sizeBytes < TB:
        sizestr = "%.5s" % (str(round(sizeBytes / GB, 2))) + " GB"
    else:
        sizestr = "%.5s" % (str(round(sizeBytes / TB, 2))) + " TB"
    return sizestr


# Required Path argument
@argh.arg('path', help='Path to process', type=str)
@argh.arg('-H', '--human', required=False, default=False, help='Human readable display')
@argh.arg('-s', '--sort', choices=['ext', 'count', 'size'], default='count',
          help='Sorting according to extension name, file count or total size')
@argh.arg('-a', '--asc', default=False, help='Ascending order')
def size(**kwargs):
    """
    walks the filesystem tree from the given path and gives basic size stats for each file extension.
    """
    mpath = kwargs['path']
    if not os.path.exists(mpath):
        print("Invalid path")
        sys.exit(-1)

    # Basic Counter variables
    foldercount = 0
    count = 0

    # List containing the collected information
    elist = []

    # Indices for the 2 dimensional list
    iext = 0
    icount = 1
    icsums = 2
    imins = 3
    imaxs = 4

    start_depth = len(mpath.split('/')) - 2
    depth = 0

    for root, dirs, files in os.walk(mpath, topdown=True):

        indircount = 0
        for name in files:
            pathfile = os.path.join(root, name)
            indircount += 1
            # Extension
            ext = (os.path.splitext(name)[1]).lower()[1:]
            if ext == '': ext = 'no ext'
            # Size
            size = os.stat(pathfile).st_size

            # Folder depth
            cdepth = len(os.path.abspath(pathfile).split('/')) - start_depth
            if depth < cdepth: depth = cdepth

            # Getting the index of the current file extension using python built-in functions
            try:
                index = list(zip(*elist))[iext].index(ext)
            except IndexError:
                # The list is empty
                index = -1
            except ValueError:
                # The list doesn't contain the extension
                index = -1

            if index >= 0:
                elist[index][icount] += 1
                elist[index][icsums] += size
                if size < elist[index][imins]: elist[index][imins] = size
                if size > elist[index][imaxs]: elist[index][imaxs] = size

            else:  # Adding the new extension in the list
                elist.append([ext, 1, size, size, size])
        count += indircount

        # Updating the directory count
        for name in dirs:
            foldercount += 1

    # Mapping arguments with indices in the list
    dict = {
        'ext': iext,
        'count': icount,
        'size': icsums
    }

    # Sorting the list
    elist.sort(key=lambda x: x[dict.get(kwargs['sort'])], reverse=not kwargs['asc'])

    print("%d files in %d folders max depth: %s\n" % (count, foldercount, depth))
    if kwargs['human']:
        print(f"{'Ext.':<8}{'Count':<13}{'Total':<10}{'Min':<11}{'Max':<13}{'Avg':<9}")
        for l in elist:
            print(f"{l[iext]:<7} {l[icount]:<12,d} {sizeformat(l[icsums]):<9} {sizeformat(l[imins]):<10} \
{sizeformat(l[imaxs]):<12} {sizeformat(l[icsums] / l[icount]):<9}")
    else:
        print(f"{'Ext.':<8}{'Count':<13}{'Total':<13}{'Min':<13}{'Max':<13}{'Avg':<2}")
        for l in elist:
            print(f"{l[iext]:<7} {l[icount]:<12,d} {l[icsums]:<12} {l[imins]:<12} {l[imaxs]:<12} \
{int(round(l[icsums] / l[icount], 0)):<12}")


if __name__ == '__main__':

    try:
        argh.dispatch_command(size)
    except KeyboardInterrupt:
        print('Interrupted')
