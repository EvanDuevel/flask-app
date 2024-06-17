from flask import Flask, jsonify

@app.route('/')
def search_ytmusic():
    query = "hi'
    return jsonify({'results': query, 'title': query, 'video_url': query})

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', threaded=True)

