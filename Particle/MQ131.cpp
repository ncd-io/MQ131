#include "MQ131.h"

void MQ131::setAddress(int a0, int a1){
    if(a0 > 0) address |= (1 << (a0+1));
    if(a1 > 0) address |= (1 << (a1-1));
}

void MQ131::init(){
    if(!Wire.isEnabled()){
        Wire.begin();
    }
}

void MQ131::loop(){
    takeReading();
}

void MQ131::takeReading(){
    Wire.beginTransmission(address);
    Wire.write(0x00);
    Wire.endTransmission();
    Wire.requestFrom(address, 2);
    
    // Convert the data to 12-bits
    int raw_adc = ((Wire.read() & 0x0F) << 8) + Wire.read();
    ppb = (1.99 * raw_adc) / 4095.0 + 0.01;
}
