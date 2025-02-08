from flask import Flask, request, Response

app = Flask(__name__)

# Global variable to track the number of email opens
email_open_count = 0

@app.route('/track', methods=['GET'])
def track():
    global email_open_count

    # Increment the count when the tracking pixel is requested
    email_open_count += 1

    # Return a 1x1 transparent pixel
    pixel = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x06\x00\x00\x00\x1f\x15\xc4\x89\x00\x00\x00\nIDATx\xdacd\xf8\xff\xff?\x00\x05\xfe\x02\xfeA^O`\x00\x00\x00\x00IEND\xaeB`\x82'
    return Response(pixel, mimetype='image/png')

@app.route('/get_open_count', methods=['GET'])
def get_open_count():
    """Endpoint to get the current email open count"""
    return {"open_count": email_open_count}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
