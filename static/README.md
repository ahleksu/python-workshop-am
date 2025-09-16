# Static Assets

This folder contains static assets for the application:

- `images/` - Profile pictures and other images
  - Place your profile picture here as `avatar.jpg` or update the config.yaml file to point to the correct image

## Adding a Profile Picture

1. Add your profile picture to the `static/images/` folder
2. Update the `avatar` field in `config.yaml` to point to your image:
   ```yaml
   profile:
     avatar: "/static/images/your-photo.jpg"
   ```

## Supported Image Formats

- JPG/JPEG
- PNG
- WebP
- SVG