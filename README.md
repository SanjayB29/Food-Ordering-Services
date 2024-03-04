# Fast Food Ordering System

This repository contains a simple fast food ordering system built with Streamlit. The application allows users to sign up, log in, order food items, generate a bill, and check their wallet balance.

## Application Structure

- `app.py`: The main entry point of the application that manages navigation and session state.
- `auth.py`: Handles user authentication, including sign-up and login functionalities.
- `ordering.py`: Presents the menu to the user and allows them to add items to their cart.
- `generate_bill.py`: Generates a PDF bill of the ordered items and manages the payment process.
- `check_balance.py`: Allows users to check and update the balance in their wallet.
- `init.py`: Initializes the user credentials file with the correct structure.
- `user_credentials.xlsx`: A spreadsheet that stores user credentials and wallet balances.
- `images/`: Contains images of the menu items.

## Features

- User authentication (sign up and login)
- Menu selection
- Cart management
- Bill generation in PDF format
- Wallet balance management

## Installation & Usage

To run this application, you will need to have Python installed along with the following packages: `streamlit`, `pandas`, `openpyxl`, and `fpdf`.

1. Clone this repository to your local machine.
2. Install the required packages using pip:

```bash
pip install streamlit pandas openpyxl fpdf
```

3. Run the Streamlit application:

```bash
streamlit run app.py
```

Navigate to the local server address provided by Streamlit in your web browser to use the application.

## Contributions

Contributions are welcome. Please fork this repository and submit a pull request if you have features or fixes to add.

## License

This project is open-sourced under the MIT License. See the LICENSE file for more information.
