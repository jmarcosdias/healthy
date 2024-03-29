# <em>MyGreenGrocer</em> website

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
   1. [Existing features](#existing-features)
   2. [Features left to implement](#features-left-to-implement)
3. [Design](#design)
   1. [User stories](#user-stories)
   2. [Wireframes](#wireframes)
   3. [Data model](#data-model)
4. [Project follow-up](#project-follow-up)
   1. [User stories defined for project's phase 1](#user-stories-defined-for-projects-phase-1)
5. [Testing](#testing)
   1. [Manual test procedures](#manual-test-procedures)
6. [Web marketing strategies](#web-marketing-strategies)
   1. [Search Engine Optimization](#search-engine-optimization)
   2. [Web marketing strategies beyond SEO](#web-marketing-strategies-beyond-seo)
7. [E-commerce business model](#e-commerce-business-model)
8. [Deployment](#deployment)
   1. [How to deploy the site to heroku](#how-to-deploy-the-site-to-heroku)
   2. [How to deploy the site locally](#how-to-deploy-the-site-locally)
9. [Credits](#credits)

## Overview

The purpose of this project is to develop the <em>My Greengrocer</em> web application, to sell fruits and vegetables online. I intend to address the needs of anyone who would like to eat more fruits and vegetables, and find it to be more practical, faster and pleasant to buy online.

The value this web application provides to the user is that they will be able to buy healthy and fresh fruits and vegetables online, of good quality, instead of having to go themselves to the grocery or to the supermarket.

The online store will start with three categories of products: fresh fruits, fresh vegetables and boxes.

The boxes are packed products that can contain anything. There is a product description field that can be used by the seller to describe the contents of each box.

The only option for payment is by credit card. In addition to the product browsing, searching and checkout features, the following features are implemented:

* Product reviews module (all CRUD functionality is implemented)
* Product requests module (all CRUD functionality is implemented)
* Contact requests module (all CRUD functionality is implemented)
* Subscribe to and unsubscribe from newsletter
* View and update user profile

The main technologies are Python, Django framework, Bootstrap framework, HTML5, CSS and JavaScript.

The following features are only available to registered users:

* Product reviews module
* Product requests module
* Contact requests module
* View and update user profile

Those features for registered users are a valuable part of the website, allowing the users to interact with the application, providing this way some engagement. For these functionalities, I need the users to register and log in so that they can update their data only, instead of letting a user update other people's data.

It is also a very good idea to keep a record of those registered users, so that I can analyze their data. For example I can analyze what they write about the products, what products they request, what they would like to talk about in a future contact. This way I will be able to provide a better experience to those registered users and perhaps to the not registered as well, at least to the ones that may like the same kind of things the registered users like.

The <em>My Greengrocer</em> website uses django-allauth as the authentication mechanism.

## Features

### Existing features

The users are able to list products by category or all products from all categories and then they can sort each list alphabetically or by price.

When browsing a list of products, the users can select a product and add it to the shopping bag, specifying the quantity.

The contents of the shopping bag are stored in the HTTP session that is established between the HTTP client (browser) and the HTTP server. By storing these contents in the HTTP session and making sure there is always a link to the checkout functionality, the web application allows the user to consolidate their purchase at any point after adding one or more products to the bag.

Registered users can see and update their profile and they can manage their own product reviews, product requests and contact requests.

Anyone can browse the products, buy and subscribe to or unsubscribe from the newsletter.

### Features left to implement

Currently, the only option to pay is by credit card. I am analyzing more payment options to implement in the future.

I will need to limit the delivery area of the products for logistics reasons. This functionality is under analysis and hopefully will be implemented soon, to allow the business to start.

There is a product details page with little content. Listing the product reviews in this page is something I would like to implement.

## Design

### Data model

The format I chose to first present here the entities and attributes of the data model is the following:

* Entity
  * attribute1 
  * attribute2
  * attribute3
  * ...
  * attributeN

For each attribute, I have included the following in parenthesis where applicable.

* The constraints:
  * pk = primary key
  * fk = foreign key 
  * unique 
  * unique per field name
* The specification of the relation:
  * one-to-one 
  * n-to-one

Said that, here are the entities and attributes of the <em>My Greengrocer</em> data model.
   
* Category
  * id (pk)
  * name
  * friendly_name
  
* ContactRequest
  * id (pk)
  * text_content
  * full_name
  * phone_number
  * contact_date
  * contact_timeslot (unique per contact_date)
  * created_by (fk to User, n-to-one relationship)
  * creation_date_time
  * last_update_date_time
  
* NewsletterSubscription
  * id (pk)
  * email (unique)
  * creation_date_time
  
* Order
  * id (pk)
  * order_number
  * user_profile (fk to UserProfile, n-to-one relationship)
  * full_name
  * email
  * phone_number
  * country
  * postcode
  * town_or_city
  * street_address1
  * street_address2
  * county
  * date
  * delivery_cost
  * order_total
  * grand_total
  * original_bag
  * stripe_pid

* OrderLineItem
  * id (pk)
  * order (fk to Order, n-to-one relationship)
  * product (fk to Product, n-to-one relationship)
  * quantity
  * lineitem_total
  
* Product
  * id (pk)
  * category (fk to Category, n-to-one relationship)
  * sku
  * title
  * subtitle
  * price
  * description
  * image_url
  * image
  * rating
  
* ProductRequest
  * id (pk)
  * created_by (fk to User, n-to-one relationship)
  * text_content
  * creation_date_time
  * last_update_date_time
  
* Review
  * id (pk)
  * product (fk to Product, n-to-one relationship)
  * created_by (fk to User, n-to-one relationship)
  * text_content
  * creation_date_time
  * last_update_date_time
  
* UserProfile
  * id (pk)
  * user (fk to User, one-to-one relationship)
  * default_phone_number
  * default_street_address1
  * default_street_address2
  * default_town_or_city
  * default_county
  * default_postcode
  * default_country

Notes: 
* Product.rating is not used by the application in this version. I decided to include it in the data model, to use it in future versions of the application.

Below, I present a simplified entity-relationship diagram. There we can see all the relationships between the entities and the attributes involved in these relationships. The remaining attributes are omitted to make the diagram simpler. The <em>My Greengrocer</em> entities are highlighted.

![image](https://user-images.githubusercontent.com/87392921/192906680-59d9a745-ab41-403d-bc1c-348f64037e12.png)


### Project goals

Here is a summary of the project goals:

* Create account (user)
* Log in (registered user)
* Select products to buy (user)
* Buy products / Finalize the purchase (user)
* Understand what they would be buying if they decided to buy each product (user)
* Easily identify what they want to purchase (user)
* Add, update and delete products (superuser only)
* Shopping bag (user)
* Profile (registered user)
* Feedback messages (user)
* Manage product reviews (registered user)
* Manage product requests (registered user)
* Manage contact requests (registered user)
* Subscribe/unsubscribe newsletter (user)

### User stories

#### Phase 1

These are the user stories defined for the first phase of the project, mapped to the project goals.

* USER STORY: Welcome Page - As a Site User I want to be able to view the welcome/landing page so that I can log in or create an account. PROJECT GOALS: Log in, Create account.
* USER STORY: Create account - As a Site User I want to be able to create an account so that I can log in to the website.  PROJECT GOALS: Log in, Create account.
* USER STORY: Log in - As a Site User I want to be able to log in to the website so that I can buy products.  PROJECT GOALS: Log in, Buy products.
* USER STORY: Recover password - As a Registered Site User I want to be able to recover my password in case I forget it, so that I can log in to the website.  PROJECT GOALS: Log in.
* USER STORY: View list of products - As a Site User I want to be able to view a list of products for each product category, so that I can select some products to purchase.  PROJECT GOALS: Select products to buy.
* USER STORY: View individual product details - As a Site User I want to be able to view the title, the subtitle, the category, the description, the price and the image of each product, so that I can understand what I would be buying if I decided to buy this product.  PROJECT GOALS: Understand what they would be buying if they decided to buy each product.
* USER STORY: Sort the list of available products - As a Site User I want to be able to sort products by title and price so that I can easily identify what I want to purchase.  PROJECT GOALS: Easily identify what they want to purchase.


#### Phase 2

Here are the user stories that make up the second phase of the project, mapped to the project goals.

* USER STORY: Products management - As a Superuser I want to be able to add, update and delete products.  PROJECT GOAL: Add, update and delete products.
* USER STORY: Shopping bag - As a Site User I want to be able to add products to the shopping bag.  PROJECT GOAL: Shopping bag.
* USER STORY: Checkout - As a Site User I want to be able to finalize my purchase by paying with credit card.  PROJECT GOAL: Buy products / Finalize the purchase.
* USER STORY: Profile - As a Registered User I want to be able to see and update my profile.  PROJECT GOAL: Profile.
* USER STORY: Feedback messages to users - As a Site User I want to receive ongoing feedback messages in the website, according to the actions I take in the website.  PROJECT GOAL: Feedback messages.
* USER STORY: Product reviews - As a Registered User I want to be able to manage my product reviews.  PROJECT GOAL: Manage product reviews.
* USER STORY: Product requests - As a Registered User I want to be able to manage my product requests.  PROJECT GOAL: Manage product requests.
* USER STORY: Contact requests - As a Registered User I want to be able to manage my contact requests  PROJECT GOAL: Manage contact requests.
* USER STORY: Newsletter signup form - As a Site User I want to be able to subscribe to and unsubscribe from the newsletters.  PROJECT GOAL: Subscribe/unsubscribe newsletter.


### Wireframes

Here are some examples of the wireframes used during the design phase. The wireframes were very useful during that phase, for me to get a first idea of how the web site would look like.

#### List of products in desktop

![image](https://user-images.githubusercontent.com/87392921/190019262-f4044f4d-64e0-4268-8345-2fd2a21e5df4.png)

#### List of products in mobile phone

![image](https://user-images.githubusercontent.com/87392921/190019667-ebc73b2e-fbcf-4a53-a6eb-cd8a4b2c2f90.png)

### Data model

## Project follow-up

This section presents the status of the development of the <em>MyGreenGrocer</em> website along the way.

### User stories defined for project's phase 1

![image](https://user-images.githubusercontent.com/87392921/190022403-80fa7233-6862-41c9-bdbe-d9dc27aca254.png)

### Start working on welcome page

The objective here is to create the my_greengrocer project and the home app.
![image](https://user-images.githubusercontent.com/87392921/190152639-052d82f9-3a44-4e34-90a0-c0a2bedc1460.png)

### Start working on create account functionality

![image](https://user-images.githubusercontent.com/87392921/190172435-7f3fecea-36ee-47e1-b960-ddd5ee720bb9.png)

The welcome page is complete.

![image](https://user-images.githubusercontent.com/87392921/190173005-596b8b17-1992-4028-996c-5170f36694b0.png)

![image](https://user-images.githubusercontent.com/87392921/190173419-c340b51e-b630-46fc-8e99-2e8475245416.png)

### Start working on list of products 

![image](https://user-images.githubusercontent.com/87392921/190215149-96744106-ac66-428e-a10c-5403e85182e8.png)

The create account, log in and recover password functionalities are complete.

![image](https://user-images.githubusercontent.com/87392921/190215671-25b9b224-edb8-463e-966b-bb5655033976.png)

![image](https://user-images.githubusercontent.com/87392921/190216037-1565721d-21a5-4877-8ff1-d86fe866380e.png)

![image](https://user-images.githubusercontent.com/87392921/190216205-c958c91b-63bc-4f9c-8064-e567f19a911f.png)

### Start working on view individual product details

![image](https://user-images.githubusercontent.com/87392921/190267108-6322e38f-b43a-4450-bfcc-056ab9f6dae4.png)

The list of products and sort by product title and price are complete.

![image](https://user-images.githubusercontent.com/87392921/190268120-909c2d16-a2ae-40c3-b113-db98474e2be0.png)

![image](https://user-images.githubusercontent.com/87392921/190270032-65edc734-d63c-42d1-b957-f9b255adf020.png)

### Phase 1 is complete

![image](https://user-images.githubusercontent.com/87392921/190402726-eb4a9f79-fb2d-4324-ab10-9e4bed0b281b.png)

### User stories defined for project's phase 2

![image](https://user-images.githubusercontent.com/87392921/190424118-887e3559-2e4d-44e8-9de3-1b85bea8c9e1.png)

### Start working on shopping bag

![image](https://user-images.githubusercontent.com/87392921/190521727-50f9028d-746d-4731-a7b6-18d760de4866.png)

The product management functionality is complete.

![image](https://user-images.githubusercontent.com/87392921/190531938-cc4c2326-ea8b-4a13-b564-474214e1f90d.png)

### Start working on feedback messages to the user

When working on shopping bag, I decided to implement the system that shows feedback messages to the user. So I am working on both items now.

![image](https://user-images.githubusercontent.com/87392921/190652564-d5ce773f-0f29-46f2-be0c-b962ac6dd6d4.png)

### Start working on checkout functionality

![image](https://user-images.githubusercontent.com/87392921/190721023-bb43ae7b-3f54-44a0-a8ba-8757156b4d75.png)

The feedback messages to the user and the shopping bag are complete. The following features to be implemented, must use feedback messages to the user.

### Add a user story to work on profile app

During the work on the checkout app, it was identified the need of the profile app, so the kanban board was updated accordingly.

![image](https://user-images.githubusercontent.com/87392921/190869688-6416f083-5669-40b3-a2c6-bf7fb2c2cc6a.png)

### Start working on product reviews

![image](https://user-images.githubusercontent.com/87392921/190874727-894afdea-2b87-476a-933d-363bc6fc76b0.png)

The following options will be implemented under "My Account" menu, as this seems to be the place where these options should live.

![image](https://user-images.githubusercontent.com/87392921/190874788-93751f6b-b1cd-42cc-9585-cfb3624ebc9d.png)

### Start working on product requests

![image](https://user-images.githubusercontent.com/87392921/190934977-a51cc481-8608-4f81-a096-fe891be9b558.png)

### Start working on contact requests 

![image](https://user-images.githubusercontent.com/87392921/191104835-3c204364-6db0-44dd-8cfd-5edbe6e4be3f.png)

The product requests functionality is complete.

![image](https://user-images.githubusercontent.com/87392921/191106097-f2fd1885-c472-4134-b3a6-74bdb8e53497.png)

### Start working on news letter sign up form

![image](https://user-images.githubusercontent.com/87392921/191142054-e3223570-eab3-418f-86ff-faadd4e10ba3.png)

The contact requests module is complete.

![image](https://user-images.githubusercontent.com/87392921/191142616-e4014f9c-c865-464a-8268-bc0f567370c1.png)

The newsletter functionality is complete

![image](https://user-images.githubusercontent.com/87392921/192100888-1200cb3f-73bf-4a76-bfb8-27733b5a9f4d.png)

## Testing

### Manual test procedures

Here I describe the manual test procedures I have designed and implemented to assess functionality, usability, responsiveness and data management within the <em>My Greengrocer</em> website.

*Testing Instructions*

Repeat the following steps in different devices including desktop and smartphone and different browsers. Pay attention to the usability and responsiveness by comparing what you see in each device with what you see in other devices. Follow the instructions at each step to assess functionality and data management.

#### Feedback messages to users

##### As a Site User I want to receive ongoing feedback messages in the website, according to the actions I take in the website.

These messages should be tested along all the test procedures. Make sure you see messages giving you feedback according to the actions you take.

For example, when signing in as User1 (Log in test below), make sure you see a message saying "Successfully signed in as User1.".

#### Welcome Page

##### As a Site User I want to be able to view the welcome/landing page so that I can log in or create an account. 

1. Go to the landing page
2. Make sure you are not logged in
3. Verify that both the Login and Register options are available

#### Create account 

##### As a Site User I want to be able to create an account so that I can log in to the website.

1. Go to the landing page
2. Make sure you are not logged
3. Utilize the Register option to create the User1 user. You should receive an email to confirm.
4. Click on the link inside the email. You should be redirected to the confirm email address page.
5. Click Confirm in that page. 
6. Verify that you can see the message "You have confirmed xxx@yyy." with xxx@yyy being the email you used to register. 
   
Note: if User1 is not available, please utilize another user and replace User1 by that user along all the manual testing procedures.

#### Log in

##### As a Site User I want to be able to log in to the website so that I can buy products

1. Go to the landing page
2. Make sure you are not logged
3. Login as User1
4. Verify that you can see the message "Successfully signed in as User1."

#### Recover password

##### As a Registered Site User I want to be able to recover my password in case I forget it, so that I can log in to the website.

1. Go to the landing page
2. Make sure you are not logged
3. Click Login and then "Forgot password?" link. 
4. Write the email you used to create User1 and click Reset My Password. You should receive an email with instructions to reset your password.
5. Make sure you are able to reset your password by testing the "Log in" again, this time with your new password.
   
#### "View list of products" AND "View individual product details" AND "Sort the list of available products"

##### As a Site User I want to be able to:
      * View a list of products for each product category, so that I can select some products to purchase.
      * View the title, the subtitle, the category, the description, the price and the image of each product, so that I can understand what I would be buying if I decided to buy this product.
      * Sort products by title and price so that I can easily identify what I want to purchase.

1. Go to the landing page
2. Make sure you are not logged
3. Login as User1
4. Click each "All Products", "Fresh Fruits", "Fresh Vegetables" and "Boxes" links and for each one make sure you utilize all the options in the corresponding region highlited in the below figure and make sure they do what they say they do.![image](https://user-images.githubusercontent.com/87392921/192921734-7053c879-7038-445d-a94e-314bd9ef34eb.png)
5. Click to see the detail of a product of each category. 
   1. For a product with a "Fresh Fruits" or "Fresh Boxes" category, you must see a title, a sub-title and a price.
   2. For a product with a "Boxes" category you must see a title, a price and a description.

In relation to step 4 above, below in yellow is what you should see and test for each case.

* All Products 

![image](https://user-images.githubusercontent.com/87392921/192923288-f076e29f-e8f0-41fa-9af7-6b515ed19a38.png)

* Fresh Fruits

![image](https://user-images.githubusercontent.com/87392921/192923477-5c76154b-d691-4299-9e1b-d444dbcdc649.png)

* Fresh Vegetables

![image](https://user-images.githubusercontent.com/87392921/192923573-f2106e3d-7c99-47b5-8fe6-26362a3fc84a.png)

* Boxes

![image](https://user-images.githubusercontent.com/87392921/192923718-1c1eb133-4b7c-44fb-b462-90289e50ac3a.png)

#### Shopping bag AND Checkout
##### As a Site User I want to be able to:
      * Add products to the shopping bag.
      * Finalize my purchase by paying with a credit card.
1. Go to the landing page
2. Make sure you are not logged
3. Login as User1
4. List some products of different categories and for each category go to the detail of a product, select a quantity and add it to the shopping bag.
5. Select again some products that are already in the bag and add them again to the shopping bag with a quantity you select.
6. Verify you see messages according to your actions. For example: Added "Avocado - 1 avocado" to your bag, Updated "Avocado - 1 avocado" quantity to 7, etc...
8. When you have products of all categories in your shopping bag, select go to secure checkout (this will bring you to the Shopping Bag page). Repeat this step by using a different link, so that you test all the possible links that will bring you the the Shopping Bag page.
9. In the Shopping Bag page, test the Update link to update the quantity by increasing and decreasing the quantity of different products.
10. In the Shopping Bag page, test the Remove link to remove a product from the shopping bag.
11. In the Shopping Bag page, with some products there, click in Secure Checkout. This will bring you to the Checkout page.
12. In the Checkout page, fill the form and complete the order. For the credit card you can use 4242424242424242 04/24 242 42424.
13. Confirm the values and the delivery amount. They must be in accordance with what the website says (free delivery for orders over $30).
14. Click Complete Order. You must see a message saying "Order successfully processed! ..." with the order number. Confirm this in your email as well.

#### Products management
##### As a Superuser I want to be able to add, update and delete products.  

Logged as a superuser (for example: admin) do the following:
1.  Click Product Management. You should be redirected to the Product Management page.
2.  Verify you are able to add products, update products and delete products.

#### Profile
##### As a Registered User I want to be able to see and update my profile.

Logged as User1 do the following:
1.  Click My Profile option. You should be redirected to My Profile page.
2.  Update the  information in My Profile page and click Update Information
3.  Verify that you can see the message "Profile updated successfully"
4.  Go to another page and then go again to the My Profile page and verify your information is correctly updated.

#### Product reviews
##### As a Registered User I want to be able to manage my product reviews.

Logged as User1 do the following:
1.  Click My Product Reviews. You should be redirected to My Product Reviews page.
2.  Click Add Review, fill the form and click Add Review. You should be redirected to the Reviews page.
3.  Confirm you can see the review you just added and also a message saying "Successfully added review!".
4.  In the review you created, click Edit. You should be redirected to the Edit Review page.
5.  Confirm you can see the message "You are editing a review for ...!" referring to the product you chose.
6.  Clean the text for your review and click Update Review. You should see a message at form validation saying to fill this field.
7.  Update the text for your review filling something different from the initial content and click Update Review. You should be redirected to the Reviews page.
8.  Confirm you can see a message saying "Successfully updated review!" and your review is correctly updated.
9.  In the review you created/updated, click Delete and then click Delete. You should be redirected to the Reviews page.
10.  Confirm you can see the message "Review deleted!" and that you cannot see the review you just deleted.
11.  Now try to add a review without anything in the review's text field.
12.  You should see a message at form validation saying to fill this field.
13.  Click Cancel. You should be redirected to the Reviews page and you should not see the empty review you tried to add in step 12.


#### Product requests
##### As a Registered User I want to be able to manage my product requests.

Logged as User1 do the following:
1.  Click My Product Requests. You should be redirected to My Product Requests page.
2.  Click Add Product Request, fill the form and click Add Product Request. You should be redirected to the Product Requests page.
3.  Confirm you can see the request you just added and also a message saying "Successfully added product request!".
4.  In the request you created, click Edit. You should be redirected to the Edit Product Request page.
5.  Confirm you can see the message "You are editing a product request".
6.  Clean the text for your request and click Update Product Request. You should see a message at form validation saying to fill this field.
7.  Update the text for your request filling something different from the initial content and click Update Product Request. You should be redirected to the Product Requests page.
8.  Confirm you can see a message saying "Successfully updated product request!" and your request is correctly updated.
9.  In the request you created/updated, click Delete and then click Delete. You should be redirected to the Product Requests page.
10.  Confirm you can see the message "Product request deleted!" and that you cannot see the request you just deleted.
11.  Now try to add a product request without anything in the request's text field.
12.  You should see a message at form validation saying to fill this field.
13.  Click Cancel. You should be redirected to the Product Requests page and you should not see the empty request you tried to add in step 12.


    
#### Contact requests
##### As a Registered User I want to be able to manage my contact requests.

Logged as User1 do the following:
1.  Click My Contact Requests. You should be redirected to thr My Contact Requests page.
2.  Click Add Contact Request, fill the form.  Note that all fields are mandatory and contact date must be a future date. Click Add Contact Request. You should be redirected to the Contact Requests page.
3.  Confirm you can see the request you just added and also a message saying "Successfully added contact request!".

Logged as another user (for example a User2 you might want to create, or a superuser), do the following:
1. Try to add a contact request with thr same Contact Date and Contact Timeslot of the contact request you created with User1.
2. You should see a message saying "Failed to add contact request. Please ensure the form is valid!" and then at form validation you should see another message in the timeslot field saying "Sorry but this time slot is already booked. Please try another day or another time slot.".
3. Try another day or another time slot that is not yet booked and you should be able to save the contact request.

Logged as User1 do the following:
1.  In the request you created, click Edit. You should be redirected to the Edit Contact Request page.
2.  Confirm you can see the message "You are editing a contact request".
3.  Try to Update Contact Request by filling an invalid value in each field at a time. You should see the corresponding message according to the field you are trying to fill with an invalid value. 
4.  Fill all the fields with valid values and click Update Contact Request. You should be redirected to the Contact Requests page.
5.  Confirm you can see a message saying "Successfully updated contact request!" and your request is correctly updated.
6.  In the request you created/updated, click Delete and then click Delete. You should be redirected to the Contact Requests page.
7.  Confirm you can see the message "Contact request deleted!" and that you cannot see the request you just deleted.
8.  Now try to add a contact request with invalid values in some fields. Try different combinations of invalid values. 
9.  You should not be able to add this request with invalid values and should see the corresponding message at form validation level. You should see one message at a time, so that you can end up fixing all the invalid values and then you should be able to add this request.
10.  Try again to add a contact request with at least one invalid value and after the error message saying the value is invalid, Click Cancel. You should be redirected to the Contact Requests page and you should not see the invalid contact request you tried to add.

#### Newsletter signup form 
##### As a Site User I want to be able to subscribe to and unsubscribe from the newsletters.

Run the below steps not logged as any user and then you can log as User1 and rerun the same steps. The result should be the same.
In steps 1, 3 and 5 utilize emails that are not present in the Newsletter Subscriptions model.

1. In the website, go to the footer and fill a valid email in the newsletter subscription field and then click Subscribe. You should see a message saying "Thank you for subscribing to our newsletter!"
2. Repeat step 1 with the same email used in step 1. You should be redirected to the "Subscribe to our Newsletter" page and see the message "Sorry, we were unable to fulfill your request. Please review your input!" and then at form validation level you should see the message "Newsletter subscription with this Email already exists."
3. Fill another valid email in the field that is in the "Subscribe to our Newsletter" page and click the Subscribe button near that field. You should be redirected to the landing page and see a message saying "Thank you for subscribing to our newsletter!"
4. In the website, go to the footer and click "Unsubscribe to our newsletter". You should be redirected to the "Unsubscribe to our Newsletter" page.
5. In the "Unsubscribe to our newsletter" page, fill the form with an email that is not present in the Newsletter Subscriptions model. You must see the message "Sorry, we are not finding this email. Are you sure you subscribed ... before?" (this message with the email you typed).
6. In the "Unsubscribe to our newsletter" page, fill the form with the email you used in step 1. You should be redirected to the landing page and see the message "We have unsubscribed ... from our newsletter!" (this message with the email you typed).
7. In the website, go to the footer and click "Unsubscribe to our newsletter". You should be redirected to the "Unsubscribe to our Newsletter" page.
8. In the "Unsubscribe to our newsletter" page, fill the form with the email you used in step 3. You should be redirected to the landing page and see the message "We have unsubscribed ... from our newsletter!" (this message with the email you typed).


## Web marketing strategies

### Search Engine Optimization

I have worked on keyword research, with the goal of using that data for search engine optimization. My focus was on finding some long-tail keywords, with a high enough volume and low enough competition.

As a result of this research, I found the following keywords that people care about. These keywords have a relatively high popularity and a relatively low competition, for the United States territory, which is where the first version of <em>My Greengrocer</em> website is planned to be implemented.

* fruit and vegetable store
* online delivery of fruits
* buy vegetables online
* online fruits and vegetables
* online fresh vegetables
* fresh fruits delivery near me
* buy online fruits

In this research, I used the [Wordtracker](https://www.wordtracker.com/) website. The sitemap was obtained by using the [XML Sitemaps](https://www.xml-sitemaps.com/) website, and then I have created the robots.txt file to tell search engine crawlers where they can go and where they cannot go.

### Web marketing strategies beyond SEO

The objective of this activity is to promote the products offered by the <em>My Greengrocer</em> website and its corresponding delivery service, in order to connect with more potential buyers. After all, what is required is to reach people that are most interested in buying fruits and vegetables online.

The content marketing strategy was initially evaluated, but due to the considerable investment that this strategy requires, it was disconsidered.

I will use email marketing, because this is a free way to get a direct line to an initially reduced list of existing and potential customers. Then, even if that list grows, the return on investment for maintaining this type of marketing is expected to be positive.

Organic social marketing is time-consuming and may not reach all the potential customers of <em>My Greengrocer</em>. On the other hand, it is free, it has the potential to reach a lot of existing and future customers, and it is a way for me to keep in touch with those customers. So I decided to choose this strategy and created a <em>My Greengrocer</em> facebook page.

#### Facebook page

Here are some screenshots of the facebook page:

![image](https://user-images.githubusercontent.com/87392921/192174444-7eeca1e2-a67c-4f0b-9dd6-3bbf21849999.png)

![image](https://user-images.githubusercontent.com/87392921/192176065-4f52d284-1ddc-40d7-8605-f563d1cc8a44.png)

## E-commerce business model

<em>My Greengrocer</em> is an online store that sells fruits and vegetables directly to the customer. 

It will be successful with all the customers who might be interested in eating fresh and healthy fruits and vegetables and have little time to spend shopping. So they will find it better to buy online.

The initial marketing strategies that were chosen are email marketing and organic social marketing, because <em>My Greengrocer</em> is a small business and there is no budget to pay for marketing at this early stage.

The fruits and vegetables are sold directly to the consumers, so the e-commerce business model of <em>My Greengrocer</em> is business-to-consumer (B2C).

The payment for the products is taken online. The current version of <em>My Greengrocer</em> website only accepts credit card payments via [Stripe](https://stripe.com/en-ie) payment processing platform. I intend to offer more options for paying in the near future.

We have a reduced number of employees. We offer a request-for-contact functionality, which is available via our website. We can contact customers 7 days a week, but we have no capacity to contact more than one customer in a given time-slot. This validation of "maximum one contact per time-slot" is a requirement for us to work, so it is implemented by the web application.

Fruits and vegetables delivery logistics require us to limit the delivery area. We are working in this direction, but this functionality is not yet implemented.


## Deployment

The website is deployed to [heroku](https://heroku.com).

Here is the link for the live site https://mdias-my-greengrocer.herokuapp.com/

### How to deploy the site to heroku

The below instructions detail how to deploy the site to https://mdias-my-greengrocer-new.herokuapp.com/. In other words, these instructions describe how to deploy this application to heroku, using the mdias-my-greengrocer-new name for the heroku app.

When deploying, you can use any other available name for the heroku app. For example, this site is currently deployed to heroku, using the mdias-my-greengrocer name for the heroku app (https://mdias-my-greengrocer.herokuapp.com/).

1. Create a GitPod workspace based on the main branch of the [GitHub repository](https://github.com/jmarcosdias/healthy)

2. In the GitPod workspace

   1. Login to heroku (use your credentials):
      ```
      heroku login -i
      ```

   2. Create heroku remote for a new app choosing the region.
      
      For example, for the Europe region:
      ```
      heroku create -a mdias-my-greengrocer-new --region eu
      ```
      
      If you prefer other regions, you can see the available regions by using:
      ```
      heroku regions
      ```

      You can confirm that the heroku remote has been created, by using the following command
      ```
      git remote -v
      ```
      and making sure you see those two heroku lines.
      
      ```
      gitpod /workspace/healthy (main) $ git remote -v
      heroku  https://git.heroku.com/mdias-my-greengrocer-new.git (fetch)
      heroku  https://git.heroku.com/mdias-my-greengrocer-new.git (push)
      origin  https://github.com/jmarcosdias/healthy.git (fetch)
      origin  https://github.com/jmarcosdias/healthy.git (push)
      ```

   3. Use heroku ```addons:create``` to create the main database
      ```
      heroku addons:create heroku-postgresql --as=DATABASE
      ```
      
   4. Use heroku config to set the SECRET_KEY variable
      ```
      heroku config:set SECRET_KEY='<a secret key you define>'
      ```
      
      You can use an online secret key generator to generate your secret key, for example https://django-secret-key-generator.netlify.app.
      
   5. Use heroku config to set disable collect static   
      ```
      heroku config:set DISABLE_COLLECTSTATIC=1
      ```
      
   6. Push to heroku git repository
      ```
      git push heroku main
      ```
      
   7. Use heroku config to unset disable collect static
      ```
      heroku config:unset DISABLE_COLLECTSTATIC
      ```
      
   8. Use heroku run to make migrations
      ```
      heroku run python3 manage.py makemigrations
      ```
      
   9. Use heroku run to migrate
       ```
       heroku run python3 manage.py migrate
       ```
       
   10. Use heroku run to load categories
       ```
       heroku run python3 manage.py loaddata categories
       ```
       
   11. Use heroku run to load products
       ```
       heroku run python3 manage.py loaddata products
       ```
   
3. In the AWS website, logged to your AWS account, do the following to setup your 
   AWS account to host media and static files for the <em>My Greengrocer</em> website. 

   1. Go to Amazon S3, create a bucked with a name equals (or similar to) the name of your
      heroku app. For example, the bucket name can be "my-green-grocer" or any other name you prefer.
      The next steps in these instructions are refering this bucket as "my-green-grocer".
      
   2. Go to the Properties of the "my-green-grocer" bucket, click edit "Static website hosting"
      and then Enable static website hosting.
      
   3. Go to the Permissions of the "my-green-grocer" bucket, click edit "Cross-origin resource sharing (CORS)"
      and update the JSON configuration there to the following.
      ```
      [
          {
              "AllowedHeaders": [
                  "Authorization"
              ],
              "AllowedMethods": [
                  "GET"
              ],
              "AllowedOrigins": [
                  "*"
              ],
              "ExposeHeaders": []
          }
      ]
      ```
      
   4. Go to the Permissions of the "my-green-grocer" bucket, click edit "Bucket policy"
      and then click "Policy Generator". The "AWS Policy Generator" page will open in a new tab.
      
   5. In AWS Policy Generator page, choose/fill the following in the form:
      Type of Policy: S3 Bucket Policy
      Principal: * (to allow all)
      Action: GetObject
      Amazon Resource Name (ARN): get this from the “my-green-grocer” bucket
      Click "Add Statement" and then click "Generate Policy".
      Copy the text that was generated (which is the policy).
      You will paste this into the bucket policy editor.
      
   6. Go back to the "Edit bucket policy" page that should be still open in your browser.
      Paste the policy text into the bucket policy editor.
      Add a slash and a star at the end of the value of the Resource key inside the policy.
      
      The policy then should look like this:
      ```
      {
        "Version": "2012-10-17",
        "Id": "Policy1659646953711",
        "Statement": [
          {
            "Sid": "Stmt1659646949079",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::my-green-grocer/*"
          }
        ]
      }
      ```
      
   7. Go to the Permissions of the "my-green-grocer" bucket, click edit "Access control list (ACL)"
      and then Enable the "Everyone (public access) - List" option.
      
   8. Go to Identity Access Management (IAM).
      
      Here you will create a group for the user to live in. Then create an access policy giving the group
      access to the s3 bucket you created ("my-green-grocer" bucket). Then you will assign the user to 
      the group so it can use the policy to access all the static and media files.
      
      Here are the steps to do what is described above:
      
      a. Create a group named "manage-my-green-grocer" (or choose another name if you prefer)
      b. In the "manage-my-green-grocer" group Permissions, choose Add permissions -> Attached policies.
      c. Click "Create policy". A new page will open (create policy page) in a new tab.
      d. In the Create policy page, click in the JSON tab, click in the "Import managed policy" link,
         then search "AmazonS3FullAccess", choose this line and then click "Import".
         The JSON text that will be imported, should look like this:
         ```
          {
              "Version": "2012-10-17",
              "Statement": [
                  {
                      "Effect": "Allow",
                      "Action": [
                          "s3:*",
                          "s3-object-lambda:*"
                      ],
                      "Resource": "*"
                  }
              ]
          }
         ```
         Get the bucket ARN from S3 and use it to fill the Resource in JSON to create a list with two resources.
         After this, the policy should look like this:
         ```
          {
              "Version": "2012-10-17",
              "Statement": [
                  {
                      "Effect": "Allow",
                      "Action": [
                          "s3:*",
                          "s3-object-lambda:*"
                      ],
                      "Resource": [
                          "arn:aws:s3:::my-green-grocer",
                          "arn:aws:s3:::my-green-grocer/*"
                      ]
                  }
              ]
          }
         ```
         You can then go ahead (click Next, Next) and when you can fill a name and a description for 
         your policy. For example: name "my-greengrocer-policy", description "Access to S3 Bucket for My Greengrocer static files".
         Then click "Create Policy" to create it. 
         
      e. Go back to the IAM page, click in "User Groups" and "manage-my-green-grocer" group, 
         then go to Permissions for this user group, click "Add Permissions" and then "Attach Policies". 
         Select the "my-greengrocer-policy" line and then click "Add Permissions".
         
      f. In the IAM page, click in "Users" and then "Add users". Give the user the 
         name "my-green-grocer-static-files-user", select AWS credential type = 
         "Access key - Programmatic access" for this user. Add this user to the "manage-my-green-grocer" group.
         Create the user and download the csv file. Keep the contents of that csv file safe. You will need this.
         
4. In Stripe (https://dashboard.stripe.com/)

   1. Create an account for your My Greengrocer business

   2. In the webhooks section, add the following endpoint:
      https://mdias-my-greengrocer-new.herokuapp.com/checkout/wh/
      

5. In the GitPod workspace
       
   1. Use heroku config to set the AWS_ACCESS_KEY_ID variable
      ```
      heroku config:set AWS_ACCESS_KEY_ID = '<get this value from your AWS account>'
      ```
      
   2. Use heroku config to set the AWS_SECRET_ACCESS_KEY variable
      ```
      heroku config:set AWS_SECRET_ACCESS_KEY = '<get this value from the csv file you got from IAM AWS when you created the user>'
      ```
      
   3. Use heroku config to set the EMAIL_HOST_PASS variable
      ```
      heroku config:set EMAIL_HOST_PASS = '<from your google (or other) account>'
      ```
      
   4. Use heroku config to set the EMAIL_HOST_USER variable
      ```
      heroku config:set EMAIL_HOST_USER = '<from your google (or other) account>'
      ```
      
   5. Use heroku config to set the STRIPE_PUBLIC_KEY variable
      ```
      heroku config:set STRIPE_PUBLIC_KEY = '<from your stripe account>'
      ```
      
   6. Use heroku config to set the STRIPE_SECRET_KEY variable
      ```
      heroku config:set STRIPE_SECRET_KEY = '<from your stripe account>'
      ```
      
   7. Use heroku config to set the STRIPE_WH_SECRET variable
      ```
      heroku config:set STRIPE_WH_SECRET = '<from the webhook section in your stripe account>'
      ```
      
   8. Use heroku run to create a superuser for you My Greengrocer website
      ```
      heroku run python3 manage.py createsuperuser
      ```
      
   9. Update the settings.py file inside my_greengrocer project, adding to the allowed hosts list, 
      the URL of the application you are deploying.
   
      a. Make sure 'mdias-my-greengrocer-new.herokuapp.com' is in the ALLOWED_HOSTS list
      
      ```
      ALLOWED_HOSTS = ['mdias-my-greengrocer-new.herokuapp.com', 'localhost']
      ```
      
      b. Commit your changes
         ```
         git add .
         git commit -m "Update allowed hosts in settings.py file"
         ```
         
   10. Push to heroku git repository
      ```
      git push heroku main
      ```
      
6. Congratulations! Your application is deployed to https://mdias-my-greengrocer-new.herokuapp.com/

Please run the manual tests as described in Testing section.

### How to deploy the site locally

1. Create a GitPod workspace based on the main branch of the 
   [GitHub repository](https://github.com/jmarcosdias/healthy)

2. Install the required packages based on the requirements.txt file

   ```
   pip3 install -r requirements.txt
   ```  
   
3. Create a new file, named env.py, on the top level directory

4. Add the following lines to the env.py file, with suitable values instead of <...>.

   ```
   import os
   os.environ["SECRET_KEY"] = "<a value you define>"
   os.environ["STRIPE_PUBLIC_KEY"] = "<from your stripe account>"
   os.environ["STRIPE_SECRET_KEY"] = "<from your stripe account>"
   os.environ["STRIPE_WH_SECRET"] = "<from the webhook section in your stripe account>"
   os.environ["DEVELOPMENT"] = "Yes"
   ```

5. Add the following import to the settings.py file so that the values above are imported.
   ```
   import env
   ```

6. Apply the migrations to the database
   ```
   python3 manage.py migrate
   ```
   
7. Load categories
   ```
   python3 manage.py loaddata categories
   ```
   
8. Load products
   ```
   python3 manage.py loaddata products
   ```
   
9. Update the settings.py file by adding the current Gitpod URL

   For example you will add the second element with the URL you see in your Gitpod browser window.
   ```
   CSRF_TRUSTED_ORIGINS = [
     'https://8000-jmarcosdias-healthy-15ruaqtykf0.ws-eu67.gitpod.io'
    ,'https://8000-jmarcosdias-healthy-1hwhz59gggh.ws-eu67.gitpod.io'
   ]
   ```

10. Create a superuser for the django admin module
    ```
    python3 manage.py createsuperuser
    ```
       
11. Congratulations. The website is deployed locally!
    
    To run the server locally:
    ```
    python3 manage.py runserver
    ```
    
Please run the manual tests as described in Testing section.
    
## Credits

1. Thanks to Code Institute and to my mentor for all the support I had.
2. The <em>My Greengrocer</em> project uses the Code Institute's Boutique ADO walkthrough project as a basis and adds the four custom models that are highlighted in the data model section in this document
3. The static files and media files are stored in [Amazon Web Services (AWS)](https://aws.amazon.com/)
4. The payment functionality uses the [Stripe](https://stripe.com/) online payment processing system.
5. Icons used from [Font Awesome](https://fontawesome.com/)
6. Fonts used from [Google Fonts](https://fonts.google.com/)
7. Free pictures used from [Pixabay](https://pixabay.com/)
   * Background
   https://pixabay.com/photos/greengrocer-produce-fresh-market-780395/
   * Lemon
   https://pixabay.com/photos/lemon-fruit-vegetable-2121307/
   * Apple, Orange, Peppers and Lemons Box
   https://pixabay.com/photos/fruit-vitamins-orange-healthy-food-320136/
   * Broccoli
   https://pixabay.com/photos/appetite-broccoli-brocoli-broccolli-1238251/
   * Kiwi
   https://pixabay.com/photos/fruits-and-vegetables-fruit-kiwi-1274079/
   * Tomato
   https://pixabay.com/photos/food-fresh-fruit-green-healthy-1239191/
   * Avocado
   https://pixabay.com/photos/appetite-avacado-avo-avocado-1238257/
   * Eggplant
   https://pixabay.com/photos/eggplant-vegetables-fruit-egg-fruit-1717224/
   * Garlics and Lemons Box
   https://pixabay.com/photos/garlic-lemons-fruit-vegetables-276356/
   * No image
   https://pixabay.com/vectors/fruit-basket-vegetable-nutrition-40276/

 
 
    
