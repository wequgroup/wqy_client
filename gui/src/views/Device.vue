<template>
  <v-card style="border-radius: 0!important;">
    <v-layout>
      <v-navigation-drawer theme="dark" rail permanent>
        <v-list-item nav prepend-avatar="@/assets/avatar.png"></v-list-item>
        <v-divider></v-divider>
        <v-list density="compact" nav>
          <v-list-item prepend-icon="mdi-monitor-cellphone-star" value="dashboard"
                       @click="showDiv('device')"></v-list-item>
          <v-list-item prepend-icon="mdi-forum" value="messages" @click="showDiv('script')"></v-list-item>
        </v-list>
      </v-navigation-drawer>
      <v-main style="height: 561px">
        <div class="device" v-if="showDevice">
          <v-card
            color="#385F73"
            dark
          >
            <v-card-title class="headline">device</v-card-title>
            <v-card-subtitle>Listen to your favorite artists and albums whenever and wherever, online and offline.
            </v-card-subtitle>
            <v-card-actions>
              <v-btn text>Listen Now</v-btn>
            </v-card-actions>
          </v-card>
        </div>
        <div class="script" v-if="showScript">
          <v-container fluid>
            <v-row>
              <v-col cols="12" style="text-align: center">
                <v-alert
                  dense
                  outlined
                  type="info"
                  style="text-align: left"
                >
                  此功能可以录制你的自动化脚本，通过语音、文字、后台等地方即可触发！第一次使用请看视频教程！
                </v-alert>
              </v-col>
            </v-row>
          </v-container>
        </div>
      </v-main>
    </v-layout>
  </v-card>
</template>
<script>
import {getCurrentInstance} from "vue";

export default {
  data: () => ({
    showDevice: true,
    showScript: false
  }),
  methods: {
    showDiv(page) {
      if (page === "device") {
        this.showDevice = true
        this.showScript = false
      }
      if (page === "script") {
        this.showDevice = false
        this.showScript = true
      }
    },
    setScript() {
      window.pywebview.api.record().then((res) => {
        console.log(res)
      })
    }
  }
}
</script>
