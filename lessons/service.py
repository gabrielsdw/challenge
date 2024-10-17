class LessonTemplateService:

    def __init__(self, template):
        self.template = template

    def get_string_alter_style_element(self, element_id, property, value):
        return f"document.getElementById('{element_id}').style.{property} = '{value}'"
    
    def fill_script_tag(self, content):
        return f'\n<script>{content}</script>'
    
    def modify_style_template(self, element_id, property, value):
        self.template += self.fill_script_tag(self.get_string_alter_style_element(element_id, property, value))
        return self.template    
    
