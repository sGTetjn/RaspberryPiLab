# RaspberryPiLab
Descripcion de la modificacion realizada en el sistema psicometrico de el laboratorio.

El unico codigo necesario para utilizar la pantalla, es el codigo de screen.py, que a su vez requiere la biblioteca de GPIO y pygame.
En cuanto a las conexiones, se debe conectar la PCB a los pines tierra, pin 17 y pin 18 de la Raspberry Pi, y en el otro lado simplente se conecta el cable, que se diseño para solo poder conectarse en una direccion, y el otro lado del cable se conecta a los dos primeros conectores de la caja que se encarga de evitar el rebote en los botones.

La interfaz grafica esta basada en la biblioteca de PyGame, por lo que para modificarse es conveniente aprender los principios basicos, y para mandar la señal de regreso a el circuito antirrebotes, se usa la libreria de GPIO, que tambien es conveniente aprender para agregar mas funcionalidad, o cambiar los pines que se utilizan.

Actualmente se utilizan los pines 17 y 18 para mandar las señales, pero esta decision es arbitraria, se puede utilizar cualquier pin, mientras este tenga capacidades de PWM (Power Wave Modulation).

<img width="462" alt="{631F12EC-8A19-4CA5-A3E9-25D4641134E1}" src="https://github.com/user-attachments/assets/eeace999-7217-4359-b677-62bd2c45751b" />
Esquema de la PCB.

![image](https://github.com/user-attachments/assets/db10893f-e55e-48ab-971e-b9dcdc386a5f)

![image](https://github.com/user-attachments/assets/2e706b93-766c-45e6-8927-261293a4f9d7)

![image](https://github.com/user-attachments/assets/93123d4b-61b5-43a2-874c-01686146d2b4)


https://github.com/user-attachments/assets/b4657882-f451-426d-b671-6650030cd52a


