# -*- mode: ruby -*-
# vi: set ft=ruby :

#Constants
VAGRANTFILE_API_VERSION = "2".freeze


Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  # All Vagrant configuration is done here. The most common configuration
  # options are documented and commented below. For a complete reference,
  # please see the online documentation at vagrantup.com.

  # Every Vagrant virtual environment requires a box to build off of.
  config.vm.box = "Microsoft/EdgeOnWindows10"
  # comment out config.vm.box_url if Microsoft ever fixes their vagrant cloud image
  config.vm.box_url = "./resources/boxFile/MSEdge - Win10.box"

  # Disable automatic box update checking. If you disable this, then
  # boxes will only be checked for updates when the user runs
  # `vagrant box outdated`. This is not recommended.
  config.vm.box_check_update = false

  config.vm.guest = :windows
  config.vm.communicator = :winrm
  config.winrm.transport = :plaintext
  config.winrm.username = "IEUser"
  config.winrm.password = "Passw0rd!"

  config.vm.synced_folder ".", "/vagrant", SharedFoldersEnableSymlinksCreate: false

  config.vm.define "testVm" do |testVm|
    testVm.vm.provision "file", source: "./resources/desktop/Exam Formatter.lnk", destination: "$HOME/Desktop/"
    testVm.vm.provision "file", source: "./resources/desktop/Visual CertExam Designer.lnk", destination: "$HOME/Desktop/"
    testVm.vm.provision "file", source: "./resources/desktop/Visual CertExam Manager.lnk", destination: "$HOME/Desktop/"
  end

  config.vm.provider "virtualbox" do |vb|
    vb.memory = 4096
    vb.cpus = 2

    vb.gui = true
    
    # video memory in MB
    vb.customize ["modifyvm", :id, "--vram", "32"]
    # graphics controller
    vb.customize ['modifyvm', :id, '--graphicscontroller', 'vboxsvga']
  end
end
