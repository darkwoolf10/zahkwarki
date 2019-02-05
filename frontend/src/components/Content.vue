<template lang="pug">
  .container
   .item(v-for="post in posts" :key="post.id")
     .item-body
       | Role: {{post.text}} <br/>
       | Punishment: {{ post.punishment_quantity }} {{ post.punishment_type }}
       <!--| Author: {{post.author.username}}-->
       .count
         | {{ post.punishment_count }}
     .item-side
       .item-controls
         .control.control-plus(v-on:click="punishmentUp(post.id, post.punishment_quantity)") +
         .control.control-minus(v-on:click="punishmentDown(post.id, post.punishment_quantity)") -
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
    },
    methods: {
      punishmentUp: function (id, punishment_quantity) {
           var that = this;
           this.axios.post(this.$store.state.url_server + 'api/punishment_up/' + id)
           .then(function (response) {
             // handle success;
               that.post.punishment_count += punishment_quantity;
           })
           .catch(function (error) {
             // handle error
             console.log(error);
           });
        },
        punishmentDown: function (id, punishment_quantity) {
           var that = this;
           this.axios.post(this.$store.state.url_server + 'api/punishment_down/' + id)
           .then(function (response) {
             // handle success;
               that.post.punishment_count -= punishment_quantity;
           })
           .catch(function (error) {
             // handle error
             console.log(error);
           });
        }
    }
}
</script>

<style scoped>
.count {
  float: right;
  font-size: 3em;
}
.control:hover {
  background-color: #ffeeba;
  cursor: pointer;
}
</style>