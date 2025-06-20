PROJECT_DIR="gec_app"
VENV_NAME="venv"

if [ ! -d "$VENV_NAME" ]; then
    echo "Creating virtual environment..."
    python3 -m venv "$VENV_NAME"
fi

echo "Activating virtual environment..."
source "$VENV_NAME/Scripts/activate"

pip install -r requirements.txt

cd "$PROJECT_DIR"
export FLASK_APP=app.py
export FLASK_ENV=development 
export FLASK_DEBUG=1

export HF_HUB_DISABLE_IMPLICIT_TOKEN=1

echo "Starting Flask application..."
flask run