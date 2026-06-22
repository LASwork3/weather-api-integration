# Weather API Data Integration

## About the project

I built this project to gain practical experience with APIs and understand how data moves between separate systems.

The Python script retrieves current weather data for Enschede and Rotterdam from the Open-Meteo REST API. It checks the returned JSON data, transforms it into a simpler structure and saves the processed records in a CSV file.

## What is an API?

An API, or Application Programming Interface, allows separate software systems to exchange information through a defined set of requests and responses.

In this project, the Python script sends an HTTP GET request to Open-Meteo. The API returns weather information in JSON format, which the script then processes.

## Purpose

The purpose of this project was to practise the main steps of a system integration:

1. Connect to an external system through an API.
2. Retrieve data through an HTTP request.
3. Validate that the expected data is present.
4. Map and transform the data into a clearer structure.
5. Save the processed data in a local output file.
6. Record successful actions and errors through logging.

## Integration flow


Open-Meteo API
      ↓
HTTP GET request
      ↓
JSON response
      ↓
Data validation
      ↓
Data mapping and transformation
      ↓
Temperature categorisation
      ↓
CSV output


## Features

* Retrieves current weather data for Enschede and Rotterdam
* Sends HTTP GET requests to a REST API
* Processes JSON responses
* Checks that required fields are present
* Maps API field names to clearer internal names
* Categorises temperatures as cold, mild or warm
* Prints a weather summary in the terminal
* Saves processed records as CSV
* Handles request timeouts, connection failures and HTTP errors
* Records activity and errors in a log file

## Technologies

* Python
* Requests
* REST API
* HTTP
* JSON
* CSV
* Git
* GitHub

## Project structure

```text
weather-api-integration/
├── main.py
├── README.md
├── requirements.txt
└── .gitignore
```

The generated `weather_data.csv` and `integration.log` files are excluded from Git.

## Setup

These instructions are for someone running the project on a new computer.

### 1. Clone the repository

```bash
git clone https://github.com/LASwork3/weather-api-integration.git
cd weather-api-integration
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
```

### 3. Activate the virtual environment

On macOS or Linux:

```bash
source .venv/bin/activate
```

On Windows:

```bash
.venv\Scripts\activate
```

### 4. Install the dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the integration

```bash
python main.py
```

## Output

The script creates a CSV file containing:

* City
* Observation time
* Temperature in degrees Celsius
* Temperature category
* Humidity percentage
* Wind speed in kilometres per hour
* Processing time

It also creates an `integration.log` file containing successful operations and error messages.

## What I learned

Through this project, I gained practical experience with:

* Sending requests to a REST API
* Understanding JSON responses
* Validating incoming data
* Mapping and transforming data
* Applying simple business rules
* Handling API and connection errors
* Writing logs
* Managing Python dependencies
* Using Git and GitHub

I also learned that an integration needs to account for failures and unexpected data, rather than only working when every request succeeds.

## Possible next steps

Future improvements could include:

* Saving records in a SQLite database
* Preventing duplicate records
* Moving locations into a configuration file
* Adding automated tests
* Scheduling the script to run automatically
