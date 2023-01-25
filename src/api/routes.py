from start import app

from api.controllers.drive_controller import DriveController


app.http.add_resource(DriveController, "/drive")
