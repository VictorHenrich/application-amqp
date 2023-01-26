from server.http import HTTPController


class UserController(HTTPController):
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)

    def post(self, *args, **kwargs):
        return super().post(*args, **kwargs)

    def put(self, *args, **kwargs):
        return super().put(*args, **kwargs)

    def delete(self, *args, **kwargs):
        return super().delete(*args, **kwargs)
