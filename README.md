# Python-JavaScript Hybrid Portfolio

A modern, responsive portfolio website built with Flask and Alpine.js, featuring a beautiful UI and smooth animations.

## Features

- 🎨 Modern, responsive design with TailwindCSS
- ⚡ Interactive UI with Alpine.js
- 🔄 Smooth animations with GSAP
- 📝 Blog system with markdown support
- 🎯 Project showcase with filtering
- ⌨️ Developer-friendly command palette (Ctrl+K)
- 📱 Mobile-first approach
- 🔍 SEO-friendly
- 🎮 Interactive timeline navigation

## Tech Stack

- **Backend**: Python/Flask
- **Database**: SQLAlchemy with SQLite
- **Frontend**: Alpine.js & TailwindCSS
- **Animations**: GSAP
- **Admin Interface**: Flask-Admin

## Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd portfolio
   ```

2. Create and activate a virtual environment:
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate

   # Linux/macOS
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   ```bash
   # Copy the sample .env file
   cp .env.example .env
   
   # Edit .env with your settings
   # Make sure to change the SECRET_KEY
   ```

5. Initialize the database:
   ```bash
   flask db upgrade
   ```

6. Run the development server:
   ```bash
   flask run
   ```

The application will be available at `http://localhost:5000`.

## Project Structure

```
portfolio/
├── app/                    # Application package
│   ├── models/            # Database models
│   ├── routes/            # Route handlers
│   ├── static/            # Static files (CSS, JS, images)
│   └── templates/         # Jinja2 templates
├── migrations/            # Database migrations
├── .env                   # Environment variables
├── config.py             # Configuration settings
├── requirements.txt      # Python dependencies
└── run.py               # Application entry point
```

## Customization

1. **Content**: Update the content in the templates directory
2. **Styling**: Modify `app/static/css/style.css` and Tailwind classes
3. **Projects**: Add your projects through the admin interface
4. **Blog Posts**: Write blog posts using the admin interface

## Deployment

1. Update `.env` with production settings
2. Set `FLASK_ENV=production`
3. Use a production-ready server (e.g., Gunicorn)
4. Set up a reverse proxy (e.g., Nginx)

Example deployment command with Gunicorn:
```bash
gunicorn -w 4 -b 127.0.0.1:8000 "run:create_app()"
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.