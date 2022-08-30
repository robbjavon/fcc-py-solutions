def add_time(start, duration, day=None):

  start_hour = int(start[:-2].split(":")[0])
  start_minute = int(start[:-2].split(":")[1])
  duration_hour = int(duration.split(":")[0])
  duration_minute = int(duration.split(":")[1])
  am_pm = start[-2:]
  days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

  if start_hour == 12 and am_pm == "AM":
    start_hour = 0
  if start_hour == 12 and am_pm == "PM":
    start_hour = 0

  if start_minute + duration_minute > 60 :
    end_minute = start_minute + duration_minute - 60
    if am_pm == "PM":
      end_hour = start_hour + duration_hour + 1 + 12
    else:
      end_hour = start_hour + duration_hour + 1
  else:
    end_minute = start_minute + duration_minute
    if am_pm == "PM":
      end_hour = start_hour + duration_hour + 12
    else:
      end_hour = start_hour + duration_hour

  if end_hour//24 < 1:
    days_no = ""
  elif end_hour//24 == 1:
    days_no = " (next day)"
  else:
    days_no = " (" + str(end_hour//24) + " days later)"
  
  if end_hour - ((end_hour//24)*24) < 12:
    if end_hour - ((end_hour//24)*24) == 0:
      new_hour = end_hour - ((end_hour//24)*24) + 12
    else:
      new_hour = end_hour - ((end_hour//24)*24)
    new_am_pm = " AM"
  else:
    if end_hour - ((end_hour//24)*24) == 12:
      new_hour = end_hour - ((end_hour//24)*24)
    else:
      new_hour = end_hour - ((end_hour//24)*24) -12
    new_am_pm = " PM"

  if day != None:
    week_days_count = int(days.index(day.lower().capitalize())) + end_hour//24
    new_day = ", " + days[week_days_count % 7]
  else:
    new_day = ""

  new_time = str(new_hour) + ":" + str(end_minute).zfill(2) + new_am_pm + new_day + days_no
  return new_time

  
