<table><tr><td> <em>Assignment: </em> IS601 - Mini Project 1 - IceCream</td></tr>
<tr><td> <em>Student: </em> Tharun Bhupathi (tbb)</td></tr>
<tr><td> <em>Generated: </em> 10/24/2022 1:25:01 AM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-005-F22/is601-mini-project-1-icecream/grade/tbb" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Create a new branch per the desired branch name below</li><li>Add the baseline files from the following link:&nbsp;<a href="https://gist.github.com/MattToegel/17d0ac833a03580d010ad92e83fc4216">https://gist.github.com/MattToegel/17d0ac833a03580d010ad92e83fc4216</a>&nbsp;</li><li>Put them into a subfolder in your repository folder (I called my folder IcecreamMachine)</li><li>git add .</li><li>git commit -m "baseline files"</li><li>git push origin (name of desired branch below)</li><li>You can go to github and open the pull request for evidence capturing later (don't close/merge the pull request until you're done with the assignment)</li><li>Do the below tasks and fill in the below entries</li><ol><li>git add/commit after any significant changes to build up history</li></ol><li>Save the input and generate the submission markdown file (copy to clipboard or download the file)</li><li>Name it something relevant to the assignment if it's not named already</li><li>git add the submission file</li><li>git commit the submission file</li><li>git push the submission file</li><li>Complete the pull request to dev</li><li>Create a pull request from dev to prod</li><li>Go to the prod branch on github, navigate to the submission file</li><li>Paste that link to Canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Code Changes - Add the calculate_cost() implementation </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of the updated method calculate_cost()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/197440635-ae35a80f-7f2a-45bf-bd16-627d54758039.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>the above screenshot shows all the details mentioned above<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain the approach to implementing the calculation</td></tr>
<tr><td> <em>Response:</em> <p>I calculated the cost by taking the iterator which calculates the sum of<br>each item in the list cost and format it to display two decimal<br>places.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Exception Handling </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of adjusted code to handle exceptions</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/197453035-f939c746-6cd6-4644-b0b4-3369de21d44b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>the above screenshot shows the OutOfStockException<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/197453189-a59401d2-2e73-45df-aad2-b9f6fd68a9ce.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>the above screenshot shows the NeedsCleaningException and ExceededRemainingChoicesExceptions<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/197453518-843272d2-dd35-4657-8aaf-0d1b55e1a8de.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>the above screenshot shows the InvalidChoiceExceptions<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/197453610-122664d1-5e22-4314-bbef-6f5cb2575f63.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>the above screenshot shows the InvalidPaymentException<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Summarize each exception handling process</td></tr>
<tr><td> <em>Response:</em> <div>When the quantity of any item is 0 and the user wants to<br>add that item, OutOfStockException is raised. After "USES_UNTIL_CLEANING" the number of ice creams<br>have been delivered and the user wants another icecream, Needs Cleaning Exception is<br>raised. If the user inputs an invalid option, one which is not part<br>of the choices, InvalidChoiceException is raised. All ice creams have max_scoops and max_toppings,<br>if the user tries to add any more than the max values, ExceededRemainingChoicesException<br>is raised. If the user enters any value other than the exact value,<br>InvalidPaymentException is raised.</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Test Cases </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of test cases per the checklist</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/197452268-a237ac92-11d7-4ccb-8eb7-9beebe5a6e41.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>the above screenshot shows the Test 1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/197452398-0d853558-5a27-4145-8382-ade141064337.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>the above screenshot shows the Test 2, test 3<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/197452563-58369dc7-e70e-4862-b60f-bd68da97790e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>the above screenshot shows test 4 , test 5<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/197452695-0c9a0aa4-ed00-43e8-8e0b-d5f92d0c7fb8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>the above screenshot shows test 6 , test 7<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/197452787-318bd200-d729-4a18-88ea-50c9a799f962.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>the above screenshot shows test 8<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/197452897-1f53cf3f-4fa9-4105-b8d2-afa175e52a96.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>the above screenshot shows all the test cases passed<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Summarize each test case logic</td></tr>
<tr><td> <em>Response:</em> <div>Test 1: test_first_selection - checks if the first stage is the container stage</div><div><br></div><div>Test<br>2: test_flavour_in_stock - changing the ice cream machine item quantity to 1 and<br>testing to see if the item can be added twice, OutOfStockException should be<br>raised</div><div><br></div><div>Test 3: test_toppings_in_stock - changing the ice cream machine item quantity to 1<br>and testing to see if the item can be added twice, OutOfStockException should<br>be raised</div><div><br></div><div>Test 4: test_max_scoops - used a loop to add a scoop max_scoops(3)<br>times and if another scoop is added, then ExceededRemainingChoicesException should be raised</div><div><br></div><div>Test 5:<br>test_max_toppings - used a loop to add a scoop max_toppings(3) times and if<br>another topping is added, then ExceededRemainingChoicesException should be raised</div><div><br></div><div>Test 6: test_total_cost - added<br>a container, some scoops, and some toppings and calculated the sum, and asserted<br>the sum to be equal to the cost calculated from the method</div><div><br></div><div>Test 7:<br>test_total_sales - added 2 ice creams, made valid payments for both, and asserted<br>the total sales to be equal to the sum of the 2 ice<br>creams' cost Test</div><div><br></div><div>Test 8: test_total_icecreams - added 3 ice creams, made valid payments<br>for both and asserted the total ice creams to be equal to 3,<br>used the pytest fixture second_order which has 2 ice creams delivered, and asserted<br>the total ice creams for the second order to be 2</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add pull request for the assignment</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/tharun-12345/IS601-005_3535/pull/5">https://github.com/tharun-12345/IS601-005_3535/pull/5</a> </td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain any issues/difficulties or something you learned while doing this assignment</td></tr>
<tr><td> <em>Response:</em> <p>At first I faced many problems while solving code, later by referring the<br>lectures and ppt&#39;s finally got solution for the mini project 1.<div>I learnt how<br>to execute loops in different situations, learnt in-depth about exceptions and&nbsp;practiced well on<br>exception handling and also I learnt how to perform test cases in for<br>python files we created.</div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of successful output</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/197447087-660edeaf-ba55-4a42-90fb-22838e82adef.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>the above screenshot shows the few successful program executions<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-005-F22/is601-mini-project-1-icecream/grade/tbb" target="_blank">Grading</a></td></tr></table>
