Step 1: Creat a lecture file

```sh
sudo vim /etc/sudo_lecture.txt
```

Sample `lecture` text
```
     ^[[00;32m  \^V//
     ^[[00;33m  |^[[01;37m. ^[[01;37m.^[[00;33m|   ^[[01;34m I AM ROOT!
     ^[[00;32m- ^[[00;33m\ - / ^[[00;32m_
     ^[[00;33m \_| |_/
     ^[[00;33m   \ \
     ^[[00;31m __^[[00;33m/^[[00;31m_^[[00;33m/^[[00;31m__
     ^[[00;31m|_______|  ^[[00;37m With great power comes great responsibility.
     ^[[00;31m \     /   ^[[00;37m Use sudo wisely.
     ^[[00;31m  \___/
^[[0m

```


Step 2: Run the following command

```sh
sudo visudo
```

Step 3: Add the following line in the opened file

```sh
Defaults       lecture=always
Defaults       lecture_file=/etc/sudo_lecture.txt
```

Step 4: Save and close that file and reset user cache

```sh
sudo --reset-timestamp
```

Now try any sudo command

[source](https://www.cyberciti.biz/open-source/command-line-hacks/adding-spice-to-your-sudo-session-with-a-lecture-file-on-linux-or-unix/)


