from decouple import config
import urllib.parse

dialect = config("dialect")
driver = config("driver")
username = config("dbUsername")
password = urllib.parse.quote_plus(config("password"))
host = config("host")
port = config("port")
database = config("database")

dbConnectionString = f"{dialect}{driver}://{username}:{password}@{host}:{port}/{database}"
