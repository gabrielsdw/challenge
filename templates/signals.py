from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Template  

@receiver(post_migrate)
def create_default_templates(sender, **kwargs):
    if not Template.objects.exists():
        
        Template.objects.create(
            name='Hello Word',
            html_content = """
                <!DOCTYPE html>
                <html lang="en">
                    <head>
                    <title>Bootstrap Example</title>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1">
                    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
                    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
                    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
                    </head>
                    <body>

                    <div class="jumbotron text-center" id="{{jumbotron}}">
                    <h1>My First Bootstrap Page</h1>
                    <p>Resize this responsive page to see the effect!</p> 
                    </div>
                    
                    <div class="container">
                    <div class="row">
                        <div class="col-sm-4" id="{{col1}}">
                        <h3>Column 1</h3>
                        <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit...</p>
                        <p>Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris...</p>
                        </div>
                        <div class="col-sm-4" id="{{col2}}">
                        <h3>Column 2</h3>
                        <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit...</p>
                        <p>Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris...</p>
                        </div>
                        <div class="col-sm-4" id="{{col3}}">
                        <h3>Column 3</h3>        
                        <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit...</p>
                        <p>Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris...</p>
                        </div>
                    </div>
                    </div>
                    </body>
                </html>
            """
        )
        # Template.objects.create(name='Template Padrão 2')
        print("Templates padrão criados.")
