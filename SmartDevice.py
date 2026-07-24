from abc import ABC, abstractmethod
 
class SmartDevice(ABC):
    def show_device(self):
        print("Device: " + self.__class__.__name__)
    
    @abstractmethod
    def turn_on(self):
        pass
 
class SmartLight(SmartDevice):
    def turn_on(self):
        print("Light is turned ON")
 
class SmartFan(SmartDevice):
    def turn_on(self):
        print("Fan is turned ON")
 
class SmartSpeaker(SmartDevice):
    def turn_on(self):
        print("Speaker is turned ON")
 
class SecurityCamera:
    def check_status(self):
        return "Security Camera is ACTIVE"
 
class DoorLock:
    def check_status(self):
        return "Door Lock is SECURED"
 
light = SmartLight()
fan = SmartFan()
speaker = SmartSpeaker()
camera = SecurityCamera()
door_lock = DoorLock()
 
print("=== Smart Home Control System ===")
print("")
 
print("Smart Devices:")
light.show_device()
light.turn_on()
 
print("")
fan.show_device()
fan.turn_on()
 
print("")
speaker.show_device()
speaker.turn_on()
 
print("")
print("Security Devices (Polymorphism without Inheritance):")
devices_list = [camera, door_lock]
 
for device in devices_list:
    print(device.check_status())
