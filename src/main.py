from start import app

@app.initializer
def start_app():
    app.cli.execute()


app.start()