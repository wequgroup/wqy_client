<template>
  <div class="device-online">
    <div class="view-log-btn">
      <v-btn size="small" text v-if="!showLog" @click="showLog=true">
        <span class="mdi mdi-eye-arrow-right-outline"></span>
        &nbsp;查看日志
      </v-btn>
    </div>
    <div class="view-close-log-btn" v-if="showLog">
      <v-btn @click="showLog=false" density="compact" icon="mdi-eye-off-outline" size="small"></v-btn>
    </div>
    <div class="log" v-if="showLog">
      <p>12:30:00 - 下发1指令：hello wordhello wordhello wordhello wordhello wordhello wordhello wordhello word</p>
      <p>12:30:01 - 下发3指令：hello word</p>
      <p>12:30:02 - 下发4指令：hello word</p>
      <p>12:30:03 - 下发指令：hello word</p>
      <p>12:30:04 - 下发指令：hello word</p>
      <p>12:30:00 - 下发指令：hello word</p>
      <p>12:30:00 - 下发指令：hello word</p>
      <p>12:30:00 - 下发指令：hello word</p>
      <p>12:30:00 - 下发指令：hello word</p>
      <p>12:30:00 - 下发指令：hello word</p>
      <p>12:30:00 - 下发指令：hello word</p>
      <p>12:30:00 - 下发指令：hello word</p>
      <p>12:30:00 - 下发指令：hello word</p>
      <p>12:30:00 - 下发指令：hello word</p>
      <p>12:30:00 - 下发指令：hello word</p>
      <p>12:30:00 - 下发指令：hello word</p>
      <p>12:30:00 - 下发指令：hello word</p>
      <p>12:30:00 - 下发指令：hello word</p>
      <p>12:30:00 - 下发指令：hello word</p>
      <p>12:30:00 - 下发指令：hello word</p>
      <p>12:30:00 - 下发指令：hello word</p>
      <p>12:30:00 - 下发指令：hello word</p>
      <p>12:30:00 - 下发指令：hello word</p>
      <p>12:30:00 - 下发指令：hello word</p>
      <p>12:30:00 - 下发指令：hello word</p>
      <p>12:30:00 - 下发指令：hello word</p>
      <p>12:30:00 - 下发指令：hello word</p>
      <p>12:30:00 - 下发指令：hello word</p>
      <p>12:30:00 - 下发指令：hello word</p>
      <p>12:30:00 - 下发指令：hello word</p>
      <p>12:30:00 - 下发指令：hello word</p>
      <p>12:30:00 - 下发指令：hello word</p>
    </div>
    <v-container style="height: 100%;">
      <v-row no-gutters>
        <v-col cols="12" md="8">
          <v-select :items="[1,2]" label="选择一个设备进行登录" variant="solo"></v-select>
        </v-col>
      </v-row>
    </v-container>
    <div class="connect">
      <v-btn color="warning" dark>与服务端断开连接</v-btn>
    </div>
  </div>
</template>
<script>
  import {
    getCurrentInstance
  } from "vue";

  export default {
    data: () => ({
      showLog: false
    }),
    methods: {

    }
  }
</script>
<style>
  .device-online {
    height: 100%;
    background-repeat: no-repeat;
    background-size: 400px;
    background-position: center;
    background-image: url(@/assets/device_online.gif);
  }

  .device-offline {
    height: 100%;
    background-repeat: no-repeat;
    background-size: 320px;
    top: tdsdsdaasda;
    background-position: center;
    background-image: url(@/assets/device_offline.png);
    -webkit-filter: grayscale(100%);
    filter: grayscale(100%);
  }

  .connect {
    position: absolute;
    bottom: 20px;
    text-align: center;
    width: 100%;
    margin-left: -30px;
  }

  .log {
    position: absolute;
    z-index: 888;
    top: 100px;
    left: 71px;
    background: black;
    height: 400px;
    width: 505px;
    opacity: 0.4;
    color: #fff;
    padding: 10px;
    font-size: 14px;
    overflow-y: scroll;
    overflow-x: scroll;
    border-radius: 5px;
  }

  .view-log-btn {
    position: absolute;
    top: 100px;
    left: 72px;
  }

  .view-close-log-btn {
    position: absolute;
    top: 100px;
    right: 18px;
    z-index: 999;
  }
</style>
