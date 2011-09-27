<VirtualHost *:80>

    ServerName unobtrusify.com
    ServerAdmin webmaster@theteam.co.uk
  
    LogLevel warn
    ErrorLog /var/log/apache2/unobtrusify.com.error.log
    CustomLog /var/log/apache2/unobtrusify.com.access.log combined
    LogFormat "%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i \" \"%{Cookie}i\""

    <Directory /var/www/unobtrusify.com>
        Order deny,allow
        Allow from all
    </Directory>

</VirtualHost>