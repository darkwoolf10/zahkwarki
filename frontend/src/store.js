import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex);

const url = process.env.NODE_ENV !== "production" ?  "http://127.0.0.1:5000/" : "real";

export default new Vuex.Store({
  state: {
    url_server: url
  },
  getters: {
    get_url_server: state => {
      return state.url_server;
    }
  },
  mutations: {

  },
  actions: {

  }
})
