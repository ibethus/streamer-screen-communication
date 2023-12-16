import re
import time
import serial

def print_data_tu_usb(data):
    s = serial.Serial("/dev/ttyACM0")
    s.write(data.encode())
    line = s.readline()
    print(str.rstrip(line.decode()))
    s.close()

def main():
    previous_rate = ""
    previous_depth = ""
    while True:
        alsa = open("/proc/asound/card0/pcm0p/sub0/hw_params")    
        if alsa is not None:
            depth = ""
            rate = ""
            for alsa_line in alsa.readlines():  
                if alsa_line.startswith("format"):
                    depth = re.search("\d{2}", alsa_line).group()
                    depth = "Bit depth {depth} bit".format(depth=depth)
                if alsa_line.startswith("rate"):
                    rate = int(alsa_line.split(":")[1].strip().split(" ")[0].strip())/1000
                    rate = "Sample rate {rate}kHz".format(rate=rate)
            if rate != previous_rate or depth != previous_depth:
                print_data_tu_usb("{depth}\n{rate}".format(depth=depth, rate=rate))
                previous_depth = depth
                previous_rate = rate
            else:
                print("nothing changed")                
        time.sleep(10)


if __name__ == "__main__":
    main()