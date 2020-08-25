from datetime import datetime

class Time:

    def get_time(self):
        time_now = datetime.now()
        current_time = time_now.strftime("%H.%M:%S")
        return current_time[:5]





