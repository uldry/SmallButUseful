# SmallButUseful


### cli_skeleton.py

	A command line interpreter cli_skeleton that uses argh, logging and tqdm.
	
### SaveCondaEnvs (envsave.py)
	
	A tool to export Conda environments in the blink of an eye, 
	especially if-build as an executable with py2exe and put in your path.

	Exports the active environment, optionally the name of the yml can be written in a .env file.

	Exports all of them for backup purpose. (for automated backups, the path needs to be taken care of)
	
### trstat.py

	Small utility to get the file statistics for the tree on a given path

	Gives the number of files, folders, maximum tree depth and also details the size stats for each file extension, 
	number of files, total size occupied, min, max 	and average file size.
	It can be useful to find files that shouldn't be in this path or that have an abnormal size.
