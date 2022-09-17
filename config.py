from fastapi import FastAPI
DB_FILE = "db.sqlite3"
database_route = f"sqlite:///{DB_FILE}"
# instantiate the FasAPI app
app = FastAPI()
# adding of middleware
