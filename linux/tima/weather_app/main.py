import server


def start():
    server.app.run(host="0.0.0.0", debug=True)


if __name__ == '__main__':
    start()
