### cli_skeleton.py
An 'as simple as possible but no simpler' command line interpreter skeleton
that uses **agrh** for argument parsing/help + two additional ones:
 - **logging**: May be required depending on the application
 - **tqdm** for progress bars: Waiting in front of a blinking cursor is not recommended :-).

Getting help:
`./cli-skeleton.py  -h`

Getting help on the main function:
`./cli-skeleton.py  main -h`

Calling the main function:
`./cli-skeleton.py  main 100 --req_arg1 blah  --opt_arg2 20 --opt_flag`

Calling the other function:
`./cli-skeleton.py  other blahblabla`
---
