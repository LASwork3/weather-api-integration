import csv
import logging
from datetime import datetime
from typing import Any

import requests


API_URL = "https://api.open-meteo.com/v1/forecast"
OUTPUT_FILE = "weather_data.csv"

LOCATIONS = [
    {
        "city": "Enschede",
        "latitude": 52.2215,
        "longitude": 6.8937,
    },
    {
       
        "city": "Rotterdam",
        "latitude": 51.9225,
        "longitude": 4.4792,
    },
]


logging.basicConfig(
    filename="integration.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)


def fetch_weather(location: dict[str, Any]) -> dict[str, Any]:
    """Retrieve current weather data from Open-Meteo."""

    params = {
        "latitude": location["latitude"],
        "longitude": location["longitude"],
        "current": [
            "temperature_2m",
            "relative_humidity_2m",
            "wind_speed_10m",
        ],
        "timezone": "Europe/Amsterdam",
    }

    response = requests.get(
        API_URL,
        params=params,
        timeout=10,
    )

    response.raise_for_status()
    return response.json()


def validate_response(data: dict[str, Any]) -> None:
    """Check that the required API fields exist."""

    if "current" not in data:
        raise ValueError("Response does not contain current weather data.")

    required_fields = [
        "time",
        "temperature_2m",
        "relative_humidity_2m",
        "wind_speed_10m",
    ]

    missing_fields = [
        field
        for field in required_fields
        if field not in data["current"]
    ]

    if missing_fields:
        raise ValueError(
            f"Missing required fields: {', '.join(missing_fields)}"
        )


def transform_data(
    city: str,
    data: dict[str, Any],
) -> dict[str, Any]:
    """Map the API response to a simpler internal format."""

    current = data["current"]

    return {
        "city": city,
        "observation_time": current["time"],
        "temperature_celsius": current["temperature_2m"],
        "humidity_percent": current["relative_humidity_2m"],
        "wind_speed_kmh": current["wind_speed_10m"],
        "processed_at": datetime.now().isoformat(timespec="seconds"),
    }


def save_to_csv(records: list[dict[str, Any]]) -> None:
    """Write transformed weather records to a CSV file."""

    if not records:
        raise ValueError("No records available to save.")

    fieldnames = list(records[0].keys())

    with open(
        OUTPUT_FILE,
        mode="w",
        newline="",
        encoding="utf-8",
    ) as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)


def run_integration() -> None:
    """Run the complete integration workflow."""

    transformed_records = []

    for location in LOCATIONS:
        try:
            logging.info("Retrieving weather for %s", location["city"])

            raw_data = fetch_weather(location)
            validate_response(raw_data)

            transformed_record = transform_data(
                location["city"],
                raw_data,
            )

            transformed_records.append(transformed_record)

            logging.info(
                "Successfully processed weather for %s",
                location["city"],
            )

        except requests.exceptions.Timeout:
            logging.error(
                "Request timed out for %s",
                location["city"],
            )

        except requests.exceptions.HTTPError as error:
            logging.error(
                "HTTP error for %s: %s",
                location["city"],
                error,
            )

        except requests.exceptions.RequestException as error:
            logging.error(
                "API request failed for %s: %s",
                location["city"],
                error,
            )

        except (ValueError, KeyError, TypeError) as error:
            logging.error(
                "Data-processing error for %s: %s",
                location["city"],
                error,
            )

    if transformed_records:
        save_to_csv(transformed_records)
        print(
            f"Integration completed. "
            f"{len(transformed_records)} records saved to {OUTPUT_FILE}."
        )
    else:
        print("Integration failed. Check integration.log.")


if __name__ == "__main__":
    run_integration()