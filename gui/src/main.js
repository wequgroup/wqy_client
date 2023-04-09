/**
 * main.js
 *
 * Bootstraps Vuetify and other plugins then mounts the App`
 */
import {createRouter, createWebHashHistory} from 'vue-router'
// Components
import App from './App.vue'
import Login from '@/views/Login.vue'
import Device from '@/views/Device.vue'
import  Axios   from './utils/request'
import axios from 'axios';
import VueAxios from 'vue-axios'

const routes = [
   { path: '/device', component: Device },
  { path: '/', component: Login }
]
const router = createRouter({
  history: createWebHashHistory(),
  routes
})

import { createApp } from 'vue'

// Plugins
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'

const vuetify = createVuetify({
  components,
  directives,
})

const app = createApp(App).use(VueAxios, axios).use(router).use(Axios).use(vuetify)

app.mount('#app')
