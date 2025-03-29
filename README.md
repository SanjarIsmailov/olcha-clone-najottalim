# Olcha.uz Clone

A full-featured e-commerce web application that replicates the functionality of [Olcha.uz](https://olcha.uz/uz), built using **Django** for the backend and **React** for the frontend.

## Features
- **User Authentication**: Registration, login, logout (custom authentication with phone number support)
- **Product Management**: List, filter, and search for products
- **Shopping Cart**: Add, remove, and update items in the cart
- **Order Processing**: Checkout, order tracking, and status updates
- **Payment Integration**: Support for online payments
- **Admin Panel**: Manage users, products, orders, and categories
- **Responsive Design**: Optimized for mobile and desktop

## Tech Stack
- **Backend**: Django, Django REST Framework (DRF)
- **Database**: PostgreSQL
- **Authentication**: Custom user model with phone number login

## Installation
### Prerequisites
Ensure you have the following installed:
- Python 3.10+
- Node.js & npm
- PostgreSQL
- Docker (optional for containerized deployment)

### Backend Setup
```sh
# Clone the repository
git clone https://github.com/yourusername/olcha-clone.git
cd olcha-clone

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt

# Configure environment variables
cp .env.example .env  # Update .env with database and secret keys

# Apply migrations
python manage.py migrate

# Create a superuser
python manage.py createsuperuser

# Start the development server
python manage.py runserver
```

### Frontend Setup
```sh
cd frontend
npm install
npm run dev  # Runs the React frontend
```

## Contribution Guidelines
1. Fork the repository
2. Create a feature branch (`git checkout -b feature-name`)
3. Commit changes (`git commit -m "Add new feature"`)
4. Push to the branch (`git push origin feature-name`)
5. Create a pull request

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact
For any inquiries, reach out via **devsanjar2299@gmail.com** or open an issue in the repository.

