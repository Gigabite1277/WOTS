![W.O.T.S Logo](https://github.com/Gigabite1277/WOTS/blob/main/assets/images/wotsbanner.png "Logo Title Text 1")

WOTS (Word On The Street) is a new/blog site.  The aim of WOTS is to give it's users up to date information on "Wots" happening in their local area.  The site will feature a number of articles that can be commented on by readers and voted up or down on accordingly.

## Strategy
The strategy of this project is to answer what our users "The Community" want and need and nothing less.  So, using Agile project princibles is one of the best ways to acheive this.  Our strategy is to answer to the User Stories throughout the production process until all the user stories have been fufilled and in turn the goals of the project. Doing so makes the entire blog site productive in both informing it's users of everything happening in the communtiy/area whilst also able to get good feedback via comments (conversations), the and the voting system for comments made.




## Project Goals ####(Site Superviser?Admin)
The aim of WOTS is to give it's users up to date information on "Wots" happening in their local area.
The site will feature a number of articles that can be commented on by readers and voted up or down on accordingly. Another goal is to bring the community together through shared interests and endeavours: things such as charity events,food banks, soup kitchens etc. Point the user towards local services and advice for social,


## User Goals ####(Readers/Contributors)
To find out whats going on in the local area. Things such as charity events, good news stories, neighbouhood watch, places shopping and other such information.

To be able to comment on all news stories to promote community interaction, aulturism, innovation. Also, being able to vote on comments left will help people decide on opinions held by people in the area.
  

## User Stories ####(Readers/Contributors/Site Admin)

Story Title:
Create a User Account

User Persona:
Reader

User Story:
As a reader, I want to create a WOTS account so that I can post a comment.

Acceptance Criteria:

Scenario: User wants to comment on a story about his busness and wishes set the record straight in the comments section.

Then: User is able to create a user account. Now able to comment on the story about him he believes is incorrect.

---

Story Title:
Browse & View Articles

User Persona:
Reader

User Story:
As a reader, I want to be able to browse multiple pages of listed articles before clicking on one to read in detail.

Acceptance Criteria:

Scenario: User search for an article on local burglaries

Then: User finds articles related to burglaries

---

Story Title:
Post a Comment

User Persona:
Reader

User Story:
As a reader, I want to post a comment, regarding a local issues.

Acceptance Criteria:

Scenario: User wants to post a comment on a road traffic accident that they witnessed on their street.

Then: User has posted a comment helped with police enquiries.

---

Story Title:
Open a News Story

User Persona:
Reader

User Story: As a reader, I want to be able to click on a news article, so that I can view the story on a full sized page.

Acceptance Criteria:

Scenario: User hears about the new WOTS and goes online to take a look.

Then: User finds an interesting news article then clicks on it.

---

Story Title:
Up & Down Comment Rating

User Persona:
Reader

User Story: As a reader, I want to be able to rate a comment using the up & down arrow symbol.

Acceptance Criteria:

Scenario: User read an article and was shocked by the top comment.

Then: User was able to vote down the comment using the up or down arrow buttons.

### User Story: Site Administrator

Story Title:
Admin Dashboard

User Persona:
Admin

User Story:
As a admin, I want to use a Django Admin interface, so that to I can manage all users, categories, and articles in one place.

Acceptance Criteria:

Scenario: Site admin wants to remove some offensive comments.

Then: Site admin removed homophobic comments

---

Story Title:
Admin Publishing Control

User Persona:
Admin

User Story:
As an admin, I want to approve and publish drafts submitted by writers to ensure quality control.

Acceptance Criteria:

Scenario: The site has been contacted by a business to inform us that a story we published about them has out of date information in it.

Then: Admin pulled the old article and published a new and corrected news article.


---

Story Title:
The About App 

User Persona(s):
Reader and Site Admin

User Story (Reader):
I want to read an introduction to the blog's superuser/editor and have a way to contact them directly.

User Story(Site Supervisor)
I want describe the purpose of the blog site and be able to receive feedback from readers and article contributors.


Acceptance Criteria (Reader):

Then: Local based user comes across the site whilst browsing and is inspired to become a contributor for the benefit of the local community. The user contatcts the site supervisor by using the About form contact form.

Acceptance Criteria (Site Admin):
Then: Site Admin receives About contact form messages from a prospective story contributor.

---



#   UX UI Design

##  Surface
The wireframes and prototypes created on the skeleton plane will be used on the surface plane – the top and most concrete plane – to create the final pages for the product. At this stage, we’re concerned with the users’ sensory experience. This includes how the colours and textures employed in the visual design help them understand how to navigate through and interact with the site, and how the presentation of content draws their eye to key information.


![W.O.T.S Logo](https://github.com/Gigabite1277/WOTS/blob/main/assets/images/WOTS_Sketches_ALL.png "Logo Title Text 1")


##  Skeleton
After deciding how the product will be structured, its skeleton can be designed. This entails deciding where the navigation and functional elements from the previous plane will go on each product page. It’s here that UX designers will make decisions about the product’s information design, creating wireframes and prototypes that arrange each part of the product, including the buttons, links, images and text. These are laid out in a way that ensures that users can quickly move through each page to find the information they need, while also understanding which elements of each page are interactive and which are not.
This will help visualise each piece of functionality and content that will appear on the page and its placement.

**W.O.T.S Wireframes**

![W.O.T.S Wireframes](https://github.com/Gigabite1277/WOTS/blob/main/assets/images/wotswireframe.png "Logo Title Text 1")


##  Structure
Once the scope of the product has been outlined, it’s time to start working on the structure. This is where each element of navigation will be decided, including where in the product each page can be found and where users can go after arriving at a given page. This involves defining the interaction design and information architecture of the product.

On the interaction design side, we need to decide how users will interact with the site and how the system will respond, including what will happen if errors are made. This can be conveyed through conceptual models that explain each part of the user interface – usually in a flow chart format – that defines what users can do and how the product will react to each potential choice the user makes.

On the information architecture side, we need to structure the content the product offers in a way that makes it easy for users to find what they’re looking for. This can be conveyed through documents like site maps that outline the hierarchy and pattern of each part of the product.



W.O.T.S DATABASE ERD

### Reader Database ERD
![Reader Database ERD](https://github.com/Gigabite1277/WOTS/blob/main/assets/images/reader_erd.png "Logo Title Text 1")


### Story Database ERD
![Story Database ERD](https://github.com/Gigabite1277/WOTS/blob/main/assets/images/story_erd.png "Logo Title Text 1")


### Comments Database ERD
![Comments Database ERD](https://github.com/Gigabite1277/WOTS/blob/main/assets/images/comment_erd.png "Logo Title Text 1")


##  Scope

After deciding on the strategy, the scope of the product can be determined and laid out in detail. It’s here that all a product’s features are decided upon, including the information that users can find and the functionality that users can interact with. On this plane, the UX team will create a set of functional specifications that identifies and describes every single feature of the product and a list of content requirements that identifies every single piece of content that will be included.




**Database Schema**

![Database Design](https://github.com/Gigabite1277/WOTS/blob/main/assets/images/dbdiagram.png "Logo Title Text 1")


##  Strategy
The bottom plane of the model is Strategy. As the most abstract and least constrained part of the project, this is where decisions should be made about what objectives the product should be designed to meet. These objectives should include the goals that both the clients and stakeholders behind the product want to meet and the goals of the users, who will eventually look to the product to solve specific problems for them.


### Design Choices






#### Fonts

  Black font lettering against a white background for best visual experience for the user.

Icons


  

### Colours

The colour scheme wil be mostly purple, black and white. We found that market research indicated that these were the most politically neutral colours, that could be accepted across the whole community.


Styling


##  Screenshots of the Finished Project that met user expectations

---


---


---

---
## Scope
## Features


---
## Technologies Used

###software###
HTML, CSS, Javascript, Python

###Developement Platforms###
Git Hub (Development), Heroku (Platform as a Service (PaaS))


## Testing 
 
    


---
## Deployment
Via Heroku

* Make sure the branch (normally "Main") you want to use as your publishing source  already exists in your repository.

* On GitHub, navigate to your site's repository.

* Under your repository name, click  Settings. If you cannot see the "Settings" tab, select the  dropdown menu, then click Settings.

* In the "Code and automation" section of the sidebar, click  Pages.

* Under "Build and deployment", under "Source", select Deploy from a branch.

* Under "Build and deployment", use the branch dropdown menu and select a publishing source.

* Optionally, use the folder dropdown menu to select a folder for your publishing source.

*  Click Save.



### How To Run This Project locally

 * In windows, open up the start menu and search for Visual Studio.
 * Select and run Visual Studio.
 * Go to the menu bar on the top left of the screen and click on the top icon which is the three horizontal lines.
 * From the drop down menu go to File > Open Folder 
 * Locate the folder labled The Match or Miss and select.
 * Your Folder will be displayed in the File Explorer on the left hand side of the Visual Studio window.
 * From the files displayed in the file explorer select index.html to start broswsing or editing the site.   



---

## Testing:
PLEASE REVIEW THE LINKED DOCUMENT REGARDING TESTING, UX ETC


## IMPROVMENTS:


### Code
All code written by me.

### Media (Picture & Video):
IMAGES: Sourced from 


## Acknowledgements

---
NOTES:
SOUNDS: 
