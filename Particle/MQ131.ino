// This #include statement was automatically added by the Particle IDE.
#include "MQ131.h"

MQ131 sensor;

void setup(){
    Particle.variable("PPB", sensor.ppb);
    sensor.init();
}

void loop(){
    sensor.loop();
}
