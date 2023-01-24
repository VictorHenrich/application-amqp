from start import app

from api.controllers.teste_controller import TesteController



app.http.add_resource(TesteController, "/")