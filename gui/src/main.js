/**
 * main.js
 *
 * Bootstraps Vuetify and other plugins then mounts the App`
 */
import {createRouter, createWebHashHistory} from 'vue-router'
// Components
import App from './App.vue'
import Login from '@/views/Login.vue'
import  Axios   from './utils/request'
import axios from 'axios';
import VueAxios from 'vue-axios'

const routes = [
  { path: '/', component: Login }
]
const router = createRouter({
  history: createWebHashHistory(),
  routes
})

import { createApp } from 'vue'

// Plugins
import { registerPlugins } from '@/plugins'

const app = createApp(App).use(VueAxios, axios).use(router).use(Axios)
registerPlugins(app)

app.mount('#app')
