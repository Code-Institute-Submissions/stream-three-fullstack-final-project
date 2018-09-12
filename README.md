# STREAM THREE FULLSTACK FRAMEWORKS PROJECT

## FILEO

A web application prototype aimed at improving the tracking of Quotes, Purchase Orders and Invoices for small businesses.

[![Build Status](https://travis-ci.org/darchard1984/stream-three-fullstack-final-project.svg?branch=master)](https://travis-ci.org/darchard1984/stream-three-fullstack-final-project)

### The Need

The payment pattern for many businesses that provide a service is relatively common. It goes a bit something like this:

    - A client contacts a service provider and asks them to produce a quote or tender for some work. 
    - The client is sent the quote, and if approved a purchase order is issued to the service provider, promising to pay them for their services upon completion of work.
    -  After which, an invoice would be generated requiring payment from the client. 

Through my own experience, and through talking to friends and colleagues about their experience. I have identified common problems in relation to aspects of this workflow.

The quote, purchase order and invoice are more often than not sent back and forth via email as PDF files. Some problems arising from this method are summarised below:

    - In a busy inbox the files can be easily missed, resulting in delayed communication, potential loss of contract or missed payments.
    - It requires the management of files after downloading each attachment, organisational mistakes can be made and files lost.
    - Keeping track of the stage you are at with any given job or payment cycle becomes difficult as multiple projects build up. It can often mean manually searching directories to identify where you are.
    - It can be difficult to easily establish how much money you are owed at any given time.
    - You have to rely on your personnel to be organised in their file management. 

### The Solution

Fileo attempts to address these issues in the following ways:

    - By displaying a feed of all current payment cycles.
    - By making this feed searchable and sortable. 
    - By displaying statuses of each payment cycle clearly in this feed.
    - By giving a user the ability to manage files, clients, jobs and cycles in one place. 
    - By creating a 'Porthole' whereby a service provider and their client can view and upload files related to a given payment cycle without the need to email files back and forth. 
    - By sending notifications when certain actions are taken.
    - By allowing the client an easy and direct means of payment through the application. 

#### Please Note:

Fileo attempts to address these issues in a simple, visual and user friendly way. Fileo is not attempting to be accounting software, it is not supposed to replace that. Fileo is not scheduling software either. Fileo is designed to sit between these current solutions as a middle man, complimenting systems that a business may already have in place, not replace them. 

## Demo

A live demo of the application is available at www.fileo.co.uk.

The github repo is here https://github.com/darchard1984/stream-three-fullstack-final-project.

## Getting Started/Deployment

Firstly, to demonstrate the workflow of the application I will outline a hypothetical use case.

Take a company that builds sets for TV and Film as an example, they are called Set Builder Co. 

    1. Set Builder Co. have a Fileo members account to manage their payment cycles. 
    2. Set Builder Co. are asked to quote for "Interior Construction" for all interior set builds for a Film called "Coder", by a film studio called Wolf.
    3. They add a _client_ to the system (this is their contact at Wolf).
    4. The _client_ is sent a link to fileo.co.uk to access their account.
    5. Builder Co. add a _job_ to the system. In this case the _job_ is called "Coder". 
    6. They create a payment _cycle_ for the _job_. For example, the payment _cycle_ would be "Interior Construction" for the _job_ "Coder".
    7. The next step is for Set Builder Co. to upload their quote to the _client_ at Wolf.
    8. Wolf get notified via email, and can view the Quote in Fileo. Approving or contesting the offering.
    9. If approved, Wolf can then proceed to upload their promise to pay (purchase order) when ready. 
    10. Set Builder Co. get's notified. If happy that the purchase order matches the quote, they can approve. 
    11. After the works are completed Set Builder Co. upload their invoice to Fox and the _client_ at Wolf is notified. 
    12. Wolf check the invoice matches the purchase order and approve it. 
    13. At this point, Wolf can proceed to payment and pay Set Builder Co. via Stripe, within Fileo. 

This is the completion of one payment _cycle_. 

Imagine next that Wolf come back to Set Builder Co. and ask them to quote again for the same film, but now for "Exterior Construction of a City Scape". Set Builder Co. can now attach the new payment _cycle_ to the same job ("Coder"), and to the same client ("Wolf"), and the file management steps repeat.
All happening at different times, in different locations, some of which happen, some of which don't. This is where Fileo comes in. 

### Demo the application live

* To demo the application live, go ahead and create a members account and follow your own hypothetical scenario in a similar manner to the above. Be sure to use real email addresses for both member and client accounts as real emails will be sent to each user at different points in the process. 

###  Deploy locally

* Download the github repo and install the dependancies listed in the requirements.txt file. You will have to set your own environment variables in an env.py file including:

    - Django app secret as SECRET_KEY.
    - Email address of host email account as EMAIL_ADDRESS.
    - Email address password of host email account as EMAIL_PASSWORD.
    - Stripe publishable key as STRIPE_PUBLISHABLE.
    - Stripe secret as STRIPE_SECRET.
    - AWS access ID as AWS_ACCESS_KEY_ID. 
    - AWS secret as AWS_SECRET_ACCESS_KEY. 

You will need to provision your own AWS bucket to host static and run ./manage.py collectstatic to push your files. Otherwise comment out STATICFILES_STORAGE to host static locally.

You will need your own Stripe account and set the environment variables as above.

When running the application, if an external database has not been provisioned, and DATABASE_URL does not exist in env.py. The application will run in 'development' mode and Django will create a sqlite.db file for you. You will need to migrate to create your models. 

Alternatively, provision a Postgres database on a cloud platform such as Heroku. Set the environment variable DATABASE_URL in env.py, then migrate models to the external database. 

### Deploy live

* Follow the steps above in the first instance. At the point of deployment you will need to create your own repo on a platform such as Heroku, set the Heroku environment variables as above, then push the app to Heroku.

## Built with

* VSCODE, DJANGO 1.11, VIRTUAL ENV, HTML, SASS/SCSS, JAVASCRIPT, JQUERY, STRIPE, TIPPY.JS, PYTHON 3, AMAZON AWS, S3, POSTGRES, HEROKU, PHOTOSHOP, BALSAMIQ.

## UX Design

Details of the UX design and research process are available in the repo "documentation" folder. The documents show how I approached the design of the site using the 5 layers approach. (Strategy, Structure, Scope, Skeleton, Surface). 

## Build Approach

1. I built the application using VSCODE and Django 1.11 in a local Virtual Environment.
2. I began by considering my Database Schema and mapped out my models to get a better understanding of the data structure of the application. 
3. I built the application app by app. Firstly, creating the model, any form related to that model and a view rendering a basic template. I tested the models using unit tests and also by manually testing them in the admin panel. If the app uses a form I'd test the form using unit tests, and/or manually by rendering the form in the template and passing form data to and from the model from the template.
4. Once happy that all apps, models, forms and signals were behaving as intended, I proceeded to work on the front-end.
5. The application utilises two types of user. Member and client. The user types are presented with different representations of certain templates to control the application flow and limit functionality to clients. I achieved this by using template logic.
6. I used SASS/SCSS to style Fileo. I tried to keep re-useable styles modular by using mixins and variables, making it easier to maintain consistent styles throughout the application. I also created separate stylesheets for each template to keep things organised, then imported each modular sheet into a master main.scss file. 
7. All styles are custom, no framework was used.
8. I split my JS into multiple files, generally one file per template, with all re-usable functions available to each modular JS file in a utility.js file. 
9. Payments are taken using Stripe.
10. I used http://pleeease.io/play/ to generate vendor prefixes once the building of the application was complete. This allowed me to concentrate on writing clean SCSS until ready for deployment.

## Testing

Automated, manual and technical testing of the site was undertaken and passed. 

1. Django Unit Tests were used as I built the logic of the application.
2. Chrome/Firefox/Safari/Opera dev tools were used throughout front-end developement to test JS, responsiveness and function.
3. I tested the site across different devices in real world scenarios. Mobiles, Tablets, Laptops, and Desktops etc..
4. I asked third party users to use the application to gather feedback and make alterations to the UI.
5. I used W3C code validator to pass HTML, CSS and JS. 

## Authors

** Dafydd Archard ** this application was created as part of Code Institute's Web Development Online Full-Stack Course in September 2018.

1. http://pleeease.io/play/
2. w3c Validator service
3. Stack Overflow
4. Font Awesome
5. Google Fonts
6. Tippy.js