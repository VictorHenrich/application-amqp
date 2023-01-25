from typing import Optional
from pathlib import Path
from patterns.service import IService
from services import MainPathCreationService
from start import app



@app.initialize
def create_drives_paths():
    main_path_creation_service: IService[
        Optional[Path], None
    ] = MainPathCreationService()

    main_path_creation_service.execute()


@app.initialize
def init_cli():
    import tasks

    app.cli.execute()



if __name__ == "__main__":
    app.start()
