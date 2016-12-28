import usb.core
import usb.util

def switchKVM():
	devs = usb.core.find(find_all=1,idVendor=0x10D5, idProduct=0x55A2)

	for d in devs:
	   d.set_configuration()
	   
	   for intf in d[0]:
		  ep = usb.util.find_descriptor( intf, custom_match = lambda e: usb.util.endpoint_direction(e.bEndpointAddress) == usb.util.ENDPOINT_OUT )
		  if not ep:
			 continue
		  ep.write(chr(5))
		  ep.write(chr(1))
      
switchKVM() 