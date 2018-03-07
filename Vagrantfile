# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|

  config.vm.define "xe1" do |node|
    node.vm.box = "iosxe/16.07.01"
    node.vm.provider "virtualbox" do |v|
          v.memory = 2048
    end
    node.vm.network "forwarded_port", guest: 22, host: 1122, id: 'ssh', auto_correct: true
    node.vm.network :private_network, virtualbox__intnet: "link1", auto_config: false
    node.vm.network :private_network, virtualbox__intnet: "link2", auto_config: false
  end
  config.vm.define "xe2" do |node|
    node.vm.box = "iosxe/16.07.01"
    node.vm.provider "virtualbox" do |v|
          v.memory = 2048
    end
    node.vm.network "forwarded_port", guest: 22, host: 2122, id: 'ssh', auto_correct: true
    node.vm.network :private_network, virtualbox__intnet: "link1", auto_config: false
    node.vm.network :private_network, virtualbox__intnet: "link3", auto_config: false
  end
  config.vm.define "xe3" do |node|
    node.vm.box = "iosxe/16.07.01"
    node.vm.provider "virtualbox" do |v|
          v.memory = 2048
    end
    node.vm.network "forwarded_port", guest: 22, host: 3122, id: 'ssh', auto_correct: true
    node.vm.network :private_network, virtualbox__intnet: "link2", auto_config: false
    node.vm.network :private_network, virtualbox__intnet: "link3", auto_config: false
  end


  #Use Ansible to provision boxes
  #config.vm.provision "ansible" do |ansible|
  #  ansible.playbook = "vagrant_provision.yaml"
  #  ansible.inventory_path = "inventory/vagrant.yaml"
  #  ansible.raw_arguments = ["--connection=paramiko"]
  #end
end
