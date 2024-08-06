from flask import Flask, render_template, request, jsonify, abort

app = Flask(__name__)

# Define some sample routes
@app.route('/')
def home():
    return "Welcome to the home page!"

@app.route('/cause_404')
def cause_404():
    # Intentionally cause a 404 error
    abort(404)

@app.route('/cause_500')
def cause_500():
    # Intentionally cause a 500 error
    raise Exception("This is a test exception for 500 error")

# Error handlers

@app.errorhandler(404)
def page_not_found(e):
    # Log the error if needed
    app.logger.error(f'404 error: {e}')
    # Return a custom HTML page for 404 error
    return render_template('error_404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    # Log the error if needed
    app.logger.error(f'500 error: {e}')
    # Return a custom HTML page for 500 error
    return render_template('error_500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)
