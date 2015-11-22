# Camp Light Part One

> “May it be a light to you in dark places, when all other lights go out.” 

There's some pretty fancy lanterns around. Some are bright, some have long battery light, some can even pulse in time to music. But I've yet to find one that can do all of that, at least for a price I'm willing to pay.

Here's what I'm looking for:

* Bright. What's the point in a camping light if the girl guides next door still have their retinas at the end of the night?
* Long battery life. I don't want to run out half way through, it should last a week of nightly usage at least.
* Water proof. I'm not planning on swimming with it, but there's a possibility of liquids (read beer) being spilt on it.
* Small packing size. No point if I can't take it with me.

Some other stuff that I'd like to add.

* Colour changing. I'd like something like [Redshift](http://jonls.dk/redshift/) or [F.lux](https://justgetflux.com/) so I can comfortably use it late at night.
* Flash to music.
* Candle flicker. I just think that would be nice.
* Clips to hang the light from. Maybe a hook, although magnets may be interesting.
* Directional control. So I can move it without blinding myself.
* Low battery warning. Or maybe a smooth indicator of power.
* Rechargeable battery pack. Preferably charged by a usb cable.
* Photovoltaic recharging. Ok admittedly this is a stretch goal, but I was told that an [atomic battery](https://en.wikipedia.org/wiki/Atomic_battery) was over engineering.
* Temperature thingy. I have an [electric thermometer](http://www.amazon.co.uk/gp/product/B00HI7LUKW) sitting on my desk, maybe I can find a use for it.
* Phone charger. This will depend on how well the battery/charging side of things is going.

You might have guessed, this isn't just going to be a *hook a AAA up to an led and call it a lamp* job, this will be a proper camping lantern.

The most important point is the leds. I'd recently ordered a pack of [50 Gorgeous ultra bright 5mm LEDs Emitting Diode](http://www.amazon.co.uk/gp/product/B008AGOLQA) (whatever that means) but at about a 50th of the price of Maplin, I can hardly complain(3.4pence each vs £1.49 each) I just hope these Light Emitting Diodes Emitting Diode should be bright enough.

I also have some [RGB LEDs](http://www.amazon.co.uk/gp/product/B005VMDROS) to add that colour into my lamp. Some will occur to see if they are bright enough without the aforementioned "Goregous ultra bright" LEDs. 
 
 We'll also need a way to control our lamp. For this I've chosen the [Arduino Nano](https://www.arduino.cc/en/Main/ArduinoBoardNano). An adaptable, battle proven board; that I just happen to have sat on my desk. The nano has 14 digital and 8 analogue io ports, along with a 3.3 volt output. Considering the LEDs run at 3.2 to 3.5 volts, this just makes it even more convenient.
 
 ![Arduino Nano](https://www.arduino.cc/en/uploads/Main/ArduinoNanoFront_3_sm.jpg)
 
 My plan for power is to find the biggest capacity rechargeable battery that will fit in my case and hope I never have to worry about changing it. [Something like this](https://www.adafruit.com/products/328) is what I'm picturing; although my drawing has a slightly lower price. I'll have to see what China can do for me. 
 
 My options for powering the board are 7-12V recommended or 6-20V limits into the Vin pin(30), 5V into the 5V pin(27), or 5V into the mini-B usb port. Unfortunately the 5V input require regulated voltage, so powering it with 7-12V seems to be the most feasible option, despite the extra cost of the battery. This will also mean that  I can probably charge it from a car battery.
 
 
 So I have an idea, some bits and motivation. According to Edison I just need to go an sweat for 99 times as long as it took me to write this and I'm done.


## Sources

* https://www.arduino.cc/en/Main/ArduinoBoardNano