from start import app


@app.initializer
def start_app():
    from tasks import run_api

    app.cli.execute()


if __name__ == "__main__":
    app.start()
    