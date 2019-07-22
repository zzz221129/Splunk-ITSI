import splunklib.client as client
import splunklib.results as results

HOST = "localhost"
PORT = 8089
USERNAME = "username"
PASSWORD = "password"

# Create a Service instance and log in
service = client.connect(
    host=HOST,
    port=PORT,
    username=USERNAME,
    password=PASSWORD)

# Print installed apps to the console to verify login
for app in service.apps:
    print app.name

# List the saved searches that are available to the current user
savedsearches = service.saved_searches

for savedsearch in savedsearches:
    print "  " + savedsearch.name
    print "      Query: " + savedsearch["search"]

