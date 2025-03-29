# VerticalCode

A simple web application that embeds the Vertical Studio AI Models platform using an iframe.

## Features

- Clean and modern user interface
- Responsive design that works on all devices
- Full-screen iframe integration of Vertical Studio
- Fixed header for easy navigation
- Auto-reload development server

## Development Setup

### Prerequisites
- Python 3.x installed on your system
- pip (Python package installer)

### Running the Development Server

1. Clone this repository
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Open a terminal in the project directory
4. Start the development server:
   ```bash
   python server.py
   ```
   The server will start on http://localhost:8000 and automatically open your default browser.

### Auto-Reload Feature

The development server includes an auto-reload feature that will:
- Automatically detect changes to HTML, CSS, and JavaScript files
- Restart the server when changes are detected
- Show a notification in the console when reloading
- Automatically recover from errors and restart

### Server Options

You can customize the server with the following options:
- `--port`: Specify a different port (default: 8000)
- `--host`: Specify a different host (default: localhost)

Example:
```bash
python server.py --port 3000 --host 0.0.0.0
```

### Alternative Setup

If you prefer not to use the development server, you can simply open `index.html` in your web browser.

## Technical Details

- Built with vanilla HTML and CSS
- Uses iframe to embed the Vertical Studio platform
- Responsive design that adapts to different screen sizes
- Modern styling with subtle shadows and rounded corners

## Note

This is a simple wrapper website that embeds the Vertical Studio platform. Make sure you have proper permissions and comply with Vertical Studio's terms of service when using this application. 