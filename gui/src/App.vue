<template>
  <v-app>
    <v-main>
      <div>
        <div class="header-bar">
          <v-icon icon="mdi-window-minimize" class="ms-2" style="height: 3px;" @click="showMini"></v-icon>
          <v-icon icon="mdi-close-box-outline" class="ms-3" @click="closeClick"></v-icon>
        </div>
        <v-dialog v-model="dialog" activator="parent" width="auto">
          <v-card>
            <v-card-text>
              隐藏后可以在托盘图标里找到
            </v-card-text>
            <v-card-actions>
              <div style="text-align: right;width: 100%;">
                <v-btn color="info" @click="minisize">最小化</v-btn>
                <v-btn color="teal-darken-4" @click="hide">隐藏到托盘</v-btn>
              </div>
            </v-card-actions>
          </v-card>
        </v-dialog>
        <v-dialog v-model="closeDialog" activator="parent" width="auto">
          <v-card>
            <v-card-text>
              这不会退出，而是会隐藏到托盘
            </v-card-text>
            <v-card-actions>
              <div style="text-align: right;width: 100%;">
                <v-btn color="success" @click="hide">我知道了</v-btn>
              </div>
            </v-card-actions>
          </v-card>
        </v-dialog>
        <v-overlay :model-value="gLoading" class="align-center justify-center" persistent>
          <v-progress-circular color="#fff" indeterminate size="30"></v-progress-circular> <span
            style="color: #fff;vertical-align: -2px;margin-left: 4px;">Loading...</span>
        </v-overlay>
      </div>
      <router-view></router-view>
    </v-main>
  </v-app>
</template>

<script>

export default {
  data: () => ({
    dialog: false,
    closeDialog: false,
    gLoading: true
  }),
  created(){
    setTimeout(() => {
        this.gLoading = false
      }, 1300)
  },
  methods: {
    showMini(e) {
      this.dialog = true
      e.stopPropagation();
    },
    hide() {
      this.closeDialog = false
      this.dialog = false
      setTimeout(function () {
        window.pywebview.api.hide().then((res) => {
        })
      }, 200);
    },
    minisize() {
      this.dialog = false
      setTimeout(function () {
        window.pywebview.api.minisize().then((res) => {
        })
      }, 200);
    },
    close(e) {
      e.stopPropagation();
      window.pywebview.api.close().then((res) => {
      })
    },
    closeClick(e) {
      this.closeDialog = true
      e.stopPropagation();
    },
  }
}

</script>
<style>
.header-bar {
  position: absolute;
  top: 2px;
  z-index: 1;
  right: 3px;
  font-size: 14px;
  cursor: pointer;
}
</style>
