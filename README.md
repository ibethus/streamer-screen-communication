# Streamer screen comunication
Ce script permet de vérifier périodiquement l'état de l'audio diffusé par ALSA.
Lorsqu'un changement est repéré, il est répercuté sur l'écran via le port usb.

## Config
Le fichier de [service](./streamer_screen.service) permet de configurer le script en tant que service linux.
Penser à modifier les placeholder dans le fichier.
Une fois cette étape complétée, exécuter les commandes suivantes :

```sh
sudo cp my_python_app.service /etc/systemd/system/
sudo systemctl enable my_python_app.service
sudo systemctl start my_python_app.service
```