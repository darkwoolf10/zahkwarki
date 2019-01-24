<template>
  <div class="wrapper">
    <SidebarComponent/>
    <HeaderComponent/>
  </div>
</template>

<script>
import SidebarComponent from "./SidebarComponent";
import HeaderComponent from "./HeaderComponent";

export default {
  name: 'IndexComponent',
    data () {
    return {
      msg: 'Hello'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
