# Setup docker containers

## PostgresQL

1. Clone or download this GitHub repository
   - https://github.com/tezcoding/tools-onboarding.git
2. Inside the terminal from the repository's root folder enter `docker-compose up -d` this will start the containers
3. Go to your PgAdmin dashboard at http://localhost:5050 to set your master password and write it down.
4. In the top left corner right click `Servers -> Register -> Servers...`
5. Enter the following values under `General` tab
   - Name: `dvdrental`
6. Enter the following values under `Connection` tab
   - Host name/address: `postgres`
   - Password: `postgres` (Enable save password)
7. Click Save (You should now have access to Postgres with dvd rental sample database)

## Python and Selenium WebDriver installation

1. Inside the terminal from the repository's root folder enter the following command depending on your processor
   - Run `docker run --name python-container -d -p 4444:4444 -p 7900:7900 --shm-size="2g" tezsolutions/python3-webdriver-chromium-amd-arm:1.0`
2. Check that container is running
   - `docker ps` python-container should be in the list of running containers.
3. Check selenium is working properly.
   1. Navigate to http://localhost:7900/ and enter password `secret`
      - This page will show you the actions the browser is taking when you run your automation scripts.
   2. In VSCode Remote-Containers attach to python-container
   3. Open terminal and enter `python3 ~/tez/test-selenium-installation.py` you should see it open chrome, navigate to google and print google's webpage title
