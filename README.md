# Python Mobile Automation

This project demonstrates how to do mobile automation in Python using Appium, UiAutomator2 and Celery.

## Prerequisites

- Python 3.x
- Appium server installed and running
- Redis server installed and running
- An Android device

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/MayThazinKhin/python-mobile-automation.git
    cd python-mobile-automation
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    

4. **Start the Appium Server:**

    Ensure that the Appium server is running. You can start it from the command line using:

    ```bash
    appium
    ```
5. **Start the Redis Server:**

    Ensure that the Appium server is running. You can start it from the command line using:

    ```bash
    redis-server
    ```

5. **Test each scripts:**

- uiautomator2 folder
- celery folder
- manage-proxies.py
- inspect-apk.py
- appium folder
