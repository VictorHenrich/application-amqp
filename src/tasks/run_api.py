from start import app
from server.cli import Task


@app.cli.add_task(
    name="run",
    task_manager_name="api",
    shortname="r",
    debug=True,
    description="Este comando inicializa a API construida!",
)
class TaskRunApi(Task):
    def run(self) -> None:
        import api.routes

        app.http.start()
