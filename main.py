import os
import yaml
from flask import Flask, render_template, redirect, jsonify

app = Flask(__name__)

def load_config():
    """Load configuration from config.yaml"""
    config_path = os.path.join(os.path.dirname(__file__), 'config.yaml')
    try:
        with open(config_path, 'r', encoding='utf-8') as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        # Return default config if file doesn't exist
        return {
            'profile': {
                'name': 'Your Name',
                'title': 'Your Title',
                'bio': 'Your Bio',
                'university': 'Your University'
            },
            'links': [],
            'theme': {
                'background_color': '#f8f9fa',
                'primary_color': '#007bff',
                'text_color': '#333',
                'link_hover_color': '#0056b3'
            },
            'analytics': {'enabled': False}
        }

@app.route('/')
def home():
    """Main page displaying the link tree"""
    config = load_config()
    return render_template('index.html', 
                         profile=config['profile'],
                         links=config['links'],
                         theme=config['theme'],
                         analytics=config.get('analytics', {'enabled': False}))

@app.route('/link/<int:link_index>')
def track_link(link_index):
    """Track link clicks and redirect"""
    config = load_config()
    links = config['links']
    
    if 0 <= link_index < len(links):
        link = links[link_index]
        
        # Optional: Track analytics here
        if config.get('analytics', {}).get('enabled'):
            # You can implement click tracking here
            pass
        
        return redirect(link['url'])
    else:
        return redirect('/')

@app.route('/api/config')
def api_config():
    """API endpoint to get configuration (for development)"""
    config = load_config()
    return jsonify(config)

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return redirect('/')

if __name__ == "__main__":
    # Use different ports for development vs production
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV') == 'development'
    
    app.run(host='0.0.0.0', port=port, debug=debug)
