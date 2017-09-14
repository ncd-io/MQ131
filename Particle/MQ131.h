#include "Particle.h"

class MQ131{
public:
    void setAddress(int a0, int a1);
    int address=0x50;
    void init();
    void loop();
    
    void takeReading();
    double ppb=0;
};
