import uiautomator2 as u2
import time

def connect_device():
    """
    Connect to the Android device. Replace 'device_ip' with your device's IP if using Wi-Fi,
    or leave it as `u2.connect()` for a USB connection.
    """
    return u2.connect()  # or u2.connect('device_ip')

def start_app(device, package_name):
    """
    Launch the specified app on the device.
    
    Args:
        device: The connected uiautomator2 device instance.
        package_name (str): The package name of the app to start.
    """
    device.app_start(package_name)
    time.sleep(10)  # Wait for the app to fully load

def scroll_down(device, steps=10):
    """
    Perform a scroll down action on the device.
    
    Args:
        device: The connected uiautomator2 device instance.
        steps (int): Number of steps for the scroll action.
    """
    if device(scrollable=True).exists:
        device(scrollable=True).scroll(steps=steps)
    else:
        print("No scrollable element found")

def save_ui_hierarchy(device, filename="../utils/login.xml"):
    """
    Save the current UI hierarchy to an XML file for inspection.
    
    Args:
        device: The connected uiautomator2 device instance.
        filename (str): The name of the file to save the hierarchy.
    """
    xml_content = device.dump_hierarchy()
    with open(filename, "w") as f:
        f.write(xml_content)
    print(f"UI hierarchy saved to {filename}")

def main():
    # Connect to the device
    device = connect_device()
    
    # Launch the app
    package_name = 'com.instagram.android'
    start_app(device, package_name)

    # Perform multiple scroll actions
    for _ in range(3):
        scroll_down(device)
        time.sleep(2)  # Allow time for the UI to stabilize after each scroll

    # Save the UI hierarchy to an XML file
    save_ui_hierarchy(device)

    # Close the app (optional)
    device.app_stop(package_name)

if __name__ == "__main__":
    main()
