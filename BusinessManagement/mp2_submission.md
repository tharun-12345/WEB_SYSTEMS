<table><tr><td> <em>Assignment: </em> IS601 Mini Project 2  Business Management</td></tr>
<tr><td> <em>Student: </em> Tharun Bhupathi (tbb)</td></tr>
<tr><td> <em>Generated: </em> 12/5/2022 8:46:41 AM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-005-F22/is601-mini-project-2-business-management/grade/tbb" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>checkout dev and pull any latest changes</li><li>Create a branch called MiniProject-2</li><li>Add all the baseline files first under a folder called BusinessManagement (included below)</li><li>Don't forget to copy your .env file from flask_sample into BusinessManagement</li><li>source the venv and pip install the requirements.txt</li><li>Run the BusinessManagement/sql/init_db.py script</li><li>Immediate add/commit/push to github</li><li>Open a pull request and keep it open until you're done adding the submission file</li><li>&nbsp;(optional) updated the deploy dev yml file and add MiniProject-2 so you can deploy to dev without needing to merge into dev</li><li>Make your code changes per the following requirements</li><ol><li>Important: run the test files indiviudally as you're working/testing to save on query quota usage</li></ol><li>Add/commit periodically (recommended after you implement a TODO item or checlist item)<br></li><li>Anywhere relevant add your ucid and the date you added the code (best to do this as you go)</li><li>You'll be capturing website screenshots from dev and code snippet screenshots (ensure you upload these properly as pull request comments to the pull request from step 5</li><ol><li>Note: You don't need separate screenshots for each checklist item, when possible it's recommended to try to capture multiple items together</li><li>Ensure all screenshots are properly captioned in the deliverable section</li></ol><li>You may save your progress when filling out this submission as often as you want</li><li>Once done, copy the markdown or download the md file and save it under the BusinessManagement folder</li><li>Do a final add/commit/push</li><li>Verify everything looks ok in the pull request</li><li>Merge the pull request</li><li>Make a new pull request from dev to prod and merge it</li><li>Navigate to the submission file under the BusinessManagement folder</li><li>Copy the github url to the exact file and submit it to Canvas</li></ol><div>You'll be implementing a basic Business Management site.</div><div>There will be some provided files fully working as-is and some skeleton files you'll need to fill in.</div><div>The files you need to fill in will have TODO items or comments mentioning what's expected.</div><div>There are provided test case files too that all must be passing for full credit. Do not edit these test case files.</div><div>The site will handle CRUD operations for Companies and Employees as well as allowing import of Company/Employee data via a csv file.</div><div><br></div><div>Baseline files:&nbsp;<a href="https://github.com/MattToegel/IS601/tree/F22-MiniProject-2">https://github.com/MattToegel/IS601/tree/F22-MiniProject-2</a></div><div>May want to download branch as a zip, then copy/paste the files into your repo</div><div><br></div><div>Provided files you don't need to edit:</div><div><ul><li>000_create_table_companies.sql</li><li>001_create_table_employees.sql</li><li>db.py</li><li>init_db.py</li><li>flash.html</li><li>company_dropdown.html</li><li>country_state_selector.html</li><li>upload.html</li><li>sort_filter.html</li><li>all test files</li><li>geography.py</li><li>__init__.py (remains empty)</li><li>Dockerfile</li><li>main.py</li><li>index.py</li></ul><div>All other files likely have requirements to fill in.</div></div><div><br></div></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Identity Edits and Setup </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the index page being displayed (from dev)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/205585081-3546d3bc-cb83-40ce-a82e-fc79561e56f4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>the above screenshot displays the index page from dev<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot from the DB extension of vs code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/205585533-f05188f7-6991-4e86-99c0-08aa5dce37ed.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>the above screenshot shows the data form IS601_MP2_Companies and DB extension<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/205585714-c36c39ed-0801-4e54-850e-aba1e1b0732c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>the above screenshot shows the data form IS601_MP2_Employees and DB extension<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Upload / Import CSV File (provided data.csv) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of /import route</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/205593066-d834be8f-f994-49dc-9f5b-b630ff815f63.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>the above screenshot shows the code for After each query a flash message<br>should be generated noting how many records were processed and If a particular<br>list was empty a flash message should note that the particular list wasn&#39;t<br>loaded or was empty<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/205592479-3bd58104-645f-4890-8321-1fccb1503d76.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>the above screenshot shows the CSV file should be read from the provided<br>stream as a dict and Extracted employee data should be append as a<br>dict to the employee list and Extracted company data should be appneded as<br>a dict to the comapny list<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/205591514-23a604d0-bab6-4ad7-bc8f-8edd2ded1d4e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>the above screenshot shows the code for checking the file .csv or not<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of the website when uploading the data.csv file</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/205593586-41ef7726-4f9f-453f-bea1-eba97e0a0f1e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>the above screenshot shows the proper success message and proper count message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/205594004-f9313998-20f2-4e58-875e-193055e8a303.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>the above screenshot shows the error message when the file is not a<br>.csv file<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/205594270-848ba064-619b-4a1e-a623-57037ca0a496.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>the above screenshot shows the error message when the form was submitted without<br>a file attached<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data (basic summary/view)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/205585533-f05188f7-6991-4e86-99c0-08aa5dce37ed.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>the above screenshot showing some company data was uploaded in database<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/205585714-c36c39ed-0801-4e54-850e-aba1e1b0732c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>the above screenshot showing some employee data was uploaded in database<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/205595530-889c7bf8-b85c-49ac-bdf5-cf82f01cf4aa.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>the above screenshot showing some company data was uploaded in HTML page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/205595584-44858216-9521-4ffd-8b8a-29bbb175fd97.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>the above screenshot showing some employee data was uploaded in HTML page<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Add Employee </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /add route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/205597115-e286e10a-81e2-44a4-8027-d356a83e6569.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>the above screenshot shows the code for retrieving first_name, last_name, company (id), email<br>and first_name is required and last_name is required and company doesn&#39;t require a<br>flash and may be empty/None and email is required <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/205597806-4c25bb55-a668-4f45-8da2-cfb6c0c33d34.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>the above screenshot shows the code for Proper INSERT query and Except block<br>should have a user friendly message flashed and a print() of the exception<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for add employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/205601280-e50ee20d-99c9-4f96-a63a-7c6fb5f7093f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>the above screenshot shows the first_name error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/205601426-40d7c4d7-5289-4520-bdc8-04689dc45432.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>the above screenshot shows the last_name error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/205601488-47d388e6-f0d2-4b53-a92e-96e13efa4812.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>the above screenshot shows the email error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/205603479-f07cd099-331a-4159-81b4-00d1ee4f1d10.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>the above screenshot shows the success message on adding an employee<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/205603719-77e95733-7b89-4b0d-8ac1-fe2d1c85d140.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>the above screenshot shows filled in valid data prior to submission<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of new employee DB record from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/205604318-e922c658-3646-40a0-a8c4-5cdb94b0b0aa.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>the above screenshot shows the new employee DB record from VS Code <br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> List/search Employees </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /search route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/205606160-86273d18-8650-47af-9aa3-0f8bb2ba6265.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>the above screenshot shows the code for select query via LEFT OUTER JOIN,<br>check req args , append first_name,last_name,email<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/205606237-27008c32-4ad1-46e0-8d3e-4bcf428d71d3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>the above screenshot shows the code for append company_id, append sorting, append limit<br><br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/205606268-1d36870b-40bf-494f-995f-672179f123a1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>the above screenshot shows the code for provide a proper error message if<br>limit isn&#39;t a number or if it&#39;s out of bounds and Except block<br>should have a user friendly message flashed and a print() of the exception<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for search employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/205608610-1660021e-0717-4462-8998-4912aa852cc9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>the above screenshot shows results with first_name filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/205608742-880e7687-4953-47b7-a1af-9ee5e330be48.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>the above screenshot shows one asc filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/205608817-c68ed4a2-b5e6-446e-ad24-2b08c2e26d10.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>the above screenshot shows one desc filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/205608944-00575b22-4e4c-4dd6-808f-d37d0e38f936.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>the above screenshot shows results with last_name filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/205609042-56887650-704b-4fee-b405-ecb53ba03347.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>the above screenshot shows results with email filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/205609130-12ab025e-42c1-4d9e-a8f5-01f1a6d9bd44.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>the above screenshot shows results with company filter applied<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Edit Employee </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /edit route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/205620304-041298ff-826b-4395-bf94-50d9168312d7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>the above screenshot shows Code retrieve id the first_name, last_name, company (id), email<br>from form and first_name , _last_name , company , email required<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/205620488-4ff4caee-35b1-4c3d-86a5-92841e690c55.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>the above screenshot shows the UPDATE query , Except blocks , SELECT query<br>, Employee data should be passed to the render_template()<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for edit employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/205625980-c0b288b0-f6c0-4fb6-b409-009c3edff4ec.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing data before edited (last_name)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/205626013-809eda6f-e54b-430c-994e-e3079ad0993d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing data after edited (last_name)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data before and after of employee data edit from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/205626267-2951c8ee-6cd1-4a8e-a4a6-6fdf4e07d2d2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshots of DB data before edit(last_name)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/205626289-8c59b0a7-f653-4b4c-8bc6-4fa582d8082b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshots of DB data after edit (last_name)<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Add company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /add route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/205626908-b8532aef-025c-4eb1-aa64-7de97b3b1a38.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>the screenshot shows the code for code should retrieve form data for name,<br>address, city, state, country, zip, website and  flash messages for name, address<br>, city , state, country required<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/205626990-7e7a644e-97a7-48fc-b675-758e31f1e014.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>the screenshot shows the code for website is not rquired , proper INSERT<br>query, Except block<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for add company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/205631967-59a549c5-1db2-4a4d-8b14-c0a157247a90.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show name error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/205631990-7b707baa-50ca-4467-99f9-796d14723bb0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show address error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/205632014-3ad25765-9861-44ad-bf98-f97b6770448a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show city error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/205632047-969e4b1c-2686-476e-a6c4-319b8aad9608.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show state error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/205632070-2f88c873-8af0-4afb-a7ef-b253e83e617e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show country error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/205632141-799ed18b-3ecc-4b55-ac1b-300aafd2d22b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show success message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of new company DB record from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/205641606-965c2bd5-09f6-4548-9302-616b830b0ad5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of new company DB record from VS Code<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> List/Search Comapny </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /search route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/205642347-b70b4d51-95f7-4524-85aa-45d69630252f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>the screenshot shows SELECT query, check request args , append a Like filter<br>for name and append an equality filter for country and state<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/205642358-d6f89d91-6387-4355-b23c-36321e115559.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>the screenshot shows append sorting, limits , provide proper error message, except block<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for search company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/205644192-f56b66af-eea5-4621-9f8e-db6031aa4be3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show results with name filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/205644226-011329ef-b9d8-4528-ade7-2d7478499736.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show results with country filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/205644262-377a81c0-f36c-4df3-af7d-73dd31338dec.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show results with state filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/205644382-c38517bc-8e27-40bd-a95e-818f90ac604a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show one asc filter applied <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/205644496-d49eb168-a4f5-4657-9171-36b63e4871d1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show one desc filter applied <br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Edit Company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /edit route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/205645468-db51248f-9412-4a34-943e-6bcde1fc81b9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>the screenshot shows code for request args, flash proper error message for name<br>, address , city , state , country<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/205645526-7f3a1c49-6b52-40e6-ab41-76d311b7168e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>the screenshot shows code for Proper UPDATE query, Except blocks , Proper SELECT<br>query , Company data should be passed to the render_template()<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for edit company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/205647590-c34002a5-6cf8-43bf-b474-385072b15910.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show data before an edit(address)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/205648728-7070448e-5c18-45cf-9bc3-62c02bf8df65.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show data after an edit<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data before and after of company  data edit from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/205648417-f62914d6-4767-4643-9b8b-f8e98feb660d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of DB data before edit (address)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/205648500-dbe346e2-496d-4940-9b57-722a0a6337f3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of DB data after edit(address)<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Delete Employee and Delete Company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /delete route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/205649733-38d15fcb-7197-4696-b3ee-3ae3a151f18c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>the screenshot shows the code for Delete employee by id , Redirect to<br>employee search , all request args and success message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a before and after website screenshot of deleting an employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/205649998-7ddc4cb7-7164-4dcc-9609-99be6bcf3b83.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of before deleting an employee<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/205650093-d7c9e7ce-bf2d-4df4-9159-a0b1ca406331.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of after deleting an employee<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of code for /delete route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/205650171-c72e2d13-6de6-4a3b-a8b2-0801930edf4b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>the screenshot shows code for deleting company by id, redirect to company search<br>, all request args, success messsage<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a before and after website screenshot of deleting a company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/205650407-3098e9d1-a1f4-4fcd-8651-224564dd8e83.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of before deleting an company<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/205650520-d09e9728-ac34-4fbe-95cd-347cc1468dc2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of after deleting an company<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Test Cases and Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot Test case Results</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/205589492-b2a89921-d13f-4935-a170-a34bdcaf7d26.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>the above screenshot shows that all the test cases are passed<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Issues / Learnings / Interesting things to note</td></tr>
<tr><td> <em>Response:</em> <p>While working on this project I learned in-depth topics on database implementation in<br>web development , handling databases through python. At first I struggled a lot<br>with virtual environment and later with the help of lectures and internet&nbsp; I<br>found the solution for my problem and solves the issues which me boost<br>on myself.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-005-F22/is601-mini-project-2-business-management/grade/tbb" target="_blank">Grading</a></td></tr></table>