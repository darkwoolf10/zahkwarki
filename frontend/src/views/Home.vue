<template>
  <div class="home wrapper">
    <Sidebar v-bind:users="users"/>
    <Header v-bind:users="users" v-bind:login="login"/>
    </div>
</template>

<script>
import Header from '@/components/Header.vue'
import Sidebar from '@/components/Sidebar.vue'

export default {
  name: 'home',
  data() {
      return {
          users: false,
          login: true
      }
  },
  components: {
    Header,
    Sidebar
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
  }
}
</script>
<style>
</style>
