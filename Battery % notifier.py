from pynotifier import Notification
import psutil
    
battery=psutil.sensors_battery()
percent=battery.percent
Notification("Battery percentage ",str(percent) + " % Percentage remaining").send()
print("Notification from Python...")

