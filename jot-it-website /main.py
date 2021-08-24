#main.py
#starts program
#Developer: Shavon Thadani
#23/08/'21
from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
