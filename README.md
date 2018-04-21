# python - 2 tools
 
# list of emotions
{0: 'angry', 1: 'disgust', 2: 'fear', 3: 'happy', 4: 'sad', 5: 'surprise', 6: 'neutral'}

## usage

```bash
# configuration
# change in subject.py
#  CONST_TIME = 2 -> period of analysis
#  CONST_TREESHOLD = 80 -> wanted mean of happiness 
#  CONST_BUZZ = "http://10.100.3.48/on/3" -> web address to wake up collaboratpor
#  MONGO_CONNECTION = "mongodb://localhost:27017" -> connection for db
#  MONGO_DATABASE = "angularfullstack" -> database
#  COLLECTION = "mood" -> collection

#  2 cameras must be connected

# launch analyser (must be launch from src directory)
# camera 0 
# subject represent the name of the collaborator
python3 emotion.py -s <subject> -u <url>

# launch server (allow streaming to manager - must be launch from src directory)
# expose port 8080
# camera 1 
# run the browser on following address (only chrome)
# http://localhost:8080/cam.mjpg
python3 server.py 


```

# dependency
keras
tensorflow
pandas
numpy
h5py
statistics
apscheduler
pymongo
python-opencv
matplotlib
python3-tk
