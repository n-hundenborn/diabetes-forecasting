# diabetes-forecasting
Techlabs project about forecasting diabetes using &amp; machine learning models.

## Getting started
Make sure the following is installed and working properly on your system:
- code editor/IDE of your choice, e.g. Visual Studio Code
- Python
- pip (Python package manager)

### Cloning the repository
After setting up your github credentials open the terminal in the desired folder destination and enter:

    git clone https://github.com/n-hundenborn/diabetes-forecasting.git


### Manage your python environment
To install all necessary python packages you can use `pip` or `pipenv`.

To install pipenv open the terminal (either integrated VS Code or OS-specific) and enter `pip install pipenv`.

To install all python dependencies defined in _requirements.txt_ run:

    pipenv install -r requirements.txt
and select the newly created environment (something like: _diabetes_forecasting-_...) if necessary on the top right corner of VS Code.
When you first run a jupyter notebook cell in a new python environment, click install in the popup that opens.

## Project Structure
You can find the main content of our project in the Jupyter-Notebook called _dev_model_training.ipynb_. The notebook has the following base structure:

1. Importing packages
2. Data Loading (for implementations, see _raw_data.py_)
3. Data Preparation
4. Model Training \
    a. Decision Tree Classifier \
    b. Random Forest Classifier \
    c. Logisticregression \
    d. Load and analyse best model
5. Process and evaluate user input \
    a. Get user input \
    b. Use before defined model for a prediction on user input \
    c. do an action recommendation based on prediction

## Note
Training some models can take more than 60 Minutes. If you don't want to train the models all over again you can skip cells from chapter 4 and continue by using the saved models files from the models folder.
