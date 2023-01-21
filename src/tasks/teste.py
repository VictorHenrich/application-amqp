from start import app
from server.cli import Task


@app.cli.add_task(
    name="teste",
    task_manager_name="teste",
    shortname="t",
    debug=False,
    description="Isso aqui é apenas um teste meu amigo",
)
class TaskTeste(Task):
    def run(self) -> None:
        print('OI ESTOU SENDO EXECUTADO!')