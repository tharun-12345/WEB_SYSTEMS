<table><tr><td> <em>Assignment: </em> IS601 Milestone 2 Shop Project</td></tr>
<tr><td> <em>Student: </em> Tharun Bhupathi (tbb)</td></tr>
<tr><td> <em>Generated: </em> 12/22/2022 3:35:18 AM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-005-F22/is601-milestone-2-shop-project/grade/tbb" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone2 branch</li><li>Create a new markdown file called milestone2.md</li><li>git add/commit/push immediate</li><li>Fill in the below deliverables</li><li>At the end copy the markdown and paste it into milestone2.md</li><li>Add/commit/push the changes to Milestone2</li><li>PR Milestone2 to dev and verify</li><li>PR dev to prod and verify</li><li>Checkout dev locally and pull changes to get ready for Milestone 3</li><li>Submit the direct link to this new milestone2.md file from your GitHub prod branch to Canvas</li></ol><p>Note: Ensure all images appear properly on github and everywhere else. Images are only accepted from dev or prod, not local host. All website links must be from prod (you can assume/infer this by getting your dev URL and changing dev to prod).</p></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Users with admin or shop owner will be able to add products </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of admin create item page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/209083458-f8311a3e-1752-4919-a23d-b791830a4642.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of admin create item page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot of populated Products table clearly showing the columns</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/209083571-f502f346-9549-4323-b670-277f8bde857c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of populated Products table clearly showing the columns<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly describe the code flow for creating a Product</td></tr>
<tr><td> <em>Response:</em> <p><span style="font-family: &quot;Times New Roman&quot;; font-size: 16px; font-variant-numeric: normal; font-variant-east-asian: normal;">After entering the<br>values in the add page, the values go to the</span><br style="font-family: &quot;Times New<br>Roman&quot;; font-size: 16px; font-variant-numeric: normal; font-variant-east-asian: normal;"><span style="font-family: &quot;Times New Roman&quot;; font-size: 16px;<br>font-variant-numeric: normal; font-variant-east-asian: normal;">item function in shop.py. It checks whether an id is<br>passed to check</span><br style="font-family: &quot;Times New Roman&quot;; font-size: 16px; font-variant-numeric: normal; font-variant-east-asian: normal;">&lt;span<br>style=&quot;font-family: &quot;Times New Roman&quot;; font-size: 16px; font-variant-numeric: normal; font-variant-east-asian: normal;&quot;&gt;if the action is<br>to edit or add. As no id will be</span><br style="font-family: &quot;Times New Roman&quot;;<br>font-size: 16px; font-variant-numeric: normal; font-variant-east-asian: normal;"><span style="font-family: &quot;Times New Roman&quot;; font-size: 16px; font-variant-numeric:<br>normal; font-variant-east-asian: normal;">passed with create action so the INSERT statement is executed passing</span>&lt;br<br>style=&quot;font-family: &quot;Times New Roman&quot;; font-size: 16px; font-variant-numeric: normal; font-variant-east-asian: normal;&quot;&gt;<span style="font-family: &quot;Times New<br>Roman&quot;; font-size: 16px; font-variant-numeric: normal; font-variant-east-asian: normal;">the values to Products table and is<br>success a flash is displayed.</span><br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/tharun-12345/IS601-005_3535/pull/54">https://github.com/tharun-12345/IS601-005_3535/pull/54</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-tbb-fp-prod.herokuapp.com/login">https://is601-tbb-fp-prod.herokuapp.com/login</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Any user can see visible products on the Shop Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot of the Shop page showing 10 items without filters/sorting applied</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/209083625-ed809a17-4c24-42e4-8020-a5b45482a00d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the Shop page showing first 6 items without filters/sorting applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/209083662-9a6b5d09-c8cc-4605-b32b-163be07c87a9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the Shop page showing last 4 items without filters/sorting applied<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the Shop page showing both filters and a different sorting applied (should be more than 1 sample product)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/209083707-cd274f54-fb0f-4215-ad29-63b49371bf02.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the Shop page showing both filters and a different sorting applied<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the filter/sort logic from the code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/209083755-7c99af58-48da-4946-a183-b0bb41eb20f0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the filter / sort logic from the code<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Briefly explain how the results are shown and how the filters are applied</td></tr>
<tr><td> <em>Response:</em> <p style="font-family: &quot;Times New Roman&quot;; font-size: 16px; font-variant-numeric: normal; font-variant-east-asian: normal;">For the shop<br>page,&nbsp; initially we get the items &amp; details from Products<br>table whose visibility is<br>1.&nbsp;</p><div style="font-family: &quot;Times New Roman&quot;; font-size: 16px; font-variant-numeric: normal; font-variant-east-asian: normal;">and in the<br>page we can search by name<br>or select a category or sort on price<br>"High to Low" or "Low<br>to High".<br>When we search using one/all of the above<br>option. we go to<br>shop_list function in shop.py and based on the input we<br>add a where<br>condition to the query. and display the results again.</div><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/tharun-12345/IS601-005_3535/pull/54">https://github.com/tharun-12345/IS601-005_3535/pull/54</a> </td></tr>
<tr><td> <em>Sub-Task 6: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-tbb-fp-prod.herokuapp.com/login">https://is601-tbb-fp-prod.herokuapp.com/login</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Show Admin/Shop Owner Product List (this is not the Shop page and should show visibility status) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of the Admin List page/results</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/209083875-3a2e7779-2ec8-4a74-a066-d50716eb9dfa.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the Admin List page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Briefly explain how the results are shown</td></tr>
<tr><td> <em>Response:</em> <p><span style="font-family: &quot;Times New Roman&quot;; font-size: 16px; font-variant-numeric: normal; font-variant-east-asian: normal;">We select all<br>fields from Products table without any filter and pass it</span><br style="font-family: &quot;Times New<br>Roman&quot;; font-size: 16px; font-variant-numeric: normal; font-variant-east-asian: normal;"><span style="font-family: &quot;Times New Roman&quot;; font-size: 16px;<br>font-variant-numeric: normal; font-variant-east-asian: normal;">to the html page.</span><br style="font-family: &quot;Times New Roman&quot;; font-size: 16px;<br>font-variant-numeric: normal; font-variant-east-asian: normal;"><span style="font-family: &quot;Times New Roman&quot;; font-size: 16px; font-variant-numeric: normal; font-variant-east-asian:<br>normal;">As no where condition is specified, every product will be</span><br style="font-family: &quot;Times New<br>Roman&quot;; font-size: 16px; font-variant-numeric: normal; font-variant-east-asian: normal;"><span style="font-family: &quot;Times New Roman&quot;; font-size: 16px;<br>font-variant-numeric: normal; font-variant-east-asian: normal;">displayed irrespective of visibility status</span><br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/tharun-12345/IS601-005_3535/pull/54">https://github.com/tharun-12345/IS601-005_3535/pull/54</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-tbb-fp-prod.herokuapp.com/login">https://is601-tbb-fp-prod.herokuapp.com/login</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Admin/Shop Owner Edit button </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the edit button visible to the Admin on the Shop page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/209084205-4846a706-5d58-4712-bb3d-26320e00bc55.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing the edit button visible to the Admin on the Shop page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the edit button visible to the Admin on the Product Details Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/209084284-0c206a00-cf4a-42e8-8911-c59f60213f6e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing the edit button visible to the Admin on the Product Details<br>Page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot showing the edit button visible to the Admin on the Admin Product List Page (The admin page)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/209084326-3ad3f64a-1f26-4488-b1b5-88ef5e005bc7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> screenshot showing the edit button visible to the Admin on the Admin<br>Product List Page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a before and after screenshot of Editing a Product via the Admin Edit Product Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/209084484-f6b500b0-08e2-4a34-9e48-15deb56bb51f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot before Editing a Product via the Admin Edit Product Page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/209084532-2b5f5da7-f33f-4365-a190-6ddb283b4455.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot after Editing a Product via the Admin Edit Product Page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Briefly explain the code process/flow</td></tr>
<tr><td> <em>Response:</em> <p style="font-family: &quot;Times New Roman&quot;; font-size: 16px; font-variant-numeric: normal; font-variant-east-asian: normal;">For the <b>Shop</b>&nbsp;page,&nbsp;</p><div<br>style="font-family: &quot;Times New Roman&quot;; font-size: 16px; font-variant-numeric: normal; font-variant-east-asian: normal;">in shop.html at the<br>end of every product we check if<br>the user is logged in and if<br>the user is a admin, if<br>both are true we display a edit button<br>which redirect to item page<br>with the product details.<br>Same for item details page, if<br>the user is a<br>admin we display the edit button.<br>The admin items page has<br>edit button default<br>as the page is only accessed by admin.</div><br></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/tharun-12345/IS601-005_3535/pull/54">https://github.com/tharun-12345/IS601-005_3535/pull/54</a> </td></tr>
<tr><td> <em>Sub-Task 7: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-tbb-fp-prod.herokuapp.com/login">https://is601-tbb-fp-prod.herokuapp.com/login</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Product Details Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the button (clickable item) that directs the user to the Product Details Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/209084651-354c2202-c9f6-473b-b524-fca33bee5b52.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing the button (clickable item) that directs the user to the Product<br>Details Page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the result of the Product Details Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/209084722-6c213ab3-2b93-4499-a787-9ee15797828a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing the result of the Product Details Page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the code process/flow</td></tr>
<tr><td> <em>Response:</em> <div style="font-family: &quot;Times New Roman&quot;; font-size: 16px; font-variant-numeric: normal; font-variant-east-asian: normal;">Created itemdetails.html &amp;&nbsp;<br>itemdetails function for this.</div><span style="font-family: &quot;Times New Roman&quot;; font-size: 16px; font-variant-numeric: normal; font-variant-east-asian:<br>normal;">Made the product name clickable, when clicked</span><br style="font-family: &quot;Times New Roman&quot;; font-size: 16px;<br>font-variant-numeric: normal; font-variant-east-asian: normal;"><span style="font-family: &quot;Times New Roman&quot;; font-size: 16px; font-variant-numeric: normal; font-variant-east-asian:<br>normal;">will pass the product id to itemdetails function and get all details from</span><br<br>style="font-family: &quot;Times New Roman&quot;; font-size: 16px; font-variant-numeric: normal; font-variant-east-asian: normal;"><span style="font-family: &quot;Times New<br>Roman&quot;; font-size: 16px; font-variant-numeric: normal; font-variant-east-asian: normal;">Products table passing the id and render<br>them in the itemdetails page.</span><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/tharun-12345/IS601-005_3535/pull/54">https://github.com/tharun-12345/IS601-005_3535/pull/54</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a direct link to heroku prod for this file (can be any specific item)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-tbb-fp-prod.herokuapp.com/login">https://is601-tbb-fp-prod.herokuapp.com/login</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Add to Cart </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot of the success message of adding to cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/209084930-08a4638c-c7c7-4168-829c-d4184eea41a9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the success message of adding to cart<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the error message of adding to cart (i.e., when not logged in)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/209085128-22938b1c-8856-4cb8-b88a-47ea8a814aa0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the error message of adding to cart (i.e., when not logged<br>in)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the Cart table with data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/209085180-3b97ced6-6dc5-478e-94de-ea5a03426aaf.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the Cart table with data in it<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Tell how your cart works (1 cart per user; multiple carts per user)</td></tr>
<tr><td> <em>Response:</em> <table style="font-family: &quot;Times New Roman&quot;; font-size: 16px; font-variant-numeric: normal; font-variant-east-asian: normal; text-indent: 0px;"><tbody><tr><td><p>1<br>cart per user, having product_id &amp; user_id as composite unique key</p></td></tr><br><tr><td><br></td></tr></tbody></table><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Explain the process of add to cart</td></tr>
<tr><td> <em>Response:</em> <p style="font-family: &quot;Times New Roman&quot;; font-size: 16px; font-variant-numeric: normal; font-variant-east-asian: normal;">Clicking the ADD<br>button, the product id as hidden field, quantity field gets<br>submitted to cart function<br>in shop.py,&nbsp;</p><div style="font-family: &quot;Times New Roman&quot;; font-size: 16px; font-variant-numeric: normal; font-variant-east-asian: normal;">and as<br>the product id is passed and<br>quantity is greater than 0, we insert the<br>product id, user id, desired<br>quantity, and unit_price(fetching it from products table)</div><br></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/tharun-12345/IS601-005_3535/pull/54">https://github.com/tharun-12345/IS601-005_3535/pull/54</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> User will be able to see their Cart </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the Cart View</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/209085276-21ba8cdc-e871-42e6-8d00-7cb0b1eb7344.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the Cart View<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain how the cart is being shown from a code perspective along with the subtotal and total calculations</td></tr>
<tr><td> <em>Response:</em> <p style="font-family: &quot;Times New Roman&quot;; font-size: 16px; font-variant-numeric: normal; font-variant-east-asian: normal;">When we click<br>the cart, the cart function checking there is no product<br>id being passed knows<br>that this is not a add or update function<br>and goes to SELECT block<br>getting, id, product id, name, desired quantity and<br>calculates the subtotal multiplying the desired<br>quantity and unit_price in select statement only,<br>passing user id. and passes these values<br>to cart.html.</p><div style="font-family: &quot;Times New Roman&quot;; font-size: 16px; font-variant-numeric: normal; font-variant-east-asian: normal;">For the<br>total calculation,&nbsp;</div><div style="font-family: &quot;Times New Roman&quot;; font-size: 16px; font-variant-numeric: normal; font-variant-east-asian: normal;">we render<br>each<br>item as a row in table in the HTML output and and<br>for every<br>row we add the subtotal value to the a variable ns.total<br>and later display<br>it as Total in the bottom.</div><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/tharun-12345/IS601-005_3535/pull/54">https://github.com/tharun-12345/IS601-005_3535/pull/54</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-tbb-fp-prod.herokuapp.com/login">https://is601-tbb-fp-prod.herokuapp.com/login</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> User can update cart quantity </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Show a before and after screenshot of Cart Quantity update</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/209085849-c02437a8-9023-4d64-aaf7-61dda5454f88.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot  before Cart Quantity update<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/209085871-d59512f2-eb3e-4079-8adb-93d1ce5eea0b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot after Cart Quantity update<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Show a before and after screenshot of setting Cart Quantity to 0</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/209085995-2ee9c471-1640-488e-9240-1dc5e4504c4b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot before setting Cart Quantity to 0<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/209086018-4fcf96da-f579-488a-aaba-f6df703f7c0a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot after setting Cart Quantity to 0<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Show how a negative quantity is handled</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/209086069-f278451d-3be6-4a5f-b7b8-382f92381100.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing how a negative quantity is handled<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain the update process including how a value of 0 and negatives are handled</td></tr>
<tr><td> <em>Response:</em> <p style="font-family: &quot;Times New Roman&quot;; font-size: 16px; font-variant-numeric: normal; font-variant-east-asian: normal;">In the cart,</p><div<br>style="font-family: &quot;Times New Roman&quot;; font-size: 16px; font-variant-numeric: normal; font-variant-east-asian: normal;">Beside the quantity field<br>&amp; update button a hidden product id<br>will be passed to the cart function<br>when we click the update button.<br>And in the code if the quantity &gt;<br>0,&nbsp;<br>First we get the price<br>&amp; name from products table, then we update the<br>quantity &amp; price in<br>cart table passing product id &amp; user id.</div><div style="font-family: &quot;Times<br>New Roman&quot;; font-size: 16px; font-variant-numeric: normal; font-variant-east-asian: normal;">When we pass the 0 in<br>quantity<br>field, as the quantity is less than 0, the code goes to<br>DELETE block,<br>we delete the product from cart table passing product id &amp;<br>user id.</div><div style="font-family:<br>&quot;Times New Roman&quot;; font-size: 16px; font-variant-numeric: normal; font-variant-east-asian: normal;"><br></div><div style="font-family: &quot;Times New Roman&quot;;<br>font-size: 16px; font-variant-numeric: normal; font-variant-east-asian: normal;">For the negative value handling in quantity field,<br>we set the min<br>value for the input field as 0 in HTML.</div><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/tharun-12345/IS601-005_3535/pull/54">https://github.com/tharun-12345/IS601-005_3535/pull/54</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Cart Item Removal </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a before and after screenshot of deleting a single item from the Cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/209086162-44882b7e-802b-404e-a433-d050667f0672.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> screenshot before deleting a single item from the Cart<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/209086182-622013fc-21ee-49ae-bb7e-d0848bafa804.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot after deleting a single item from the Cart<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a before and after screenshot of clearing the cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/209086206-c13c76c0-d548-4f98-a952-255fb67a6e50.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot before clearing the cart<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/57798320/209086227-78a4117d-0d1f-442e-a0e4-b0bdcb24ec00.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot after clearing the cart<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how each delete process works</td></tr>
<tr><td> <em>Response:</em> <p style="font-family: &quot;Times New Roman&quot;; font-size: 16px; font-variant-numeric: normal; font-variant-east-asian: normal;">When deleting a<br>single item in cart,</p><div style="font-family: &quot;Times New Roman&quot;; font-size: 16px; font-variant-numeric: normal; font-variant-east-asian:<br>normal;">Beside the delete button, a hidden field<br>quantity of -1 will be submitted and<br>in the cart function when the<br>quantity is less than zero, it processes the<br>Delete query passing product id.</div><div style="font-family: &quot;Times New Roman&quot;; font-size: 16px; font-variant-numeric: normal;<br>font-variant-east-asian: normal;"><br></div><div style="font-family: &quot;Times New Roman&quot;; font-size: 16px; font-variant-numeric: normal; font-variant-east-asian: normal;">When<br>clearing the<br>total cart,</div><div style="font-family: &quot;Times New Roman&quot;; font-size: 16px; font-variant-numeric: normal; font-variant-east-asian: normal;">we pass<br>a variable delete_all equal to 1, and in<br>the cart function, if the delete_all<br>value is True we delete the records<br>in Cart table passing user_id.</div><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/tharun-12345/IS601-005_3535/pull/54">https://github.com/tharun-12345/IS601-005_3535/pull/54</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <div>Got some errors while implementing cart page for couple of minutes and later<br>solved it by adding appropriate code for it. At first I got some<br>error while deploying the data to heroku, and later solved with help of<br>friends and internet.</div><div><br></div><div>Learnt how we can add the items to the cart so<br>that they will be automatically added to the cart database and also learnt<br>how to arrange list the values according to the condition given.</div><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a link to your herok prod project's login page</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-tbb-fp-prod.herokuapp.com/login">https://is601-tbb-fp-prod.herokuapp.com/login</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-005-F22/is601-milestone-2-shop-project/grade/tbb" target="_blank">Grading</a></td></tr></table>