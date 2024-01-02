# aquapulse-haven
AquaPulse Haven is a riverside destination that offers a range of activities and beautiful views for visitors. Situated by the riverbanks, this site provides opportunities for picnics, entertainment, and enjoying the scenic beauty of the river. Visitors can choose from activities such as kayaking, fishing, or having a barbecue. Our user-friendly reservation system makes it easy for you to plan your visit and enjoy a day by the river. Explore all that AquaPulse Haven has to offer and make lasting memories along the river.

# UX
## Overview

AquaPulse Haven is a fictional riverside destination brought to life through this web-based reservation system. The primary aim is to provide visitors with an enticing glimpse of the serene location, unique recreational offerings, and the ability to effortlessly plan their visits.

## Design

In crafting this platform, we've opted for a modern and minimalist design ethos, with a predominant color palette of soothing black and white tones. We deviate from this scheme only when it enhances user interactions, such as through user-friendly buttons, informative links, and streamlined booking feedback.

##  Site User

Our target audience includes:

Locals seeking exciting, new riverside experiences.
Enthusiasts of themed events and outdoor activities.
Individuals who prefer the convenience of digital reservations over traditional booking methods.
Goals for the Website


## Agile Development

This project was initiated alongside a GitHub Projects Page to facilitate the tracking and management of the expected workload. The primary goal was to outline the anticipated workload, identify epics, and subsequently break them down into user stories or manageable tasks. This systematic approach allowed for efficient progress and tracking.


Throughout the development process, I continually worked on and updated the user stories, acceptance criteria, and tasks. This dynamic approach allowed for real-time adaptation to project needs and a more agile response to evolving requirements.


Upon completing a task, I marked it as done, and if all aspects of a user story were completed, I moved it from the "In Progress" column to the "Completed" column.

This dynamic and adaptive approach ensures that I have a clear understanding of my project's status and allows for efficient management of user stories in response to evolving project needs.

## User stories

- As a customer I can create an account on AquaPulse Haven website so that I can easily book spots for various recreational activities.
- As a customer I can update my profile information and relevant details so that I can keep my profile up-to-date with current information.
- As a customer I can cancel my reservation so that I have the flexibility to change my plans if needed.
- As a customer of River Picnic Adventure I can able to make a reservation so that I can secure a spot for a riverside picnic experience.
- As a customer I can learn about the various services and offerings provided by Riverside Picnic Adventure so that I can make informed decisions about planning a riverside picnic.
- As a developer I can deploy the project to Heroku early so that to ensure a smooth submission process.
- As a developer I can perform website testing so that the final product is error-free and ready for a successful launch.

# Features
## Navigation Link 
The AquaPulse Haven website boasts a navigation menu to ensure a seamless and user-centric experience. Below are the key navigation elements designed to facilitate efficient access to various sections of the site:

 - **Home**: Clicking on "Home" instantly transports users to the main hub of our website, offering an inviting starting point for exploring the offerings.

 - **Reservations**: The "Reservations" link provides a direct path to the booking platform, simplifying the reservation process and enhancing user convenience.

 - **Profile**: Access a personalized profile through the "Profile" link to manage preferences and reservation information within the dashboard.


 - **Sign Up**: Newcomers can easily join AquaPulse Haven by clicking on "Sign Up" to initiate their journey.

 - **Log In**: Existing members can securely log in to their accounts via the "Log In" option, ensuring a smooth continuation of their AquaPulse Haven experience.

 - **Logo**: The AquaPulse Haven logo, placed on the left side of the  navigation menu. Clicking the logo at any point during the user's journey will swiftly return them to the homepage, maintaining a consistent and user-friendly browsing experience.

 - **Log Out**: When you're ready to conclude your session, simply log out by clicking on "Log Out" to ensure the security of your account.



### About Us

The project features an "About Us" section dedicated to providing insights into the services and offerings. This section is designed to offer transparency and establish a connection with users by sharing relevant information about the services provided.

### Image for the River Side Picnic

A notable feature of the project is the inclusion of captivating images showcasing the serene riverside picnic spots. These images are intended to create an immersive experience for users, offering a visual glimpse of the scenic beauty available at AquaPulse Haven.

### Footer

The project incorporates a well-structured footer that provides essential information. In the footer, users can find links to social media profiles, contact details, and other relevant resources. The footer is designed to enhance the overall user experience and improve site accessibility.

## Reservation Form (Booking and User Details)

The Reservation Form is designed for booking and capturing user details.

# Tools & Technologies Used

HTML: Utilized for creating the main site content, ensuring a structured and semantic layout.

CSS: Employed for crafting the main site design and layout, enhancing the visual presentation.

JavaScript: Empowered user interaction on the site, enhancing user engagement and functionality.

Python: Serves as the backend programming language, enabling server-side functionality.

Django: Utilized as the Python framework to construct and manage the site's backend logic.

PostgreSQL and ElephantSQL: Employed for relational database management, ensuring data integrity and efficiency.

Heroku: Chosen as the hosting platform for the deployed backend site, ensuring reliability and scalability.

Git: Employed for efficient version control, including operations like "git add," "git commit," and "git push."

GitHub: Utilized for secure online code storage, facilitating collaboration and code management.

Gitpod: Served as the cloud-based Integrated Development Environment (IDE) for streamlined development processes.


CSS Flexbox and CSS Grid: Employed to create an advanced responsive layout, ensuring optimal adaptability across various devices.

Gunicorn: Employed as a server provider to serve the site efficiently and reliably.

Psycopg2: Utilized as the PostgreSQL database adapter, facilitating seamless communication between the application and the database.

# Testing

### Account Registration Tests

| Test                                   | Result |
|----------------------------------------|---------|
| User can create account                | Pass  |
| User can successfully log in           | Pass  |
| User can log out successfully          | Pass  |

### User Navigation Tests

| Test                                       | Result |
|--------------------------------------------|---------|
| User successfully navigates to Reservations | Pass |
| User accesses the account profile page      | Pass  |
| SuperUser successfully accesses admin panel | Pass  |

### Security Verification Tests for User Accounts

| Test                                              | Result |
|---------------------------------------------------|---------|
| Non-logged-in user can make a reservation          | Pass    |
| Non-logged-in user can access the profile page     | Pass    |
| Non-superuser can access the admin panel           | Pass    |

### Reservation Tests

| Reservation Functionality            | Test Description                                             | Outcome |
|--------------------------------------|-------------------------------------------------------------|---------|
| **Reservation Creation**             | User successfully makes a reservation with all fields completed | Pass    |
| **Form Submission Handling**         | User can not  submit a reservation with an empty form       | pass   |
|                                      | User can not submit a form without an email address        | pass    |
| **Visibility and Management**        | User can view their  reservations from their profile      | Pass    |
| **Reservation updating**             | User can update a reservation                                   | Pass    |
| **Reservation Deletion**             | User can delete a pending reservation                          | Pass    |

