import uiautomator2 as u2
import time

def connect_device():
    """
    Connect to the Android device.
    """
    return u2.connect()  # Connects via USB; replace with IP if necessary for Wi-Fi connection

def start_app(device, package_name):
    """
    Launch the specified app on the device.
    
    Args:
        device: The connected uiautomator2 device instance.
        package_name (str): The package name of the app to start.
    """
    device.app_start(package_name)
    time.sleep(10)  # Wait briefly for the app to load

def navigate_to_tab(device, tab_id):
    """
    Navigate to a specific tab in the app by resource ID.
    
    Args:
        device: The connected uiautomator2 device instance.
        tab_id (str): The resource ID of the tab to navigate to.
    """
    tab = device(resourceId=tab_id)
    if tab.exists:
        tab.click()
        time.sleep(3)  # Wait for the UI to stabilize after navigation
    else:
        print(f"Tab '{tab_id}' not found")

def get_story_username(device):
    """
    Retrieve and print the username of the first IG Story in the reels tray.
    
    Args:
        device: The connected uiautomator2 device instance.
    """
    try:
        story_container = device(resourceId="com.instagram.android:id/reels_tray_container").child(resourceId="com.instagram.android:id/outer_container")
        if story_container.exists:
            username = story_container[1].child(resourceId="com.instagram.android:id/username").info.get('text', 'Username not found')
            print("First IG Story's username:", username)
        else:
            print("Story container element not found")
    except Exception as e:
        print(f"An error occurred while retrieving the story username: {e}")

def print_current_activity(device):
    """
    Print the current activity of the app.
    
    Args:
        device: The connected uiautomator2 device instance.
    """
    try:
        # Execute the command to get the current activity
        current_activity = device.shell("dumpsys activity | grep mResumedActivity")
        print("Current activity:", current_activity)
    except Exception as e:
        print(f"An error occurred while retrieving the current activity: {e}")



def stop_app(device, package_name):
    """
    Stop the specified app on the device.
    
    Args:
        device: The connected uiautomator2 device instance.
        package_name (str): The package name of the app to stop.
    """
    device.app_stop(package_name)

def main():
    # Initialize device connection
    device = connect_device()
    
    # Launch Instagram app
    package_name = 'com.instagram.android'
    start_app(device, package_name)
    
    # Navigate through Instagram tabs
    tab_ids = [
        "com.instagram.android:id/search_tab",
        "com.instagram.android:id/clips_tab",
        "com.instagram.android:id/profile_tab",
        "com.instagram.android:id/feed_tab"
    ]
    
    for tab_id in tab_ids:
        navigate_to_tab(device, tab_id)
    time.sleep(1)
    
    # Retrieve the username from the first IG Story
    get_story_username(device)

    # print_current_activity(device)
    
    # Stop the app
    stop_app(device, package_name)

if __name__ == "__main__":
    main()
