<table><tr><td> <em>Assignment: </em> IS601 Milestone1 Deliverable</td></tr>
<tr><td> <em>Student: </em> Tharun Bhupathi (tbb)</td></tr>
<tr><td> <em>Generated: </em> 12/13/2022 3:57:46 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-005-F22/is601-milestone1-deliverable/grade/tbb" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone1 branch</li><li>Create a milestone1.md file in your Project folder</li><li>Git add/commit/push this empty file to Milestone1 (you'll need the link later)</li><li>Ensure your images display correctly in the sample markdown at the bottom</li><ol><li>NOTE: You may want to try to capture as much checklist evidence in your screenshots as possible, you do not need individual screenshots and are recommended to combine things when possible. Also, some screenshots may be reused if applicable.</li></ol><li>Save the submission items</li><li>Copy/paste the markdown from the "Copy markdown to clipboard link" or via the download button</li><li>Paste the code into the milestone1.md file or overwrite the file</li><li>Git add/commit/push the md file to Milestone1</li><li>Double check the images load when viewing the markdown file (points will be lost for invalid/non-loading images)</li><li>Make a pull request from Milestone1 to dev and merge it (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku dev</li></ol></li><li>Make a pull request from dev to prod (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku prod</li></ol></li><li>Submit the direct link from github prod branch to the milestone1.md file (no other links will be accepted and will result in 0)</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Feature: User will be able to register a new account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/207429790-5988d391-bd5d-4070-97e2-cb4051c52f2a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing invalid email validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/207429816-69b030c0-b796-4e0d-b50e-f4907c225dab.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing invalid password validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/207429849-606a5449-5b0b-4cd8-b67e-ee7b2ebc68f7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing passwords not match validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/207429875-dccbff7b-e3b4-4cac-8abb-487c3a4bdcce.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing username not available validation (username is taken)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/207429900-d5159682-5fed-4f57-8a18-5b7bf7193aea.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing email not available validation (already registered)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/207429924-f993b72b-6857-4894-9949-03a9322755f0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing the form with valid data filled in before the form is<br>submitted<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the Users table with data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/207429955-b190a608-7bf6-4e1a-928f-bc9e90162fef.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the Users table with data in it<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/tharun-12345/IS601-005_3535/pull/28">https://github.com/tharun-12345/IS601-005_3535/pull/28</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <p>We utilize WT-forms for form generation and validation. The form submission will try<br>to deliver data to our Python POST route, which will extract the data<br>and<br>run an insert query to our sample table.</p><br><ul><br><li>WT-form validators are used<br>to validate<br>data both in frontend &amp; backend, username is validated to be<br>of length between<br>2 &amp; 30 characters and it shouldn&#39;t be previously used<br>by another user, email<br>validation is done using an email validator.</li><br><li>password &amp;<br>confirm password should both be<br>the same and should be of a length<br>of 8, This is validated using<br>WT-form&nbsp;validators and it is stored in<br>the database after hashing it using the bcrypt<br>hashing algorithm</li><br><li>email, username, and<br>hashed password is stored in the users table.<br></li><br></ul><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Feature: User will be able to login to their account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/207429984-3b565138-e56a-4f49-8b6a-985701712f41.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing validation based on non-existing user<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/207430015-69e70857-ef4a-4c3d-9c55-3e3bd340b418.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing password mismatch validation (doesn&#39;t match what&#39;s in the DB)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of successful login</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/207430039-57d06613-6fad-472f-9902-103ac6e35bc5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing the successful login<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/tharun-12345/IS601-005_3535/pull/28">https://github.com/tharun-12345/IS601-005_3535/pull/28</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <p>We have handled the login form using wt forms, which is similar<br>to how<br>we handle register forms, but we&#39;ll utilize the username or email<br>field instead of<br>the confirm password field.</p><br><ul><br><li>In the front end, if the<br>username or email field<br>checks if data is entered or not, and if<br>the field has &#39;@&#39; it<br>will use an email validator else it checks<br>for the username format, if the<br>length is between 2 &amp; 30 or<br>not, and checks if the password is<br>entered or not.&nbsp;<br>In the backend, we<br>fetch the data from the users table by<br>passing the email/username, if we<br>get something we compare the password &amp;then check if<br>the user is assigned<br>roles&nbsp;<div>- In the front end, we first check if the<br>password is entered<br>&amp; then in the back we fetch the password from the<br>database based<br>on username/email &amp; then check if the passwords match, if they match<br>then<br>we delete the password from that point in the program.</li><br><li>we fetch username,<br>email,<br>password from users table passing username/email, and then check if passwords match,<br>and then<br>check if the user is assigned is any roles from user roles<br>tables &amp;<br>fetch it.&nbsp;<br></div><br></li><br></ul><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Feat: Users will be able to logout </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the successful logout message</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/207433184-4c5f6c98-142d-4f10-82c7-f0de38ccac90.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing message as successfully logged out<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the logged out user can't access a login-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/207433221-19abb123-6a78-4745-80c8-269862f72d3d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> screenshot showing the logged out user can&#39;t access a login-protected page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/tharun-12345/IS601-005_3535/pull/28">https://github.com/tharun-12345/IS601-005_3535/pull/28</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <p>we use flask_login package to work with user session &amp; manage it,&nbsp;<br>In our<br>main.py<br>we’ll utilize LoginManager, this handles our user session and provides helpful utilities<br>Since<br>we’re using<br>an app factory we’ll defined a variable for login_manager outside of<br>the factory, then<br>inside the factory we use its init_app() method to associate<br>the app<br>Next, inside of<br>the app factory we’ll use the user_loader decorator, this<br>will run a process to<br>lookup a user by id&nbsp;<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Feature: Basic Security Rules Implemented / Basic Roles Implemented </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the logged out user can't access a login-protected page (may be the same as similar request)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/207433221-19abb123-6a78-4745-80c8-269862f72d3d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing the logged out user can&#39;t access a login-protected page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing a user without an appropriate role can't access the role-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/207433292-30edb922-6dcb-4bf0-9992-b0541dc7bdf7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing a user without an appropriate role can&#39;t access the role-protected page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the Roles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/207433349-59bee2f3-55b3-4d45-a662-3f23eb9ffe5b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the Roles table with valid data<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a screenshot of the UserRoles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/207433366-fb20e085-2efd-4963-bee2-b1527c7b504d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the UserRoles table with valid data<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add the related pull request(s) for these features</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/tharun-12345/IS601-005_3535/pull/30">https://github.com/tharun-12345/IS601-005_3535/pull/30</a> </td></tr>
<tr><td> <em>Sub-Task 6: </em> Explain briefly how the process/code works for login-protected pages</td></tr>
<tr><td> <em>Response:</em> <p>Since we’re using an app factory we’ll defined a variable for login_manager outside<br>of<br>the factory, then inside the factory we use its init_app() method to<br>associate the<br>app,&nbsp;<br>For the login protected pages, we decorate the views with @login_required<br>function, If the<br>user is not logged in, it calls the LoginManager.unauthorized function.&nbsp;<br></p><br></td></tr>
<tr><td> <em>Sub-Task 7: </em> Explain briefly how the process/code works for role-protected pages</td></tr>
<tr><td> <em>Response:</em> <p>similar to login protected page, here we use @admin_permission_require function from roles.permissions.&nbsp; If<br>the<br>user is not a admin,&nbsp; we raise 403 exception and display 403<br>html page<br>saying permission denied.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Feature: Site should have basic styles/theme applied; everything should be styled </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots to show examples of your site's styles/theme</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/207433404-f4ffe826-4f07-4395-bb77-059568a37210.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing Navigation bar with basic styles and with a clean UI<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/207433421-15546ade-a2a0-4674-939f-41463e2400ad.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing a forms which represents the profile page of the user/admin and<br>with a clean UI<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/207433477-a79f82ed-f912-4e1b-8c6d-c330332a3016.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Data output of sample lists and with a clean UI<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/tharun-12345/IS601-005_3535/pull/30">https://github.com/tharun-12345/IS601-005_3535/pull/30</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain your CSS at a high level</td></tr>
<tr><td> <em>Response:</em> <p>Using Bootstrap, a navigation bar can extend or collapse, depending on the screen<br>size.<br>A standard navigation bar is created with the .navbar class,<br>followed by a<br>responsive extend<br>and collapsing class<br>collapse. navbar-collapse for grouping and hiding navbar contents by<br>a parent breakpoint.<br>navbar-brand<br>for your company, product, or project name.<br>navbar-toggler for use with<br>our collapse plugin and<br>other navigation toggling behaviors.<br>Using the nav-item class allows developers<br>to quickly change between different<br>types of navigation in the bootstrap system while<br>only changing the wrapping class and&nbsp;Containers<br>are a fundamental building<br>block of Bootstrap that contain, pad, and align your content<br>within a given<br>device or viewport.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Feature: Any output messages/errors should be "user friendly" </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of some examples of errors/messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/207433503-0028b822-35fa-483d-865c-194f57493925.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Message showing something about not being logged in<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/207433533-d21f92f0-3145-496b-a251-57b21aa08b96.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Message showing something about not having proper role or permission (i.e., different than<br>the not logged in message)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a related pull request</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/tharun-12345/IS601-005_3535/pull/30">https://github.com/tharun-12345/IS601-005_3535/pull/30</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how you made messages user friendly</td></tr>
<tr><td> <em>Response:</em> <p>To better handle this, we have created two functions in main.py<br>that’ll return a<br>render_template() to new respective files for 403 (access denied) and<br>404 (page not found)<br>For<br>sake of simplicity ,these files are identical<br>and just have a basic user friendly<br>messages applied, can customize these as<br>we wish<br>The main purpose for this is to<br>include our navigation<br>to allow our user to easily navigate to a proper location.<br>And<br>also<br>included some flash messages which will guide the users where they did<br>wrong and<br>which helps then recorrect the data.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Feature: Users will be able to see their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/207433565-1b35dff4-c466-4e31-9ece-0cd8869152f9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>user profile page where Email and username are properly prefilled<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/tharun-12345/IS601-005_3535/pull/32">https://github.com/tharun-12345/IS601-005_3535/pull/32</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Explain briefly how the process/code works (view only)</td></tr>
<tr><td> <em>Response:</em> <p>when profile page is opened, if it is not a POST request then<br>email,<br>username are fetched from users table passing user id, then these are<br>rendered into<br>the profile form.&nbsp;<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Feature: User will be able to edit their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page validation messages and success messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/207433594-16dc1c05-a711-4119-b57e-0ad581bf30fe.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>showing username changed message which tells that username validated<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/207433621-91a9811c-039d-4d1d-a759-76d029789833.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>showing email changed message which tells that email validated<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/207433650-4520071d-b616-4284-a9e3-4006581c011f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>showing password changed message which tells that password is validated<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add before and after screenshots of the Users table when a user edits their profile</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/207433676-397809e2-3296-4634-9c50-830db2e2c684.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> screenshot of the Users table before a user edits their profile<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/207433697-9d4d919f-1a26-434f-b559-301c58924ec9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> screenshot of the Users table after a user edits their profile<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/tharun-12345/IS601-005_3535/pull/32">https://github.com/tharun-12345/IS601-005_3535/pull/32</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works (edit only)</td></tr>
<tr><td> <em>Response:</em> <p>the code first checks for if it is POST request, if it is,<br>then<br>it checks if current_password, password &amp; confirm are given, then it retrieves<br>password from<br>users table, then the current password &amp; pwd from DB are<br>compared to check<br>if they are the same or not, if they are<br>not same we will<br>raise a invalid password flask, if they are same<br>then the new password is<br>stored &amp; pushed to the database.<br>Then the username<br>&amp; email are updated in the<br>database and a flash message &quot;saved profile&quot;<br>is displayed.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <p>By completing this milestone I have got a chance to learn about user<br>login<br>session, registration system, an authentication system. I learnt how to integrate the DB<br>utility and manage<br>the website by storing and retrieving the data from the database<br>.<div>By mistakenly I have placed another folder in the flask_sample main one which<br>lead me to the lots of errors during pushing to heroku-dev and tried<br>replacing the files but it doesn&#39;t worked out, later I have started the<br>whole process right from the beginning and completed the milestone-1.&nbsp;&nbsp;</div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Prod Application Link to Login Page</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-tbb-fp-prod.herokuapp.com/login">https://is601-tbb-fp-prod.herokuapp.com/login</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-005-F22/is601-milestone1-deliverable/grade/tbb" target="_blank">Grading</a></td></tr></table>