<template>
  <v-card style="border-radius: 0!important;">
    <v-layout>
      <v-navigation-drawer theme="dark" rail permanent>
        <v-list-item nav prepend-avatar="@/assets/avatar.png"></v-list-item>
        <v-divider></v-divider>
        <v-list density="compact" nav>
          <v-list-item prepend-icon="mdi-monitor-cellphone-star" value="dashboard" @click="showDiv('showDevice')">
          </v-list-item>
          <v-list-item prepend-icon="mdi-forum" value="messages" @click="showDiv('showRecord')"></v-list-item>
        </v-list>
      </v-navigation-drawer>
      <v-main style="height: 561px">
        <Device v-if="pageDict.showDevice" />
        <Record v-if="pageDict.showRecord" />
      </v-main>
    </v-layout>
  </v-card>
</template>

<script>
  import Device from '@/views/device/Device.vue'
  import Record from '@/views/device/Record.vue'
  export default {
    data: () => ({
      pageDict: {
        showDevice: true,
        showRecord: false
      }
    }),
    components: {
      Device,
      Record
    },
    methods: {
      showDiv(page) {
        for (let p in this.pageDict) {
          if (p == page) {
            this.pageDict[p] = true
          } else {
            this.pageDict[p] = false
          }
        }
      }
    }
  }
</script>

<style>
</style>
