# pontianmyhometown

## Hosted on Google Cloud VM
```
gunicorn --certfile cert.pem --keyfile key.pem --workers=3 --threads=2 -b 0.0.0.0:5000 --reload wsgi:app
```

## To-do list
- [x] pontian (atm, hotel, school)
- [] pekan (hotel, school)
- [] benut (atm, hotel, school)
- [] kukup (atm, restaurant, hotel, school)