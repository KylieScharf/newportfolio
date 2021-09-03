
##Wonders Of The World
## Where We Started: [Flask Portfolio Starter](https://nighthawkcodingsociety.com/projectsearch/details/Flask%20Portfolio%20Starter)
Group Members: Kylie Scharf, Kevin Chen, Khushi Bagri, Daniel Bertino, Hamza Hakak

###Our Github Repository:
https://github.com/KylieScharf/flask_portfolio
###Scrum Board:
https://github.com/KylieScharf/flask_portfolio/projects/2

###Pair Share Journals
####Kylie and Khushi: https://docs.google.com/document/d/1eyTgQhMv7jFi28SIGlwOs3k95a9KklfJFCS0O9pXCzA/edit
####Danny, Hamza, and Kevin: https://docs.google.com/document/d/1fy-J_PVrvafykD-OTxMm-Pe0L_UKrYUTC4-DP4vGXEw/edit?usp=sharing
###Notes:
####General Notes: https://docs.google.com/document/d/1Sk4kdFS8o3iUE9MSoS8R0oeG13owbyw91XDAEudpfVo/edit?usp=sharing
####In-Class video notes: https://docs.google.com/document/d/1ryaAXia9cBviGVs9KxgRe6caFzp20b449Sjkh3S65TA/edit?usp=sharing
####Collab Notetaker/Webstorming: https://docs.google.com/document/d/12dsUnpEVu57HyiE23_80cQSTKghdxiLHDVVv7iYlNCA/edit?usp=sharing
####Padlet: https://padlet.com/kyliekylie10/s80zfwqjy2386ovv
####AP review:AP review/Leader Notes: https://docs.google.com/document/d/1oJNWx6yepYdKIuTszi_hgSbdDPv9pNZVhOblzeZSmXo/edit?usp=sharing 
###Roles
####Kylie: Scrum master, developer
####Khushi: Technical Lead and Developers (integration of greet). Also, find if then statements for how the journey game works.
####Daniel: Developer(2 dropdown menus-about me/mini labs)
####Hamza: navigator and designer
####Kevin: developer


###Inspiration: https://chooseyourstory.com/

###Project Overview/Ideation: 
####This website will be an informative website about the wonders of the world including the great pyramid of giza, the bermuda triangle, and area 51. Each wonder will have it’s own adventure linked to it where the user will be able to design their own adventure within the theme of the wonder they have chosen.

###Specifications: 
####This website will have a home page that displays text about what the website is about and what they can do within the website (limitations and specifications). There will be tabs for 3 wonders in the navigation bar located within a drop down menu that makes the page look neater. The navigation will bring them to an informative page about the wonder they have chosen and on the bottom of the page there will be a button that they press to start the adventure for their wonder. This may be a search bar or just a button (decide later). This will lead them to a new HTML page that will stay within the same tab because it will not have its own tab in the nav bar. They will then navigate the story by clicking one of two buttons which will display one of two possible text outcomes and this will continue until they are done with the story. These buttons may be a search bar or just buttons (decide later). The navigation bar at the top will also have a drop down menu for the about you portion where each of us will have our own tab within the drop down that will navigate to a page with information about ourselves. The navigation bar will have another drop down menu with the many mini labs we do, including the Journal 0 video, the greet page, _____. Additionally, there will be a tab where the user will be able to put feedback on our project by typing it in and posting it to the page. There may also be a login feature where the user can create an account for the page.

###Wireframe:
https://docs.google.com/document/d/1t8cRoSjdcl2BHJ1eOqjS7T4RPHXwugz9jqXOsz4qo_w/edit?usp=sharing




###Technical complexities: 
####We need to figure out how to create multiple buttons where each button displays a different text option when pressed. This will include many if statements which are conditional logic. We also need to figure out how to swap the HTML with different text after the user clicks the adventure button on the informative page. We will need to swap this HTML while remaining in the same tab. We also need to figure out how to code a drop down menu and have each option go to a different page within the same tab. We also need to figure out how to create a text box for users to type and post feedback into and we need to figure out how to display such typed information within the box on the page and keep it there. Additionally, if we do the login feature, we will need to figure out how to allow users to create accounts and store their data.
####Khushi: I have figured out how to create a webpage of the wonder, the description, and a button for the user to click on to start their journey. However, we still need to figure out the colors that we want to use for the font. I had tried to make a border line which would indicate the end of the lines of that page. Also, we need to work on how we can use our button to navigate to the informative page.

###Code Journal:
####Week 0: Downloaded the tools needed to exceed in the class including the IDE (IntelliJ), github, git, and slack which is our messaging tool
####Week 1: Added the greet code to our project and changed some names and variables to make it work for our project. Each person has their own greet code that corresponds to their name. This code included displayed text, a text box, and a submit button tied to the text box. The text in the displayed text changes to the text entered into the text box when the submit button is pressed. The default text before any buttons are pressed is hello world.
####Week 2: We figured out how to code both vanta visual backgrounds and gradient/multicolored backgrounds and decided on using a multicolored background. This is because the vanta visuals become the top layer and block all menu items so drop-down menus do not work on pages with vanta visuals. We also discovered how to get rid of the lining of the header and merge it with the color of the rest of the site by taking away the “bg” statement at the top. Additionally, we learned how to code drop down menus to organize our program which are located both in the nav bar and in HTML files where users have a choice between multiple options within the page. We also figured out how to change the text size, color, and font and to set defaults of all 3 in the CSS of the base where it says so.

###Friday’s learnings:
####Friday 08/28: When we run our code, we are running a web application on our computer. If we get a notification saying the port/address is already in use, it means that the python is already running on our computer, so the port is taken (sort of like trying to plug something into a computer when there is already something plugged in where you want to plug into). To fix this issue, we need to go to the activity monitor for mac or task manager for windows and search python and force quit/kill it. This will stop the application from running on our computer, so we can rerun it through IntelliJ. Through this, we learned how to kill processes on our computer, such as python or IntelliJ. Processes are entities/instances of programs that run on the computer. Our browsers are also processed to interpret HTML. We also created a template project.html file to make coding the theme pages more efficient. 
