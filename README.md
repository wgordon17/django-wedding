# Deploying

## nginx

```bash
$ sudo dnf install nginx
$ sudo ln -s /path/to/Wedding/root/www.stephandwill.com.conf /etc/nginx/conf.d/www.stephandwill.com.conf
# Install SELinux module to grant nginx permissions to write to sockets
$ sudo semodule -i nginx.pp
```

## Lets Encrypt

```bash
$ sudo dnf install certbot
$ sudo pip install certbot-nginx
$ sudo certbot --nginx -d stephandwill.com -d www.stephandwill.com -d willandsteph.com -d www.willandsteph.com
```

Add `0 12 * * * /usr/bin/certbot renew --quiet` within `sudo crontab -e`
> https://www.nginx.com/blog/using-free-ssltls-certificates-from-lets-encrypt-with-nginx/

## python

```bash
$ source /path/to/Wedding/root/../py-venvs/Wedding/bin/activate
$ pip install -r /path/to/Wedding/root/requirements.txt
```

## Services/Gunicorn

```bash
$ sudo echo "d /run/gunicorn-wedding 0755 <someuser> <somegroup> -" > /etc/tmpfiles.d/gunicorn-wedding.conf
```
> http://docs.gunicorn.org/en/stable/deploy.html#systemd

```bash
$ sudo systemd-tmpfiles create
```
> The above _may_ be needed
> https://developers.redhat.com/blog/2016/09/20/managing-temporary-files-with-systemd-tmpfiles-on-rhel7/

```bash
$ sudo systemctl enable /path/to/Wedding/root/gunicorn-wedding.socket
$ sudo systemctl enable /path/to/Wedding/root/gunicorn-wedding.service
```
> https://unix.stackexchange.com/a/344843

```bash
$ sudo systemctl start gunicorn-wedding.socket
```

# Troubleshooting

## SELinux

```bash
sudo tail -F /var/log/audit/audit.log
```
> How to create a module to allow permissions comes from http://nts.strzibny.name/allowing-nginx-to-use-a-pumaunicorn-unix-socket-with-selinux/
```bash
$ sudo grep nginx /var/log/audit/audit.log | audit2allow -m nginx > nginx.te
$ checkmodule -M -m -o nginx.mod nginx.te
$ semodule_package -o nginx.pp -m nginx.mod
$ sudo semodule -i nginx.pp
```

## Services/Gunicorn

```bash
$ systemctl status gunicorn-wedding.socket
$ systemctl status gunicorn-wedding.service
```

### Reloading everything after config changes

```bash
$ sudo systemctl daemon-reload && sudo rm /run/gunicorn-wedding/socket && sudo systemctl stop gunicorn-wedding.socket && sudo systemctl stop gunicorn-wedding.service && sudo systemctl stop nginx && sudo systemctl start gunicorn-wedding.socket && sudo systemctl start gunicorn-wedding.service && sudo systemctl start nginx
```

## Nginx

```bash
$ sudo tail -F /var/log/nginx/wedding-error.log
$ sudo nginx -t
```
> Test nginx configurations
```bash
$ sudo systemctl reload nginx
```
