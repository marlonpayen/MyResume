from django.template import loader
from django.http.response import HttpResponse
from resume.models import Contact, WorkExperience, Education, Skill, Language
import pdfkit
from MyResume.settings import MEDIA_URL
# Create your views here.
def index(request):
    # Fetch objects that needs to be displayed on the main page
    contact = Contact.objects.first()
    work_experiences = WorkExperience.objects.all().order_by('-id')
    educations = Education.objects.all()
    skills = Skill.objects.all()
    languages = Language.objects.all()
    
    # Define the index page + passing the objects we want to display
    template = loader.get_template('resume/index.html')
    context = {
        'contact' : contact,
        'work_experiences' : work_experiences,
        'educations' : educations,
        'skills' : skills,
        'languages' : languages,
        'MEDIA_URL' : MEDIA_URL
    }
    
    #pdfkit.from_file('resume/index.html', 'resume.pdf', verbose=True, options={'enable-local-file-access': True})
    
    
    return HttpResponse(template.render(context, request))