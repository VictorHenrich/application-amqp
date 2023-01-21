from start import app

@app.initializer
def start_app():
    from tasks import teste

    app.cli.execute()


app.start()