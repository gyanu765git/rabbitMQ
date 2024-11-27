# rabbitMQ

sudo apt-get update -y && sudo apt-get upgrade -y

apt install net-tools -y

curl -1sLf 'https://dl.cloudsmith.io/public/rabbitmq/rabbitmq-erlang/setup.deb.sh' | sudo -E bash

sudo apt install rabbitmq-server -y

sudo systemctl is-enabled rabbitmq-server

sudo systemctl status rabbitmq-server

ss -tulpn

sudo nano /etc/rabbitmq/rabbitmq-env.conf

NODENAME=rabbitmq
NODE_IP_ADDRESS=your domain or IP
NODE_PORT=5672

sudo systemctl restart rabbitmq-server

ss -tulpn | grep 5672

sudo rabbitmq-plugins enable rabbitmq_management

rabbitmqctl add_user gy_admin gy1234!
rabbitmqctl set_user_tags gy_admin administrator
rabbitmqctl set_permissions -p / gy_admin ".*" ".*" ".*"

sudo systemctl restart rabbitmq-server

ss -tulpn

sudo ufw enable

sudo ufw allow ssh

sudo ufw allow http

sudo ufw allow https

sudo ufw allow 5672 && sudo ufw reload

sudo ufw status verbose

sudo ufw allow 15672 && sudo ufw reload
