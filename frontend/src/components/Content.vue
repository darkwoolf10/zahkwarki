<template lang="pug">
  .container
   .item(v-for="post in posts" :key="post.id")
     PunishmentCount(:post="post")
</template>

<script>
import PunishmentCount from '@/components/PunishmentCount.vue'

export default {
    name: "Content",
    data() {
      return {
        count: 0
      }
    },
    props: {
        posts: ""
    },
    components: {
        PunishmentCount
    }
}
</script>

<style scoped>
</style>