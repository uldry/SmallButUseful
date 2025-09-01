# SmallButUseful


### cli_skeleton.py

A command line interpreter cli_skeleton that uses argh, logging and tqdm.
	
### SaveCondaEnvs (envsave.py)
	
A tool to export Conda environments in the blink of an eye, 
especially if-build as an executable with py2exe and put in your path.

Exports the active environment, optionally the name of the yml can be written in a .env file.

Exports all of them for backup purpose. (for automated backups, the path needs to be taken care of)
	
### SimpleFileBackup
	
The story is that I just wanted to backup a small binary file from one cloud drive to another cloud. Boths drives are transcient.
I'm already using a backup solution, but it couldn't do something so basic.
I was in a bash mood, so I used git bash and set a windows task to trigger every hour.
		
``` archive_file.sh <path-filename>```
It backs up the file if it has changed, A bit to bit comparison had to be used due to metadata being part of hashes,
so if the file big, rely on the modification date.
A timestamp is added to the file name of the older version (the creation date is prepended)
A couple of things are logged, errors and each time a new version is archived.  
The past 5 versions or the past 5 days (Up to you) are kept That's it!
	
```Scheduler command: C:\Program Files\Git\git-bash.exe"  --hide "C:\Users\<USER>\bin\archive_file.sh" <FILE NAME>```

### trstat.py

Small utility to get the file statistics for the tree on a given path

Gives the number of files, folders, maximum tree depth and also details the size stats for each file extension, 
number of files, total size occupied, min, max 	and average file size.
It can be useful to find files that shouldn't be in this path or that have an abnormal size.
	
