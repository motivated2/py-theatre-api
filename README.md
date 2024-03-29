# Theatre Reservation API

This project provides an API for managing reservations for a local theatre. It allows visitors to make reservations online and choose seats without having to visit the theatre physically.
## Features

- JWT authentication
- Admin panel /admin/
- Documentation is located at /api/theatre/doc/swagger
- Managing reservation and tickets
- Creating plays with genres, actors
- Creating theatre halls
- Adding performances
- Filtering plays and performances

## Database Structure

The database schema consists of the following models:

![database_structure.png](database_structure.png)
## Installing using GitHub

To set up the project locally, follow these steps:
   ```bash
   git clone https://github.com/motivated2/py-theatre-api.git   
   cd py_theatre_api
   python -m venv venv
   source venv/bin/activate
   pip install requirements.txt
   set DB_HOST=<your db hostname>
   set DB_NAME=<your db name>
   set DB_USER=<your db username>
   set DB_PASSWORD=<your db user password>
   set SECRET_KEY=<your secret key>
   docker-compose build
   docker-compose up
   docker-compose exec theatre python manage.py createsuperuser 
   ```

## API Endpoints

The following endpoints are available:

- **Theatre**:
  - `http://127.0.0.1:8001/api/theatre/actors/`
  - `http://127.0.0.1:8001/api/theatre/genres/`
  - `http://127.0.0.1:8001/api/theatre/plays/`
  - `http://127.0.0.1:8001/api/theatre/reservations/`
  - `http://127.0.0.1:8001/api/theatre/theatre_halls/`
  - `http://127.0.0.1:8001/api/theatre/performances/`

- **User**:
  - `http://127.0.0.1:8001/api/theatre/user/register/`
  - `http://127.0.0.1:8001/api/theatre/user/token/`
  - `http://127.0.0.1:8001/api/theatre/user/token/refresh`
  - `http://127.0.0.1:8001/api/theatre/user/token/verify/`
  - `http://127.0.0.1:8001/api/theatre/user/me/`

- **Doc**:
  - `http://127.0.0.1:8001/api/theatre/doc/`
  - `http://127.0.0.1:8001/api/theatre/doc/swagger/`
  - `http://127.0.0.1:8001/api/theatre/doc/redoc/`
## Screenshots
![Screenshot_1.png](screenshots%2FScreenshot_1.png)
![Screenshot_2.png](screenshots%2FScreenshot_2.png)
![Screenshot_3.png](screenshots%2FScreenshot_3.png)
![Screenshot_4.png](screenshots%2FScreenshot_4.png)
![Screenshot_5.png](screenshots%2FScreenshot_5.png)
![Screenshot_6.png](screenshots%2FScreenshot_6.png)
![Screenshot_7.png](screenshots%2FScreenshot_7.png)
## Contributors

- Bondarenko Ihor (@motivated2)
