from django.contrib import admin
from resume.models import Contact, WorkExperience, Education, Skill, Language


class ContactAdmin(admin.ModelAdmin):
    #fields = ['first_name', 'last_name']
    list_display = ('full_name', 'title', 'updated_at')

    # This will help you to disbale add functionality
    def has_add_permission(self, request):
        if Contact.objects.exists():
            return False
        
        return True
    
# Register Contact and ContactAdmin
admin.site.register(Contact, ContactAdmin)  




class WorkExperienceAdmin(admin.ModelAdmin):
    #fields = ['first_name', 'last_name']
    list_display = ('role', 'company', 'country', 'city')

    
# Register Work_Experience and WorkExperienceAdmin
admin.site.register(WorkExperience, WorkExperienceAdmin)   




class EducationAdmin(admin.ModelAdmin):
    #fields = ['first_name', 'last_name']
    list_display = ('degree', 'school', 'place')

    
# Register Education and EducationAdmin
admin.site.register(Education, EducationAdmin) 



class SkillAdmin(admin.ModelAdmin):
    #fields = ['first_name', 'last_name']
    list_display = ('name', 'proficiency')

    
# Register Skill and SkillAdmin
admin.site.register(Skill, SkillAdmin) 



class LanguageAdmin(admin.ModelAdmin):
    #fields = ['first_name', 'last_name']
    list_display = ('name', 'proficiency')

    
# Register Language and LanguageAdmin
admin.site.register(Language, LanguageAdmin) 
    
    