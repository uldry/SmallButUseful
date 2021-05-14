### envsave.py
 Small utility to save Conda environments in the blink of an eye.
 It's far from being bulletproof, but fulfils my current needs 
 (backup, deployment and traceability)

 An executable can easily be build using py2exe and moved in a folder that is in the `PATH`

Saving the active environment: `envsave`
Doing the same and creating a .env file containing the yml name `envsave --mark`
Saving all environments `envsave --all`
