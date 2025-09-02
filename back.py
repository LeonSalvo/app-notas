import asyncio
import tornado
import json

class Actuator(tornado.web.RequestHandler):
    def get(self):
        self.write("{\"status\": \"ok\"}")

class AddNoteHandler(tornado.web.RequestHandler):
    def post(self, path):
        data = json.loads(self.request.body)
        with open("data/data.txt", "a") as f:
            f.write(path + "\n" + data.get("message") + "\n" + "-EOF-" + "\n")
        self.write("{\"status\": \"note added\"}")

class ListNotesHandler(tornado.web.RequestHandler):
    def get(self):
        with open("data/data.txt", "r") as f:
            notes = f.read().strip().split("\n-EOF-\n")
            notes = [n.strip().split("\n", 1) for n in notes if n.strip()]
            notes = [{"title": n[0], "message": n[1]} for n in notes if len(n) == 2]
            notes[-1]["message"] = notes[-1]["message"].replace("-EOF- ESTO DEFINITIVAMENTE ES UN CAMBIO", "").strip()

        self.write("{\"status\": \"ok\", \"data\": [\n" + ",\n".join([json.dumps(n) for n in notes]) + "\n]}")
        self.set_header("Content-Type", "application/json")

def make_app():
    return tornado.web.Application([
        (r"/:", Actuator),
        (r"/add/(.*)", AddNoteHandler),
    (r"/list", ListNotesHandler),
])

async def main():
    app = make_app()
    app.listen(8888)
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())