from http.server import HTTPServer
from src.myserver import MyServer

hostName = "localhost"
serverPort = 8080

if __name__ == "__main__":
    """
    Инициализация веб-сервера, который будет по заданным параметрам в сети
    принимать запросы и отправлять их на обработку классу MyServer
    """
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
    webServer.server_close()
    print("Server stopped.")
