<template lang="pug">
  #app
      transition(name="fade")
        .sidebar-overlay(
          v-if="sidebar"
          @click="toggleSidebar"
        )
      transition(name="slide")
        .sidebar(v-if="sidebar")
          .btn(
            @click="toggleSidebar"
            color="secondary"
          ) Close menu
          ul
            li: a(href="/about") about
            li: a(href="/codex") codex
            li(v-for="user in users"): a(href="#") {{user.username}}

      .header
        .btn(
          @click="toggleSidebar"
        ) Open menu
        mdb-btn(
          color="primary"
          class="float-right"
          @click="goToLogin"
        ) Login

      Content(:posts="posts")
</template>

<script>
import Header from '@/components/Header.vue'
import Sidebar from '@/components/Sidebar.vue'
import Content from '@/components/Content.vue'
import { mdbBtn, mdbBtnFixed, mdbBtnFixedItem, mdbIcon } from 'mdbvue';

export default {
  name: 'home',
  data() {
      return {
          users: false,
          login: true,
          posts: "",
          sidebar: false,
          itemCount: false
      }
  },
  components: {
    Header,
    Sidebar,
    Content,
    mdbBtn,
    mdbIcon
  },
  mounted() {
  },
  created() {
    $.ajax({
        url: this.$store.state.url_server + 'api/users/',
        type: 'GET',
        headers: {
            'Authorization':'Token ' + sessionStorage.getItem("token"),
        },
        success: (response) => {
            this.users = response;
            this.login = false;
        }
    });
    let self = this;
    this.axios.get(this.$store.state.url_server + 'api/posts/',{
        headers: {'Authorization':'Token ' + sessionStorage.getItem("token")}
    })
    .then(function (response) {
      self.posts = response.data;
    })
    .catch(function (error) {
      console.log(error);
    });
  },
  methods: {
    toggleSidebar() {
      this.sidebar = !this.sidebar;
    },
    goToLogin() {
      this.$router.push('login');
    }
  }
}
</script>
<style lang="scss">
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}

a {
    text-decoration: none;
}

.sidebar-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0,0,0,0.7);
  z-index: 1000;
}

.sidebar {
  position: fixed;
  top: 0;
  left: 0;
  width: 260px;
  height: 100%;
  background: #69306D;
  z-index: 1000;
  color: #C0ABAF;
  text-align: center;
}

.sidebar ul {
  margin-top: 10%;
}

.sidebar ul li {
  list-style:none;
  text-decoration: none;
  width: 100%;
  font-size: 2em;
  background-color: #965D7F;
  margin-top: 1%;
}

.sidebar ul li a{
  text-decoration: none;
  color: #fff;
}

.sidebar ul li:hover {
  background-color: #AF8594 ;
}

.header {
  width: 100%;
  z-index: 900;
  background: #fff;
  padding: 10px;
  box-shadow: 0 0 40px -15px #000;
  margin-bottom: 1%;
}

.item {
  border: 1px solid #000;
  display: flex;
  background-color: #f6f6f6;
  /*box-shadow: #000;*/
  margin-bottom: 1%;

  &-body {
    flex-grow: 1;
    padding: 15px;
  }

  &-side {
    position: relative;
    width: 8%;
    flex-shrink: 0;
    border-left: 1px solid #000;
    display: flex;
    align-items: center;
    justify-content: center;
    min-height: 100px;
    & .item-controls {
      display: flex;
    }
  }
  .control-plus {
    border-bottom: 1px solid #000;
  }

  &-controls {
    display: none;
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    flex-direction: column;
  }
}

.control {
  flex-grow: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #1b1e21;
}

.slide-enter-active,
.slide-leave-active {
  transition: transform .5s;
  transform: translateX(0%)
}

.slide-enter,
.slide-leave-to {
  transform: translateX(-100%)
}


.fade-enter-active,
.fade-leave-active {
  transition: opacity .5s;
}

.fade-enter,
.fade-leave-to {
  opacity: 0;
}
.float-right {
  float: right;
}
</style>
