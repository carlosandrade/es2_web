#!/usr/bin/python
import cgi
<html>
<head>
<title> Bla </title>
</head>
<body>
<form action="/cgi-bin/hello_get.py" method="post">
First Name: <input type="text" name="first_name"><br />
Last Name: <input type="text" name="last_name" />

<input type="submit" value="Submit" />
</form>
</body>
</html>
