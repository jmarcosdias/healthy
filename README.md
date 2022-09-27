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
   1. [Manual tests](#manual-tests)
   2. [Validator tests](#validator-tests)
6. [Web marketing strategies](#web-marketing-strategies)
   1. [Search Engine Optimization](#search-engine-optimization)
   2. [Web marketing strategies beyond SEO](#web-marketing-strategies-beyond-seo)
7. [E-commerce business model](#e-commerce-business-model)
8. [Deployment](#deployment)
   1. [How to deploy the site to heroku](#how-to-deploy-the-site-to-heroku)
   2. [How to deploy the site locally](#how-to-deploy-the-site-locally)
9. [Credits](#credits)

## Overview

The purpose of this project is to develop a website to sell fruits and vegetables. We intend to address the needs of anyone who would like to eat more fruits and vegetables, and find to be more practical, faster and pleasant to buy online.

The online store will start with three categories of products: fresh fruits, fresh vegetables and boxes.

The boxes are packed products that can contain anything. There is a product description field that can be used by the seller to describe the contents of each box.

The only option for payment is by credit card. In addition to the product browsing, searching and checkout features, the following is implemented:

* Product reviews module (all CRUD functionality is implemented)
* Product requests module (all CRUD functionality is implemented)
* Contact requests module (all CRUD functionality is implemented)
* Subscribe to and unsubscribe from newsletter

The main technologies are Python, Django framework, Bootstrap framework, HTML5, CSS and JavaScript.

Before completing the purchase, the user needs to register and login, because the greengrocer needs to collect and keep some essential information, for each user and each order, not only to deliver the product to the user but also to communicate to the greengrocer's sales and billing systems. This website is using django-allauth as the authentication mechanism.

## Features

### Existing features

The users are able to list products by category or all products from all categories and then they can sort each list alphabetically or by price.

When browsing a list of products, the users can select a product and add it to the shopping bag, specifying the quantity.

The contents of the shopping bag are stored in the HTTP session that is established between the HTTP client (browser) and the HTTP server. By storing these contents in the HTTP session and making sure there is always a link to the checkout functionality, the web application allows the user to consolidate their purchase at any point after adding one or more products to the bag.

Registered users can buy products and they can also manage their own product reviews, product requests and contact requests.

Anyone can browse the products and subscribe to or unsubscribe from the newsletter.

### Features left to implement

The only option to pay is by credit card. I am analyzing more options for the customer to pay in the future.

I need to limit the delivery area of the products for logistics reasons. This functionality is under analysis and hopefully will be implemented soon, to allow the business to start.

## Design

### User stories

#### Phase 1

These are the users stories defined for the first phase of the project.

* USER STORY: Welcome Page - As a Site User I want to be able to view the welcome/landing page so that I can log in or create an account.
* USER STORY: Create account - As a Site User I want to be able to create an account so that I can log in to the website.
* USER STORY: Log in - As a Registered Site User I want to be able to log in to the website so that I can buy products.
* USER STORY: Recover password - As a Registered Site User I want to be able to recover my password in case I forget it, so that I can log in to the website.
* USER STORY: View list of products - As a Registered Site User I want to be able to view a list of products for each product category, so that I can select some products to purchase.
* USER STORY: View individual product details - As a Registered Site User I want to be able to view the title, the subtitle, the category, the description, the price and the image of each product, so that I can understand what I would be buying if I decided to buy this product.
* USER STORY: Sort the list of available products - As a Registered Site User I want to be able to sort products by title and price so that I can easily identify what I want to purchase.

#### Phase 2

Here are the user stories that make up the second phase of the project.

* USER STORY: Products management
* USER STORY: Shopping bag
* USER STORY: Checkout
* USER STORY: Profile
* USER STORY: Feedback messages to user
* USER STORY: Products reviews
* USER STORY: Products requests
* USER STORY: Contacts requests
* USER STORY: Newsletter signup form

### Wireframes

Here are the main wireframes for viewing products in both desktop and mobile app. They were used during the design phase, to get a first idea of how the web site will look like.

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

### Manual tests

#### Navigation on the entire site

#### Broken links

#### Ease of Navigation

### Validator tests

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

### How to deploy the site to heroku

### How to deploy the site locally

## Credits

 
    
