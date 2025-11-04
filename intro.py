from datetime import datetime
now = datetime.now()
h = input("Enter hour (0–23, Enter = now): ").strip()
m = input("Enter minute (0–59, Enter = now): ").strip()

if h == "" or m == "":
    hour, minute = now.hour, now.minute   # use local time if blank
else:
    hour = int(h)                         # convert after blank check
    minute = int(m)

print("Good morning!" if hour < 12 else "Good evening!")
