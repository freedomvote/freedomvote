#!/bin/bash
# vim:sw=4:ts=4:et:

export DEBIAN_FRONTEND=noninteractive

source /vagrant/tools/vagrant/provision_funcs.sh

disable_ipv6
install_packages
install_requirements
setup_postgres
enable_services
prepare_database
prepare_django
configure_apache

# Make sure the return code is zero, so vagrant doesn't break things
exit 0
