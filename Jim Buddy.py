import os
from datetime import datetime

class GymAttendanceTracker:
    def __init__(self, gym_name):
        self.gym_name = gym_name
        self.attendance_file = f"{gym_name}_attendance.txt"
        self.attendance = set()

    def record_attendance(self, member_id): 
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
        attendance_entry = f"{timestamp} - Member ID: {member_id}"
        self.attendance.add(attendance_entry)

    def save_attendance_to_file(self):
        with open(self.attendance_file, 'a') as file:
            for entry in self.attendance:
                file.write(entry + '\n')

    def display_attendance(self):
        print(f"Attendance for {self.gym_name}:")
        for entry in self.attendance:
            print(entry)

def main():
    gym_name = "FitHub"
    tracker = GymAttendanceTracker(gym_name)
