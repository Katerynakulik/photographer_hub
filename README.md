# Photographer Hub

**Photographer Hub** is a professional full-stack e-commerce application built with Python (Django), designed to provide a "Fine Art" digital marketplace for photography enthusiasts and a booking management system for exclusive photoshoot sessions. The platform operates on a B2C (Business to Consumer) business model, selling high-resolution digital art licenses and professional photography services directly to clients.

<img src="docs/screenshots/hero.png" width="800">

The application is deployed to Heroku and can be accessed at:
* **[Link to Live Site](https://photographer-hub-94aeeeedb69e.herokuapp.com/)**
* **[Link to GitHub Repository](https://github.com/your-username/photographer_hub)** ---

## Table of Contents
1. [Project Overview](#1-project-overview)
    * [Business Model (B2C)](#business-model-b2c)
    * [User Goals](#user-goals)
    * [Target Audience](#target-audience)
    * [User Requirements and Expectations](#user-requirements-and-expectations)
2. [Agile Methodology](#2-agile-methodology)
    * [User Stories](#user-stories)
    * [Kanban Board](#kanban-board)
    * [Project Milestones](#project-milestones)
3. [Design](#3-design)
    * [Colours](#colours)
    * [Typography](#typography)
4. [Structure](#4-structure)
    * [Website Pages](#website-pages)
    * [Database](#database)
5. [Technologies Used](#5-technologies-used)
6. [Marketing Strategy](#6-marketing-strategy)
    * [Social Media Marketing](#social-media-marketing)
    * [Email Marketing (MailChimp Integration)](#email-marketing-mailchimp-integration)
7. [SEO Implementation](#7-seo-implementation)
8. [Features](#8-features)
    * [Header & Footer](#header--footer)
    * [Home Page](#home-page)
    * [Authentication (Registration & Login)](#authentication-registration--login)
    * [Digital Gallery (Shop)](#digital-gallery-shop)
    * [Photoshoot Booking Selection](#photoshoot-booking-selection)
    * [Client Dashboard ("My Profile")](#client-dashboard-my-profile)
    * [Photographer Management Dashboard](#photographer-management-dashboard)
    * [Gallery & Session CRUD Management](#gallery--session-crud-management)
9. [Testing Accounts](#testing-accounts)
10. [Features Overview](#features-overview)
11. [Validation](#11-validation)
    * [HTML Validation](#html-validation)
    * [CSS Validation](#css-validation)
    * [JavaScript Validation (JSHint)](#javascript-validation-jshint)
    * [Python (PEP8) Validation](#python-pep8-validation)
    * [Lighthouse Audit](#lighthouse-audit)
    * [WAVE Accessibility Audit](#wave-accessibility-audit)
    * [Detailed Accessibility Summary](#detailed-accessibility-summary)
    * [Manual Testing](#manual-testing)
    * [Automated Testing](#automated-testing)
12. [Bugs](#12-bugs)
    * [Fixed Bugs](#fixed-bugs)
    * [Known Issues](#known-issues)
13. [Deployment](#13-deployment)
    * [Heroku Deployment](#heroku-deployment)
    * [Local Deployment](#local-deployment)
14. [Credits](#14-credits)
15. [Conclusion](#15-conclusion)

---

# 1. Project Overview

## Business Model (B2C)
**Photographer Hub** operates as a **Business-to-Consumer (B2C)** e-commerce platform. The site owner (a professional photographer) manages a centrally-owned dataset of artistic works and service offerings. The platform provides value through two primary revenue streams:
* **Digital Goods:** Sale of high-resolution digital licenses for photography enthusiasts and interior designers.
* **Professional Services:** A pre-registration and deposit system for exclusive photoshoot sessions, allowing the photographer to gauge interest and plan high-demand events effectively.

## User Goals
### As a Visitor:
* To browse a high-quality portfolio and understand the photographer's aesthetic.
* To easily find pricing and service details without administrative friction.
* To register an interest in upcoming sessions to secure a potential spot.

### As a Registered Customer:
* To manage a personal library of purchased high-resolution digital assets.
* To pay deposits securely and track active photoshoot interests.
* To communicate with the photographer via dedicated contact and interest forms.

### As the Site Owner (Photographer):
* To maintain full CRUD control over the gallery and session listings via a frontend dashboard.
* To collect marketing data and gauge demand for specific photoshoot themes before committing to a schedule.
* To automate the payment process for both products and service deposits.

## Target Audience
* **Art Collectors & Designers:** Individuals looking for professional digital art for personal or commercial displays.
* **Photography Clients:** People interested in booking high-end, themed photoshoots (portraits, weddings, seasonal events).
* **Newsletter Subscribers:** A community interested in photography tips and exclusive first-look access to new collections.

## User Requirements and Expectations
* **Visual Excellence:** A "Fine Art" aesthetic that prioritizes the imagery.
* **Security:** Industry-standard encryption for payments (Stripe) and authentication (Django Allauth).
* **Intuitive UX:** A navigation system that allows reaching any product or session in under 3 clicks.
* **Instant Feedback:** Clear notifications for cart updates, form submissions, and payment status.
---

# 2. Agile Methodology

The development of Photographer Hub followed an Agile workflow, utilizing GitHub Projects to manage a Kanban board and prioritize tasks using the MoSCoW method.

## User Stories
The following User Stories formed the basis of the development process:

### **Visitor Stories**
* **#1 View Homepage:** As a visitor, I want to view a clear homepage so that I understand the purpose of the site.
* **#2 Navigate Website:** As a visitor, I want a consistent main menu so that I can access all sections easily.
* **#7 Browse Products:** As a visitor, I want to browse photo products with pricing so that I can decide what to buy.
* **#12 View Sessions:** As a visitor, I want to see upcoming sessions so that I can choose one to join.
* **#18 Contact Form:** As a visitor, I want to send a message so that I can ask questions.

### **Customer Stories**
* **#4 Register Account:** As a visitor, I want to register so that I can purchase photos and book sessions.
* **#9 Add to Cart:** As a user, I want to add products to a cart so that I can purchase multiple items.
* **#10 Checkout:** As a user, I want to pay securely using Stripe.
* **#16 Express Interest:** As a user, I want to register interest in a session to show my intent.
* **#17 Pay Deposit:** As a user, I want to pay a deposit so that my interest is confirmed.
* **#11 Access Purchases:** As a user, I want to access my purchased photos in a private library.

### **Admin (Site Owner) Stories**
* **#6 Role-Based Access:** As a site owner, I want admin-only access to management tools to protect core data.
* **#CRUD:** I want to Create, Read, Update, and Delete products and sessions from the frontend dashboard.

## Kanban Board
The project was managed via GitHub Projects, categorizing tasks into:
* **Must Have:** Core authentication, Stripe integration, Product CRUD.
* **Should Have:** Session interest forms, Deposit payments, Custom 404 page.
* **Could Have:** Newsletter integration, automated slot management (moved to future).

## Project Milestones
1.  **Milestone 1: Infrastructure & Auth (Stories #2, #5, #6, #1, #4)** - Setting up the core Django project and user roles.
2.  **Milestone 2: E-commerce Core (#7, #8, #9, #10, #11)** - Product gallery and secure Stripe checkout.
3.  **Milestone 3: Service Planning (#12, #13, #16, #17)** - Photoshoot sessions and the deposit/interest system.
4.  **Milestone 4: Marketing & SEO (#3, #18, #19)** - Custom error pages, Newsletter, and SEO optimization.

## Future Implementations

### **Automated Capacity Management (#14)**
While the current system allows interest registration and deposit payments, it does not strictly enforce a maximum number of participants per session in real-time. 
* **Planned:** Implementation of a `max_capacity` field in the `Photoshoot` model and a calendar view for specific date selection.
* **Target Status:** Backlog for Milestone 5.

### **Persistent Message Storage (#18)**
Currently, the contact form provides immediate feedback to the user.
* **Planned:** Creation of a `ContactMessage` model to store all inquiries in the database for the photographer to review in the dashboard.
---

---

## 3. Design

### Colours
The colour palette is curated to maintain a "Fine Art" aesthetic using muted, sophisticated tones.
* **Warm Ivory (#F8F5F2):** Primary background.
* **Muted Sage (#A8BBA3):** Primary branding and buttons.
* **Soft Blush (#E8CFCB):** Accents and borders.
* **Dusty Rose (#D6A5A1):** Hover effects and error highlights.

### Typography
* **Serif Titles:** 'Playfair Display' (700 weight) for an elegant, artistic feel.
* **Body Text:** 'Montserrat' or 'Inter' (Sans-Serif) for readability across devices.

---

## 4. Structure

### Website Pages
* **Home:** Featuring the latest gallery highlights and newsletter signup.
* **Gallery (Shop):** A comprehensive grid of digital photos for sale.
* **Photoshoot Detail:** Full details and deposit booking for specific sessions.
* **Dashboards:** Role-based views for clients (orders/bookings) and the photographer (management).

### Database
The system uses a relational PostgreSQL database with three original custom models linked to the Django User model:
* **PhotoProduct:** Metadata for digital images, including Cloudinary paths and pricing.
* **Photoshoot:** Details for service sessions, including deposit logic.
* **Booking:** Transactional link connecting users to their specific booked photoshoot sessions.

---

## 5. Technologies Used
* **Languages:** HTML5, CSS3, JavaScript, Python.
* **Framework:** Django (5.2).
* **Database:** PostgreSQL.
* **Payments:** Stripe API.
* **Media Storage:** Cloudinary.
* **Email/Newsletter:** MailChimp.

---

## 6. Marketing Strategy

### Social Media Marketing
A Facebook Business Page mockup was created to demonstrate the brand's social presence and engagement strategy.
<img src="docs/marketing/facebook_mockup.png" width="400">

### Email Marketing
Integration with MailChimp enables a newsletter subscription system.
* Signup form located on the Home Page footer.
* Automated signals invite registered users to join the marketing list.

---

## 7. SEO Implementation
* **Robots.txt:** Configured to allow crawling of products while blocking admin areas.
* **Sitemap.xml:** Dynamically generated to help search engines index active products and sessions.
* **Meta Tags:** Descriptive keywords and site descriptions included in the base template.
* **Rel Attributes:** Used `rel="noopener noreferrer"` for all external links.

---

## 8. Features
* **Header & Footer:** Minimalist navigation with role-based links.
* **Newsletter Signup:** Clean, AJAX-ready subscription form linked to MailChimp.
* **Shopping Cart:** Real-time badge updates and persistent sessions.
* **Frontend CRUD:** Site owner can Add, Edit, or Delete items directly from the dashboard without using Django Admin.
* **Custom 404/500:** Branded error pages to improve overall UX.

---

## 11. Validation

* **HTML:** Checked via W3C Markup Validator.
* **CSS:** Validated via Jigsaw Service.
* **JavaScript:** ES6 compliant, checked via JSHint.
* **Python:** 100% PEP8 compliance across all apps.
* **Lighthouse:** High scores (90+) in Accessibility and Best Practices.
### **Automated Testing**
The application employs automated testing via the Django `TestCase` framework to ensure high code reliability, security, and consistent business logic performance.

#### **Testing Strategy**
Following a robust testing approach, every User Story is supported by at least two automated test cases covering both "Happy Path" (success) and "Defensive" (failure/security) scenarios.

#### **Core Test Suites**
* **Role-Based Access (#6):** * `test_admin_access`: Confirms that users identified as photographers can access the management dashboard.
    * `test_client_denial`: Verifies that standard users are redirected when attempting to access administrative URLs.
* **Cart & E-commerce (#9, #10):**
    * `test_add_to_cart`: Ensures products are correctly stored in the session-based cart.
    * `test_license_limit`: Confirms digital photo licenses are limited to one per customer to prevent accidental duplicate purchases.
* **Service Management (#12, #15):**
    * `test_delete_session`: Validates that a photographer can permanently remove a photoshoot session from the database.
    * `test_public_visibility`: Ensures only active products and sessions are displayed to non-staff visitors.

#### **Execution Instructions**
To run the automated test suite, ensure your virtual environment is active and execute:
```bash
python3 manage.py test


```
[<img src="docs//testing/auto_tests.png" width="800">](docs/testing/auto_tests.png)

---

## 12. Bugs

### Fixed Bugs
* **Static Manifest Error:** Resolved ValueError where Whitenoise could not find the logo file by disabling strict manifest mode.
* **Import Errors:** Corrected circular imports in sitemaps.py by using application-specific models.

### Known Issues
* Manual cache clearing (Ctrl+F5) may be required after CSS updates due to aggressive browser caching.

---

## 13. Deployment

### Heroku Deployment
1. Connect GitHub repo to Heroku app.
2. Set `DEBUG = False`.
3. Add Config Vars: `DATABASE_URL`, `STRIPE_SECRET_KEY`, `CLOUDINARY_URL`, `MAILCHIMP_API_KEY`.
4. Run `python manage.py collectstatic`.

---

## 14. Credits
* **Images:** Professional photography sourced from Unsplash and Pexels.
* **Icons:** FontAwesome.
* **Logic:** Inspired by the Code Institute Boutique Ado walkthrough.

---

## 15. Conclusion
Photographer Hub is a comprehensive e-commerce solution that bridges fine art appreciation with modern service management, delivering a secure and aesthetically pleasing user experience.