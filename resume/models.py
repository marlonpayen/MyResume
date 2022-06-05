from django.db import models
from django.db.models.fields.json import JSONField
from django.core.exceptions import ValidationError
from resume.util.resume import constants
from MyResume.settings import MEDIA_URL

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    country = models.CharField(max_length=30, choices=constants.Languages_Countries.countries) # Dropdown list with all the countries defined in the constants file
    city = models.CharField(max_length=20)
    email = models.CharField(max_length=80)
    about_me = models.TextField() # Bigger than CharField object and text area rendered on the HTML file
    phone_number = models.CharField(max_length=20)
    image = models.ImageField(upload_to='') # Upload of the profile image in the media folder (defined in MEDIA_ROOT)
    links = JSONField
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # We can only have one contact, the person who is creating her own resume
    def clean(self):
        if Contact.objects.exists() and not self.pk:
            raise ValidationError('There can only be one contact')
         
         
    def save(self, *args, **kwargs):
        return super(Contact, self).save(*args, **kwargs) #saves the record
    
    # Concatenate first and last name for display
    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)
    
    
class WorkExperience(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()     
    is_current = models.BooleanField() # There can be only one current job
    role = models.CharField(max_length=50)
    country = models.CharField(max_length=30, choices=constants.Languages_Countries.countries) # Dropdown list with all the countries defined in the constants file
    city = models.CharField(max_length=20)
    company = models.CharField(max_length = 60)
    description = models.TextField() # Bigger than CharField object and text area rendered on the HTML file
    
    class Meta:
        ordering = ('start_date',)
        constraints = [
            models.UniqueConstraint(fields=['is_current'], name='unique is_current')
        ]
        
    
class Education(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()  
    school = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    degree = models.CharField(max_length=50)
    type_of_degree = models.CharField(max_length=50)
    
    
    
class Skill(models.Model):
    name = models.CharField(max_length=30)
    proficiency = models.CharField(max_length=20, choices=constants.Skill_Proficiency.skill_proficiencies)# Dropdown list with all the skill proficiencies defined in the constants file
    
        
class Language(models.Model):
    name = models.CharField(max_length=30, choices=constants.Languages_Countries.languages) # Dropdown list with all the languages defined in the constants file
    proficiency = models.CharField(max_length=20, choices=constants.Language_Proficiency.language_proficiencies) # Dropdown list with all the language proficiencies defined in the constants file
    
    
    
    
    