# Sauce Demo BDD Automation Framework

This project is a Behavior-Driven Development (BDD) framework designed to test the functionalities of the Sauce Demo website using Python, Behave, and Playwright.

## Project Structure
```
project-root/
├── features/
│   ├── environment.py           # Environment hooks for setup and teardown
│   ├── login.feature            # Gherkin feature file
│   ├── checkout.feature         # Gherkin feature file
│   ├── ...                      # Other Gherkin feature files
│   ├── steps/
│   │   ├── shared_steps.py      # Step definitions
│   │   ├── login_steps.py       # Step definitions
│   │   └── ...                  # Other step definitions
│── pages/
│   ├── base_page.py             # Base Page Object
│   ├── login_page.py            # Login Page Object
│   └── ...                      # Other Page Objects
├── resources/
│   ├── i18n/                       
│   │   └── locales.json         # Localized text data│
│   └── test_data/               # Data to use in automated tests
│── utilities/  
│   └── utils.py                 # Helper functions
├── behave.ini                   # Configuration file
├── requirements.txt             # Project dependencies
└── README.md                    # Documentation
```


## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/andrey-metelsky/lego_code_challenge.git
cd lego_code_challenge
```
### 2. Select Python Interpreter and create virtual environment
  
### 3. Install Dependencies

```pip install -r requirements.txt```

### 4. Install Playwright Browsers

```playwright install```

## Running the Tests

Run all test

```behave```

Run test with test tag

``` behave --tags=@login```

Alternative Locale (e.g., Spanish)

```behave -D LOCALE=eu-ES```

Generate Allure report locally

```behave -f allure_behave.formatter:AllureFormatter -o allure_results ./features```
```allure serve allure_results```





