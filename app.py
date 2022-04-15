from flask import Flask, render_template
from scraper import data_scraper

app = Flask(__name__)

TOTAL_PERSONS = 500

ranks, names, links, worths, last_changes, ytds, countries, industries = data_scraper(TOTAL_PERSONS)
response_dict = {}
for i in range(TOTAL_PERSONS):
    temp_dict = {
        "rank": ranks[i], 
        "name": names[i], 
        "link": links[i],
        "worth": worths[i],
        "country": countries[i], 
        "last_changes": last_changes[i],
        "ytds": ytds[i],
        "industry": industries[i]
    }
    response_dict[i+1] = temp_dict


@app.route('/test')
def hello_world():
    data = {
        "Status": 200,
        "Message": "Up and Running",
        "Developed by": "Ashutosh Krishna"
    }
    return data, 200


@app.route('/')
def index():
    return render_template('index.html', data=response_dict, num=TOTAL_PERSONS)


if __name__ == "__main__":
    app.run(debug=True)
