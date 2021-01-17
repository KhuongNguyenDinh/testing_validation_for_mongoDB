<html> 
<head> 
	<meta charset="UTF-8"> 
	<style> 
		h3 { 
			text-align: center; 
		} 
		img { 
			display: block; 
			margin: auto; 
			height: 150px; 
			width: 150px; 
		} 
		.input { 
			margin: 6px; 
			padding: 10px; 
			display: block; 
			margin: auto; 
			color: palevioletred; 
			font-size: 30px; 
		} 
		input { 
			width: 90%; 
			display: block; 
			margin-left: 12px; 
			background: none; 
			background-color: lightyellow; 
		} 
		select { 
			width: 90%; 
			display: block; 
			margin-left: 12px; 
			background: none; 
			background-color: lightyellow; 
		} 
		#heading { 
			font-family: cursive; 
			text-align: center; 
			color: green; 
			padding-top: 20px; 
		} 
		#form_page { 
			height: 500px; 
			width: 50%; 
			display: flex; 
			flex-wrap: wrap; 
			flex-direction: row; 
			margin: auto; 
		} 
		#form_body { 
			border-radius: 12px; 
			height: 330px; 
			width: 450px; 
			background-color: beige; 
			border: 1px solid pink; 
			margin: auto; 
			margin-top: 12px; 
		} 

		#text { 
			color: red; 
			width: 100px; 
		} 

		#head { 
			border-bottom: 2px solid red; 
			height: 100px; 
			background-color: aliceblue; 
		} 

		#submit { 
			background-color: white; 
			width: 70px; 
		} 
	</style> 

</head> 
<body> 
	<form method="post" action="convert.php"> 
		<div id="form_page"> 
			<div id="form_body"> 
				<div id="head"> 
					<h1 id="heading">Register form</h1> 
				</div> 
				<br /> 
				<div id="input_name" class="input"> 
					<input id="nickname" type="text"
						Placeholder="Nickname" name="nickname"
						required> 
				</div> 
				<div id="input_username" class="input"> 
					<input id="input_username" type="text" placeholder= 
						"Username" name="username" required> 
				</div> 
				<div id="input_password" class="input"> 
					<input id="input_password" type="text"
						placeholder="Password" name="password" required> 
				</div> 
				<div id="input_phone" class="input"> 
					<input id="input_phone" type="text"
						name="phone"
						placeholder="Phone" required> 
				</div> 
				<div id="input_email" class="input"> 
					<input id="input_email" type="text"
						name="email"
						placeholder="Email" required> 
				</div> 
				<div class="id input"> 
					<input id="submit" type="submit"
						name="submit" value="submit"
						onclick="on_submit()"> 
				</div> 
			</div> 
		</div> 
	</form> 
</body> 
</html> 
<?php 
    if ($_SERVER['REQUEST_METHOD'] == 'POST') {   
        function get_data() { 
            $datae = array(); 
            $datae[] = array( 
                'Name' => $_POST['name'], 
                'Branch' => $_POST['branch'], 
                'College' => $_POST['college'], 
            ); 
            return json_encode($datae); 
        } 
        $name = "gfg"; 
        $file_name = $name . '.json'; 
       
        if(file_put_contents( 
            "$file_name", get_data())) { 
                echo $file_name .' file created'; 
            } 
        else { 
            echo 'There is some error'; 
        }} 
?> 