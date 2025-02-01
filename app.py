from app import create_app,db

# Create the Flask application instance
app = create_app()
with app.app_context():
    db.create_all()
# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
