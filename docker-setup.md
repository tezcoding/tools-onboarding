# Setup docker containers

## PostgresQL
1. Clone this repository
    -  `git clone https://github.com/tezcoding/tools-onboarding.git`
2. In terminal from the repos root directory enter `docker-compose up -d` this will start the containers
3. Go to http://localhost:5050 and set your master password and write it down.
4. In the top left corner right click `Servers -> Register -> Servers...`
5. Enter the following values under `General` tab
    - Name: `dvdrental`
6. Enter the following values under `Connection` tab
    - Host name/address: `postgres`
    - Password: `postgres` (Enable save password)
7. Click Save (You should now have access to Postgres with dvd rental sample database)

## Python container that supports selenium webdriver and other necessary libraries out of the box
TODO