# STREAM THREE FULLSTACK FRAMEWORKS FINAL PROJECT - Fileo

## FILEO

A web application prototype aimed at improving the tracking of Quotes, Purchase Orders and Invoices for small businesses.

[![Build Status](https://travis-ci.org/darchard1984/stream-three-fullstack-final-project.svg?branch=master)](https://travis-ci.org/darchard1984/stream-three-fullstack-final-project)

### The Need

The payment pattern for many businesses that provide a service is to produce a quote or tender for work, if approved by their client and dates booked for the work, a purchase order is issued to the service provider by their client, and then on completion an invoice would be generated requiring payment from the client. 

Through my own experience, and through talking to friends and colleagues about their experience. I recently identified common problems faced by small to medium sized businesses in relation to this.

The quote files, purchase order files and invoice files are more often than not sent back and forth via email. Problems that can arise from this method are summarised below:

    - In a busy inbox the files can be easily missed, resulting in delayed communication, potential loss of contract or missed payments. My company recently missed out on a £45k payment because of this.
    - It requires the management of files after downloading each attachment, organisational mistakes can be made and files lost if the individual is not computer savvy or organised.
    - Keeping track of what stage you are at with any given job or payment cycle is difficult and can often mean manually searching directories to identify where you are.
    - It can be difficult to easily establish how much money you are owed at any given time.


### The Solution

Fileo attempts to address these issues in the following ways:

    - By displaying a feed of all current payment cycles. A member can see all cycles relating to their company. A client can see of all cycles relating to projects they are involved in with that given member.
    - By making Cycles searchable and sortable. 
    - By displaying statuses of each payment clearly.
    - By allowing certain management functionality of files, clients, jobs and cycles. 
    - By creating a 'Porthole' whereby a service provider and it's client can view and upload files related to a given payment cycle without the need to email files back and forth. 
    - By sending notifications when certain actions are taken.
    - By allowing the client an easy and direct means of payment through the application. 


#### Please Note:

Fileo attempts to address these issues in a simple, visual and user friendly way. Fileo is not attempting to be accounting software, it is not supposed to replace that. Fileo is not scheduling software either. Fileo is designed to sit between these current solutions as a middle man, complimenting systems that a business may already have in place, not replace them. 

## Demo

A live demo of the application is available [here] (www.fileo.co.uk.)

The github repo is [here] (https://github.com/darchard1984/stream-three-fullstack-final-project).

## Getting Started/Deployment

Firstly, to demonstrate the workflow of the application I will outline a hypothetical use case.

Take a company that builds sets for TV and Film as an example, they are called Set Builder Co. 

    1. Set Builder Co. sign up for a members account to manage their payment cycles. 
    2. Set Builder Co. are asked to quote for "Interior Construction" for all interiors for a Film called "Coder", by the film studio Wolf.
    3. They add a client to the system (this is their contact at Wolf).
    4. The client is sent a link to fileo.co.uk to access their account.
    5. Builder Co. add a job to the system. In this case the job is "Coder". 
    6. They create a payment cycle for the job. For example, the payment cycle would be "Interior Construction" for the job "Coder".
    7. The next step is for Set Builder Co. to upload their quote to the client at Wolf.
    8. Wolf get notified via email, and can view the Quote in Fileo. Approving or contesting the offering.
    9. If approved, Wolf can then proceed to upload their promise to pay (purchase order) when ready. 
    10. Set Builder Co. get's notified. If happy that the purchase order matches the quote, they can approve. 
    11. After the works are completed Set Builder Co. upload their invoice to Fox and Wolf are notified. 
    12. Again, Wolf check the invoice matches the purchase order and approve it. 
    13. At this point, Wolf can proceed to payment and pay Set Builder Co via Stripe. 

This is the completion of one payment cycle. 

Imagine next that Wolf come back to Set Builder Co. and ask them to quote again for the same film, but now for "Exterior Construction of a City Scape". Set Builder Co. can now attach the new payment cycle to the same job ("Coder"), and to the same client ("Wolf"), and the steps repeat.

Now imagine Set Builder Co. are pitching and quoting for 100's of films a year. They are all happening at different times, and in different locations, some of which happen, some of which don't. This is where Fileo comes in. 

### Demo the application live

* To demo the application live, go ahead and create a members account and follow your own hypothetical scenario in a similar to the above. Be sure to use real email addresses for both member and client accounts as real emails will be sent to each user at different points in the process. 

###  Deploy locally

* Download the github repo and install the dependancies listed in the requirements.txt file. You will have to set your own environment variables in an env.py file including:

    - Django app secret as SECRET_KEY.
    - Email address of host email account as EMAIL_ADDRESS.
    - Email address password of host email account as EMAIL_PASSWORD.
    - Stripe publishable key as STRIPE_PUBLISHABLE.
    - Stripe secret as STRIPE_SECRET.
    - AWS access ID as AWS_ACCESS_KEY_ID. 
    - AWS secret as AWS_SECRET_ACCESS_KEY. 

You will need to provision your own AWS bucket to host static and run ./manage.py collectstatic to push them. Otherwise comment out STATICFILES_STORAGE to host locally.

You will need your own Stripe account and set the environment variables as above.

When running the application, if an external database has not been provisioned, and DATABASE_URL does not exist in env.py. The application will run in 'development' mode and create a sqlite.db for you. You will need to migrate to create your models. 

Alternatively, provision a Postgres database on a cloud platform like heroku and set the environment variable DATABASE_URL in env.py, then migrate to the external databse. 

### Deploy live

* Follow the steps above in the first instance. At the point of deployment you will need to create your own repo on a platform such as Heroku, set the Heroku environment variables as above, then push the app to Heroku.

## Built with

** VSCODE, DJANGO 1.11, VIRTUAL ENV, HTML, SCSS, JAVASCRIPT, JQUERY, STRIPE, TIPPY.JS, PYTHON 3, POSTGRES, PHOTOSHOP, BALSAMIQ

## UX Design

Details of the UX design and research process is available in the repo "documentation" folder. The documents show how I approached the design of the site using the 5 layers approach. (Strategy, Structure, Scope, Skeleton, Surface). 

## Build Approach

