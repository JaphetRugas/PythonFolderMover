# FolderMover

**FolderMover** is a simple web application built with Python and Flask that allows users to move folders from one directory to another through a user-friendly interface.

## Project Structure

```
FolderMover/
│
├── app/
│   ├── static/
│   │   └── js/
│   │       └── script.js
│   ├── templates/
│   │   └── index.html
│   └── main.py
│
├── venv/
├── requirements.txt
└── README.md
```

## Requirements

- Python 3.7 or higher
- Flask (for the backend web server)

## Installation

1. **Clone the repository** (if using version control).
   ```bash
   git clone https://github.com/your-username/FolderMover.git
   cd FolderMover
   ```

2. **Set up a virtual environment** (recommended).
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. **Start the Flask server**:
   ```bash
   python app/main.py
   ```

2. **Open the application** in your web browser:
   ```
   http://127.0.0.1:5000
   ```

## Usage

1. On the main page, enter the source folder path and the destination folder path.
2. Click the **Move Folder** button.
3. The application will move the specified folder to the new location and provide a success or error message.

## File Descriptions

- `app/main.py`: The main Flask application that defines routes for rendering the HTML page and handling folder movement requests.
- `app/templates/index.html`: The HTML template for the main page where users enter folder paths.
- `app/static/js/script.js`: JavaScript file to handle the folder move request via an API call to the Flask server.
- `requirements.txt`: Lists required Python packages.
  
## Functionality

The app allows users to:

- Enter a source folder path and destination path.
- Move folders from the source to the destination location.

## Example

- **Source**: `C:\Users\YourName\Documents\OldFolder`
- **Destination**: `C:\Users\YourName\Documents\NewFolder`

Upon clicking **Move Folder**, `OldFolder` will be moved to the `NewFolder` location.

---

**Note**: Ensure you have the appropriate permissions for both source and destination directories.
