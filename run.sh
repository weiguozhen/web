#source /etc/profile
#!/bin/bash -ilex
source ~/.bash_profile
echo $PATH
robot -P . tc
