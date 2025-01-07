
# Restaurant QR Code Generator

Restaurant QR Code Generator is a Django-based web application designed to streamline the dining experience by generating QR codes for restaurant menus. These QR codes can be scanned by customers to access digital menus, enhancing hygiene and convenience.

## Features

- **QR Code Generation:** Create unique QR codes for individual menu items or entire menus.
<!-- - **Menu Management:** Easily add, update, or remove menu items through an intuitive interface. -->
- **Digital Menu Access:** Customers can scan QR codes to view menus on their devices, reducing the need for physical menus.
- **Responsive Design:** Optimized for various devices, ensuring a seamless user experience across smartphones, tablets, and desktops.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/DevanshUpadhyay26/RestaurantQRCodeGenerator.git
   ```

2. **Navigate to the Project Directory:**

   ```bash
   cd RestaurantQRCodeGenerator
   ```

3. **Create a Virtual Environment:**

   ```bash
   python -m venv env
   ```

4. **Activate the Virtual Environment:**

   - On Windows:

     ```bash
     env\Scripts\activate
     ```

   - On Unix or MacOS:

     ```bash
     source env/bin/activate
     ```

5. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

6. **Apply Migrations:**

   ```bash
   python manage.py migrate
   ```

7. **Create a Superuser:**

   ```bash
   python manage.py createsuperuser
   ```

8. **Run the Development Server:**

   ```bash
   python manage.py runserver
   ```

   Access the application at `http://127.0.0.1:8000/`.

## Usage
<!-- 
1. **Admin Panel:**

   - Log in to the Django admin panel at `http://127.0.0.1:8000/admin/` using the superuser credentials.
   - Add or manage menu items under the "Menu" section. -->

2. **QR Code Generation:**
   - Add the Restaurant Name and URL of the Menu in the form.
   - After that, you will be redirected to QR Code Page where you will be able to see the QR Code Generated for that Menu.
   - Download and print the QR codes for placement in the restaurant.

3. **Customer Access:**

   - Customers scan the QR codes using their smartphones to access the digital menu.
   - The menu is displayed in a user-friendly format, allowing customers to browse items effortlessly.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your proposed changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

Special thanks to the Django community and the developers of the libraries used in this project.

---

For more information, visit the [GitHub repository](https://github.com/DevanshUpadhyay26/RestaurantQRCodeGenerator).
