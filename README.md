# 🔗 Academic Link Tree - Professor's Smart Showcase

A simple, elegant Link Tree-style application designed for professors and academics to showcase their professional links and social media in one place.

## Features

- 📱 **Mobile-friendly responsive design**
- ⚙️ **YAML-based configuration** - Easy to customize without touching code
- 🎨 **Professional UI** with smooth animations
- 📊 **Optional analytics** support (Google Analytics 4)
- 🚀 **One-click deployment** to Vercel
- 🔗 **Click tracking** for link analytics

## Quick Start

### Prerequisites

- Python 3.13+
- `uv` package manager (recommended) or `pip`

### Installation & Setup

1. **Clone or download this repository**

2. **Install dependencies:**
   ```bash
   # Using uv (recommended)
   uv pip install -r requirements.txt
   
   # Or using pip
   pip install -r requirements.txt
   ```

3. **Customize your profile:**
   Edit `config.yaml` with your information:
   ```yaml
   profile:
     name: "Your Name"
     title: "Your Title"
     bio: "Your bio description"
     university: "Your Institution"
     avatar: "/static/images/your-photo.jpg"  # Optional
   ```

4. **Add your links:**
   Update the `links` section in `config.yaml`:
   ```yaml
   links:
     - name: "Google Scholar"
       url: "https://scholar.google.com/citations?user=your-id"
       icon: "scholar"
       color: "#4285f4"
   ```

5. **Run locally:**
   ```bash
   # Using uv
   uv run main.py
   
   # Or using python
   python main.py
   ```

6. **Open your browser:**
   Visit `http://localhost:5000`

## Configuration

### Profile Settings

```yaml
profile:
  name: "Dr. Jane Smith"                    # Your full name
  title: "Professor of Computer Science"     # Your title/position
  bio: "Researcher in AI and ML"           # Short bio
  university: "Tech University"            # Institution name
  avatar: "/static/images/avatar.jpg"      # Profile picture (optional)
```

### Adding Links

```yaml
links:
  - name: "Display Name"        # Text shown on button
    url: "https://example.com"  # Target URL
    icon: "scholar"             # Icon type (see below)
    color: "#4285f4"           # Button color (optional)
```

### Supported Icons

- `scholar` - Google Scholar (📚)
- `github` - GitHub (🐙)
- `linkedin` - LinkedIn (💼)
- `university` - University/Institution (🏛️)
- `book` - Publications/Papers (📖)
- `email` - Email contact (✉️)
- `default` - Generic link (🔗)

### Theme Customization

```yaml
theme:
  background_color: "#f8f9fa"     # Page background
  primary_color: "#007bff"        # Main accent color
  text_color: "#333"              # Text color
  link_hover_color: "#0056b3"     # Hover state color
```

### Analytics (Optional)

```yaml
analytics:
  enabled: true
  google_analytics_id: "G-XXXXXXXXXX"  # Your GA4 Measurement ID
```

## Deployment

### Deploy to Vercel

1. **Push to GitHub:**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/yourusername/your-repo.git
   git push -u origin main
   ```

2. **Deploy to Vercel:**
   - Visit [vercel.com](https://vercel.com)
   - Import your GitHub repository
   - Vercel will automatically detect the Flask app and deploy it

3. **Environment Variables (if needed):**
   In Vercel dashboard, add any environment variables under Settings → Environment Variables

### Alternative Deployment Options

- **Heroku:** Add a `Procfile` with `web: gunicorn main:app`
- **Railway:** Works with the existing configuration
- **DigitalOcean App Platform:** Compatible out of the box

## File Structure

```
├── main.py              # Flask application
├── config.yaml          # Your configuration
├── requirements.txt     # Python dependencies
├── pyproject.toml      # Project metadata
├── vercel.json         # Vercel deployment config
├── wsgi.py             # WSGI entry point
├── templates/
│   └── index.html      # Main template
├── static/
│   ├── images/         # Profile pictures
│   └── README.md       # Static assets info
└── README.md           # This file
```

## Customization

### Adding a Profile Picture

1. Add your image to `static/images/` folder
2. Update `config.yaml`:
   ```yaml
   profile:
     avatar: "/static/images/your-photo.jpg"
   ```

### Custom Colors

Each link can have a custom color:
```yaml
links:
  - name: "Custom Link"
    url: "https://example.com"
    color: "#ff6b6b"  # Custom red color
```

### Custom Icons

Add new emoji icons by editing the template in `templates/index.html`:
```html
{% elif link.icon == 'custom' %}🌟
```

## Development

### Local Development

```bash
# Install in development mode
uv pip install -e .

# Run with auto-reload
FLASK_ENV=development python main.py
```

### API Endpoint

The app provides a configuration API at `/api/config` for development purposes.

## Troubleshooting

### Common Issues

1. **Port already in use:**
   ```bash
   # Change port
   PORT=8000 python main.py
   ```

2. **Missing dependencies:**
   ```bash
   uv pip install -r requirements.txt
   ```

3. **Config file not found:**
   Ensure `config.yaml` exists in the root directory

### Support

For issues or questions:
1. Check the configuration format in `config.yaml`
2. Verify all URLs are valid and accessible
3. Ensure image files exist in the `static/images/` folder

## License

This project is open source and available under the MIT License.

---

Built with ❤️ using Flask and designed for academic professionals.