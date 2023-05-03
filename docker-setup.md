# Setup docker containers

## PostgresQL

1. Clone this repository
   - `git clone https://github.com/tezcoding/tools-onboarding.git`
2. In terminal from the repositories root directory enter `docker-compose up -d` this will start the containers
3. Go to http://localhost:5050 and set your master password and write it down.
4. In the top left corner right click `Servers -> Register -> Servers...`
5. Enter the following values under `General` tab
   - Name: `dvdrental`
6. Enter the following values under `Connection` tab
   - Host name/address: `postgres`
   - Password: `postgres` (Enable save password)
7. Click Save (You should now have access to Postgres with dvd rental sample database)

## Python

1. Clone this repository if haven't already.
   - `git clone https://github.com/tezcoding/tools-onboarding.git`
2. Inside the terminal from the repository root enter the following command depending on your processor
   - Intel/AMD chips
     - `docker run --name python-container -d -p 4444:4444 -p 7900:7900 --shm-size="2g" tezsolutions/python-webdriver-amd`
   - ARM chips
     - `docker run --name python-container -d -p 4444:4444 -p 7900:7900 --shm-size="2g" tezsolutions/python-webdriver-arm`
3. Check that container is running
   - `docker ps` python-container should be in the list of running containers.
4. Check selenium is working properly.
   1. In VSCode Remote-Containers attach to python-container
   2. Open terminal and enter `python3 ~/tez/test-selenium-installation.py` it should open chrome, navigate to google and print google's webpage title
   3. Navigate to http://localhost:7900/ and enter password `secret`
      - This page will show you the actions the browser is taking when you run your automation scripts.
      - You should see chrome with one tab logged in to google.com. You can rerun step 2 and pay attention how a new browser window opens.
5. Run commands from [post-install-script file](./post-install-script.txt) inside docker container
