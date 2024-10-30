import requests
import logging
from celery import Celery
from sqlalchemy.orm import Session
from model import Launch, SessionLocal
from celery_config import app
from datetime import datetime

# New API URL for SpaceX launches
API_URL = "https://api.spacexdata.com/v4/launches"

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.task(bind=True, max_retries=3)
def fetch_and_store_launches(self):
    """
    Fetch SpaceX launches from the API and store them in the database.
    Retries on failure are handled automatically.
    """
    try:
        launches_data = fetch_launch_data()
        store_launch_data(launches_data)
        
        # Log success
        logger.info(f"Successfully fetched and stored {len(launches_data)} SpaceX launches.")

    except requests.RequestException as exc:
        logger.error(f"Network error occurred: {exc}")
        raise self.retry(exc=exc, countdown=60)
    except Exception as exc:
        logger.error(f"An unexpected error occurred: {exc}")
        raise self.retry(exc=exc, countdown=60)

def fetch_launch_data():
    """
    Fetch the launch data from the SpaceX API.

    Returns:
        list: A list of launch objects.
    """
    response = requests.get(API_URL)
    response.raise_for_status()
    return response.json()  # Return the list of launches

def store_launch_data(launches):
    """
    Store the fetched launches in the database.

    Args:
        launches (list): The list of launch objects to store.
    """
    with SessionLocal() as session:
        for launch in launches:
            launch_record = create_launch_record(launch)
            session.merge(launch_record)  # Merge to update if exists or add if new
        session.commit()

def create_launch_record(launch):
    """
    Create a Launch object from the launch data.

    Args:
        launch (dict): The launch data from the SpaceX API.

    Returns:
        Launch: An instance of the Launch model.
    """
    failures = ', '.join(f"{f['reason']} at {f['time']} seconds" for f in launch.get('failures', []))
    return Launch(
        id=launch['id'],  # SpaceX launch ID
        name=launch['name'],  # Title of the launch
        details=launch.get('details', "No details available."),  # Launch details
        success=launch['success'],  # Launch success status
        date_utc=datetime.fromisoformat(launch['date_utc'].replace("Z", "+00:00")),  # UTC datetime
        rocket_id=launch['rocket'],  # Rocket ID used
        failures=failures if failures else "No failures reported.",  # Failure descriptions
        web_url=launch['links'].get('article')  # Article link if available
    )
