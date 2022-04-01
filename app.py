from flask import Flask, render_template, url_for
from flask_mongoengine import MongoEngine
from datetime import datetime
from models import StinkAppearances

app = Flask(__name__)

# DB stuff
app.config['MONGODB_SETTINGS'] = {
    'db': 'stink',
    'host': 'localhost',
    'port': 27017
}
db = MongoEngine(app)

# Seed the database if it's empty
if not StinkAppearances.objects():
    seeds = [
        {'ep_number': 1, 'stinky': False, 'air_date': datetime(2020, 5, 7)},
        {'ep_number': 2, 'stinky': True, 'air_date': datetime(2020, 5, 14), 'stink_start': 100, 'stink_end': 200},
        {'ep_number': 3, 'stinky': False, 'air_date': datetime(2020, 5, 21)}
    ]
    # This code should be refactored as the general insertion code for this table
    for seed in seeds:
        d = StinkAppearances(
            ep_number=seed['ep_number'],
            isStinky=seed['stinky'],
            air_date=seed['air_date']
        )
        # Add start and end if available
        if 'stink_start' in seed:
            d.stink_start = seed['stink_start']
        if 'stink_end' in seed:
            d.stink_end = seed['stink_end']
        d.save()


@app.route('/')
def hello_world():
    message = "Hello world!  Were you looking for <a href={}>a stinky list</a>?".format(url_for('stinky'))
    return message


@app.route('/stink_sightings')
def stinky():
    return render_template("main.html", episodes=StinkAppearances.objects.order_by('-ep_number'))


if __name__ == "__main__":
    app.run()
