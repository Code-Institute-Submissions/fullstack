# [Fullstack](https://mk-fullstack.herokuapp.com/) | developed by Minesh Kothari

<br />
<br />

## Overview

### About Fullstack

Fullstack is an online hub bringing together web developers of all skillset and backgrounds whether they're a newbie, a hobbyist or a veteran.

The website allows you to share knowledge through the Forum, learn how to code with our extensive Courses and becoming inspired reading through the Blogs.

### What is it for?



### Who is it targeted at?



<br />
<br />

## User Experience

<br />
<br />

## Features

### Features Implemented

Homepage
1. Act as a launchpad to the:
	- About page
	- Courses App
	- Blog App
	- Forum App
2. Personalised message if user logged in & link to 'My Profile'
3. Three featured Languages to choose from the homepage
4. Latest Blog Post on homepage

Courses App
1. View available languages and courses
2. Add a course to the Cart
3. View course (requires purchase)
4. Allow Admin to add a new Language
5. Allow Admin to add a new Module (Course) 

Cart App
1. Proceed to checkout with cart item(s)
2. Continue shopping
3. Remove item(s) from cart
4. Informative message if cart empty

Checkout App
1. Purchase item(s) in cart session
2. Informative message if cart empty

Blog App
1. View all posts
2. View 'Top' posts
3. Comment on blog with Disqus API
4. Allow Admin to add a new blog post
5. Allow Admin to edit existing blog post

Forum App (Polls)
1. View forum subjects
2. View threads in each subject
3. Start a new Thread
4. View existing threads
5. Comment/reply on thread
6. Prompt user to register/login in order to contribute on thread
7. Edit post
8. Delete post

Account App (& Admin)
1. Registration - Allowing users to register
2. Login - Allowing users to login using their registered details
3. Password Reset - Allowing users to reset their forgotten password
4. Profile:
	- Allowing users to manage their profile
	- Allowing users to view their purchased courses
	- Allowing Admin to add a new Language
	- Allowing Admin to add a new Module (Course)


### Features yet to be implemented

<br />
<br />

## Technologies Implemented

- HTML5

- CSS

- JavaScript

<br />
<br />

## Contributing


**Prerequisites:**
```
This portfolio has no prerequisites
```

### Forking The Repo

1. In order to make changes, you will need to fork the repository. Click on the **Fork** button in the top-right corner of this page.
2. You will now need a copy of these files on your computer to make changes. To do this, you will need to clone or download the repo you forked in the previous step onto your local computer:
    - Click on the green **Clone or download** button
    - Under **Clone with HTTPS**, copy the clone URL for the repository
    - Open your Git terminal
    - Type ```git clone``` followed by the URL copied in the second step. This should look something like the following:
```console
$ git clone https://github.com/YOUR-USERNAME/fullstack.git
```
3. Once you have the file path all written down, go and hit Enter on your keyboard to request the clone.

### Making Changes

Now you're all set to make changes. You can open the project on you preferred text editor or IDE and begin making changes.

### Submitting Pull Requests

Now that you've made changes to the portfolio, you can submit a pull request to the master branch to await approval. To do this:
1. Navigate to the [original repository](https://github.com/mineshkothari/fullstack "https://github.com/mineshkothari/fullstack")
2. Click on **New pull request** on the right of the Branch menu
3. On the compare page, click **compare across forks**
4. Confirm that the *base fork* is the repository you'd like to merge into
5. Use the *head fork* drop-down menu to select your fork, then use the compare branch drop-down menu to select the branch you made your changes in
6. Type a little description for your pull request
7. If you do not want to allow anyone with push access to the upstream repository to make changes to your PR, unselect **Allow edits from maintainers**
8. Click **Create pull request**

For further information about forking a repository, please click [here](https://help.github.com/articles/fork-a-repo/).

For further information about creating pull requests, please click [here](https://help.github.com/articles/creating-a-pull-request-from-a-fork/).

<br />
<br />

## Testing

This project has undergone rigorous testing with each new implementation to ensure every aspect of this site works robustly.

*All tests were done on a Windows 10 64-bit PC unless otherwise stated*

**Desktop Browsers Tested:**
```
Google Chrome
Firefox
Microsoft Edge
Internet Explorer 11
```

**Mobile Browsers Tested:**
```
None yet
```

### UX/UI Testing

Manual tests were carried out at every stage to ensure the user experience standards remained at consistently high levels with each new implementation, no matter how big or small. This proved an excellent way of identifying and thwarting any issues, reducing the time spent on bug fixes to a small fraction.

### Responsive Design

### Cross-Browser Testing

### Testing the Contact Form

### Mobile Devices

<br />
<br />

## Deployment

This project will be deployed to Heroku using AWS S3 to host static and media files.

<br />
<br />

## Report

Want to learn about some of the known issues/bugs/limitations with this project? Continue reading to find out more. Perhaps, you will find a solution, or a better solution and if so - feel free to create a pull request with your changes.

### Responsive Design


<br />
<br />

## Credits

### Courses

The guides from [HTML Dog](https://htmldog.com/guides/) were used as courses for this project

HTML Courses:

- HTML for beginners - [Getting Started](https://htmldog.com/guides/html/beginner/gettingstarted), [Tags, Attributes, and Elements](https://htmldog.com/guides/html/beginner/tags)

- HTML Headings - [Headings](https://htmldog.com/guides/html/beginner/headings/)

- HTML Lists - [Lists](https://htmldog.com/guides/html/beginner/lists/)

- HTML page titles - [Page Titles](https://htmldog.com/guides/html/beginner/titles/)

CSS Courses:

- CSS for beginners - [Applying CSS](https://htmldog.com/guides/css/beginner/applyingcss/)

- CSS Selectors - [Selectors, Properties, and Values](https://htmldog.com/guides/css/beginner/selectors/)

JavaScript Courses:

- Variables and Data - [Variables and Data](https://htmldog.com/guides/javascript/beginner/variables/)

### Blog Posts



### Media

Many of the images from this site have been sourced from Unsplash. I created a [collection](https://unsplash.com/collections) which I called using their API https://source.unsplash.com/collection/{COLLECTION ID} during testing. This worked particularly well as it's quick and lightweight. An example of how it was used can be seen below.

```css
section.intro {
    background: linear-gradient(rgba(245,245,245,1),rgba(204,204,204,0.6)), url("https://source.unsplash.com/collection/3320800/") no-repeat center center / cover;
}
```

### Acknowledgements
