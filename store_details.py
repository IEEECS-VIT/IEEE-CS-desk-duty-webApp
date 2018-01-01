from pymongo import MongoClient
import collections
client=MongoClient('mongodb://localhost:27017');
db=client.StudentDetails
days=["monday","tuesday","wednesday","thursday","friday"]

#storing details of the student in the database
	
def store(regno,mobile,email,branch):
	details={
	"regno":regno,
	"mobile":mobile,
	"email":email,
	"branch":branch
	}
	det=db.stud_det
	result=det.insert_one(details)


#storing details of the schedule of the student in the database

def store_time_table(timetable,regno):
	TimeTable=db.schedule
	schd=collections.OrderedDict()
	for day in days:
		i=days.index(day)
		schd[str(regno)]=collections.OrderedDict()
		for pos_day_schedule in range(len(timetable[i])):
			schd[regno][str(pos_day_schedule+1)]=str(timetable[i][pos_day_schedule])
		TimeTable.update_one({"day":day},{"$push":{"schedule":schd}})
	print(schd)

