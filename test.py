import time
from pymavlink import mavutil

# İlk olarak, MAVLink bağlantısı oluşturun
master = mavutil.mavlink_connection('udpin:127.0.0.1:14550', baud=56700,source_system=255,source_component=0)

# Döngü, yeni bir mesaj alındığında çalışır
while True:
    # MAV_MODE_FLAG_CUSTOM_MODE_ENABLED bayrağı etkin olan son mod mesajını isteyin
    master.mav.command_long_send(
        master.target_system,
        master.target_component,
        mavutil.mavlink.MAV_CMD_REQUEST_MESSAGE,
        0, mavutil.mavlink.MAVLINK_MSG_ID_STATUSTEXT, 0, 0, 0, 0, 0, 0)
    
    msg = master.recv_match(type='STATUSTEXT', blocking=True)
    if msg and "Mode:" in msg.text:
        # Mevcut uçuş modunu yazdırın
        print(msg.text.split(":")[1].strip())
        
    time.sleep(1) # 1 saniye bekle
    
# Bağlantıyı kapatın
    master.close()
