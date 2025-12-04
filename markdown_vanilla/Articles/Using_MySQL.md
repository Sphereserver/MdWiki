## Installation

In order to use MySQL for your SphereServer, you must first install MySQL onto your computer. You can find a tutorial on how to install MySQL in the [MySQL Reference Manual](http://dev.mysql.com/doc/mysql/en/installing.html).

After you have installed MySQL, you will need to configure Sphere to connect to your MySQL server. Open Sphere.ini, and scroll down until you see the section beginning with "// MySql configuration." This is where you will fill in all of your basic MySQL information.

Replace these lines with the correct information corresponding to your server:

MySql=1 // This must be set to 1 for MySQL to be enabled. MySqlHost=localhost // The address to your MySQL db host. MySqlUser=root
```
// Replace this with your MySQL username. MySqlPassword=password //
```
Replace this with your MySQL password. MySqlDatabase=sphere // This is the name of your MySQL database.

You will also need to navigate to your scripts folder, and open the file sphere_serv_triggers.scp. You now need to find the definition for the function `f_onserver_start`, and place the following line inside the function:

DB.CONNECT

This will make sure Sphere connects to the MySQL database. You can also add some error checking to make sure it is connected by adding the following lines after that:

```
IF (\<DB.CONNECTED\>)

`   SERV.LOG MySQL debug: MySQL successfully connected!`

ELSE

`   SERV.LOG MySQL debug: MySQL not connected!`

ENDIF
```

```
If you find the line "*MySQL debug: MySQL not connected!*" in your console, this means that Sphere could not connect, and there is probably an error in either your Sphere.ini configuration, or your MySQL installation.

```
## Sphere Commands
```

MySQL has a number of basic commands you will need to know. In Sphere, these commands differ slightly in use, because they have to be used in conjunction with Sphere commands.

In Sphere, all MySQL commands will begin with the **DB** object. You can view a full list of all the properties and functions of the DB object in the [Database](Database "wikilink") object page of the [Reference Compendium](:Category:Reference_Compendium "wikilink").

```
### DB Properties
```

Syntax: \<DB.\<*property*\>\>

```
|  |  |
|----|----|
| **Property** | **Description** |
| CONNECTED | Returns 1 if the server is connected to MySQL, and 0 if it is not. |
| ROW.NUMROWS | The number of rows returned by the last query. |
| ROW.NUMCOLS | The number of columns returned by the last query. |
| ROW.\* | A list of all of the columns returned by the last query. Both column names and numbers are saved in the list, so you can reference them using indexes (1,2,3) or column names (id, name, etc.). |
```

```
### DB Methods
```

Syntax: DB.\<*method*\>

```
|  |  |
|----|----|
| **Method** | **Description** |
| CLOSE | Disconnects from the MySQL server. |
| CONNECT | Connects to the MySQL using the information supplied in Sphere.ini. |
| EXECUTE | Executes the given MySQL commands without returning any information. |
| QUERY | Returns information from the MySQL database, filling the ROW.\* properties. |
```

```
## Examples
```

```
### Creating a Table and Inserting Data
```

This section is just a few basic examples to get you started into the MySQL+Sphere world.

What you'll need to do to begin with MySQL is to create a table to put your data in. The following is an example, with an explanation afterwards.

DB.EXECUTE "create table demo (id int unsigned not nullauto_increment primary key,account varchar(15), name varchar(15),guild text,kills int,fame int,karma int);"

**DB.EXECUTE**
This is just Sphere's command to execute a statement in MySQL.

**create table demo**
This tells MySQL to create a table named 'demo', with the enclosed information.

**id int unsigned not null auto_increment primary key**
This creates a column named 'id', that holds the id number for the entry. You could really just use the row number for the id number, but this allows us to access it through PHP if you wanted to also make a PHP website through your shard (PHP tutorials will come later). The 'not null auto_increment' part means that whenever you add a new row, you will just set id as 'NULL' and MySQL will replace it with the next id number. So if you have 3 rows and you insert a new one, MySQL will automatically set it as id '4'.

**account varchar(15)**
varchar(15) means that it can be a text-entry with 15 characters or less. Most accounts only consist of a few characters, so it shouldn't ever really be longer than 15.

**name varchar(15)**
Same as 'account varchar(15)'.

**guild text**
This is where the name of the guild goes. Since some guild names can be quite long, I simply set this as "text", because it allows it to be of an infinite length.

**kills int**
Just an integer column for holding the number of kills a player has.

**fame int**
An integer column for holding the fame a player has.

**karma int**
An integer column for holding the karma a player has.

Now that the fields have been explained, we need to insert information into the table. To do this, we'll use the following command:

DB.EXECUTE "INSERT INTO demo(id, account, guild, kills,fame, karma) values (NULL,<ACCOUNT>,\<MEMORYFINDTYPE.MEMORY_GUILD.NAME\>,<KILLS>,<FAME>,<KARMA>);"

This command will make the table of information look something like this:

```
|          |        |             |              |           |          |           |
|----------|--------|-------------|--------------|-----------|----------|-----------|
| **demo** | **id** | **account** | **guild**    | **kills** | **fame** | **karma** |
| row.1    | 1      | warangel    | Staff_Ownage | 2         | 15,000   | -7,000    |
```

```
### Simple MySQL and PHP Output Tutorial
```

```
#### Introduction
```

This article is designed to be a tutorial to explain how to use Sphere's MySQL capabilities to create output to your shard's webpage via PHP.

```
#### Create The Table
```

The first thing we will need to do is to create the table which we will use to store our information. This table will store the following information for our sample system: the integer 'id', used to store the id number of the added row; the varchar 'account' with a length of 30, used to store the current account name; the varchar 'name' with a length of 30, used to store the current player name; the text block 'guild', used to store the current guild's name; the integer 'kills', used to store the amount of kills the player has; the integer 'fame', used to store the amount of fame the current player has; and the interger 'karma', which is used to store the amount of karma the current player has. The code I used to create this table is the following:

\[FUNCTION create_table\] DB.EXECUTE "create table demo (id int unsigned not null auto_increment primary key, accountvarchar(15), name varchar(15), guild text, kills int, fame int, karma int);"

```
#### Insert The Data
```

The next thing we will need to do is insert some information into the table we just created. The following function will insert data about your own character into the table:

\[FUNCTION insert_info\] DB.EXECUTE "insert into demo (id,account, name, guild, kills, fame, karma) values (NULL, '<ACCOUNT>','<NAME>', '\<MEMORYFINDTYPE.memory_guild.LINK.NAME\>', <KILLS>, <FAME>, <KARMA>);"

```
#### Read The Data
```

Now that we actually have some information in our MySQL table, we need to create a PHP file to read the information from the table and display it. Create a file named sphere_info.php, and then insert the following code into it.

    <html> <head> <title>sphere_info</title> </head>

    <body> <?php

        //fill in your mysql information here $hostname = "localhost"; $username = "root"; $password = "password"; $database = "database_name";

        //the tablename demo was used for this tutorial. change this to the actual name of the table. $table = "demo";

        //connects to mysql and selects the corresponding database. mysql_connect($hostname,$username,$password); mysql_select_db($database);

        //selects all rows from the provided table name. $query = "select * from $table"; $result = mysql_query($query);

        //this if makes sure there is information in the table. if there isn't, there will be no output. if (mysql_num_rows($result) > 0) { //this creates a variable named $query_data and fills it with the information from the first row. //using a while statement, this will repeat for each row the table contains. while ($query_data = mysql_fetch_array($result)) { //we create new variables for each different column in the row. $id = $query_data['id']; $account = $query_data['account']; $name = $query_data['name']; $guild = $query_data['guild']; $kills = $query_data['kills']; $fame = $query_data['fame']; $karma = $query_data['karma'];

                //this is where you can format your output using html. $echo = "$id - $account - $name - $guild - $kills - $fame - $karma<br>";

                //this displays the actual output. echo $echo; } }

    ?>

    </body> </html>

```
#### Output
```

The output we receive using this method of reading the table should look something like the following:

    1 - god - God - PWNAGE - 1 - 1000 - 1000 2 - warangel - WarAngel - 4HM - 15 - 1000 - 5000

```
#### Conclusion
```

This method of writing to the table and reading using PHP can be used to create nearly anything you can imagine in terms of data storage and retrieval systems. Something like this could be combined to make an online interactive control panel for your shard administrators, a duel system that shows scores online, or any number of things. Where there's a will there's a way, and with this article you now have both.

[Category:Articles](Category:Articles "wikilink")
```
