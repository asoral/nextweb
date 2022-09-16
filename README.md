## nextwebsite

nextwebsite

#### License

MIT
<!-- {% set doc = frappe.get_doc("Website Builder") %} -->
<!-- <img src ="{{doc.hero_image}}" style="z-index:-1;position:absolute;height:550px;width: 1740px; margin-left:70px;margin-right:70px;overflow-x: hidden;"/> -->



UI should be run while logged out for better experience. Or UI and app can be operated on same time with two different browser for better performance. 
			



<br>
<div class="sticky-menu theme-menu-four container-fluid" style="background-color: ##f9fafa;border-bottom: black 2px solid;height:100px;overflow-y:hidden; margin-top:-30px;width:100%;overflow-y:hidden;">
					   <div class="d-flex align-items-center justify-content-between">
						   <div class="logo">
							{% set doc = frappe.get_doc("Website Builder") %}
							<a href="http://localhost:3000/"><img src="{{doc.company_logo}}" alt=""></a>
							
						   </div>
						   <nav id="mega-menu-holder" class="navbar navbar-expand-lg">
							   <div  class="container nav-container">
								   <button class="navbar-toggler">
									   <span></span>
								   </button>
								  <div class="navbar-collapse collapse" id="navbarSupportedContent">
										  <div class="d-lg-flex align-items-center">
											  <ul class="navbar-nav">
												  
											   <li class="nav-item dropdown">
												   <a class="nav-link dropdown-toggle" href="#" data-toggle="dropdown" style="color:#326799;;"><b>BUY EQUIPMENTS</b></a>
												   <ul class="dropdown-menu">
													   <li>
														   <a href="" class="dropdown-item" style="color:black;">Product 1</a>
													   </li>
													   <li>
														   <a href="" class="dropdown-item" style="color:black;">Product 2</a>
													   </li>
													   <li>
														   <a href="" class="dropdown-item" style="color:black;">Product 3</a>
													   </li>
													   <li>
														   <a href="" class="dropdown-item" style="color:black;">Product 4</a>
													   </li>
													   
												   </ul> <!-- /.dropdown-menu -->
											   </li>
	   
											   <li class="nav-item dropdown">
												   <a class="nav-link" href="#" style="color:#326799;" ><b>OUR PLATFORM</b></a>
												   
											   </li>	   
										  </ul>
											  <ul class="right-button-group d-flex align-items-center justify-content-center" style="margin-left: 30px;">
												  <li style="background-color:#326799; height: 60px;width: 200px;border-radius: 30px;">
												   <a href="custom_login#custom" class="signIn-action" style="text-align: center;padding-left:72px;margin-top:10px;color: white;">LOGIN</a>
											   </li>
										 </ul>
										 <ul class="right-button-group d-flex align-items-center justify-content-center">
											<li style="margin-right: 20px;" ></li>
										</ul>
										   <ul class="right-button-group d-flex align-items-center justify-content-center">
											<li style="background-color:#689769; height: 60px;width: 200px;border-radius: 30px;margin-right: 20px;">
											 <button><a href="custom_login#signup" class="signIn-action" style="text-align: center;padding-left:65px;margin-top:10px;color: white; ">SIGN UP</a></button>
										  </li>
										 
									       </ul>
									   
										  </div>
									  </div>
							   </div> 
						   </nav>
					   </div>
				   </div> <!-- /.theme-main-menu -->
