# DE_Toxicity_Monitor

## Run the flask app
---

Go to the root directory  

Excute this command :
```
flask run
```

If this command does not work, try this one :
```
python app_flask.py
```

The application should be running at this adress :
http://localhost:5000/

## Run Docker
---

Go to the root directory  

Excute this command :
```
docker-compose build
```

After this command, enter this one :
```
docker-compose up
```

The application should be running at this adress :
http://localhost:5000/

Do not forget to stop the container after using the application :
```
docker-compose down
```