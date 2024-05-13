from flask import Flask, render_template, request, jsonify, redirect, send_from_directory
from plyer import notification

app = Flask(__name__)

# Initializing variables
current_status = "Home"
thumbs_up_count = 0
TOKEN = ""

@app.route('/')
def status():
    return render_template("status.html", current_status=current_status)

@app.route('/thumbsup', methods=['POST'])
def thumbs_up():
    global thumbs_up_count
    thumbs_up_count += 1
    return jsonify(success=True, count=thumbs_up_count)

@app.route('/admin', methods=['GET', 'POST'])
def admin_page():
    global current_status
    if request.method == 'POST':
        current_status = request.form['status']
        return redirect('/admin')
    return render_template('admin.html', current_status=current_status, thumbs_up=thumbs_up_count)

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('./static', filename)

@app.route('/send_notification', methods=['GET'])
def send_notification():
    notification.notify(
        title='Notification from Notable',
        message="Someone's at the door!",
        app_icon=None,
        timeout=10
    )
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
