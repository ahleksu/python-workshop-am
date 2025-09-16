#!/usr/bin/env python3
"""
Development server script for testing the application
"""

import sys
import os

def check_dependencies():
    """Check if required dependencies are installed"""
    try:
        import flask
        import yaml
        print("✅ All dependencies are installed")
        return True
    except ImportError as e:
        print(f"❌ Missing dependency: {e}")
        print("Please install dependencies with: uv pip install -r requirements.txt")
        return False

def check_config():
    """Check if config.yaml exists and is valid"""
    if not os.path.exists('config.yaml'):
        print("❌ config.yaml not found")
        return False
    
    try:
        import yaml
        with open('config.yaml', 'r') as f:
            config = yaml.safe_load(f)
        
        required_keys = ['profile', 'links']
        for key in required_keys:
            if key not in config:
                print(f"❌ Missing required key '{key}' in config.yaml")
                return False
        
        print("✅ config.yaml is valid")
        return True
    except Exception as e:
        print(f"❌ Error reading config.yaml: {e}")
        return False

def main():
    """Main function to run development checks and start server"""
    print("🔗 Academic Link Tree - Development Server")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not os.path.exists('main.py'):
        print("❌ main.py not found. Please run this script from the project root.")
        sys.exit(1)
    
    # Check dependencies
    if not check_dependencies():
        sys.exit(1)
    
    # Check configuration
    if not check_config():
        sys.exit(1)
    
    print("\n🚀 Starting development server...")
    print("📱 Open your browser to: http://localhost:5000")
    print("⏹️  Press Ctrl+C to stop the server")
    print("-" * 50)
    
    try:
        # Start the Flask development server
        os.environ['FLASK_ENV'] = 'development'
        from main import app
        app.run(host='0.0.0.0', port=5000, debug=True)
    except KeyboardInterrupt:
        print("\n👋 Server stopped. Goodbye!")
    except Exception as e:
        print(f"❌ Error starting server: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()