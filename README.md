# statistics-FastAPI

# Start project:
  1) Start docker machine on your PC
  2) Change main project directory in terminal
  3) Create .env file near core directory by .env.example 
  4) Run command **"sudo docker-compose up --build"** in your terminal
  5) Go to localhost in your browser (without port 8000)
  6) Project was successful started

# API
  1) Go to **http://localhost/statistic/add/** in Postman and set to body this
     - {
          "date": "2022-12-31 01:00:00",
          "views": 1,
          "clicks": 1,
          "cost": 2.3
        }
     - Select POST method
     
  2) Go to **http://localhost/statistic/get/** in Postman and set to body this
     - {
          "from": "2022-12-31 00:00:00",
          "to": "2022-12-31 10:00:00",
        }
     - Select POST method
     
  3) Go to **http://localhost/statistic/** in Postman and set to body this
   
     - Select POST method
