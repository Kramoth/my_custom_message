# my_custom_message

## Installation
Pour installer ce package, dans le dossier source de votre catkin workspace faire un clone du package:
On supposera que votre catkin workspace s'appelle catkin_ws et se situe dans votre home, remplacer par le bon chemin suivant l'oragnisation de vos dossiers.

```sh
cd catkin_ws/src
git clone https://www.github.com/kramoth/my_custom_message.git
```

Puis compiler et sourcer le setup.bash
```sh
catkin build
source ~/catkin_ws/devel/setup.bash
rosmsg list
rosmsg show my_custom_message/my_message
```
## Utilisation

Dans un premier terminal lancer le serveur ROS
```sh
roscore
```
Dans un second terminal
```sh
source ~/catkin_ws/devel/setup.bash
rosrun my_custom_message publisher.py
```

Dans un troisieme terminal
```sh
source ~/catkin_ws/devel/setup.bash
rostopic echo /published_topic
```
