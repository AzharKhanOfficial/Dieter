# Diet Generator Project

The Diet Generator Project is a web application that provides a suite of tools to help users with their diet and nutrition needs. It incorporates features such as calculating BMI (Body Mass Index), determining daily caloric requirements, generating personalized diet plans, and collecting diet-related information from news articles.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup](#setup)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

1. **BMI Calculator:** Calculate your BMI based on your height and weight to assess your health.

2. **Caloric Needs Calculator:** Determine your daily caloric requirements based on factors like age, gender, weight, and activity level.

3. **Diet Plan Generator:** Generate personalized diet plans tailored to your caloric needs, dietary preferences, and restrictions.

4. **Diet-Related News:** Fetch diet and nutrition-related news articles from The Guardian News API and store relevant information in a PostgreSQL database using web scraping.

## Technologies Used

- **Frontend:** HTML, CSS (Tailwind CSS), JavaScript
- **Backend:** Django, Python (OpenAI GPT-3)
- **Database:** PostgreSQL
- **APIs:** The Guardian News API
- 

## Setup

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/AzharKhanOfficial/dieter.git
   cd Dieter

2. Install project dependencies:
   ```bash
   pip install -r requirements.txt
3. Set up your PostgreSQL database and configure the database connection in your Django settings.
4. Obtain API keys for The Guardian News API and OpenAI.
5. Apply Django migrations:
    ```bash
   python manage.py migrate
6. Start the Django development server:
   ```bash
   python manage.py runserver
7. Access the application in your web browser by navigating to http://localhost:8000.

## Usage
- Visit the web application to use the BMI Calculator, Caloric Needs Calculator, and Diet Plan Generator features.
- The application will also fetch and display diet-related news articles from The Guardian.
- To access the diet-related information database, use the provided API endpoints.

## Contributing
Contributions to this project are welcome. Please follow our Contribution Guidelines.

## License
This project is licensed under the MIT License.


   
