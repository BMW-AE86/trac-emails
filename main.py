from flask import Flask, request, redirect, Response

app = Flask(__name__)

# Global variables for tracking
email_open_count = 0
email_click_count_A = 0
email_click_count_G = 0

# Email Open Tracking
@app.route('/track', methods=['GET'])
def track():
    global email_open_count
    email_open_count += 1

    # Return a 1x1 transparent pixel
    pixel = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x06\x00\x00\x00\x1f\x15\xc4\x89\x00\x00\x00\nIDATx\xdacd\xf8\xff\xff?\x00\x05\xfe\x02\xfeA^O`\x00\x00\x00\x00IEND\xaeB`\x82'
    return Response(pixel, mimetype='image/png')

# Click Tracking Apple
@app.route('/click_Apple', methods=['GET'])
def click():
    global email_click_count_A
    email_click_count_A += 1

    # Get the original destination URL
    destination_url = request.args.get('url', 'https://apps.apple.com/us/app/dukascopy-swiss-mobile-bank/id1414311580')

    # Redirect to the destination URL
    return redirect(destination_url)

# Click Tracking Google
@app.route('/click_Google', methods=['GET'])
def click():
    global email_click_count_G
    email_click_count_G += 1

    # Get the original destination URL
    destination_url = request.args.get('url', 'https://play.google.com/store/apps/details?id=com.dukascopy.swissbank')

    # Redirect to the destination URL
    return redirect(destination_url)

# Get counts
@app.route('/get_counts', methods=['GET'])
def get_counts():
    """Endpoint to get the current open and click counts"""
    return {
        "open_count": email_open_count,
        "click_count_Apple": email_click_count_A,
        "click_count_Google": email_click_count_G,
    }, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
