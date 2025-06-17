from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.staticfiles.storage import staticfiles_storage

def home(request):
    return render (request, "home.html")

def about(request):
    return render(request, "about.html")

def projects(request):
    projects_show=[
        {
            "title":"Job Portal Using Python",
         "path":"css/images/python_crud.png",
         "git_hub":"https://github.com/Santoshkumar70/Assignment_two/blob/main/jobportal.py"
         },
         {
            "title":" ",
         "path":"css/images/digital_clock.png",
         "git_hub":"https://github.com/Santoshkumar5371/digital-clock-using-JavaScript-/blob/main/clock.html"
         }
        
    ]
    return render(request, "projects.html",{"projects_show":projects_show} )

def experience(request):
    experience_list=[
        {
            "company":"YOTTA TECH PORT'S.",
            "position":"PROJECT INTERN" },
    ]

    return render(request, "experience.html",{"experience_list":experience_list})

def cerifications(request):
    return render(request, "certifications.html")

def contact(request):
    return render(request, "contact.html")

def resume(request):
    resume_path = "my_resume/santosh_kumar.pdf"
    resume_path = staticfiles_storage.path(resume_path)
    if staticfiles_storage.exists(resume_path):
        with open(resume_path,"rb") as resume_files:
            response = HttpResponse(resume_files.read(),content_type="application/pdf")
            response['Content-Disposition']='attachment';filename = "santosh_kumar.pdf"
            return response
    else:
        return HttpResponse("Resume not found",status=404)