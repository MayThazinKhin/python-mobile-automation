from androguard.misc import apk

class APKAnalyzer:
    def __init__(self, apk_path):
        self.apk_path = apk_path
        self.apk = None

    def load_apk(self):
        """Loads APK file and initializes the APK object."""
        self.apk = apk.APK(self.apk_path)

    def get_metadata(self):
        """Extracts and returns APK metadata as a dictionary."""
        if not self.apk:
            self.load_apk()
            
        return {
            'package_name': self.apk.get_package(),
            'version_name': self.apk.get_androidversion_name(),
            'version_code': self.apk.get_androidversion_code(),
            'permissions': self.apk.get_permissions(),
            'main_activity': self.apk.get_main_activity(),
            'signature': self.apk.get_signature(),
        }

# Example usage
if __name__ == "__main__":
    analyzer = APKAnalyzer("sample.apk")
    metadata = analyzer.get_metadata()
    print(metadata)
