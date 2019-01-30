<template>
  <div class="home wrapper">
    <Sidebar v-bind:users="users"/>
    <div id="content">
      <Header v-bind:users="users" v-bind:login="login"/>
      <Content v-bind:posts="posts"/>
    </div>
  </div>
</template>

<script>
import Header from '@/components/Header.vue'
import Sidebar from '@/components/Sidebar.vue'
import Content from '@/components/Content.vue'

const axios = require('axios');

export default {
  name: 'home',
  data() {
      return {
          users: false,
          login: true,
          posts: ""
      }
  },
  components: {
    Header,
    Sidebar,
    Content
  },
  mounted() {
      $(document).ready(function () {
          $('#sidebarCollapse').on('click', function () {
              $('#sidebar').toggleClass('active');
          });
      });
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
    axios.get(this.$store.state.url_server + 'api/posts/',{
        headers: {'Authorization':'Token ' + sessionStorage.getItem("token")}
    })
    .then(function (response) {
      // handle success
      self.posts = response.data;
    })
    .catch(function (error) {
      // handle error
      console.log(error);
    });
  }
}
</script>
<style>
</style>
