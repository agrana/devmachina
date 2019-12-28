# Create key and authorize it.
KEYPRESENT=$(stat ~/.ssh/id_rsa)
if [ -z $KEYPRESENT ]; then
   ssh-keygen -b 4096 &&\
   cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
fi
# Ansible should be installed.
ANSIBLE=$(which ansible-playbook)
if [ -z $ANSIBLE ]; then
	sudo apt-get install ansible
fi