def add_time(start, duration, startDay=None):
  time = start.split()
  value = time[0]
  dayNight = time[1]

  split_further = value.split(":")
  hours = split_further[0]
  minutes = split_further[1]

  split = duration.split(":")
  hours1 = split[0]
  minutes1 = split[1]

  if dayNight == "PM":
    hours = str(int(hours) + 12)

  new_hours = str(int(hours) + int(hours1))

  new_minutes = str(int(minutes) + int(minutes1))

  if int(new_minutes) >= 60:
    new_minutes = str(int(new_minutes) - 60)
    new_hours = str(int(new_hours) + 1)

  if int(new_minutes) < 10:
    new_minutes = "0" + new_minutes

  days = 0
  while int(new_hours) >= 24:
    new_hours = str(int(new_hours) - 24)
    days += 1

  if int(new_hours) > 12:
    new_hours = str(int(new_hours) - 12)
    dayNight = "PM"
  elif int(new_hours) > 0 and int(new_hours) < 12:
    dayNight = "AM"
  elif int(new_hours) == 12:
    dayNight = "PM"
  else:
    dayNight = "AM"
    new_hours = str(int(new_hours) + 12)

  if days > 0:
    days_later = " (" + str(
        days) + " days later)" if days > 1 else " (next day)"
  else:
    days_later = ""

  weekDay = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
             "Saturday", "Sunday")

  #calculate weekday
  if startDay:
    dayWeek = days // 7
    startDay = startDay.lower().capitalize()
    week = weekDay.index(startDay) + (days - 7 * dayWeek)
    if week > 6:
      week -= 7
    dayOfTheWeek = ", " + weekDay[week]
  else:
    dayOfTheWeek = ""

  new_time = new_hours + ":" + new_minutes + " " + dayNight + dayOfTheWeek + days_later
  return new_time
