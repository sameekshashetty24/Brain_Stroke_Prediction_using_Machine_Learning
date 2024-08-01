# Brain_Stroke_Prediction_using_Machine_Learning Web Site

This project is a website built using Flask that utilizes a machine learning model to predict the likelihood of a stroke based on user input. The model is trained using a dataset containing various health features. The web application allows users to input their health details and receive a prediction on whether they are at risk of having a stroke.

## Project Structure

- `app.py`: The main Flask application file containing server logic and routes.
- `s_prediction_model.pkl`: The serialized machine learning model used for predictions.
- `templates/`: Directory containing HTML templates for the web application.
  - `index.html`: The main form where users can input their health details.
  - `stroke_alert.html`: The page displayed if the model predicts a stroke risk.
  - `no_stroke.html`: The page displayed if the model predicts no stroke risk.
- `static/`: Directory containing static files such as images and CSS.
  - `2.jpg`: Favicon for the web application.
  - `style.css`: CSS stylesheet for styling the web pages.

## Setup Instructions

### Prerequisites

- Python 3.x
- Flask
- scikit-learn
- NumPy
- Pickle

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/sameekshashetty24/stroke-prediction-web-app.git
   cd stroke-prediction-web-app

2. Create a virtual environment and activate it:

  ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
```

3. Install the required packages:

```bash
  pip install Flask scikit-learn numpy
```

4. Ensure the machine learning model s_prediction_model.pkl is in the same directory as app.py.

### Running the Application
1. Start the Flask development server:
   ```bash
     python app.py
   ```
2. Open your web browser and navigate to http://127.0.0.1:5000/ to access the application.
