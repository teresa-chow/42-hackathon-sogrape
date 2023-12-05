# Sogrape Webscraper
![Sogrape × 42 Porto: Hackathon](https://img.shields.io/badge/Sogrape%20×%2042%20Porto-Hackathon-%23af5b2c)

_Web scraping website developed in a 3-day period, during the Hackathon promoted by Sogrape and 42 Porto (23 - 26 Oct. 2023)._
___

### Table of contents
[Prerequisites](#prerequisites) · [Installation](#installation) · [Usage](#usage) · [Acknowledgements](#raised_hands-acknowledgements) · [License](#license)

___

</br>

# :compass: Usage
## Prerequisites

Before you begin, ensure you have met the following requirements:

- [XAMPP](https://www.apachefriends.org/index.html) installed
- [Python](https://www.python.org/downloads/) installed

</br>

## Installation

1. Clone the repository
```bash
git clone git@github.com:teresa-chow/42-hackathon-sogrape.git
```

2. Start Apache and MySQL in XAMPP

   - Launch XAMPP Control Panel;
   - Click "Start" next to Apache and MySQL.

3. Configure your project

   - Copy your project files to the XAMPP web server directory (usually `C:\xampp\htdocs\hack_dashboard` on Windows);
   - Edit your project configuration files if necessary.

4. Install Python and required packages

   - Download and install [Python](https://www.python.org/downloads/);
   - Open the Windows command prompt;
   - Navigate to your project directory;
   - Install the required packages using pip:

      ```bash
      python -m pip install -r requirements.txt
      ```

       or install them individually using:

      ```bash
      pip install <package>
      ```

</br>

## Usage

1. Start XAMPP

   - Launch XAMPP Control Panel;
   - Click "Start" next to Apache.
  
2. Run an SQL server instance and use our 'mydb_wine.sql' file
   This will ensure you are connected to a database that our program is compatible with. It can also run on any web server/host.

4. Access your PHP website

   - Ensure XAMPP is running;
   - Click "Admin" button to acces the root/index of our website.

5. Run the Python code

   - Open a terminal/command prompt;
   - Navigate to your project directory;
   - Execute your Python script using the following command:
   
      ```bash
      python main.py
      ```

6. Refresh the dashboard using the button
    All the data of the SQL will appear.

___

</br>

# :raised_hands: Acknowledgements
Bernardo Esteves [@berestv](https://github.com/berestv)

Bruno Lopes [@brpereiraa](https://github.com/brpereiraa)

João Ramalhosa [@joaoped2-42PORTO](https://github.com/joaoped2-42PORTO)

Ricardo Santos [@rssantos342](https://github.com/rssantos342)

Teresa Chow (me)

Vinicius Vaccari [@vivaccar](https://github.com/vivaccar)
___

</br>

### License
This work is published under the terms of the [MIT License](./LICENSE).

</br>

[⬆ back to top](#sogrape-webscraper)
