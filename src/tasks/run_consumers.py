from start import app
from server.cli import Task


@app.cli.add_task(
    name="run",
    task_manager_name="consumers",
    shortname="r",
    debug=True,
    description="Este comando inicializa os consumers da aplicação!",
)
class TaskRunConsumers(Task):
    def run(self) -> None:
        import consumers

        app.amqp.start_consumers()