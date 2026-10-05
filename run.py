from src.python_uv import create_app
from dotenv import load_dotenv
import os

load_dotenv()

app = create_app()

if __name__ == "__main__":
    app.run(debug=True, port=int(os.getenv("PORT")))