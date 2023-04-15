import paho.mqtt.client as mqtt
import time
import json


class MQTT:

    def __init__(self, user_name, password, host, port, auto_online=False, win=None):
        self.client = mqtt.Client(client_id=user_name)
        self.client.keep_alive = 60
        self.client.username_pw_set(username=user_name, password=password)
        self.host = host
        self.port = port
        self.auto_online = auto_online
        self.client.on_disconnect = self.on_disconnect
        self.client.on_message = self.on_message
        self.client.on_connect = self.on_connect
        self.username = user_name
        self.stop = False
        self.win = win

    # 定义连接断开的回调函数
    def on_disconnect(self, rc, a, b):
        while rc != 0 and rc != 5:
            time.sleep(5)
            try:
                rc = self.client.reconnect()
            except:
                print("Failed to reconnect to MQTT broker")
                time.sleep(15)

    def on_connect(self, client, userdata, rc, msg):
        a = open('log.txt', 'a', encoding="utf-8")
        a.write('3追加写入' + str(msg))
        a.close()
        if msg == 5:
            print("鉴权失败，不重连")
            self.auto_online = False
            self.stop = True
            self.client.loop_stop()
        if msg == 0:
            data = {"ok": "yes"}
            self.win.evaluate_js(f"connectSuccess('{json.dumps(data)}')")

    def on_message(self, client, userdata, rc):
        """收到消息了"""
        msg = rc.payload  # 将信息转换成json格式
        try:
            params = json.loads(msg)
            self.win.evaluate_js(f"connectSuccess('{msg}')")
        except:
            return False
        return True

    def ping(self):
        """50秒发个心跳"""
        while True:
            print("ping bang")
            if self.stop is True:
                break
            self.client.publish("0", "1")
            time.sleep(20)

    def start(self):
        # 连接到MQTT服务器
        print("Connecting to MQTT broker...")
        rc = self.client.connect(self.host, self.port)
        if rc == 0:
            self.client.subscribe(topic=str("duck/" + self.username), qos=0)
            self.client.loop_start()
            self.ping()
        else:
            # print("连接失败")
            pass

# m = MQTT("49137218", "2342341", "mqtt-hw.wequ.net", 1883, False)
#
# m.start()
