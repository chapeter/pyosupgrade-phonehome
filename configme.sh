#!/bin/bash
hostname=$1
ansible-playbook -i inventory/live.yml push_config.yml --limit $hostname  > ansible.log
