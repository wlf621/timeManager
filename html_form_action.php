<?php
    $time = $_GET["time"]; //You have to get the form data
    $event = $_GET["event"];
	
	
	$dbhost = 'localhost';  // mysql服务器主机地址
	$dbuser = 'root';       // mysql用户名
	$dbpass = 'wanwan621x'; // mysql用户名密码
	$conn = mysqli_connect($dbhost, $dbuser, $dbpass);
	if(! $conn )
	{
		die('Could not connect: ' . mysqli_error());
	}
	echo "数据库连接成功!\r\n";

	mysqli_query($conn , "set names utf8");

	$sql = "insert into test".
        "(time, event) ".
        "VALUES".
        "('$time','$event')";
		
	mysqli_select_db( $conn, 'timeManager' );
	$retval = mysqli_query( $conn, $sql );
	if(! $retval )
	{
		die('无法插入数据: ' . mysqli_error($conn));
	}
	echo "数据插入成功\n";
	mysqli_close($conn);
?>
