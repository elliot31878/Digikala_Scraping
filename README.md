# Web Scraping Application: Digikala Mobile Prices

This Python application is a practical example of web scraping. The app scrapes the [Digikala](https://www.digikala.com) website to gather mobile phone names and their corresponding prices. The scraped data is then saved into an SQLite database, and the application provides the option to export the data to an Excel file.

![digikala](https://user-images.githubusercontent.com/63051195/127722615-ac17b8ec-64a4-44f1-8162-bb6feb3eced5.gif)


## Table of Contents
- [Features](#features)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Step 1: Clone the Repository](#step-1-clone-the-repository)
  - [Step 2: Create and Activate a Virtual Environment](#step-2-create-and-activate-a-virtual-environment)
  - [Step 3: Install Dependencies](#step-3-install-dependencies)
  - [Step 4: Running the Application](#step-4-running-the-application)
- [Application Overview](#application-overview)
  - [Web Scraping](#web-scraping)
  - [Database Management](#database-management)
  - [Excel Export](#excel-export)
- [Code Structure](#code-structure)
- [Future Features](#future-features)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Web Scraping**: Scrape mobile names and prices from Digikala.
- **SQLite Database**: Save scraped data into an SQLite database for persistence.
- **Excel Export**: Export the scraped data from the database to an Excel file for further analysis or reporting.
- **Automated Data Collection**: Gather data from the web automatically and organize it in a structured format.

## Installation

Follow the steps below to set up and run the application on your local machine.

### Prerequisites

- **Python 3.x**: Ensure Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
- **PyCharm**: (Optional but recommended) Use PyCharm IDE for a better development experience. You can download it from [jetbrains.com](https://www.jetbrains.com/pycharm/download/).

### Step 1: Clone the Repository

Start by cloning the GitHub repository:

```bash
git clone https://github.com/elliot31878/Digikala_Scraping.git
cd Digikala_Scraping
