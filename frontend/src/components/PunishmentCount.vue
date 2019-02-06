<template lang="pug">
  .post
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
const axios = require('axios');

export default {
    name: "PunishmentCount",
    data: function() {
         return  {
           show: true
         }
    },
    props: {
        post: ""
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
<style lang="scss">
.post {
  width: 100%;
}
.item-body {
  width: 90%;
  float: left;
}
.count {
  float: right;
  font-size: 2em;
}
.item-side {
  width: 20%;
  float: right;
}
.control:hover {
  cursor:pointer;
}
.control-plus:hover {
  background-color: #1c7430;
}
.control-minus:hover {
  background-color: #721c24;
}
</style>