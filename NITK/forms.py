from django import forms
import datetime

class StudenLogin(forms.Form):

    rollNo = forms.CharField(label='Roll Number', required=True,max_length=50, widget= forms.TextInput
                                (attrs={'placeholder':'Roll number'})
                               )

    Password = forms.CharField(max_length=32, required=True,widget=forms.PasswordInput
                                    (attrs={'placeholder':'Password'})
                                  )


class StudentRegisterF(forms.Form):
    rollNo = forms.CharField(label='Roll Number', required=True, max_length=50, widget=forms.TextInput(attrs={'placeholder':'Roll number'}))
    Password = forms.CharField(max_length=32, required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    Name = forms.CharField(max_length=32, required=True, widget=forms.TextInput
    (attrs={'placeholder': 'Name'}))
    course = forms.CharField(max_length=32, required=True, widget=forms.TextInput
    (attrs={'placeholder': 'Course'}))
    branch = forms.CharField(max_length=32, required=True, widget=forms.TextInput
    (attrs={'placeholder': 'Branch'}))
    semester = forms.IntegerField( required=True,initial=1)
    cgpa = forms.FloatField( required=True,initial=0.0)
    credits = forms.IntegerField(required=True,initial=0)


class NewsUpdateF(forms.Form):
    date = forms.DateField(label = 'Date', initial=datetime.date.today(), disabled=True)
    news = forms.CharField(label='Enter News', required=True,max_length=500, widget= forms.TextInput
                                (attrs={'placeholder':'News'}))


class FacultyLoginF(forms.Form):
    Fid = forms.CharField(label='Faculty Id', required=False,max_length=50, widget= forms.TextInput
                                (attrs={'placeholder':'Faculty Id'}))

    Password = forms.CharField(max_length=32, required=False, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

class SubjectRegister(forms.Form):
    subj1 = forms.CharField(label='Subject 1', required=True, max_length=50, widget=forms.TextInput
    (attrs={'placeholder': 'Subject Name'}))
    subj2 = forms.CharField(label='Subject 2', required=True, max_length=50, widget=forms.TextInput
    (attrs={'placeholder': 'Subject Name'}))
    subj3 = forms.CharField(label='Subject 3', required=True, max_length=50, widget=forms.TextInput
    (attrs={'placeholder': 'Subject Name'}))
    subj4 = forms.CharField(label='Subject 4', required=True, max_length=50, widget=forms.TextInput
    (attrs={'placeholder': 'Subject Name'}))
    subj5 = forms.CharField(label='Subject 5', required=True, max_length=50, widget=forms.TextInput
    (attrs={'placeholder': 'Subject Name'}))