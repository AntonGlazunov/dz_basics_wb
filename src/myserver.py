from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs, urlparse

from src.utils import read_file


class MyServer(BaseHTTPRequestHandler):
    """
        Специальный класс, который отвечает за
        обработку входящих запросов от клиентов
    """

    def do_GET(self):
        """ Метод для обработки входящих GET-запросов """
        query_component = parse_qs(urlparse(self.path).query)
        page_content = read_file()
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(page_content, "utf-8"))
