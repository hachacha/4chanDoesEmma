<html>
	<head>
		<title>EMMA BY 4CHAN</title>
		<style>
			
.texty a {
    background-color: snow;
}
.texty {
    font-size: .85em;
    color: black;
    background-color: #eca9e4;
}
a {
    background-color: yellow;
}
	

		</style>
		<script>
			    function foo() {
			        var isShowing = document.getElementById("wishes").style.visibility;
			        if(isShowing=="visible"){
			        	document.getElementById("wishes").style.visibility="hidden";
			        }
			        else{
			        	document.getElementById("wishes").style.visibility="visible";
			        }
			    }
			    setInterval(foo, 300);
			}
		</script>
	</head>
	<body>
		<center>
			<p>runs a search every 7 hours</p>
			<p>it's <b>all</b> of 4chan</p>
			<img src="http://www.sumcct.org/assets/images/animated-coffee-doughnut.gif"/>
			<div id="wishes">
				<p style="color:red;font-size:2em;"><blink>MERRY CHRISTMAS, EMMA</blink></p>
				<p style="color:red;font-size:2em;"><blink>WITH <b>LOVE</b> FROM, <i>JON</i></blink></p>
			</div>
		</center>
<?php
$run = $_GET['r'];
include("incl/conn.php");

$crawl = mysqli_query($conn, "SELECT * FROM crawl WHERE exist = 1;");
	while($rows = mysqli_fetch_array($crawl)){
		echo "<h2>".$rows['board']."</h2>";
		echo "<div id='".$rows['id']."'>";
			echo "<a href='".$rows['url']."'>".$rows['title']."</a>";
			echo "<blockquote class='texty'>".$rows['body']."</blockquote>";
		echo "</div>";
	}
	//mysql_close($conn);



?>
<center>
	<img src="sde.jpeg"/>
	<p>words used:</p>

		<i>"petite","feet","gluten","shrill","annoying","stompy","cutie",
		"publications","kitties","stampy","nervous","self-deprecating","insecure",
		"A-cup","snickers","grumpy","pale","anal","breakable", "white","gaydrunk","smart",
		"opinionated","cooldrunk","tapeworm","compact", "emma","valley","cuba","irate","pouty","bitchface",
		"toilet", "books", "journalism", "white","rhode", "coffee", "adderall", "wine", "whiskey", "sister", "bangs", 
		"fringe", "lotr", "lord", "hobbit", "frump", "bolano", "roberto", "lipstick","baltimore", "bobbing", "apples", "beyonce"
		"chat"</i>
</center>
</body>
</html>
