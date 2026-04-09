# Photographer Hub

**Photographer Hub** is a professional full-stack e-commerce application built with Python (Django), designed to provide a "Fine Art" digital marketplace for photography enthusiasts and a booking management system for exclusive photoshoot sessions. The platform operates on a B2C (Business to Consumer) business model, selling high-resolution digital art licenses and professional photography services directly to clients.

<img src="docs/screenshots/hero.png" width="800">

The application is deployed to Heroku and can be accessed at:
* **[Link to Live Site](https://photographer-hub-94aeeeedb69e.herokuapp.com/)**
* **[Link to GitHub Repository](https://github.com/your-username/photographer_hub)** ---

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

## 2. Agile Methodology

The development of **Photographer Hub** followed an Agile workflow, utilizing **GitHub Projects** to manage a Kanban board and prioritize tasks using the **MoSCoW method**. This ensured a structured development process where core e-commerce features were delivered first, followed by specialized booking services and final quality assurance.

### User Stories
The following User Stories, each with specific Acceptance Criteria, formed the basis of the development process:

#### Visitor Stories
* **#1 View Homepage:** As a visitor, I want to view a clear homepage so that I immediately understand the purpose of the site.
* **#2 Navigate Website:** As a visitor, I want a consistent main menu so that I can access all sections easily.
* **#7 Browse Products:** As a visitor, I want to browse photo products with pricing so that I can decide what to buy.
* **#8 View Product Details:** As a visitor, I want to see detailed product information and a preview image so that I understand what I am purchasing.
* **#12 View Sessions:** As a visitor, I want to see upcoming photo sessions so that I can choose one to join.
* **#13 View Session Details:** As a visitor, I want to view session themes and descriptions to understand the creative concept.
* **#18 Contact & Marketing:** As a visitor, I want to send a message through a contact form so that I can ask specific questions.
* **#3 View 404 Page:** As a visitor, I want to see a custom branded 404 page if I access a non-existing URL to return safely to the home page.

#### Customer Stories
* **#4 Register Account:** As a visitor, I want to register an account so that I can purchase photos and manage my bookings.
* **#5 Login / Logout:** As a registered user, I want to log in and out securely to protect my data and purchases.
* **#9 Add to Cart:** As a user, I want to add products or session deposits to a cart to purchase multiple items at once.
* **#10 Checkout with Stripe:** As a user, I want to pay securely using Stripe to complete my purchase.
* **#16 Express Interest:** As a user, I want to register interest in a new session to help the photographer plan upcoming sets.
* **#17 Pay Deposit:** As a user, I want to pay a small deposit for pre-registration to confirm my intent to participate.
* **#11 Access Purchased Photos:** As a logged-in user, I want to access my purchased photos in a private library anytime.
* **#14 Book a Slot (Future):** As a user, I want to reserve a specific time slot (Should Have/Backlog).
* **#15 Cancel Booking:** As a user, I want to cancel my interest/booking to free up space if my plans change.

#### Admin (Site Owner) Stories
* **#6 Role-Based Access:** As a site owner, I want admin-only access to management tools to protect the integrity of the gallery and session data.
* **#CRUD Management:** As an admin, I want to Create, Read, Update, and Delete products and sessions directly from a frontend dashboard.

### Kanban Board & MoSCoW Prioritization
The project utilized the **MoSCoW method** to ensure the most critical business value was delivered within the timeframe:

* **Must Have:** Secure authentication, Stripe integration, and core Product CRUD functionality.
* **Should Have:** Session interest forms, deposit payments, and user profile management.
* **Could Have:** Automated slot management, newsletter integration, and advanced SEO tools.

### Project Milestones
The development was organized into five distinct milestones, as reflected in the project management board:

1. **Milestone 1: Products + Stripe Checkout** (#1, #2, #3, #4, #5, #7, #8, #10) - Core storefront and payment foundation.
2. **Milestone 2: Sessions + Slots + Booking** (#9, #11, #12, #13, #14, #15) - Service listings and post-purchase content access.
3. **Milestone 3: Pre-registration + Deposit** (#16, #17) - Gauging user interest and securing commitments for upcoming events.
4. **Milestone 4: Marketing + SEO** (#18, #19, #20) - Brand reach through Facebook Business integration and Search Engine Optimization.
5. **Milestone 5: QA, Testing, Polish, Documentation** (#22, #25, #26, #27, #28, #29) - Final verification of code integrity, security audits, and deployment.

### GitHub Projects Board Overview
<img src="docs/screenshots/kanban_1.png" width="800">
<img src="docs/screenshots/kanban_2.png" width="800">

*Figure: Snapshots of the GitHub Projects board showing issue tracking and milestone distribution.*

## Future Implementations

### **Automated Capacity Management (#14)**
While the current system allows interest registration and deposit payments, it does not strictly enforce a maximum number of participants per session in real-time. 
* **Planned:** Implementation of a `max_capacity` field in the `Photoshoot` model and a calendar view for specific date selection.
* **Target Status:** Backlog for Milestone 5.

### **Persistent Message Storage (#18)**
Currently, the contact form provides immediate feedback to the user.
* **Planned:** Creation of a `ContactMessage` model to store all inquiries in the database for the photographer to review in the dashboard.

---

## 3. Design

The design of **Photographer Hub** is rooted in a "Fine Art" aesthetic, emphasizing minimalism, sophisticated proportions, and a serene atmosphere that complements high-end photography without over-powering it.

### **Colours**

The project uses a muted, earthy colour palette to evoke a sense of professional artistry and calm. Instead of high-contrast vibrant tones, the site relies on soft ivories, sages, and blush tones to create a premium gallery feel.

<img src="docs/screenshots/color_palette.png" width="600" alt="Photographer Hub Color Palette">

*Figure: The unified colour palette extracted from Adobe Color.*

| Variable | Hex Code | Name | Primary Usage |
|:---|:---:|:---|:---|
| `--bg-color` | `#F8F5F2` | **Warm Ivory** | Primary site background for a soft, premium feel. |
| `--primary-color` | `#A8BBA3` | **Muted Sage** | Main brand colour, buttons, and navigation links. |
| `--hover-color` | `#D6A5A1` | **Dusty Rose** | Interaction states, cart badges, and error highlights. |
| `--accent-soft` | `#E8CFCB` | **Soft Blush** | Decorative accents (e.g., the oval avatar border). |
| `--text-color` | `#3A3A3A` | **Charcoal** | Primary body and heading text for high readability. |
| `--border-color` | `#E9E1DC` | **Taupe** | Subtle dividers, card borders, and input outlines. |

### **Typography**

The typography is a strategic pairing of Serif and Sans-Serif fonts, balancing classic editorial elegance with modern functional clarity.

* **Primary Font (Headings):** **'Playfair Display'** (Serif). 
    * Applied to all `h1`, `h2`, `h3`, and special `.serif-title` elements. 
    * The high-contrast serif style provides a high-end, artistic feel typical of fine art publications.
* **Secondary Font (Body Content):** **'Montserrat'** (Sans-Serif). 
    * The primary font for general site content, descriptions, and UI labels. 
    * Chosen for its geometric clarity and excellent readability across all devices.
* **UI & Form Font:** **'Inter'** (Sans-Serif). 
    * Specifically used for form inputs and textareas. 
    * Provides a clean, neutral, and highly functional interface for user data entry tasks.

### **Enhanced Interaction (JavaScript)**

To elevate the user experience beyond static HTML/CSS, several custom JavaScript modules were implemented to provide a dynamic and responsive interface:

* **Defensive Programming (Custom Modals):** * A bespoke deletion modal was created to replace standard browser alerts. 
    * It handles all **CRUD confirmation requests** (Cart and Dashboard) to ensure a consistent brand look and prevent accidental data loss.
* **Dynamic Feedback (Toast Notifications):** * Real-time feedback for user actions, such as adding items to the cart or successful login/logout.
    * These custom-styled Toasts provide non-intrusive alerts that automatically hide after **5 seconds**.
* **Immersive Viewing (GLightbox):** * The **GLightbox** library is integrated to showcase photography in its best possible light. 
    * This allows users to view high-resolution versions of digital art in a responsive, touch-friendly lightbox with zoom capabilities.

---

# 4. Structure

## Website Pages
The application is structured to provide a seamless transition between public content and private user areas. The following table outlines the primary pages, their purpose, and the logic governing their access.

| Page | Description | Desktop | Tablet | Mobile |
|:---|:---|:---:|:---:|:---:|
| **Home** | Hero section with photographer bio, featured products scroller, and upcoming sessions. | ![<img src="docs/screenshots/home_1.png" width="300">](docs/screenshots/home_1.png) ![<img src="docs/screenshots/home_2.png" width="300">](docs/screenshots/home_2.png) ![<img src="docs/screenshots/home_3.png" width="300">](docs/screenshots/home_3.png)| ![<img src="docs/screenshots/home-t_1.png" width="400">](docs/screenshots/home-t_1.png) ![<img src="docs/screenshots/home-t_2.png" width="400">](docs/screenshots/home-t_2.png) ![<img src="docs/screenshots/home-t_3.png" width="400">](docs/screenshots/home-t_3.png)| ![<img src="docs/screenshots/home-m_1.png" width="400">](docs/screenshots/home-m_1.png) ![<img src="docs/screenshots/home-m_2.png" width="400">](docs/screenshots/home-m_2.png) ![<img src="docs/screenshots/home-m_3.png" width="400">](docs/screenshots/home-m_3.png) ![<img src="docs/screenshots/home-m_4.png" width="400">](docs/screenshots/home-m_4.png)|
| **Shop Gallery** | A grid of all active digital photo products with ownership-aware "Add to Cart" logic. | ![<img src="docs/screenshots/shop_1.png" width="300">](docs/screenshots/shop_1.png) ![<img src="docs/screenshots/shop_2.png" width="300">](docs/screenshots/shop_2.png)| ![<img src="docs/screenshots/shop-t_1.png" width="300">](docs/screenshots/shop-t_1.png) ![<img src="docs/screenshots/shop-t_2.png" width="300">](docs/screenshots/shop-t_2.png)| ![<img src="docs/screenshots/shop-m_1.png" width="300">](docs/screenshots/shop-m_1.png) ![<img src="docs/screenshots/shop-m_2.png" width="300">](docs/screenshots/shop-m_2.png) ![<img src="docs/screenshots/shop-m_3.png" width="300">](docs/screenshots/shop-m_3.png) |
| **Session Details** | Detailed concept description, expected dates, and deposit payment for photoshoots. | ![<img src="docs/screenshots/detail.png" width="300">](docs/screenshots/detail.png) | ![<img src="docs/screenshots/detail-t.png" width="300">](docs/screenshots/detail-t.png) | ![<img src="docs/screenshots/detail-m_1.png" width="300">](docs/screenshots/detail-m_1.png) ![<img src="docs/screenshots/detail-m_2.png" width="300">](docs/screenshots/detail-m_2.png)|
| **Shopping Cart** | Overview of selected items with session-based quantity adjustment for sessions. | ![<img src="docs/screenshots/cart.png" width="300">](docs/screenshots/cart.png) | ![<img src="docs/screenshots/cart-t_1.png" width="300">](docs/screenshots/cart-t_1.png) ![<img src="docs/screenshots/cart-t_2.png" width="300">](docs/screenshots/cart-t_2.png) | ![<img src="docs/screenshots/cart-m_1.png" width="300">](docs/screenshots/cart-m_1.png) ![<img src="docs/screenshots/cart-m_2.png" width="300">](docs/screenshots/cart-m_2.png)|
| **User Profile** | Personal dashboard showing the digital library of purchased photos and active bookings. | ![<img src="docs/screenshots/profile_1.png" width="300">](docs/screenshots/profile_1.png) ![<img src="docs/screenshots/profile_2.png" width="300">](docs/screenshots/profile_2.png)| ![<img src="docs/screenshots/profile-t_1.png" width="300">](docs/screenshots/profile-t_1.png) ![<img src="docs/screenshots/profile-t_2.png" width="300">](docs/screenshots/profile-t_2.png)| ![<img src="docs/screenshots/profile-m_1.png" width="300">](docs/screenshots/profile-m_1.png) ![<img src="docs/screenshots/profile-m_2.png" width="300">](docs/screenshots/profile-m_2.png) |
| **Admin Dashboard** | Central management hub for the photographer to perform full CRUD on products and sessions. | ![<img src="docs/screenshots/dash_1.png" width="300">](docs/screenshots/dash_1.png) ![<img src="docs/screenshots/dash_2.png" width="300">](docs/screenshots/dash_2.png)| ![<img src="docs/screenshots/dash-t_1.png" width="300">](docs/screenshots/dash-t_1.png) ![<img src="docs/screenshots/dash-t_2.png" width="300">](docs/screenshots/dash-t_2.png) ![<img src="docs/screenshots/dash-t_3.png" width="300">](docs/screenshots/dash-t_3.png)| ![<img src="docs/screenshots/dash-m_1.png" width="300">](docs/screenshots/dash-m_1.png) ![<img src="docs/screenshots/dash-m_2.png" width="300">](docs/screenshots/dash-m_2.png)| ![<img src="docs/screenshots/dash-m_3.png" width="300">](docs/screenshots/dash-m_3.png)|

## Database Design

### Logical Schema (ERD)
The following diagram illustrates the relational structure of the database. The system relies on a central **User** model connected to specific profiles, orders, and ownership records to ensure high data integrity.

<img src="docs/screenshots/models.png" width="600" alt="Models">

**Data Modeling Architecture**
- User & UserProfile: Utilizes a One-to-One relationship to extend the base Django User. It includes an is_photographer flag which acts as the gatekeeper for administrative frontend CRUD operations.
- Order & Stripe Integration: The Order model serves as the transaction header. Metadata passed to Stripe ensures that upon a successful webhook signal, the system knows exactly which PurchasedPhoto or Booking records to create.
- Defensive Deletion (Protected Records): The relationship between PhotoProduct and PurchasedPhoto uses models.PROTECT. This prevents the photographer from deleting a file that a customer has already paid for, automatically triggering a "deactivation" instead of a hard delete.
- Session Management: The Cart is stored in the Django Session, allowing users to build an order without immediate database writes, optimizing performance and reducing database clutter from abandoned carts.

---

## 5. Technologies Used
* **Languages:** HTML5, CSS3, JavaScript, Python.
* **Framework:** Django (5.2).
* **Database:** PostgreSQL.
* **Payments:** Stripe API.
* **Media Storage:** Cloudinary.
* **Email/Newsletter:** MailChimp.

---

---

## 6. Marketing Strategy

To ensure a steady flow of clients and brand recognition, the platform employs a strategic marketing approach focusing on visual storytelling and community engagement.

### Social Media Marketing

Facebook is the cornerstone of the project's social media presence. It is chosen for its strong community features and its popularity among the target audience (families, couples, and wedding planners). 

#### Conceptual Design & Prototyping
The visual identity on social media was prototyped using **Balsamiq Cloud** (based on the Code Institute mockup template). This ensured that the photographer's brand message is delivered clearly through a cohesive layout.

* **Visual Consistency:** The profile uses a signature "camera-in-hand" avatar to establish a professional yet personal connection.
* **Clear Value Proposition:** The bio emphasizes the photographer's niche: *Specializing in lifestyle family, children, and wedding photography.*
* **Portfolio Showcasing:** Strategic use of the "Photos" grid and "Posts" allows for immediate exposure to recent works, emphasizing soft light and genuine emotive connections.

[<img src="docs/mockups/facebook_1.png" width="600">](docs/mockups/facebook_1.png)
*Figure: Facebook Page Mockup - Profile and Cover overview.*

[<img src="docs/mockups/facebook_2.png" width="600">](docs/mockups/facebook_2.png)
*Figure: Facebook Page Mockup - Post engagement and community links.*

#### Brand Message
> "I am dedicated to preserving your life's greatest milestones. Inspired by soft light and genuine connection, my goal is to create authentic, emotive, and timeless imagery that speaks to your heart for generations to come." — **Oksana Key**

---

Email Marketing (Mailchimp Integration)
To build a loyal community, the site features a built-in newsletter system integrated with the **Mailchimp API**.

* **Content Strategy:** Subscribers receive exclusive photography tips, early-bird notifications for upcoming thematic photoshoot sets, and "behind-the-scenes" insights.
* **Subscription Points:**
    1.  **Global Footer:** A minimalist AJAX-ready form available on every page.
    2.  **Registration Opt-in:** A checkbox on the Sign-Up page allowing new users to join the marketing list during account creation.
* **Implementation:** The system uses the `mailchimp3` library to synchronize user data with the Mailchimp Audience API, ensuring automated lead generation.

### Account Verification & Security (Django SMTP)
To ensure the platform's integrity and protect user data, the project implements a mandatory email verification process.

* **Process:** Upon registration, Django (via `django-allauth`) generates a unique, time-sensitive confirmation link. 
* **Access Control:** Users are restricted from accessing private dashboard features until their email address is verified, preventing bot registrations and ensuring a valid point of contact for digital photo delivery.
* **Configuration:** The system is configured with a secure SMTP backend, utilizing environment variables for credentials to ensure maximum security on the production server (Heroku).

#### Communication Implementation Proofs:

[<img src="docs/screenshots/confirm_email.png" width="600">](docs/screenshots/confirm_email.png)
*Figure: Automated transactional email sent via Gmail SMTP for account verification.*

[<img src="docs/screenshots/mailchimp.png" width="600">](docs/screenshots/mailchimp.png)
*Figure: Mailchimp Audience Dashboard showing real-time subscriber updates synchronized via API.*

#### Marketing Implementation Proofs:

[<img src="docs/screenshots/subscribe_form.png" width="600">](docs/screenshots/subscribe_form.png) <br>
*Figure: Built-in HTML5 validation for the subscription form.*

[<img src="docs/screenshots/toast_success.png" width="300">](docs/screenshots/toast_success.png)<br>
*Figure: Custom Toast notification confirming successful API synchronization.*

[<img src="docs/screenshots/mailchimp.png" width="600">](docs/screenshots/mailchimp.png)<br>
*Figure: Mailchimp Audience Dashboard showing real-time subscriber updates via API.*

---

## SEO Implementation
* **Robots.txt:** Configured to allow crawling of products while blocking admin areas.
* **Sitemap.xml:** Dynamically generated to help search engines index active products and sessions.
* **Meta Tags:** Descriptive keywords and site descriptions included in the base template.
* **Rel Attributes:** Used `rel="noopener noreferrer"` for all external links.

---

## Features

The **Photographer Hub** platform is designed with a "Fine Art" aesthetic, focusing on high-quality visual presentation and a seamless user experience across different roles (Guest, Client, and Photographer).

## Header & Footer
The navigation bar is dynamic and changes based on the user's authentication status and role.

* **Guest View:** Minimalist icons for Home, Facebook, and Login/Register. The shopping bag redirects to the login page to encourage conversion.
* **Client View:** Adds a link to "My Profile" and an active shopping cart with a real-time **badge notification** showing the number of items.
* **Photographer View:** Replaces commerce links with a **Management Dashboard** icon (gauge), giving the site owner immediate access to administrative tools.
* **Footer:** A simple, branded footer that stays out of the way of the visual content, featuring the signature: *"Made with passion for photography."*

[<img src="docs/screenshots/header_gest.png" width="300">](docs/screenshots/header_gest.png)
[<img src="docs/screenshots/header_client.png" width="300">](docs/screenshots/header_client.png)
[<img src="docs/screenshots/header_ph.png" width="300">](docs/screenshots/header_ph.png)
[<img src="docs/screenshots/footer.png" width="300">](docs/screenshots/footer.png)

## Home Page
The landing page serves as an immersive portfolio and sales funnel:
* **Hero Section:** A centered biography of the photographer featuring a signature **oval-style avatar**, professional tagline, and mission statement.
* **Photoshoot Scroller:** A "Limited Offers" section with a custom JavaScript-powered horizontal scroller. Users can browse upcoming themes with smooth navigation arrows.
* **Featured Shop:** Automatically displays the latest 4 digital photo products, utilizing the reusable product card component.
* **Newsletter:** A "Join the Journey" section with a Mailchimp-integrated form to capture leads and notify users of new drops or sessions.

[<img src="docs/screenshots/home_1.png" width="300">](docs/screenshots/home_1.png)
[<img src="docs/screenshots/home_2.png" width="300">](docs/screenshots/home_2.png)
[<img src="docs/screenshots/home_3.png" width="300">](docs/screenshots/home_3.png)

## Authentication (Registration & Login)
Powered by **Django Allauth**, the system provides a secure and branded experience.
* **Registration:** A clean form that includes a pre-checked marketing consent for the newsletter.
* **Login:** Features a "Remember Me" option and intuitive redirects back to the user's previous page (e.g., the Cart).

[<img src="docs/screenshots/sign_in.png" width="300">](docs/screenshots/sign_in.png)
[<img src="docs/screenshots/sign_up.png" width="300">](docs/screenshots/sign_up.png)

## Digital Card (Shop Gallery)
The **Product Card** is the most complex UI component, featuring extensive "Defensive Logic" to prevent invalid actions:

* **Defensive States:**
    1.  **Guest:** Displays "Login to Buy".
    2.  **Photographer:** Shows "Management Mode" (Disabled) to prevent self-purchasing and preserve data integrity.
    3.  **In Cart:** If the item is already selected, the button turns into a disabled "In Cart ✓" to prevent duplicate licenses.
    4.  **Already Owned:** If the user previously purchased the photo, the card identifies the record and shows "Already Owned," protecting the user from redundant costs.
* **Visual Interaction:** Features a "Full View" overlay that triggers the **GLightbox** for a high-resolution, watermarked preview of the art.

[<img src="docs/screenshots/card_guest.png" width="200">](docs/screenshots/card_guest.png)
[<img src="docs/screenshots/card_client.png" width="200">](docs/screenshots/card_client.png)
[<img src="docs/screenshots/card_cart.png" width="200">](docs/screenshots/card_cart.png)
[<img src="docs/screenshots/card_owned.png" width="200">](docs/screenshots/card_owned.png)
[<img src="docs/screenshots/card_phot.png" width="200">](docs/screenshots/card_phot.png)

## Photoshoot Booking Selection
A specialized detail view for service offerings. Users can view the concept description, check the **Expected Dates**, and pay a **Waitlist Deposit** to secure their interest. The UI clearly highlights the deposit vs. the full value for total transparency.

[<img src="docs/screenshots/photoshoot_guest.png" width="300">](docs/screenshots/photoshoot_guest.png)
[<img src="docs/screenshots/photoshoot_client.png" width="300">](docs/screenshots/photoshoot_client.png)
[<img src="docs/screenshots/photoshoot_phot.png" width="300">](docs/screenshots/photoshoot_phot.png)

## Client Dashboard ("My Profile")
A private hub for customers to manage their digital assets and services:
* **Purchase Library:** Displays all owned digital licenses with direct "Download High-Res" buttons linking to the protected digital files.
* **Booking History:** A table-based overview of active photoshoot registrations, showing expected dates and payment status.

[<img src="docs/screenshots/profile_1.png" width="300">](docs/screenshots/profile_1.png)
[<img src="docs/screenshots/profile_2.png" width="300">](docs/screenshots/profile_2.png)

## Photographer Management Dashboard
An administrative command center with table-based views for all site content.
* **Session Management:** Monitor all upcoming photoshoots, their status (Active/Draft), and deposit pricing.
* **Shop Management:** Track and edit prices, status, and details of all gallery photos.

[<img src="docs/screenshots/dash_1.png" width="300">](docs/screenshots/dash_1.png)
[<img src="docs/screenshots/dash_2.png" width="300">](docs/screenshots/dash_2.png)

## Gallery & Session CRUD Management
The photographer has full control over the site via custom frontend forms:
* **Create/Edit Photoshoots:** Manage session images, themes, and dates.
* **Add/Update Photos:** Separate upload fields for **Preview Images** (optimized for web) and **High-Resolution Files** (for customer delivery).
* **Soft Deletion Logic:** If a photo has already been purchased, the system intelligently deactivates it (hides it from the shop) instead of deleting it, ensuring existing customers never lose access to their purchases.

[<img src="docs/screenshots/photoshoot_create.png" width="250">](docs/screenshots/photoshoot_create.png)
[<img src="docs/screenshots/photo_create.png" width="250">](docs/screenshots/photo_create.png)
[<img src="docs/screenshots/photoshoot_table.png" width="250">](docs/screenshots/photoshoot_table.png)
[<img src="docs/screenshots/photo_table.png" width="250">](docs/screenshots/photo_table.png)

## Toast Notifications
To ensure immediate user feedback, the site implements custom-styled **Toast Notifications**. These alerts are color-coded (Sage for success, Dusty Rose for errors) and feature a JavaScript auto-hide logic (5 seconds) with a manual close override.

[<img src="docs/screenshots/toast.png" width="300">](docs/screenshots/toast.png)

## Custom Error Pages (404 & 500)
To maintain the "Fine Art" aesthetic even during unexpected navigation errors, branded **404 (Not Found)** and **500 (Server Error)** pages were implemented. These pages provide clear feedback and a "Return Home" path, preventing user frustration through a professional design.

[<img src="docs/screenshots/404.png" width="500">](docs/screenshots/404.png)

---

## Features Overview

The platform is built around a robust set of features categorized by their business value using the MoSCoW method.

| Feature Area | Description | Implementation Detail |
| :--- | :--- | :--- |
| **E-Commerce** | Secure digital transactions. | Integrated **Stripe API** for card payments with webhook-based fulfillment. |
| **RBAC System** | Role-Based Access Control. | Custom logic within `UserProfile` model and `user_passes_test` decorators. |
| **CRUD Management** | Content administration. | Full frontend management of `PhotoProducts` and `Photoshoots` without Django Admin access. |
| **Defensive Design** | Prevention of invalid actions. | Logic to disable "Add to Cart" for owned items or restrict quantities for digital licenses. |
| **Cloud Services** | Media and File handling. | **Cloudinary** for image optimization and Django **FileField** for secure high-res digital downloads. |
| **Interaction** | Modern web experience. | Custom **Toast Notifications**, **GLightbox** for art viewing, and **Confirmation Modals**. |

---

## Validation

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