# Moderation Review App

This is a Django-based content moderation web application that utilizes OpenAI's AI-powered moderation API. The app allows users to input text, which is then analyzed by the AI for content moderation purposes. The AI returns category scores and flags inappropriate content. The results are displayed asynchronously, providing a seamless user experience.

For a detailed tutorial on building this app, please visit the Medium article: [Build an AI-Powered Content Moderation Review App](https://medium.com/p/2b5285d4ce54/)

## Prerequisites

-   Python 3.8
-   Django 4.1.7

## Installation & Setup

1.  Clone this repository and navigate to the project directory.
    
2.  Create and activate a virtual environment:
    
```bash 
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```
    
3.  Install the required dependencies:
    
```bash 
pip install -r requirements.txt
```

4.  Apply migrations and start the development server:
```bash 
python manage.py migrate
python manage.py runserver
```
    
6.  Open your browser and visit `http://127.0.0.1:8000/` to use the moderation review app.
    

## Features

-   User-friendly interface for submitting text to be moderated
-   Asynchronous AJAX calls to fetch moderation results without page refresh
-   AI-powered content moderation using OpenAI's API
-   Customizable categories and moderation rules

## Learn More
**Read the [Full Article On Medium](https://medium.com/p/2b5285d4ce54)** Were we cover step by step how to build this same project: 

- Initial Setup
- Import Libraries and Dependencies
- Design Your Models
- Create Your Views
- Set Up URL Paths
- Design the HTML Template
- Migrate & Test Your App
- (Optional) Deploy Your App

## Contributing

Feel free to contribute to this project by submitting issues or pull requests. Your feedback is highly appreciated!

## License

This project is licensed under the MIT License.
