# PasswordManager
<p>A Python project which uses SQLite to create and store usernames and passwords, as well as the website name.</p>

---
Research Needed:
1. How does a password manager works?
2. How does hashing work?
3. Is there any extensions I need to use to allow Python to interact with the SQLlite database?
---
Research Results:
1. There are 3 main types of password managers:
    1. Offline - The passwords are stored locally
    2. Online - The passwords are stored on a remote server
    3. Token-based / Stateless - A physical hardware, such as a USB, which contains a key to unlock a user's account
    
    <p>I will be creating an <b>offline password manager</b> which will use SQLcipher to encrypt an SQLite database.</p>
    <p>Source: <a href="https://cybernews.com/best-password-managers/how-do-password-managers-work/">https://cybernews.com/best-password-managers/how-do-password-managers-work/</a></p><br>

2. Hashing changes the input into a series of characters, letters and numbers, using an hashing algorithm. The length of the hash will depend on the hash funtion used and the size of the hash will always be the same length, whether it be the input is 1 character or 100 characters.<br>
    <p>Source: <a href="https://thycotic.com/company/blog/2020/05/07/how-do-passwords-work/">https://thycotic.com/company/blog/2020/05/07/how-do-passwords-work/</a></p><br>

3. A Python module called pysqlcipher3 can be used to allow a python script to interact with an encrypted SQLite database.<br>
    <p>Source: <a href="https://github.com/rigglemania/pysqlcipher3">https://github.com/rigglemania/pysqlcipher3</a></p><br>
