from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# Sample data for national parks
national_parks = [
    {
        'id': 'park01',
        'name': 'Yellowstone National Park',
        'description': 'First national park in the U.S.',
        'image': 'images/park1.jpg',
        'likes': 0,
        'dislikes': 0,
    },
    {
        'id': 'park02',
        'name': 'Yosemite National Park',
        'description': 'Known for its waterfalls.',
        'image': 'images/park2.jpg',
        'likes': 0,
        'dislikes': 0,
    },
    {
        'id': 'park03',
        'name': 'Grand Canyon National Park',
        'description': 'Famous for its immense size.',
        'image': 'images/park3.jpg',
        'likes': 0,
        'dislikes': 0,
    },
]

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/all')
def all_parks():
    return render_template('all_parks.html', parks=national_parks)

@app.route('/park/<park_id>')
def park_detail(park_id):
    park = next((p for p in national_parks if p['id'] == park_id), None)
    return render_template('park_detail.html', park=park) if park else 'Park not found', 404

if __name__ == '__main__':
    app.run(debug=True)
