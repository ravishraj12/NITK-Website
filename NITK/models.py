from django.db import models
import datetime

loggedIn = {}
# Create your models here.
class StudentData(models.Model):
    rollNo = models.CharField(max_length=8, primary_key=True)
    Name = models.CharField(max_length=50)
    Course = models.CharField(max_length=10)
    branch = models.CharField(max_length=25)
    password = models.CharField(max_length=10)
    semester = models.IntegerField(default=1)
    cgpa = models.FloatField(default=0.0)
    credits = models.IntegerField(default=0)
    isIcPc = models.BooleanField(default=False)

    class Meta:
        managed = True

    def __str__(self):
        return "%s" % (self.rollNo)

    def MakeIcPc(self, rollNo):
        d = StudentData.objects.get(rollNo = rollNo)
        d.isIcPc = True
        d.save()


    def GetStudentData(self, RollNo):
        d = StudentData.objects.filter(rollNo = RollNo).values()
        if (len(d) != 0):
            return d[0]
        else: return 0

    def LoginStudent(self,rollNo, pwd):
        password = self.GetStudentData(rollNo)["password"]

        if (pwd == password):
            l = LoggedInUsers(0, rollNo)
            l.save()
            return True
        else:
            return False

    def LogoutStudent(self,user):
        l = LoggedInUsers(0, user)
        l.__class__.objects.get(ids = user).delete()

    def GetSubjects(self, rollNo):
        s = Subjects.objects.all().values()
        if (len(s) != 0):
            return s[0]
        else: return 0


class Subjects(models.Model):
    rollNo = models.CharField(max_length=8)
    Subj1 = models.CharField(max_length=50)
    Subj2 = models.CharField(max_length=50)
    Subj3 = models.CharField(max_length=50)
    Subj4 = models.CharField(max_length=50)
    Subj5 = models.CharField(max_length=50)

    def GetStudentSubjects(self, RollNo):
        s = Subjects.objects.filter(rollNo=RollNo).values()
        if (len(s) != 0):
            return s[0]
        else: return 0

class NewsUpdates(models.Model):
    date = models.DateField()
    News = models.TextField()

    class Meta:
        ordering = ('date',)

    def GetNews(self):
        p = NewsUpdates.objects.all()

        if (len(p) != 0):
            return p
        else:
            return 0


class FacultyData(models.Model):
    FacultyId = models.TextField(max_length=8, primary_key=True)
    password = models.CharField(max_length=8)
    name = models.CharField(max_length=20)

    def GetFacultyData(self, id):
        d = FacultyData.objects.filter(FacultyId = id).values()
        if (len(d) != 0):
            return d[0]
        else: return 0

    def LoginFaculty(self,id, pwd):
        password = self.GetFacultyData(id)["password"]
        if (pwd == password):
            l = LoggedInUsers(1, id)
            l.save()
            return True
        else:
            return False

    def LogoutFaculty(self,user):
        l = LoggedInUsers(1, user)
        l.__class__.objects.get(ids = user).delete()


    def AddNews(self, news):
        n = NewsUpdates(datetime.date.today(), news)
        n.save()


class PlacementsUpdate(models.Model):
    date = models.DateField()
    update = models.TextField()

    class Meta:
        ordering = ('date',)

    def GetPlacementsUpdate(self):
        p = PlacementsUpdate.objects.all()

        if (len(p) != 0):
            return p
        else: return 0


    def AddPlacementUpdate(self, update):
        p = PlacementsUpdate(datetime.date().today(),update )
        p.save()


class LoggedInUsers(models.Model):
    type = models.IntegerField()        #0-student, 1-faculty 2-IC/PC
    ids = models.CharField(max_length=8,primary_key=True)

    def IsLoggedIn(self, id):
        logged = LoggedInUsers.objects.filter(is_deleted=False).values(id)
        for user in logged:
            print(user)


class Career(models.Model):
    position = models.CharField(max_length=25)
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    college = models.CharField(max_length=50)
    degree = models.CharField(max_length=50)
    exp = models.CharField(max_length=100)

class Career2(models.Model):
    position = models.CharField(max_length=25)
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    college = models.CharField(max_length=50)
    degree = models.CharField(max_length=50)
    exp = models.CharField(max_length=100)


class Fedback(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    dept = models.CharField(max_length=20)
    feedback = models.CharField(max_length=500)


