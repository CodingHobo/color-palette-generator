# Color Palette Generator

## Overview
The Color Palette Generator is a web application that allows users to enter descriptive phrases or titles, such as "misty morning on the lake in spring" or "Wes Anderson's 'The Life Aquatic'", and get a corresponding color palette generated. The palettes consist of between 2 and 8 colors, returned as hexadecimal color codes.

This app combines a frontend built with HTML, CSS, and JavaScript with a backend powered by Flask and OpenAI's GPT-3 API.

## Features
- **User Prompts**: Users can input descriptive text to get a corresponding color palette.
- **Dynamic Palette Display**: Generated palettes dynamically update on the page without a full reload.
- **Copy to Clipboard**: Users can click on a specific color to copy its hexadecimal value to their clipboard, with a confirmation tooltip.
- **Clear Functionality**: A clear button allows users to reset the palette and input field.

## Backend Implementation
The backend, written in Python using Flask, communicates with OpenAI's GPT-3 API. It sends the user's descriptive text to the model and processes the returned color codes to be displayed on the frontend.

## Setup and Installation
1. Clone the repository.
2. Navigate to the project directory.
3. Install necessary dependencies. If using pip:
```pip install -r requirements.txt```
4. Ensure you have set up your `.env` file with your OpenAI API key:
```OPENAI_API_KEY=your_api_key_here```
5. Run the Flask application:
```python app.py```
6. Visit the local server URL (typically `http://127.0.0.1:5000/`) in your browser.

## Deployment
The frontend can be deployed to platforms like Netlify or Vercel. For the backend, consider using cloud platforms like DigitalOcean, Google Cloud Platform, AWS, Azure, or Render, especially if avoiding Heroku due to its sleeping dynos on the free tier.

## Future Improvements
- Introduce user accounts to save favorite palettes.
- Integrate more advanced color manipulation and visualization tools.
- Provide additional customization options for palette generation.
