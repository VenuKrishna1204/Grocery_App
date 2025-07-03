**Venu Mart Grocery App**

  ✅This is a Django-based web application for a Grocery Store where users can:
  
  ✅Login securely
  
  ✅View vegetables and fruits
  
  ✅Add products to cart
  
  ✅Make payments based on their account balance

**🗂️ Project Structure**

 ![image](https://github.com/user-attachments/assets/7b39ba95-740f-4134-b73a-6eb31d4498ab)

![image](https://github.com/user-attachments/assets/8060a547-fde9-4979-8c19-7d041bac5761)

**Step-by-step structured explanation of your grocery Django project files and their purpose (without code) for clear understanding and revision:**

**✅ 1. models.py**

  Purpose: Defines database tables for your app.
  
 **Contains:**
  
  Bank model – stores user’s balance.
  
  Product model – stores products (name, price, category, image).
  
  Order model – stores user orders, quantity, payment status, total price.

**✅ 2. views.py**

  Purpose: Handles logic and processing for each URL request.
  
  **Key Views:**
  
  login_view – authenticates users and logs them in.
  
  grocery_home – shows home page after login.
  
  vegetables – shows vegetable products page.
  
  fruits – shows fruit products page.
  
  add_to_cart – adds products to user’s cart.
  
  cart – shows cart with orders and total.
  
  payment – processes payment if balance is sufficient.
  
  success / failure – shows payment success or failure page.
  
  logout_view – logs the user out.

**✅ 3. urls.py**

  Purpose: Maps URLs to views in your project.
  
  Contains:
  
  URL patterns for login, home, vegetables, fruits, add to cart, cart, payment, success, failure, logout.

**✅ 4. templates/store/ folder**

  Contains all HTML files used in your app:
  
  base.html
  
  The master template with common header, footer, navigation.
  
  Other pages extend this file for consistency.
  
  login.html
  
  Login page design with username & password form.
  
  Uses base.html for styling.
  
  grocery_home.html
  
  Home page after login.
  
  Displays welcome message and links to vegetables, fruits, cart.
  
  vegetables.html
  
  Shows all vegetable products with image, price, quantity selection, and add to cart button.
  
  fruits.html
  
  Similar to vegetables.html but for fruits.
  
  cart.html
  
  Displays cart contents, total amount, and proceeds to payment.
  
  payment.html
  
  Shows payment page with balance and total; submits payment request.
  
  success.html
  
  Shows payment success message and updated balance.
  
  failure.html
  
  Shows payment failure due to insufficient balance.

**✅ 6. admin.py (if used)**

  Registers models to Django admin for adding products, user balances, etc.

**✅ 7. migrations/ folder**

  Stores auto-generated migration files after running makemigrations for database schema changes.

**✅ **8. Execution Flow**

  User visits login page (login_view)
  
  Upon successful login → redirects to home page (grocery_home)
  
  User selects:
  
  Vegetables page (vegetables)
  
  Fruits page (fruits)
  
  Adds items to cart (add_to_cart)
  
  Visits cart page (cart)
  
  Proceeds to payment page (payment)
  
  If balance is sufficient → success page
  
  Else → failure page
  
  Logout returns user to login page.

**✅ 9. settings.py (project level)**
  Not specific to app, but ensures:
  
  store app is included in INSTALLED_APPS
  
  Templates, static files, media files configurations.

**output:**

![1](https://github.com/user-attachments/assets/77e8c7c3-2895-4442-b3eb-45ad0f557ab6)

![2](https://github.com/user-attachments/assets/e80dd2a8-d397-493d-b04e-c6ad4a563084)

![3](https://github.com/user-attachments/assets/5e11f975-d746-4f57-b6ee-70e3bcbd2814)

![4](https://github.com/user-attachments/assets/4e2e6cd4-124f-4731-b9bc-8bc8cd35c315)

![5](https://github.com/user-attachments/assets/e040758b-b77b-4910-ad61-9f7c0e32ee1e)

![6](https://github.com/user-attachments/assets/88b7131f-fd95-435f-a263-433729e28281)

![7](https://github.com/user-attachments/assets/0456b97b-6594-4324-a5ef-2ecc4b2952e1)

![9](https://github.com/user-attachments/assets/e643b607-56b9-4048-9816-abc9ca647b03)

![10](https://github.com/user-attachments/assets/590a9b61-ac06-4f7b-a29f-281d5ffce66e)


**Final Conclusion for Your Grocery Django App Project**

  You have successfully built a full-stack Grocery Store web application with:
  
  Secure Login system
  
  Categorized products (Vegetables & Fruits)
  
  Add to cart functionality
  
  Balance-based payment with success/failure status
  
  Admin management for products and user bank balances












