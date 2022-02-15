### Insteructions:
Each service is in his own directory just choose dir A or B and run python3 ./service.py.

I gave the possibility to give a port and address args to the service so it will be easier to create a script that creates a couple of instences for the same service.
we can also just set up a couple of docker containers that we will expose them to different ports.
than we can use nginx to make the url work with all the instances of the service or the with all the containers.

now just use wget on the url and receive the configuration you want.


### Stage 2:
1. Once the feature has been merged in github it will activate the hook to jenkins and there it will start doing static analysis, unit tests and system test if all is done without failures than now we can create a docker image that contains all the needs for the service to run and deploy it to the local docker artifactory. After it is in the artifactory we can use it as pleased for dev and prod needs.

2. We can make it possible through the api and we will need to think of a smart and safe way to authenticate so a random person wont be able to do it by him self.
Same as befor we can just add a restart possibility in the api.
Now if we use flask it knows to restart itself when ever he recognizes a change in the code so it makes it easy for us.