# filewow
A simple file transfer program using python and html

## How to use
Run the python script, then go to `yourlocalip:42020`.
There will be a button where you can choose a file and a button where you upload that file.
Once you upload the file, there will be an "uploads" folder in the same folder that contains the file.

If you're trying to use the program on a different network (for example, if a friend is trying to send you a file), then you'll need to port forward.
You can either do this in your router or use Universal Plug and Play (UPnP).
How to do the former varies on your router, but you'll almost always find the router at `192.168.1.1`.
To configure UPnP, I'd recommend using [MiniUPnP](https://github.com/miniupnp/miniupnp). Once you have it installed, run `upnpc -a yourlocalip 42020 42020 TCP`.
