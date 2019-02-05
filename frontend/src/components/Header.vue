<template lang="pug">
  .header
    .btn(
      @click="toggle"
    ) Open menu
    mdb-btn(
      color="primary"
      class="float-right"
    ) Login
</template>

<script>
import { mdbBtn } from 'mdbvue';

export default {
  name: "Header",
  data() {
    return {
      sidebar: false
    }
  },
  components: {
    mdbBtn
  },
  props: {
      users: "",
      login: true
  },
  created() {

  },
  methods: {
    toggle() {
      this.sidebar = !this.sidebar;
      console.log(this.sidebar)
    }
  }
}
</script>

<style scoped>

</style>