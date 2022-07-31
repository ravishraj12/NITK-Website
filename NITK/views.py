from django.shortcuts import render
from .forms import *
from .models import *
from django.shortcuts import render,redirect, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def HomePage(request):
    #load news, placement updates  from database
    n = NewsUpdates()
    news = n.GetNews()

    p = PlacementsUpdate()
    Pnews = p.GetPlacementsUpdate()

    content = {
        "news" : news,
        "Pnews" : Pnews,
    }

    return render(request, 'Home.html', content)

def OrgChart(request):
    return render(request, 'org.html')

def About(request):
    return render(request,'About.html')

def RegisterSubjects(request, rollNo):
    s1 = request.POST["subj1"]
    s2 = request.POST["subj2"]
    s3 = request.POST["subj3"]
    s4 = request.POST["subj4"]
    s5 = request.POST["subj5"]

    if (len(s1)==0 or len(s2)==0 or len(s3)==0 or len(s4)==0 or len(s5)==0):
        messages.error(request, "Enter all subjects!")

    s = Subjects(0, rollNo,s1,s2,s3,s4,s5)
    s.save()
    return redirect(StudentPage, rollNo)



def StudentPage(request, rollNo):
    s = StudentData()
    d = s.GetStudentData(rollNo)
    su = Subjects()
    subj = su.GetStudentSubjects(rollNo)
    reg = SubjectRegister()
    subjects = []
    if subj == 0:
        isSubj = 0
    else:
        isSubj = 1
        for i in range(1, 6):
            subjects.append(subj["Subj" + str(i)])

    n = PlacementsUpdate()
    news = n.GetPlacementsUpdate()

    content = {
        "stdData": d,
        "isSubj" : isSubj,
        "Subjects":subjects,
        "form": reg,
        "news": news,
    }

    return render(request, 'StudentHome.html', content)


def StudentLogin(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = StudenLogin(request.POST)
        # check whether it's valid:
        if form.is_valid():
            rollNo = request.POST["rollNo"]
            pwd = request.POST['Password']
            s = StudentData()
            d = s.GetStudentData(rollNo)
            if (d != 0 ):
                if d["password"] == pwd:
                    s.LoginStudent(rollNo,pwd)
                    return redirect(StudentPage,rollNo)
                else:
                    form = StudenLogin()
                    messages.error(request, "Roll number or password is incorrect.")
                    return render(request, 'StudentLogin.html', {'form': form})
            else:
                messages.error(request, "Student is not registered.")
                return render(request, 'StudentLogin.html', {'form': form})
    else:
        form = StudenLogin()
        return render(request, 'StudentLogin.html', {'form': form})

def LogoutS(request, rollNo):
    logout(request)
    s = StudentData()
    s.LogoutStudent(rollNo)
    return redirect(HomePage)

def LogoutF(request, Fid):
    logout(request)
    s = FacultyData()
    s.LogoutFaculty(Fid)
    return redirect(HomePage)

def StudentRegister(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = StudentRegisterF(request.POST)
        rollNo = request.POST["rollNo"]
        Name = request.POST["Name"]
        course = request.POST["course"]
        branch = request.POST["branch"]
        semester = request.POST["semester"]
        cgpa = request.POST["cgpa"]
        credits = request.POST["credits"]
        password = request.POST.get("Password")
        print(request.POST.get("dummy"))
        print("HII 2")
        std = StudentData(rollNo,Name,course,branch,password,semester,cgpa,credits)
        std.save()
        std.LoginStudent(rollNo, password)
        return redirect(StudentPage, rollNo)

    else:
        form = StudentRegisterF()
        return render(request, 'StudentRegister.html', {'form': form})

def FacultyPage(request, Fid):
    s = FacultyData()
    d = s.GetFacultyData(Fid)
    f = NewsUpdateF()
    Nmsg = ""
    Pmsg=""
    #post request means news is updated or IC/PC is added.
    if request.method=='POST' and 'AddNews' in request.POST:
        print("News: ",request.POST.get("news", ""))
        n = NewsUpdates(date=datetime.date.today(), News=request.POST["news"])
        n.save()
        Nmsg = "Student News added successfully."

    if request.method=='POST' and 'UpdatePlacements' in request.POST:
        print("PNews: ",request.POST.get("Pnews", ""))
        n = PlacementsUpdate(date=datetime.date.today(), update=request.POST.get("Pnews"))
        n.save()
        Pmsg="Placement News added successfully."

    if request.method == "POST" and "DeleteStd" in request.POST:
        print(request.POST.get("TrollNo"))
        l = StudentData.objects.get(rollNo=request.POST.get("TrollNo"))
        l.delete()

    if request.method == "POST" and "UpdateStd" in request.POST:
        sem = int(request.POST.get("Tsemester"))
        c = float(request.POST.get("Tcgpa"))
        cr = int(request.POST.get("Tcredits"))
        l = StudentData(rollNo =request.POST.get("TrollNo"),
                        Name=request.POST.get("Tname"),
                        Course=request.POST.get("Tcourse"),
                        branch=request.POST.get("Tbranch"),
                        semester=sem,
                        cgpa=c,
                        credits=cr
                        )
        l.save()


    #show data of searched student
    std = {}
    n= []
    if request.method == 'POST' and 'Student' in request.POST:
        r = request.POST.get("rollNo")
        s = StudentData()
        std = s.GetStudentData(r)
        if std == 0:
            messages.error(request, "Student is not registered.")


    content = {
        "Fdata": d,
        "NewsForm": f,
        "Nmsg":Nmsg,
        "Pmsg":Pmsg,
        "std": std,
    }

    return render(request, "FacultyHome.html", content)

def FacultyLogin(request):
    if request.method == "POST":
        form = FacultyLoginF(request.POST)
        if form.is_valid():
            Fid = request.POST["Fid"]
            pwd = request.POST['Password']
            s = FacultyData()
            d = s.GetFacultyData(Fid)
            if (d != 0 ):
                if d["password"] == pwd:
                    s.LoginFaculty(Fid, pwd)
                    return redirect(FacultyPage, Fid)
                else:
                    form = FacultyLoginF()
                    messages.error(request, "Faculty ID or password is incorrect.")
                    return render(request, 'facultyLogin.html', {'form': form})
            else:
                messages.error(request, "Faculty is not registered.")
                return render(request, 'facultyLogin.html', {'form': form})
    else:
        form = FacultyLoginF()
        return render(request, 'facultyLogin.html', {'form': form})


def AcademicOffice(request):
    return render(request, 'academic_office.html');

def Hod(request):
    return render(request, 'Hod.html');

def Director(request):
    return render(request, 'director.html');

def DeleteData(request, rollNo):
    if request.method == "POST":
        l = StudentData.objects.get(rollNo=rollNo)
        l.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def updateData(request, rollNo):
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def pgProgram(request):
    return render(request, 'pg_programme.html');

def ugProgram(request):
    return render(request, 'ug_program.html');

def AcadCal(request):
    return render(request, 'AcademicsCalender.html');

def Depart(request):
    return render(request, 'Dep&Cen.html');

def Fee(request):
    return render(request, 'FeeStr.html');

def Feed(request):
    if request.method == "POST":
        fname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        email = request.POST.get("mailid")
        dept = request.POST.get("dept")
        feedback = request.POST.get("feedback")
        name = fname+lastname

        f = Fedback(
            name = name,
            email = email,
            dept = dept,
            feedback=feedback
        )
        f.save()

        messages.info(request, "Feedback submitted successfully!")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    else:
        return render(request, 'feedback.html');

def NonTeach(request):
    if request.method == "POST":
        c = Career2(
            position=request.POST.get("position"),
            name=request.POST.get("fname"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            gender=request.POST.get("gender"),
            college=request.POST.get("college"),
            degree=request.POST.get("degree"),
            exp=request.POST.get("exp")
        )
        c.save()
        messages.info(request, "Application form submitted successfully.You will be contacted shortly.")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return render(request, 'NonTeaching.html');

def Teach(request):
    if request.method == "POST":
        c = Career(
            position=request.POST.get("position"),
            name=request.POST.get("fname"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            gender=request.POST.get("gender"),
            college=request.POST.get("college"),
            degree=request.POST.get("degree"),
            exp=request.POST.get("exp")
        )
        c.save()
        messages.info(request, "Application form submitted successfully.You will be contacted shortly.")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return render(request, 'Teaching.html');


def UgPgSyllabus(request):
    return render(request, 'ug&pg_syllabus.html');

def UgPgTt(request):
    return render(request, 'ug&pg_tt.html');
