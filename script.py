# -*- coding: utf-8 -*-

import os

def create_nginx_site_conf():
    # Demander les informations nécessaires
    domain_name = input("Entrez le nom de domaine principal (ex : pixelserver.fr) : ")
    additional_domain = input("Entrez un domaine supplémentaire (ex : www.pixelserver.fr) ou laissez vide : ")
    root_path = input("Entrez le chemin du répertoire racine du site (ex : /home/root/pixelserver.fr) : ")

    # Générer la configuration Nginx
    server_name = f"{domain_name} {additional_domain}" if additional_domain else domain_name
    nginx_conf_content = f'''
server {{
    listen 80;
    listen [::]:80;

    root {root_path};
    index index.html;
    server_name {server_name};

    location / {{
        try_files $uri $uri/ =404;
    }}

    error_page 404 /error.html;

    location = /error.html {{
        root {root_path};
        internal;
    }}
}}
    '''
    
    # Créer le fichier de configuration
    conf_filename = f"/etc/nginx/sites-available/{domain_name}.conf"
    with open(conf_filename, "w") as conf_file:
        conf_file.write(nginx_conf_content)
    
    # Créer le lien symbolique
    os.system(f"ln -s {conf_filename} /etc/nginx/sites-enabled/{domain_name}.conf")

    print(f"Configuration Nginx créée pour {domain_name}.")
    print(f"Fichier de configuration : {conf_filename}")
    
if __name__ == "__main__":
    create_nginx_site_conf()
