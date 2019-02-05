import Vue from 'vue'
import 'bootstrap-css-only/css/bootstrap.min.css';
import 'mdbvue/build/css/mdb.css';
import App from './App.vue'
import router from './router'
import store from './store'
import './registerServiceWorker'
import { library } from '@fortawesome/fontawesome-svg-core'
import { faMinus, faPlus } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import axios from 'axios'
import VueAxios from 'vue-axios'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

library.add(faMinus, faPlus)
Vue.use(VueAxios, axios)

axios.defaults.headers.common['Authorization'] = "Token " + sessionStorage.getItem("token");
axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';

Vue.component('font-awesome-icon', FontAwesomeIcon)


Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
