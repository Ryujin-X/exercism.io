from datetime import date
import calendar

class MeetupDayException(Exception):
	pass
	
def meetup_day(year, month, weekday, day):
	weekdays_dict = {'Monday':0, 'Tuesday':1, 'Wednesday':2, 'Thursday':3, 'Friday':4, 'Saturday':5, 'Sunday':6}
	weekday_list = []
	days_in_month = calendar.monthrange(year, month)
	days_in_month = days_in_month[-1]

	for i in range(1, days_in_month+1):
		if calendar.weekday(year, month, i) == weekdays_dict[weekday]:
			weekday_list.append(i)
	if day[0].isdigit():
		day_number = int(day[0]) - 1
		if day_number > len(weekday_list) - 1:
			raise MeetupDayException("Error: That is not a valid date!")
		else:
			output_date = date(year, month, weekday_list[day_number])
	elif day == "teenth":
		for chosen_day in weekday_list:
			if chosen_day in range(13, 20):
				output_date = date(year, month, chosen_day)
	else:
		output_date = date(year, month, weekday_list[-1])
	return output_date
