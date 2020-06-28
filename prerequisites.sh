# Create key and authorize it.
# The connection could be changed in ansible to use local and avoid this.
# This works with the default ansible config.
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
mkdir -p ~/environment
cd ~/environment && git clone https://github.com/agrana/devmachina.git

