import time
import can

bustype = 'socketcan'
channel = 'vcan0'

"""
; Speed
[transmit1]                  ; Transmit message
destination = 0              ; 0 = None, 1 = Logger, 2 = Interface, 3 = Both
period = 200                 ; Period in ms (DEC, 10 ms resolution)
delay = 0                    ; Delay in ms (DEC, 10 ms resolution)
extendedID = false           ; Use extended 29 bit message IDs (2.0B)
msgID = 7DF                  ; Transmit message ID (HEX)
msgData = {02010D5555555555} ; Message data (HEX)


; RPM 
[transmit2]                  ; Transmit message
destination = 0              ; 0 = None, 1 = Logger, 2 = Interface, 3 = Both
period = 200                 ; Period in ms (DEC, 10 ms resolution)
delay = 10                   ; Delay in ms (DEC, 10 ms resolution)
extendedID = false           ; Use extended 29 bit message IDs (2.0B)
msgID = 7DF                  ; Transmit message ID (HEX)
msgData = {02010C5555555555} ; Message data (HEX)


; MAF
[transmit3]                  ; Transmit message
destination = 0              ; 0 = None, 1 = Logger, 2 = Interface, 3 = Both
period = 200                 ; Period in ms (DEC, 10 ms resolution)
delay = 20                   ; Delay in ms (DEC, 10 ms resolution)
extendedID = false           ; Use extended 29 bit message IDs (2.0B)
msgID = 7DF                  ; Transmit message ID (HEX)
msgData = {0201105555555555} ; Message data (HEX)


; Throttle position
[transmit4]                  ; Transmit message
destination = 0              ; 0 = None, 1 = Logger, 2 = Interface, 3 = Both
period = 200                 ; Period in ms (DEC, 10 ms resolution)
delay = 30                   ; Delay in ms (DEC, 10 ms resolution)
extendedID = false           ; Use extended 29 bit message IDs (2.0B)
msgID = 7DF                  ; Transmit message ID (HEX)
msgData = {0201115555555555} ; Message data (HEX)


; Run time since engine start
[transmit5]                  ; Transmit message
destination = 0              ; 0 = None, 1 = Logger, 2 = Interface, 3 = Both
period = 200                 ; Period in ms (DEC, 10 ms resolution)
delay = 40                   ; Delay in ms (DEC, 10 ms resolution)
extendedID = false           ; Use extended 29 bit message IDs (2.0B)
msgID = 7DF                  ; Transmit message ID (HEX)
msgData = {02011F5555555555} ; Message data (HEX)


; Distance traveled with malfunction indicator lamp (MIL) on
[transmit6]                  ; Transmit message
destination = 0              ; 0 = None, 1 = Logger, 2 = Interface, 3 = Both
period = 200                 ; Period in ms (DEC, 10 ms resolution)
delay = 50                   ; Delay in ms (DEC, 10 ms resolution)
extendedID = false           ; Use extended 29 bit message IDs (2.0B)
msgID = 7DF                  ; Transmit message ID (HEX)
msgData = {0201215555555555} ; Message data (HEX)


; Calculated engine load
[transmit7]                  ; Transmit message
destination = 0              ; 0 = None, 1 = Logger, 2 = Interface, 3 = Both
period = 100                 ; Period in ms (DEC, 10 ms resolution)
delay = 60                   ; Delay in ms (DEC, 10 ms resolution)
extendedID = false           ; Use extended 29 bit message IDs (2.0B)
msgID = 7DF                  ; Transmit message ID (HEX)
msgData = {0201045555555555} ; Message data (HEX)
"""


def producer_sample(id):    
    """:param id: Spam the bus with messages including the data id."""
    bus = can.interface.Bus(channel=channel, bustype=bustype)
    for i in range(10):
        msg = can.Message(arbitration_id=0xc0ffee, data=[id, i, 0, 1, 3, 1, 4, 1], is_extended_id=False)
        bus.send(msg)

    time.sleep(1)


def ecu_producer():
    bus = can.interface.Bus(channel=channel, bustype=bustype)
    msg = can.Message(arbitration_id=0x7df, data=[0x1F, 0xC, 0x33, 0x00, 0x00, 0x00, 0x00], is_extended_id=False)
    bus.send(msg)

    # 0x1F 0xC 0x33 0x3D 0x00 0x00 0x00 0x00

    
if __name__ == '__main__':
    ecu_producer()