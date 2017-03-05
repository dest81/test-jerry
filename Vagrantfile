# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/xenial64"

  config.vm.synced_folder "../words/", "/srv/words", create: true

  config.vm.provider "virtualbox" do |vb|
    # Customize the amount of memory on the VM:
    vb.memory = "2048"
    # vb.cpus = 1
  end

  config.vm.hostname = "test"
  # config.vm.network :private_network, ip: '192.168.0.101'
  config.vm.network "forwarded_port", guest: 8000, host: 8000

  config.vm.provision "shell", inline: <<-SHELL
    sudo apt-get update
    sudo apt-get install -y python python-pip
    pip install -r /srv/words/requirements.txt
  SHELL

  config.vm.provision "shell", run: "always", inline: <<-SHELL
    python /srv/words/manage.py runserver 0.0.0.0:8000 &
    echo "Started!"
  SHELL

end
