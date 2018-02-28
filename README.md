# infra

This is my personal cloud infrastructure.

Currently it consists of a few EC2 t2.nano nodes running debian.
The inventory is at present static and requires manual spinup of
the nodes and manual DNS setup.

**DISCLAIMER!!!**

Under normal circumstances I would consider it a very bad idea to
make a repository such as this public, as it provides a detailed
blueprint for hackers to attack one's services. However, this
infrastructure exists only for personal demonstration and learning
purposes, contains no sensitive information, and is of no
commercial value.

## Why

I manage a tiny personal cloud infrastructure as a learning and
professional development experience, as well as to host a small
personal website. Things I hope to accomplish here:

- Improve general cloud infrastructure and operational skills
- Learn ansible
- Learn new database systems
- Generally explore building interesting-to-me web services
- Keep my personal website easy to set up and maintain

## Setup Instructions

- Create a virtual environment and pip install pacakges in `requirements.txt`
- Create a secure `.secrets` directory outside this repository and fill in
  expected values, create certificates, etc...
- Modify `group_vars/all` values to point at EC2 private key and the
  `.secrets` directory.
- Set up required nodes in EC2, setup DNS to point at the nodes, see
  `hosts` for expected inventory
- Run `ansible-playbook -i hosts infra.yml`

## Other Stuff

- To only update the static jekyll website and save time debugging, run `ansible-playbook -i hosts infra.yml --tags "ericwebsite-update"`
