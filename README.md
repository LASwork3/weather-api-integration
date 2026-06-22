# Weather API Data Integration

A Python integration project that retrieves current weather data from the Open-Meteo REST API, validates and transforms the JSON response, and saves the processed records as a CSV file.

## Project purpose

This project demonstrates a simple end-to-end system integration workflow:

Open-Meteo API → HTTP GET request → JSON validation → data mapping → data transformation → CSV output

The project was created to practise REST APIs, data integration, error handling, logging and technical documentation.

## Features

- Retrieves weather data for Enschede and Rotterdam
- Sends HTTP GET requests to a REST API
- Processes JSON responses
- Validates required data fields
- Maps external API fields to clearer internal field names
- Transforms data into a simplified structure
- Exports processed records to CSV
- Handles timeouts, HTTP errors and invalid responses
- Records successful actions and errors in a log file

## Technologies

- Python
- Requests
- REST API
- HTTP
- JSON
- CSV
- Git

## Project structure

```text
weather-api-integration/
├── main.py
├── README.md
├── requirements.txt
└── .gitignore
```

Generated files such as `weather_data.csv` and `integration.log` are excluded from Git.

## Setup

These instructions are for someone running the project on a new computer.

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
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

### 4. Install the required packages

```bash
pip install -r requirements.txt
```

Using a separate virtual environment keeps this project’s dependencies isolated from other Python projects. :contentReference[oaicite:1]{index=1}

### 5. Run the integration

```bash
python main.py
```

## Output

After running the program, it creates:

- `weather_data.csv` — transformed weather records
- `integration.log` — execution information and error messages

Example CSV fields:

```text
city
observation_time
temperature_celsius
humidity_percent
wind_speed_kmh
processed_at
```

## Integration process

1. The program sends an HTTP GET request to the Open-Meteo API.
2. The API returns current weather information in JSON format.
3. The program checks that all required fields are present.
4. The API fields are mapped to clearer internal field names.
5. The transformed records are saved as CSV.
6. Successful actions and errors are written to a log file.

## Error handling

The project handles:

- Request timeouts
- HTTP errors
- Connection failures
- Missing JSON fields
- Invalid data structures
- Empty output records

## What I learned

Through this project, I practised:

- Working with REST APIs
- Processing JSON data
- Data validation
- Data mapping and transformation
- Building an integration workflow
- Logging and error handling
- Managing Python dependencies
- Using Git and GitHub