from server.cli import Task
from start import app


@app.cli.add_task(
    name="migrate",
    task_manager_name="databases",
    shortname="m",
    debug=True,
    description="Este comando inicializa os consumers da aplicação!",
)
class TaskRunMigration(Task):
    def run(self) -> None:
        import models

        app.databases.migrate()