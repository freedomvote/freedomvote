.PHONY:

.SUFFIXES: .po .mo

.mo.po:
	@msgfmt $< -o $@

halt:
	@vagrant halt

bye:
	@vagrant suspend

destroy:
	@vagrant destroy -f

up:
	@vagrant up

vagrant:
	@vagrant plugin install vagrant-hostsupdater
	@vagrant up
	@vagrant ssh -c '/vagrant/envpy /vagrant/app/manage.py createsuperuser --username=admin'

dup: destroy vagrant

hup: halt up

restart-services:
	@vagrant ssh -c 'sudo service apache2 restart'
	@vagrant ssh -c 'sudo service postgresql restart'

runserver:
	@vagrant ssh -c '/vagrant/envpy /vagrant/app/manage.py runserver 0.0.0.0:8000'

makemessages:
	@vagrant ssh -c 'cd /vagrant/app; /vagrant/envpy /vagrant/app/manage.py makemessages -l de'

compilemessages:
	@vagrant ssh -c 'cd /vagrant/app; /vagrant/envpy /vagrant/app/manage.py compilemessages'

collectstatic:
	@vagrant ssh -c 'cd /vagrant/app; /vagrant/envpy /vagrant/app/manage.py collectstatic'
	@vagrant ssh -c 'cd /vagrant/app; /vagrant/envpy /vagrant/app/manage.py collectstatic_js_reverse'

dev-collectstatic:
	@vagrant ssh -c 'cd /vagrant/app; /vagrant/envpy /vagrant/app/manage.py collectstatic_js_reverse'
	@vagrant ssh -c 'mv /vagrant/app/static/django_js_reverse/ /vagrant/app/core/static/django_js_reverse/'
