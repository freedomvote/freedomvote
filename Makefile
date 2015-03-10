.PHONY:

.SUFFIXES: .po .mo

.mo.po:
	@msgfmt $< -o $@

vagrant-halt:
	@vagrant halt

vagrant-suspend:
	@vagrant suspend

vagrant-destroy:
	@vagrant destroy -f

vagrant-up:
	@vagrant up

vagrant:
	@vagrant plugin install vagrant-hostsupdater
	@vagrant up

vagrant-restart: vagrant-destroy vagrant-up

vagrant-restart-services:
	@vagrant ssh -c 'sudo service apache2 restart'
	@vagrant ssh -c 'sudo service postgresql restart'

vagrant-runserver:
	@vagrant ssh -c '/vagrant/envpy /vagrant/app/manage.py runserver 0.0.0.0:8000'

vagrant-makemessages:
	@vagrant ssh -c 'cd /vagrant/app; /vagrant/envpy /vagrant/app/manage.py makemessages -l de'

vagrant-compilemessages:
	@vagrant ssh -c 'cd /vagrant/app; /vagrant/envpy /vagrant/app/manage.py compilemessages'

vagrant-collectstatic:
	@vagrant ssh -c 'cd /vagrant/app; /vagrant/envpy /vagrant/app/manage.py collectstatic'
	@vagrant ssh -c 'cd /vagrant/app; /vagrant/envpy /vagrant/app/manage.py collectstatic_js_reverse'

vagrant-collectstatic-dev:
	@vagrant ssh -c 'cd /vagrant/app; /vagrant/envpy /vagrant/app/manage.py collectstatic_js_reverse'
	@vagrant ssh -c 'mv /vagrant/app/static/django_js_reverse/ /vagrant/app/core/static/django_js_reverse/'
