---
- hosts: dbservers
  remote_user: root
  tasks:
  - name: Update all packages to the latest version
    apt:
      upgrade: dist
      update_cache: yes
  - name: Ensure redis is the latest version
    apt:
      name: redis-server
      state: present
  - name: Ensure redis is running
    service:
      name: redis-server
      state: started
