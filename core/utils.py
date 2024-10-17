from lessons.service import LessonTemplateService
import re

def search_element_ids_template(template):
    items = re.findall(r'{{(.*?)}}', template)
    return items
    
def fill_template_with_user_preferences(preferences, template):
    service = LessonTemplateService(template)
    if not preferences:
        return None
    
    template_edit = ''
    for key in preferences.keys():
        template_edit = service.modify_style_template(key, preferences[key]['property'], preferences[key]['value'])
    
    template_edit = template_edit.replace('{{', '').replace('}}', '')
    return template_edit
